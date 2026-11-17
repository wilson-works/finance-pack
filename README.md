# WilsonWorks Finance Pack

An eight-person finance team for Claude: a controller (Hal) and two accountants (Lila and Theo), a treasurer
(Imani), a tax director (Anya), an FP&A director (Nadia), a CFO (Elle) and an assistant who routes questions
(Soph). It comes with a practice company, so you can try a month-end close before you use it on your own books.

The team finds, explains and recommends. It never moves money, posts to the books, or files anything: a person
decides and acts. There is no QuickBooks connection. You work from CSV exports.

You can use the pack two ways: **on its own**, as a folder you open in the Claude desktop app, or **as an add-on**
to a WilsonWorks Workspace you already have.

You need Python 3 (`python3` on a Mac, `python` on Windows). Nothing else to install.

## Way 1: on its own

1. Get this repo: **Code → Download ZIP** on GitHub, then unzip it. Or `git clone https://github.com/wilson-works/finance-pack`.
2. Open a terminal in the folder and run:

   ```
   python build_kit.py
   ```

   It checks every file, then prints `leak scan: 0 hits` and writes `dist/WilsonWorks-Finance-Kit.zip`.
3. Unzip `WilsonWorks-Finance-Kit.zip` wherever you keep your work (double-click on a Mac, **Extract All** on
   Windows).
4. In the Claude desktop app, open the `WilsonWorks-Finance-Kit` folder.
5. Open `Start-Here.html` in your browser and follow it. Your first ask can be: "Hal, walk me through closing last
   month for the sample company."

## Way 2: add it to your Workspace

This adds the eight teammates and their five skills to a Workspace you already have. It never changes a file that is
already there.

1. Get this repo, as in step 1 above.
2. See what it would add, without writing anything:

   ```
   python build_kit.py --into <your workspace folder> --dry-run
   ```

3. Add it:

   ```
   python build_kit.py --into <your workspace folder>
   ```

   - The teammates go in your workspace's `.claude/agents/`, and the skills (`close-month`, `cash-flow-snapshot`,
     `month-end-prep`, `invoice-chase`, `plan-payroll`) go in `.claude/skills/`.
   - The guide, the practice company, the `outputs/` folder and the message board go in `packs/finance/`.
   - If any of those names is already in your workspace, it stops, names the file, and writes nothing. Rename or
     move your file, then run it again.
4. Open your workspace in Claude and ask by name: "Hal, walk me through closing last month for the sample company."
   The team's guide is `packs/finance/CLAUDE.md`, and the walkthrough is `packs/finance/Start-Here.html`.

## What's in the repo

| | |
|---|---|
| `kit/` | the kit itself: `CLAUDE.md`, `Start-Here.html`, the eight agent files and their references, the five skills, the message board, `sample-company/` and `outputs/` |
| `build_kit.py` | builds the zip or adds the team to a workspace. Before it writes anything it checks every file for things that must never ship (computer paths, client codes, settings files, and the words in a private list given with `--fence-file`) and refuses on any hit |
| `proof/` | a recorded run of the kit: what Hal produced for the practice company's September close |

## Two more build checks

- `python build_kit.py --names-file <file>` also checks every file against a list of names, one per line, that the
  kit must never contain (matched as whole words, in any case). Any match stops the build, and the report gives
  only the name's number in your list, never the name.
- `python build_kit.py --copy-to <folder>` also copies the finished zip there. It never overwrites: a zip already in
  that folder is renamed with a `-prev` suffix first.

There is a premium edition with the firm reference library (IRS, Drake, tax and bookkeeping) and the tax skills. It
is private, for WilsonWorks clients.
