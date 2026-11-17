#!/usr/bin/env python3
"""Build the WilsonWorks Finance Kit, as a zip or into a workspace.

Everything the kit needs is in this repo:

  kit/            the basic kit: CLAUDE.md, Start-Here.html, the eight agent files and
                  their references, five skills, the message board, sample-company/, outputs/
  premium/        only in finance-pack-premium: library/ (the firm reference library),
                  skills/ (the tax skills), and the two notes that tell the team the library is there

Two ways to use it:

    python build_kit.py                      zip to unzip and open in the Claude desktop app
    python build_kit.py --into <workspace>   add the team to an existing workspace

The edition is premium when premium/ is here, public otherwise; --edition public builds the
public kit from either repo. Before writing anything it scans every file and refuses on any hit:
drive paths, Hub-folder paths, 'py -3', client codes C00-C10, a client name from the Run-8 guard
list or from --names-file, a word from the private --fence-file (reported by file and line,
never by word), a byte copy of a Run-8 live-data file,
settings files, and (public edition) any library or premium file. The repo's own files outside
kit/ and premium/ (the build scripts, README files and proof/) are checked for fence words and
Hub-folder paths too.

The Run-8 checks run only when --run8-dir, or the FINANCE_KIT_RUN8_DIR environment variable,
names the live-data folder, and the fence-word check only when --fence-file, or
FINANCE_KIT_FENCE_FILE, names a word list. Without them those checks are skipped with a note,
so a buyer with neither can still build.

The premium edition also refuses to run unless --names-file names a non-empty list of client
names (one per line, matched as whole words, any case), --fence-file names a non-empty word
list, and the 'premium' git remote reads
PRIVATE in `gh repo view --json visibility`. --copy-to never overwrites: a zip already there is
renamed with a -prev suffix first.

    python build_kit.py [--edition public|premium] [--out DIR] [--copy-to DIR]
                        [--into DIR [--dry-run]] [--run8-dir DIR] [--names-file FILE]
                        [--fence-file FILE]

Stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "kit"
PREMIUM = HERE / "premium"
ZIP_NAMES = {"public": "WilsonWorks-Finance-Kit", "premium": "WilsonWorks-Finance-Kit-Premium"}
PREMIUM_MARK = "WilsonWorks Finance Kit Premium"
PACK_DIR = "packs/finance"

AGENTS = [
    "cfo-eleanor", "cfo-ea-sophia", "head-controller-hal", "head-treasurer-imani",
    "head-tax-anya", "head-fpa-nadia", "senior-accountant-lila", "senior-accountant-theo",
]
SKILLS = ["close-month", "cash-flow-snapshot", "month-end-prep", "invoice-chase", "plan-payroll"]
OPENING_FILES = ["CLAUDE.md", "Start-Here.html"]

LEAK_PATTERNS = [
    ("drive path", re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]")),
    ("Hub path", re.compile(r"[\\/]Hub[\\/]", re.IGNORECASE)),
    ("'py -3'", re.compile(r"\bpy -3\b")),
    ("client code", re.compile(r"\bC(?:0\d|10)\b")),
    ("Run-8 reference", re.compile(r"_?Run8(?:-LiveData)?", re.IGNORECASE)),
]
SKIP_PARTS = {"__pycache__"}

# Words that must never ship are read at build time from a private file (--fence-file or FINANCE_KIT_FENCE_FILE),
# one per line. Each word of a file, and each pair of words joined by '-', ' ', '_' or '.', is compared in lower
# case; a match is reported by file and line only.
FENCE_WORD = re.compile(r"[^\W_]+")
FENCE_JOINS = {"-", " ", "_", "."}


def read_fence(arg: Path | None) -> frozenset[str] | None:
    """The fence words, from --fence-file or FINANCE_KIT_FENCE_FILE; None when neither is given."""
    env = os.environ.get("FINANCE_KIT_FENCE_FILE")
    path = arg or (Path(env) if env else None)
    if path is None:
        return None
    words = frozenset(w.lower() for w in read_names(path))
    if not words:
        die("the fence file given by --fence-file or FINANCE_KIT_FENCE_FILE is missing or empty; nothing written")
    return words


def fence_lines(text: str, fence: frozenset[str]) -> list[int]:
    """Line numbers holding a fence word: whole words, any case. Never returns the word."""
    lines = []
    for n, line in enumerate(text.lower().splitlines(), 1):
        words = list(FENCE_WORD.finditer(line))
        cands = [w.group() for w in words]
        cands += [a.group() + line[a.end():b.start()] + b.group()
                  for a, b in zip(words, words[1:]) if line[a.end():b.start()] in FENCE_JOINS]
        if any(c in fence for c in cands):
            lines.append(n)
    return lines

# --into: the agents and skills sit at the workspace's .claude/, everything else in packs/finance/,
# so the paths the agents and skills name are pointed there.
ADDON_PATH = re.compile(r"(?<![\w./-])(sample-company/|outputs/|library/|\.claude/comms/comms\.py)")


def die(msg: str) -> None:
    print(f"REFUSED: {msg}", file=sys.stderr)
    sys.exit(1)


def find_run8(arg: Path | None) -> Path | None:
    """The Run-8 live-data folder, from --run8-dir or FINANCE_KIT_RUN8_DIR; there is no default."""
    given = arg or (Path(os.environ["FINANCE_KIT_RUN8_DIR"]) if os.environ.get("FINANCE_KIT_RUN8_DIR") else None)
    if given is not None and not given.is_dir():
        die("the Run-8 folder given by --run8-dir or FINANCE_KIT_RUN8_DIR is not a folder; pass the live-data folder")
    return given


def repo_files() -> list[Path]:
    """The repo's own files outside kit/ and premium/: top-level files and everything under proof/."""
    top = [p for p in HERE.iterdir() if p.is_file() and p.name != ".git"]  # a worktree's .git file is git's, not ours
    proof = [p for p in (HERE / "proof").rglob("*") if p.is_file()] if (HERE / "proof").is_dir() else []
    return sorted(p for p in top + proof if not SKIP_PARTS & set(p.parts))


def repo_scan(fence: frozenset[str] | None) -> list[str]:
    """Fence words and Hub-folder paths in the build scripts, README files and proof/."""
    hits: list[str] = []
    files = repo_files()
    hub = dict(LEAK_PATTERNS)["Hub path"]
    for p in files:
        rel = p.relative_to(HERE).as_posix()
        text = p.read_bytes().decode("utf-8", errors="replace")
        for line in fence_lines(text, fence) if fence else []:
            hits.append(f"repo {rel}:{line}: a word on the fence list")  # never print the word
        for m in hub.finditer(text):
            hits.append(f"repo {rel}:{text.count(chr(10), 0, m.start()) + 1}: Hub path")
    print(f"repo-file check: {len(files)} build, README and proof files")
    return hits


def assemble(stage: Path, edition: str) -> None:
    if stage.exists():
        shutil.rmtree(stage)
    shutil.copytree(KIT, stage, ignore=shutil.ignore_patterns("__pycache__"))
    for name in OPENING_FILES:
        if not (stage / name).is_file():
            die(f"kit/{name} is missing")
    for name in AGENTS:
        if f"name: {name}\n" not in (stage / ".claude" / "agents" / f"{name}.md").read_text(encoding="utf-8"):
            die(f"kit copy of {name} is missing or has the wrong name")
    if edition == "public":
        return
    if not PREMIUM.is_dir():
        die("premium/ is not in this repo; the premium edition builds from finance-pack-premium")
    shutil.copytree(PREMIUM / "library", stage / "library")
    for skill in sorted(p for p in (PREMIUM / "skills").iterdir() if p.is_dir()):
        dest = stage / ".claude" / "skills" / skill.name
        if dest.exists():
            die(f"premium skill {skill.name} has the same name as a basic skill")
        shutil.copytree(skill, dest, ignore=shutil.ignore_patterns("__pycache__"))
    append(stage / "CLAUDE.md", PREMIUM / "CLAUDE.append.md")
    for name in AGENTS:
        append(stage / ".claude" / "agents" / f"{name}.md", PREMIUM / "agent.append.md")


def append(path: Path, extra: Path) -> None:
    text = path.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + extra.read_text(encoding="utf-8")
    path.write_text(text, encoding="utf-8", newline="\n")


def kit_files(stage: Path) -> list[Path]:
    return sorted(p for p in stage.rglob("*") if p.is_file() and not SKIP_PARTS & set(p.parts))


def client_tokens(run8: Path) -> list[str]:
    path = run8 / "_guard" / "tokens.txt"
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    return [t.strip() for t in lines if t.strip() and not t.lstrip().startswith("#")]


def public_guard(stage: Path) -> list[str]:
    """The public kit carries the basic kit only: no library, no premium skill or note."""
    hits: list[str] = []
    allowed_agents = {f"{a}.md" for a in AGENTS}
    for p in kit_files(stage):
        rel = p.relative_to(stage).as_posix()
        parts = rel.split("/")
        if parts[0] == "library":
            hits.append(f"{rel}: library file in the public kit")
        elif parts[:2] == [".claude", "skills"] and parts[2] not in SKILLS:
            hits.append(f"{rel}: skill '{parts[2]}' is not one of the five basic skills")
        elif parts[:2] == [".claude", "agents"] and len(parts) == 3 and parts[2] not in allowed_agents:
            hits.append(f"{rel}: agent not in the basic team")
        elif PREMIUM_MARK in p.read_bytes().decode("utf-8", errors="replace"):
            hits.append(f"{rel}: carries the premium mark")
    return hits


def read_names(path: Path) -> list[str]:
    """One client name per line; blank lines and '#' lines are skipped."""
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    return [n.strip() for n in lines if n.strip() and not n.lstrip().startswith("#")]


def private_remote_guard() -> None:
    """The premium edition builds only from a clone whose 'premium' remote GitHub reports PRIVATE."""
    try:
        url = subprocess.run(["git", "-C", str(HERE), "remote", "get-url", "premium"],
                             capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as e:
        die(f"could not run git to find the 'premium' remote ({e})")
    if url.returncode != 0 or not url.stdout.strip():
        die("this clone has no 'premium' git remote; the premium edition builds only from finance-pack-premium")
    try:
        view = subprocess.run(["gh", "repo", "view", url.stdout.strip(), "--json", "visibility", "-q", ".visibility"],
                              capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        die(f"could not run gh to check the 'premium' remote's visibility ({e})")
    visibility = view.stdout.strip()
    if view.returncode != 0 or visibility != "PRIVATE":
        die(f"the 'premium' remote does not read PRIVATE (gh says {visibility or 'nothing'}); nothing written")
    print("private-repo check: the 'premium' remote reads PRIVATE")


def leak_scan(stage: Path, run8: Path | None, names: list[str] | None = None,
              fence: frozenset[str] | None = None) -> list[str]:
    hits: list[str] = []
    files = kit_files(stage)
    tokens = client_tokens(run8) if run8 else []
    token_pats = [re.compile(r"(?<!\w)" + re.escape(t) + r"(?!\w)", re.IGNORECASE) for t in tokens]
    name_pats = [re.compile(r"(?<!\w)" + re.escape(n) + r"(?!\w)", re.IGNORECASE) for n in names or []]
    for p in files:
        rel = p.relative_to(stage).as_posix()
        text = p.read_bytes().decode("utf-8", errors="replace")
        if re.fullmatch(r"settings(\..*)?\.json", p.name):
            hits.append(f"{rel}: settings file in the kit" + (" (contains 'hooks')" if "hooks" in text else ""))
        for label, pat in LEAK_PATTERNS:
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append(f"{rel}:{line}: {label} {m.group(0)!r}")
        for i, pat in enumerate(token_pats, 1):
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append(f"{rel}:{line}: client name (guard token #{i})")  # never print the name
        for i, pat in enumerate(name_pats, 1):
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append(f"{rel}:{line}: client name (names-file entry #{i})")  # never print the name
        for line in fence_lines(text, fence) if fence else []:
            hits.append(f"{rel}:{line}: a word on the fence list")  # never print the word
    if fence:
        print(f"fence-word check: {len(fence)} words against {len(files)} kit files")
    else:
        print("note: no fence file given (--fence-file or FINANCE_KIT_FENCE_FILE); fence-word check skipped")
    if names is not None:
        print(f"names-file check: {len(name_pats)} client names against {len(files)} kit files")
    if run8 is None:
        print("note: no Run-8 folder given (--run8-dir or FINANCE_KIT_RUN8_DIR); client-name and byte-copy checks skipped")
        return hits
    print(f"client-name check: {len(tokens)} guard tokens against {len(files)} kit files")
    kit_hashes = {hashlib.sha256(p.read_bytes()).hexdigest(): p for p in files}
    checked = 0
    for p in run8.rglob("*"):
        if p.is_file():
            checked += 1
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            if h in kit_hashes:
                hits.append(f"{kit_hashes[h].relative_to(stage).as_posix()}: identical to a Run-8 live-data file")
    print(f"Run-8 byte-copy check: {checked} live-data files compared against {len(files)} kit files")
    return hits


def write_zip(stage: Path, zip_path: Path, top: str) -> int:
    if zip_path.exists():
        zip_path.unlink()
    files = kit_files(stage)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, f"{top}/{p.relative_to(stage).as_posix()}")
    return len(files)


def install_into(stage: Path, target: Path, dry_run: bool) -> None:
    if not target.is_dir():
        die(f"{target} is not a folder")
    plan: list[tuple[Path, str]] = []
    for p in kit_files(stage):
        rel = p.relative_to(stage).as_posix()
        at_claude = rel.startswith(".claude/agents/") or rel.startswith(".claude/skills/")
        plan.append((p, rel if at_claude else f"{PACK_DIR}/{rel}"))
    claimed = {f"{PACK_DIR}/"} | {"/".join(d.split("/")[:3]) + "/" for _, d in plan if d.startswith(".claude/skills/")}
    clashes = sorted({c for c in claimed if (target / c).exists()} | {d for _, d in plan if (target / d).exists()})
    if clashes:
        for c in clashes:
            print(f"  already in the workspace: {c}", file=sys.stderr)
        die(f"{len(clashes)} name(s) would clash; nothing was written")
    for src, dest in plan:
        out = target / dest
        if dry_run:
            print(f"would add {dest}")
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if dest.startswith(".claude/") and src.suffix == ".md":
            text = src.read_text(encoding="utf-8")
            out.write_text(ADDON_PATH.sub(PACK_DIR + r"/\1", text), encoding="utf-8", newline="\n")
        else:
            shutil.copy2(src, out)
    verb = "would add" if dry_run else "added"
    print(f"{verb} {len(plan)} files to {target}: agents and skills in .claude/, the rest in {PACK_DIR}/")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--edition", choices=["public", "premium"],
                    default="premium" if PREMIUM.is_dir() else "public")
    ap.add_argument("--out", type=Path, default=HERE / "dist")
    ap.add_argument("--run8-dir", type=Path, default=None,
                    help="the Run-8 live-data folder (or set FINANCE_KIT_RUN8_DIR); skipped when neither is given")
    ap.add_argument("--copy-to", type=Path, default=None, help="also copy the finished zip here")
    ap.add_argument("--into", type=Path, default=None, help="add the team to this workspace folder instead of zipping")
    ap.add_argument("--dry-run", action="store_true", help="with --into: list what would be added, write nothing")
    ap.add_argument("--fence-file", type=Path, default=None,
                    help="private words, one per line, never in the kit (or set FINANCE_KIT_FENCE_FILE); "
                         "skipped when neither is given; required for the premium edition")
    ap.add_argument("--names-file", type=Path, default=None,
                    help="client names, one per line, never in the kit (required for the premium edition)")
    args = ap.parse_args()

    names = read_names(args.names_file) if args.names_file else None
    fence = read_fence(args.fence_file)
    if args.edition == "premium":
        if not names:
            die("the premium edition needs --names-file with at least one client name; nothing written")
        if not fence:
            die("the premium edition needs --fence-file (or FINANCE_KIT_FENCE_FILE); nothing written")
        private_remote_guard()
    top = ZIP_NAMES[args.edition]
    stage = args.out / top
    args.out.mkdir(parents=True, exist_ok=True)
    assemble(stage, args.edition)
    hits = leak_scan(stage, find_run8(args.run8_dir), names, fence)
    hits += repo_scan(fence)
    if args.edition == "public":
        hits += public_guard(stage)
    if hits:
        for h in hits:
            print("  " + h, file=sys.stderr)
        die(f"{len(hits)} leak-scan hit(s); nothing written")
    print(f"leak scan: 0 hits ({args.edition} edition)")
    if args.into:
        install_into(stage, args.into.resolve(), args.dry_run)
        return
    zip_path = args.out / f"{top}.zip"
    n = write_zip(stage, zip_path, top)
    print(f"wrote {zip_path} ({n} files, {zip_path.stat().st_size} bytes)")
    if args.copy_to:
        args.copy_to.mkdir(parents=True, exist_ok=True)
        dest = args.copy_to / zip_path.name
        if dest.exists():
            n = 1
            while True:
                prev = dest.with_name(f"{dest.stem}-prev{n if n > 1 else ''}{dest.suffix}")
                if not prev.exists():
                    break
                n += 1
            dest.rename(prev)
            print(f"kept the earlier zip as {prev.name}")
        shutil.copy2(zip_path, dest)
        print(f"copied to {dest}")


if __name__ == "__main__":
    main()
