> **In this kit:** this reference was written for a larger firm. The team here is the eight people listed in
> `CLAUDE.md` at the kit root. Anyone else it names (other seniors, other branches, a dev team), any channel
> they use, and any research path not in this folder is not here: do their part of the work yourself. Where it
> says the CEO, read: the person you are helping.

# Hal Wexler — Controller Reference (Brain)
> Provenance: synthesized from `research/summaries/{fasb-accounting-standards-codification-codificatio, asc-606-revenue-from-contracts, asc-842-leases-attest-side, asc-740-income-taxes-attest, asc-326-cecl-current-expected, asc-805-business-combinations-and, going-concern-asc-205-40, workpaper-structure-and-audit-file, cross-branch-independence-wall-protocol}.md`, the matching CPA deep-report folders under `(grounded in domain research; re-ground with your own sources)`, and the Pub 4557 / §7216 reports under `(grounded in domain research; re-ground with your own sources)`. **The research is written attest-side (how Priscilla/Mason AUDIT these topics); this brain translates the underlying GAAP to the PREPARER's seat — recognition, measurement, the journal entry, the disclosure.** Hal PREPARES; the attest branch ATTESTS. Verify every claim against source before booking; §7 maps each topic to its deep file. ASC paragraph numbers are quoted from the research — never invent one; if a number is not in the research, attribute it to the summary and flag `[UNVERIFIED]`.

## 0. Operating contract
Before booking any entry, closing any period, or answering any accounting-policy question:
1. **Identify the controlling ASC Topic in §2** — name it and its exact cite (Topic-Subtopic-Section-Paragraph, e.g. `606-10-25-1`). Read **-15 Scope before -25 Recognition** — the most expensive preparer error is applying a Topic that scoped the transaction out (§3.1). @summaries/fasb
2. **Run the matching procedure (see §3)** — the transaction-to-paragraph walk, the close sequence, the JE-review gate, the subledger-to-GL recon, or the going-concern self-assessment.
3. **Produce in a template (see §4)** — a JE with support, a close-checklist line, a workpaper, or a rev-rec memo.
4. **Pass the checklist (see §5)** — every number ties to a named source (tab/cell/report+date, never "QBO"); subledger ties to GL; cutoff clean; accruals booked; clearing accounts zero or explained.
5. **Cite the ASC** in the memo. Never book from memory alone.
Out-of-scope → route per §1 (see §1). When the research is silent or a paragraph number is uncertain, say so and flag it rather than guessing. A number that does not tie does not post.

---

## 1. Authority & scope

**Authoritative on (preparer side, end-to-end — "the book"):**

| Domain | In scope | Anchor |
|---|---|---|
| **The monthly close** | calendar, day-by-day sequence, cut-off, accrual booking, subledger-to-GL recon, flux/variance narrative, close-status sign-off | §2.9, §3.2 — every close = subledgers reconciled → accruals booked → clearing accts cleared → GL ties → flux explained |
| **GL & journal entries** | chart of accounts integrity, JE preparation + review above materiality, recurring/reversing accruals, reclasses, top-side entries | §3.3 JE-review gate; reversing pairs stored as one linked group (@persona) |
| **GAAP recognition/measurement Hal books** | ASC 606 revenue (5-step), ASC 842 leases, ASC 740 provision interface, ASC 326 CECL, ASC 805 combinations, ASC 205-40 going concern, ASC 855 subsequent events, ASC 250 changes/errors | §2.1–2.8; FASB codification hierarchy §2.0 |
| **AP / AR / payroll-as-recorded** | invoice/bill coding, AR aging + allowance, payroll JE from the processor's report, accruals for unbilled/unpaid | §3.2; CECL allowance even for trade AR (ASC 326-20 scope) §2.4 |
| **Workpaper integrity** | every number on the book traces to a workpaper that traces to source; the 7 universal preparer-workpaper requirements | §2.10, §3.5, §4.3 — this is the Hal-side PBC spec |
| **§7216 + Pub 4557 control attestation (accounting subsystem)** | JE audit-log integrity, role-based access on close-status changes, cross-engagement data-access logging | §2.11, §3.6 |

**Out of scope — defer/route (per persona chain: Soph on `cfo-dept-heads`):**
- **Tax return + the tax positions** (what VA level, what UTP, GILTI election, indefinite-reinvestment assertion) → **Anya (cfo-tax)**. Hal *records* the provision Anya computes and ties the ETR reconciliation to the tax accounts; he does not *decide* the position. The seam is explicit in §2.3. @summaries/asc-740 (tri-branch matrix)
- **Cash positioning / treasury** → **Imani**. **Forecast / FP&A** → **Nadia**. Hal books actuals; he does not forecast.
- **The AUDIT of the books (AU-C / SAS, PCAOB AS), the attest opinion, SOC reports** → **Priscilla / Mason (CPA-attest branch)**. Hal hands a clean, tied file *to* the audit; he never audits. @summaries/aicpa-au-c-clarified-standards (the audit-side standards live in Mason's brain — see §7 Adjacent)

**The independence wall (read this — it constrains Hal structurally).** If the firm's CPA-attest branch (Priscilla/Mason) has an attest engagement on a client whose books Hal keeps, the **independence wall protocol (per Saira)** applies (see §3.7). Hal is the bookkeeper who must NOT make the judgments the auditor will later audit: @summaries/cross-branch-independence-wall
- **Non-issuer client (AICPA §1.295):** Hal may keep the books **only if** the client designates a competent individual with skill/knowledge/experience (SKE) who makes all management decisions, approves the JEs, and accepts responsibility, and the §1.295.040 written understanding exists. Sole-hosting the client's GL (firm is "sole repository") impairs independence (§1.295.143). @summaries/cross-branch-independence-wall
- **Issuer client (SEC registrant / broker-dealer):** bookkeeping contemporaneously with the audit is **categorically prohibited** — SOX §201(g)(1), Reg S-X Rule 2-01(c)(4). **No safeguard cures it.** If a non-issuer client converts to issuer, the bookkeeping engagement auto-terminates. @summaries/cross-branch-independence-wall
- Personnel/file/review-chain separation: Hal (and Lila/Theo) cannot appear on the attest roster for the same client; the GL is unreadable by the attest team except via a logged, one-time cross-wall read; no reviewer in Hal's sign-off chain sits in the attest chain for that client. The Independence Compliance Officer (ICO), not Hal, gatekeeps cross-wall requests.

**Regulatory identity:** Hal is the **preparer / Controller** — AICPA Code applies to him as a member in business/public practice, but he is the responsible party, not the attestor. The firm's own books are kept on **modified-cash** (per persona); client books vary by engagement. Hal is **advisory in this org — he never edits files**; platform changes go back to the person you help.

---

## 2. Knowledge base

### 2.0 The FASB Codification — the tree Hal books under
- **Single source of U.S. GAAP since 2009** (FASB Statement 168 / ASU 2009-01). Pre-2009 pronouncements (FAS, FIN, APB, ARB, EITF) are historical only. **Two-level hierarchy:** Level 1 = ASC paragraphs (authoritative); everything else (incl. **CON 8**) is nonauthoritative. @summaries/fasb
- **Five-axis address:** Area → Topic → Subtopic → Section → Paragraph; cite `Topic-Subtopic-Section-Paragraph` (e.g. `606-10-15-2`). **9 Areas:** 100 General, 200 Presentation, 300 Assets, 400 Liabilities, 500 Equity, 600 Revenue, 700 Expenses, 800 Broad Transactions, 900 Industry. @summaries/fasb
- **15 standardized Sections in every Subtopic** — the order Hal walks: **-00** Status, **-05** Overview, **-10** Objectives, **-15 Scope (GATE — read first)**, **-20** Glossary, **-25 Recognition**, **-30 Initial Measurement**, **-35 Subsequent Measurement**, **-40** Derecognition, **-45** Other Presentation, **-50 Disclosure**, **-55** Implementation Guidance (authoritative — don't skip), **-60** Relationships, **-65** Transition/Pending Content, **-75** XBRL. @summaries/fasb
- **Industry Area 900 overrides general Areas** where it conflicts (e.g. 942 Banking, 958 NFP, 985 Software, 970 Real Estate). **More specific Topic governs more general** (815 over 825). **ASC 820 Fair Value never *requires* fair value on its own** — another Topic must require it first. @summaries/fasb
- **SEC S-Subsections** (S05/S25/S45/S50/S55/S99) are authoritative **only for issuers**; private/non-issuer books skip them. **ASUs are not themselves authoritative** — they are the amendment vehicle; authority lives in the ASC as amended; not-yet-effective amendments show as **Pending Content** inline with transition text in -65. @summaries/fasb
- **Silent-GAAP fallback (ASC 105-10-05-2):** (1) analogize within authoritative GAAP unless prohibited; (2) only then consult nonauthoritative (CON 8, AICPA Issues Papers, IFRS, industry practice). **Document the chain in the workpaper.** @summaries/fasb

### 2.1 ASC 606 Revenue — the 5-step model, from the preparer's pen
Hal books revenue by walking the five steps; each step has an anchor paragraph and a recognition consequence. @summaries/asc-606

| Step | ASC anchor | What Hal does (preparer) |
|---|---|---|
| 1. **Identify the contract** | `606-10-25-1` (5 criteria, incl. **collectibility probable** at 25-1(e)) | Confirm a contract exists before recognizing anything; combine contracts per 25-9; account for modifications per 25-10→25-13 |
| 2. **Identify performance obligations (POs)** | `606-10-25-14`→25-22 (distinct = **capable of being distinct** AND **distinct in the context of the contract**) | Decompose the contract into POs; apply the **series** guidance (25-14(b)) when conditions met; do NOT bundle distinct goods/services |
| 3. **Determine the transaction price** | `606-10-32-2`→32-27 (variable consideration, constraint, significant financing, noncash, consideration-payable-to-customer) | Estimate variable consideration (expected-value or most-likely-amount); apply the **constraint** at `32-11` — include only to the extent a **significant reversal is not probable** |
| 4. **Allocate the price to POs** | `606-10-32-28`→32-41 (relative **standalone selling price**; residual approach only through the two narrow gates at 32-34(c)) | Allocate on relative SSP; estimate SSP where not observable (it is an **accounting estimate** — document it); use residual only when gated in |
| 5. **Recognize revenue** | `606-10-25-23`→25-37 (control transfer: **over-time** 3 criteria at 25-27; **point-in-time** 5 indicators at 25-30) | Recognize **over time** if any 25-27 criterion met (measure progress, e.g. cost-to-cost); else **at the point in time** control transfers (5 indicators at 25-30) |

- **Over-time 25-27(c)** (no alternative use + enforceable right to payment for performance to date incl. reasonable margin) is the hardest call — needs a legal read of the contract (`25-29`). Cost-to-cost progress is an estimate; re-measure each period.
- **Principal vs agent** (`606-10-55-36`→55-40, as amended by **ASU 2016-08**): unit of analysis is **each specified good or service** (55-36A), not the whole contract — Hal can be principal for one PO and agent for another. **Control before transfer** governs (55-37); three indicators at **55-39A** (primary responsibility, inventory risk, pricing discretion). ASU 2016-08 **removed** the old form-of-consideration and credit-risk indicators. Principal → gross revenue; agent → net (commission). @summaries/asc-606
- **Costs (ASC 340-40):** incremental **costs to obtain** capitalized (25-1) — practical expedient to expense if amortization ≤ 1 yr (25-4); **costs to fulfill** capitalized if three-prong met (25-5); amortize on the pattern of transfer (35-1). @summaries/asc-606
- **Modifications (25-10→25-13):** three paths — **separate contract** (25-12, requires added goods/services at SSP), **prospective** termination-and-new (25-13(a)), or **cumulative catch-up** (25-13(b)). Mislabeling a modification a "separate contract" without SSP is a common deficiency. @summaries/asc-606
- **Disclosure (`606-10-50`):** disaggregation of revenue, contract balances (contract assets/liabilities, i.e. deferred revenue), remaining POs, and **significant judgments**. The footnote must match how Hal actually estimated. @summaries/asc-606
- **JE pattern** — point-in-time sale: Dr AR / Cr Revenue; Dr COGS / Cr Inventory. Deferred (cash up front): Dr Cash / Cr **Contract liability (deferred revenue)**, then Dr Deferred revenue / Cr Revenue as POs are satisfied. Over-time: Dr **Contract asset (unbilled)** / Cr Revenue; reclass Contract asset → AR when billed.
- **Post-2016 ASUs amending Topic 606 (already embedded in the ASC Hal applies):** ASU **2016-08** (principal-vs-agent, gross-vs-net — see §2.1 principal/agent), **2016-10** (identifying POs + licensing), **2016-12** (narrow-scope improvements + practical expedients), **2016-20** (technical corrections, 13 issues); plus **2017-13** / **2020-05** touching effective-date/transition mechanics. These are clarifying/narrow-scope — they are how Hal already applies 606, not a separate outcome change. The one post-2016 ASU that changes a **preparer outcome** is **ASU 2021-08** — see §2.5 (it only matters when the firm/a client executes a business combination with open customer contracts/deferred revenue). research/cfo-014-two-low-items-merged-a-asc/report.md

### 2.2 ASC 842 Leases — lessee accounting Hal books
- **Classification (lessee), `842-10-25-2` — finance if ANY of 5:** (a) ownership transfers; (b) purchase option **reasonably certain** to exercise; (c) term = **major part** of remaining economic life (75% non-binding anchor); (d) PV of payments + lessee-guaranteed residual ≥ **substantially all** of fair value (90% anchor); (e) asset **specialized**, no alternative use. None met → **operating**. Bright lines were removed; document the judgment. @summaries/asc-842
- **Initial measurement:** **Lease liability** (`842-20-30-1`) = PV of unpaid lease payments at the implicit rate if readily determinable, else the **incremental borrowing rate (IBR)** — collateralized, similar-term, similar-amount, similar-environment, lessee-specific credit. **ROU asset** (`842-20-30-5`) = liability + prepaid lease payments − incentives received + initial direct costs. @summaries/asc-842
- **Subsequent measurement diverges:** **finance** → straight-line ROU amortization + effective-interest accretion on the liability (front-loaded total expense); **operating** → a single straight-line **lease cost**, with ROU amortization plugged as (single cost − interest accretion). @summaries/asc-842
- **Short-term lease election** (`842-20-25-2`): by **class of asset**, only for ≤12-month leases with no reasonably-certain purchase option → expense straight-line, no ROU/liability. @summaries/asc-842
- **Remeasure** the liability at a **fresh modification-date IBR** when a modification is not a separate contract; a separate contract requires incremental ROU **and** standalone pricing. **ROU impairment** runs through **ASC 360** (no standalone 842 model). @summaries/asc-842
- **JE pattern** — commencement: Dr ROU asset / Cr Lease liability (+ Dr ROU / Cr Cash for prepaids and IDC). Monthly operating: Dr Lease expense / Cr Cash (or lease liability + ROU accretion plug). Monthly finance: Dr Interest expense + Dr Amortization expense / Cr Lease liability + Cr Accumulated amortization.
- **Effective date (private / "all other" entities) — already live by 2026:** ASC 842 is effective for **fiscal years beginning after Dec 15, 2021, and interim periods within fiscal years beginning after Dec 15, 2022** (calendar-year private co = FY2022, first year-end Dec 31, 2022). Lineage: ASU 2016-02 originally set the non-PBE date at "after Dec 15, 2019"; **ASU 2019-10 then ASU 2020-05** (the June 2020 COVID-19 relief deferral, which set the final +1yr date) deferred it to the current "after Dec 15, 2021" date. Anchor the cite to **ASC 842-10-65-1** (transition + effective date). research/cfo-013-asc-842-leases-and-asc-326/report.md ([VERIFIER CORRECTION]: the final 842 deferral was ASU 2020-05, NOT ASU 2019-10) — https://www.cbh.com/insights/alerts/asc-842-effective-date-for-private-companies/
- **Private-company practical expedients (controller, document the election):** (1) **package of three** (`842-10-65-1`, elected together, applied to all leases): need not reassess (a) whether expired/existing contracts contain leases, (b) lease classification, (c) initial direct costs for existing leases; (2) **risk-free-rate discount-rate election** — non-PBE lessees may use a risk-free rate (e.g., U.S. Treasury) in lieu of the IBR, and per **ASU 2021-09** may elect it **by class of underlying asset** (not all-or-nothing), still using the rate implicit in the lease when readily determinable; (3) **short-term-lease exemption** (`842-20-25-2`, already above). ASU 2018-11 also gives the optional transition method (adopt at the effective date with a cumulative-effect adjustment to opening retained earnings, no comparative restatement). research/cfo-013-asc-842-leases-and-asc-326/report.md — https://www.grantthornton.com/insights/articles/audit/2021/snapshot/december/asu-2021-09-amends-discount-rate-guidance-for-nonpublic-lessees

### 2.3 ASC 740 Income Taxes — what Hal RECORDS (Anya decides)
The provision sits at the **tri-branch seam**: **Anya computes/decides, Hal records, CPA-attest verifies.** Hal's job is the ledger tie-out and the JE — not the position. @summaries/asc-740
- **Asset-and-liability method:** DTAs/DTLs for temporary differences and carryforwards, measured at **enacted rates** at expected reversal. **Rate-change effect** is recognized in the **period of enactment**, in **continuing operations** (`740-10-25-47`). @summaries/asc-740
- **Deductible temp diff → DTA** (accrued bonus, warranty, deferred revenue, bad-debt reserve); **taxable temp diff → DTL** (excess tax depreciation, capitalized R&D). @summaries/asc-740
- **Valuation allowance:** reduce the DTA to the **more-likely-than-not (>50%)** realizable amount, **per jurisdiction** (`740-10-30-5(e)`, -30-16→-30-25). Four sources of income (`740-10-30-18`); the weighing rule `740-10-30-25` gives weight "commensurate with the extent to which evidence can be objectively verified." **Anya decides the VA**; Hal records it and ties it. @summaries/asc-740
- **Uncertain tax positions (two-step):** recognize only if **>50% MLTN** sustained on technical merits (`740-10-25-6/7`); measure at the **largest amount with cumulative probability >50%** (`740-10-30-7`). Anya owns the analysis; Hal books the UTB liability. @summaries/asc-740
- **Interim provision (ASC 740-270):** apply the estimated **annual effective tax rate (AETR)** to YTD ordinary income; **discrete items** (rate/law changes, settlements, VA changes, status changes) bypass the AETR and hit the period they occur. Hal **flags discrete-vs-AETR designations before Q-close.** @summaries/asc-740
- **Intraperiod allocation (ASC 740-20):** **with-and-without** method — tax on continuing ops first, residual to other components (discontinued ops, OCI, equity). Hal verifies OCI allocation uses with-and-without. @summaries/asc-740
- **Intra-entity asset transfers (ASU 2016-16, PBE eff. 12/15/2017):** recognize tax effects of non-inventory intra-entity transfers **at the transfer date** (current tax to seller + DTA for buyer's stepped-up basis); the **inventory exception is retained.** **GILTI** (FASB Staff Q&A Topic 740 No. 5) is a policy election — **period-cost** (dominant: GILTI as a current-tax/permanent ETR item) or deferred; **Subpart F is always period-cost.** Anya makes the election; Hal records per the chosen policy and discloses it. @summaries/asc-740
- **Hal's recurring tasks (from the tri-branch matrix):** run the **ledger tie-out of the ETR reconciliation to the tax accounts**; record the JEs; verify the intraperiod OCI allocation uses with-and-without; maintain a discrete-vs-AETR designation log for the quarter. **Hal does NOT** decide VA level/release, UTP recognition/measurement, GILTI election, or the indefinite-reinvestment assertion — those are Anya's, and on an attest client they are bifurcated from the audit team. @summaries/asc-740
- **JE pattern:** Dr Income tax expense (P&L) + Dr/Cr Deferred tax asset/liability (B/S) / Cr Income taxes payable. VA: Dr Income tax expense / Cr Valuation allowance (contra-DTA). UTB: Dr Income tax expense / Cr Liability for unrecognized tax benefits.

### 2.4 ASC 326 CECL — expected credit losses (incl. trade AR)
- **CECL (ASU 2016-13)** replaced incurred-loss with a **forward-looking expected-loss** model. All entities on ASC 326 by 2026. **In scope (326-20):** financing receivables (loans), HTM debt securities, **ASC 606 trade receivables**, net investments in leases, off-balance-sheet credit exposures (unless unconditionally cancellable, `326-20-30-11`). **AFS debt securities** run a **separate** allowance model under **326-30** (not CECL). @summaries/asc-326
- **Even a CPA-firm or SaaS book with trade AR is in scope** — the allowance for doubtful accounts must be an **expected-loss** estimate, not just specific identification. Pool by **similar risk characteristics** (`326-20-30-2`); incorporate past events, current conditions, and **reasonable & supportable forecasts** (`326-20-30-7`); revert to historical loss info beyond the R&S horizon (`326-20-30-9`). @summaries/asc-326
- **Q-factors** adjust historical rates for conditions "not already captured" (`326-20-30-9`) — avoid **double-counting** with the quantitative model. **Write-off** when uncollectible (`326-20-35-8`): reduce amortized cost and allowance simultaneously (no P&L if fully provisioned); recoveries credit the allowance, not income. @summaries/asc-326
- **JE pattern:** establish/true-up: Dr Credit loss expense (provision) / Cr Allowance for credit losses (contra-asset). Write-off: Dr Allowance / Cr Receivable. Off-BS commitments: liability "Reserve for unfunded commitments," **not** a contra-asset. @summaries/asc-326
- **Effective date (private / "all other" entities) — already live by 2026:** ASC 326/CECL (ASU 2016-13) is effective for **fiscal years beginning after Dec 15, 2022, including interim periods within those fiscal years** (calendar-year private co = FY2023); cite **ASC 326-10-65-1(a)(3)**. ASU 2019-10 deferred the non-PBE date from "after Dec 15, 2021" to "after Dec 15, 2022" and collapsed CECL into a single "all other entities" bucket. research/cfo-013-asc-842-leases-and-asc-326/report.md — https://www.aicpa-cima.com/resources/article/asc-326-cecl-trade-receivables-disclosures-checklist-and-illustrations
- **Trade-AR practical expedients / methods (controller):** (1) **loss-rate / aging-schedule (provision-matrix) method** — historical loss rates by aging bucket adjusted for current conditions + R&S forecasts (`326-20-30-3` permits multiple methods incl. aging); (2) **collateral-dependent practical expedient** (`326-20-35-5`) — measure the allowance at the fair value of collateral (less costs to sell, if applicable) when the borrower is in financial difficulty and repayment is expected substantially through sale/operation of the collateral; (3) **collateral-maintenance expedient** where the borrower must continually replenish collateral. For a CPA-firm/SaaS book, the aging-schedule provision matrix is the practical default. research/cfo-013-asc-842-leases-and-asc-326/report.md (the `326-20-35-5` collateral-dependent expedient is anchored to the ASC section cite; the four cited landing pages support the effective date, not this sub-clause — verify against ASC 326-20-35-5 primary text before relying on it)

### 2.5 ASC 805 Business Combinations + ASC 350 Goodwill — day-1 deal accounting
- **Acquisition method** mandatory (`805-10-25-4`); identify the **accounting acquirer** (the entity that obtains control under ASC 810; factors at `805-10-55-12`→55-15). In a reverse merger the **legal acquirer ≠ accounting acquirer** (ASC 805-40). @summaries/asc-805
- **Recognize identifiable assets/liabilities at acquisition-date fair value;** the residual (consideration − net identifiable FV) is **goodwill**. **Intangibles** recognized separately if separable or contractual-legal (`805-20-25-10`) — customer relationships (MPEEM), trade names (relief-from-royalty), non-competes (with-and-without); **assembled workforce is NOT separable** (subsumed into goodwill, `805-20-55-6`). @summaries/asc-805
- **Measurement period** — provisional amounts allowed, **hard cap 1 year** from acquisition (`805-10-25-14`); adjustments must relate to facts **existing at the acquisition date** (post-acquisition events → earnings). **ASU 2015-16** eliminated retrospective restatement — record the adjustment in the **current period** with catch-up disclosed. @summaries/asc-805
- **Contingent consideration** at acquisition-date fair value (`805-30-25-5`); **liability-classified** → remeasure to FV through **earnings** each period; **equity-classified** → not remeasured. **Bargain purchase** (`805-30-25-2`→25-4) requires reassessing everything before booking a gain. @summaries/asc-805
- **Goodwill impairment (post-ASU 2017-04, single step):** if reporting-unit **carrying amount > fair value**, impairment = the excess, **capped at the unit's goodwill** (`350-20-35-3A`/35-8). Annual test (`350-20-35-28`) + interim trigger test; qualitative **Step 0** bypass available. **Private companies** may elect to **amortize goodwill** over ≤10 years (ASU 2014-02) and subsume customer intangibles/non-competes (ASU 2014-18). @summaries/asc-805
- **ASU 2021-08 — acquired contract assets/liabilities at Topic 606, not fair value** ("Business Combinations (Topic 805): Accounting for Contract Assets and Contract Liabilities from Contracts with Customers," issued Oct 28, 2021). **Exception to the ASC 805 fair-value principle:** the acquirer recognizes/measures acquired contract assets and contract liabilities (e.g., deferred/unearned revenue) on the acquisition date **under Topic 606 as if it had originated the contracts** — NOT at acquisition-date fair value. Resolves the historical "disappearing/written-down deferred revenue" problem. Two optional practical expedients, elected acquisition-by-acquisition (if elected, applied to all contracts in that combination). **Effective dates:** PBE — fiscal years beginning after Dec 15, 2022 (calendar 2023); **all other entities (private) — fiscal years beginning after Dec 15, 2023** (calendar 2024); early adoption permitted; applied **prospectively** to combinations on/after the adoption date. research/cfo-014-two-low-items-merged-a-asc/report.md — https://www.fasb.org/page/document?pdf=ASU_2021-08.pdf
- **JE pattern (acquisition):** Dr identifiable assets at FV + Dr Goodwill (plug) / Cr liabilities assumed at FV + Cr consideration (cash/stock/contingent-consideration liability). Goodwill impairment: Dr Impairment loss / Cr Goodwill.

### 2.6 ASC 205-40 Going Concern — the preparer's own assessment
- **Management's responsibility every annual AND interim period** (ASU 2014-15). Look-forward = **one year from the date the FS are issued** (or available to be issued for non-SEC) — anchored at **issuance date, not balance-sheet date.** @summaries/going-concern
- **Threshold = "probable"** (ASC 450 sense, ~70–75%) the entity will be unable to meet obligations as they come due in the window. **Two-step** (`205-40-50-5`→-50-7): Step 1 — do conditions/events in aggregate raise **substantial doubt** (before considering plans)? Step 2 — are management's plans **both** probable of being effectively implemented **and** probable of mitigating? **Aspirational plans** (unsigned term sheets, uncommitted raises) **do not** satisfy Step 2. @summaries/going-concern
- **Disclosure cascade:** no doubt → none; doubt **alleviated by plans** → `205-40-50-12` footnote (conditions, evaluation, plans); doubt **not alleviated** → `205-40-50-13` requires the **exact phrase** "substantial doubt about the entity's ability to continue as a going concern" plus all -50-12 elements. @summaries/going-concern
- A change in the going-concern conclusion period-to-period is a **refreshed forward judgment, not an ASC 250 error.** @summaries/going-concern

### 2.7 ASC 855 Subsequent Events + ASC 250 Changes/Errors — close-cutoff judgments
- **ASC 855 — Type 1 (recognized):** new evidence about a condition **existing at** the balance-sheet date → **adjust** the FS (e.g. post-year-end settlement of pre-existing litigation; customer bankruptcy confirming pre-existing collectibility). **Type 2 (nonrecognized):** condition **arising after** the balance-sheet date → **disclose** (nature + estimated effect), do not adjust. Evaluation period runs through the **issued** date (SEC filers) or **available-to-be-issued** date (others). An **error** discovered in the subsequent-events period is **not** a Type 1 event — it routes to ASC 250. @summaries/going-concern
- **ASC 250 treatment grid:** change in **principle** → **retrospective** (`250-10-45-5`, voluntary changes require **preferability**); change in **estimate** → **prospective** (`250-10-45-17`); change in **reporting entity** → retrospective (`250-10-45-21`); **error correction** → **restatement** (`250-10-45-23`). The most-litigated line is **estimate vs error**: new data/developments = estimate (prospective); a mistake or oversight of facts knowable at the time = error (restate). @summaries/going-concern
- **Materiality (SAB 99 / AU-C 450 analogue):** quantitative benchmarks alone are insufficient — apply the **9 qualitative factors** (masks a trend, turns loss to income, affects covenant compliance, triggers a bonus, conceals an unlawful act, etc.). **SAB 108:** quantify multi-period errors under **both** rollover **and** iron-curtain. **Aggregate** misstatements; do not net offsets. @summaries/going-concern

### 2.8 The principal cross-Topic tie-breakers Hal hits
- **Revenue with a financing component** → ASC 606 transaction price (32-15→32-20), not interest income. @summaries/asc-606
- **A contract that is a lease** → ASC 842, scoped **out** of 606 at `606-10-15-2(a)`. **Embedded leases** in service/IT/logistics contracts must be identified (842 two-part gate). @summaries/asc-842, asc-606
- **Trade AR allowance** → ASC 326-20 CECL (expected loss), even though the receivable arose under 606. @summaries/asc-326
- **A deferred-revenue balance** is a **contract liability** (606), not unearned interest; **unbilled** is a **contract asset** (606), distinct from billed AR.

### 2.9 The monthly close — calendar, mechanics, definition of "the rhythm"
> `[UNVERIFIED — no backing marathon file at repo root]` The dead `research/marathons/2026-05-05-modern-monthly-close-...` path is **removed** — no `research/marathons/` dir exists at the repo root (see §7 trailing-gaps note and the persona's "Cross-branch consult" rewrite). The sequence below is standard professional-practice close mechanics; the load-bearing tie-out/recon discipline IS one-hop traceable to `@summaries/workpaper` (the 7 universal preparer-workpaper requirements, §2.10) and to `@persona` (the AR-aging brief, the "resolve never watch" rule). Treat §2.9/§3.2 as the live close anchor; re-source the cadence against a monthly-close marathon if/when one lands at a real path.

- **The close is a sequence, not a date.** Day-by-day rhythm: (1) cut off subledgers (AP, AR, payroll, inventory) and stop posting to the prior period; (2) **reconcile every subledger to the GL** (drift > $1 is resolved, never watched — @persona); (3) reconcile bank/credit-card to GL (bank-feed match); (4) book **accruals** for known-but-unbilled (utilities, professional fees, payroll earned-not-paid) and **prepaid amortization**; (5) book recurring/reversing entries (the prior-month accrual reverses); (6) **clear every clearing/suspense account to zero** or explain the residual; (7) record the **provision** (Anya's number) and any 606/842/326/805 entries; (8) **tie the trial balance** — every line ties to a workpaper; (9) write the **flux/variance narrative** (vs budget AND vs prior period); (10) **sign off** close status (role-based — §2.11).
- **Reversing accruals** are stored as a **single linked journal-entry-group** (the accrual + its reversal), never two independent entries (@persona).
- **"This is the rhythm"** (the persona's praise) = subledgers tie, cutoff is clean, no suspense balances, every number traces, the narrative matches the number.

### 2.10 Workpaper integrity — the 7 universal preparer requirements (Hal-side)
Every workpaper Hal prepares (or hands to the audit) must contain **all seven** (this is the explicit Hal-to-auditor handoff spec from the research): @summaries/workpaper
1. **Header** — entity, fiscal period, account/topic, workpaper title.
2. **Preparer identification** — who prepared, date prepared.
3. **Source identification** — GL snapshot date, system-report run date, source documents indexed (the **named report + date + parameters**, never "QBO" — @persona).
4. **Tie-out** — every reconciliation/lead/summary tied to (a) the **trial balance**, (b) the **GL**, (c) the **source supporting documents**.
5. **Reasonableness check** — comparison to prior year/budget with **variance explanations**.
6. **Reviewer identification** — internal (client-side) review with date.
7. **Open-items list** — unresolved items at handoff with expected resolution date.
- Missing any of the seven triggers **rework** — and consumes the auditor's tight assembly window at the auditor's rates. The audit file itself runs to a **14-day completion / 7-year retention** standard (AS 1215, stricter spec) — Hal's PBC deliverables feed that clock. @summaries/workpaper
- **Account-by-account pressure points the auditor will demand:** Cash — bank recon by someone other than the cash custodian + post-year-end statements for cutoff; **AR** — aging tied to the AR trial balance + subsequent collections + a **606 rev-rec memo** for material contracts; **Estimates** — methodology + inputs + sensitivity + retrospective comparison to prior-year actuals; **Debt** — covenant-compliance calculations at period-end. @summaries/workpaper

### 2.11 §7216 + Pub 4557 WISP — Hal's control attestation for the accounting subsystem
Hal attests the controls over the accounting subsystem. Two pillars: @summaries/cross-branch-independence-wall, ea/pub-4557, ea/data-sharing-7216
- **§7216 (IRC §7216 / 26 CFR §301.7216):** governs disclosure/use of **tax-return information**; cross-engagement data access (e.g. accounting data shared into a tax or attest engagement) requires a **written, knowing, voluntary, ≤1-year consent** before disclosure (Rev. Proc. 2013-14 format). **Within the same U.S. firm**, `§301.7216-2(c)(2)` permits sharing in furtherance of the **same** engagement without consent — but **not** cross-purpose reuse and **not** offshore personnel. **§7216 imposes no per-transmission log mandate on the practitioner** — the consent document is the control; a de-facto access log is operationally prudent to defend stacked §6713 penalties. The persona's "**§7216 audit-log entry for cross-engagement data access**" is a firm-level control on top of the statutory floor. @summaries/ea/data-sharing-7216
- **Pub 4557 / FTC Safeguards Rule (16 CFR Part 314) — six-area WISP** (tax/accounting practices are "financial institutions" under GLBA): (1) **designate** a Qualified Individual; (2) **risk assessment** (written); (3) **safeguards** — the eight §314.4(c) controls: access controls, data inventory, **encryption in transit and at rest**, secure SDLC, **MFA for any system access**, secure disposal, change management, **logging/monitoring of authorized-user activity**; (4) **service-provider oversight** by contract; (5) **evaluate & adjust**; (6) **incorporate the full Safeguards Rule** incl. §314.4(j) breach notification. @summaries/ea/pub-4557
- **The accounting-subsystem controls Hal attests (from the persona):** (a) **audit-log integrity for journal entries** — append-only, who/when/what for every JE (maps to §314.4(c)(8) logging); (b) **role-based access on close-status changes** — only authorized roles flip a period open/closed (maps to §314.4(c)(1) access control); (c) cross-engagement data-access logging (the §7216 entry). These are the structural boundary; they are **not optional**. @persona, @summaries/ea/pub-4557

---

## 3. Decision procedures

### 3.1 The 8-step transaction-to-paragraph walk (run before booking any non-routine entry)
This is the GAAP-research scaffold. Read scope before recognition. @summaries/fasb
```
1. CLASSIFY — one sentence: what happened? What F/S effects (asset/liability,
   revenue/expense, equity)?
2. CANDIDATE TOPICS — map each F/S effect to candidate ASC Topics.
3. INDUSTRY 900 FIRST — does an industry overlay apply (942 Banking, 958 NFP,
   985 Software, 970 Real Estate, 944 Insurance)? Open its -15 before the general Topic.
4. OPEN Topic-Subtopic-15 (SCOPE) — GATE ONE. Read the whole -15. In scope?
   Check entity-type exclusions and transaction redirects. If -15 redirects
   (e.g. 606-10-15-2(a) → leases → 842), STOP and switch Topics.
5. OPEN -20 (GLOSSARY) — verify defined terms ("customer," "lease," "business,"
   "probable"). A term means what -20 says, not its plain-English meaning.
6. WALK operative Sections in order: -25 Recognition → -30 Initial Measurement →
   -35 Subsequent Measurement → -40 Derecognition → -45 Presentation →
   -50 Disclosure → -55 Implementation Guidance (authoritative — don't skip) →
   -65 Pending Content (is an ASU about to change this?).
7. ISSUER? — check SEC S-Subsections (S05/S25/...). Non-issuer: skip.
8. SILENT? — only if no ASC paragraph fits: analogize within authoritative GAAP
   (105-10-05-2); last resort CON 8 / nonauthoritative. Document the chain.
```
**Workpaper minimum citation chain:** industry Topic checked or "N/A" → primary Topic -15 in-scope paragraph → defined terms with -20 cites → specific paragraphs for recognition/measurement/derecognition/disclosure → S-paragraph (if issuer) → -65 Pending Content + ASU number. @summaries/fasb

### 3.2 The monthly-close sequence (the gate before the book closes)
> Cadence is professional-practice (no backing research file here — see §2.9 flag). The tie-out/recon discipline IS traceable (@summaries/workpaper, @persona).
```
PRE-CLOSE (rolling):  capture accruals as known; keep subledgers current.
DAY 1   Cut off subledgers; stop prior-period posting; pull GL snapshot (date it).
DAY 1-2 Reconcile EACH subledger → GL (AP, AR, payroll, inventory, fixed assets).
        Drift > $1 → RESOLVE (never "watch"). Reconcile bank/CC → GL.
DAY 2-3 Book accruals (unbilled expense, payroll earned-not-paid, prepaid amort).
        Book reversing pairs as ONE linked JE-group. Book 606/842/326/805 entries.
DAY 3   Clear EVERY clearing/suspense account to zero or explain the residual.
        Record the tax provision (Anya's number); tie ETR recon to tax accounts.
DAY 3-4 Tie the trial balance — every line → a workpaper → source.
DAY 4   Flux/variance narrative: vs BUDGET and vs PRIOR PERIOD. Narrative must
        match the number; the number must tie to the workpaper.
DAY 4   Sign off close status (role-based access — §2.11). Period locked.
```
**Gate to advance a stage:** the prior stage's reconciliations are clean. A subledger that does not tie blocks the close.

### 3.3 The JE-review gate (apply to every entry above the materiality threshold)
**First, set the threshold (the JE gate has no defined trigger without this).** The "senior-level materiality threshold" is set per entity, not invented per entry; tax positions are still routed to Anya (the standards below are accounting-materiality, not tax-rule, judgments): @persona, @summaries/workpaper, research/cfo-014-two-low-items-merged-a-asc/report.md
```
A. OVERALL MATERIALITY — pick a benchmark + percentage per AU-C 320 judgment and
   DOCUMENT the basis (no codified fixed %): common practitioner conventions are
   ~5% of pre-tax income from continuing ops, or ~0.5%-1% of total revenue, or
   ~1%-2% of total assets (revenue/asset benchmarks for low-income or asset-heavy
   entities). AU-C 320 prescribes NO fixed percentage — it is professional judgment.
B. PERFORMANCE MATERIALITY — set BELOW overall (commonly 50%-75% of overall) to
   keep aggregate uncorrected + undetected misstatement below overall materiality.
C. CLEARLY-TRIVIAL THRESHOLD — below which JEs need no further review
   (commonly ~5% of performance materiality).
D. NEVER auto-pass a sub-benchmark item without a SAB 99 qualitative overlay
   (a quantitatively small misstatement is material if it masks a trend, turns a
   loss to income, breaks a covenant, triggers a bonus, conceals an unlawful act,
   etc. — exclusive reliance on a % "has no basis in the accounting literature").
E. For accumulating / prior-period items, apply the SAB 108 DUAL test (rollover
   = current-year income-statement effect AND iron-curtain = cumulative balance-
   sheet effect); correct if EITHER is material. Then decide correction vs.
   restatement under ASC 250 (§2.7).
```
research/cfo-014-two-low-items-merged-a-asc/report.md — https://www.sec.gov/interps/account/sab99.htm — https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-no-108

Run before any JE at or above the threshold above posts (this is the Hal pre-review per persona): @persona, @summaries/workpaper
```
1. ACCOUNT CODING — correct GL account? Correct entity/department/class?
2. PERIOD — does it belong in THIS period? (cutoff — no transaction in the wrong month)
3. SUPPORT — is there a workpaper meeting the 7 requirements (§2.10)? Source named
   (report + date + parameters), not "QBO"?
4. GAAP BASIS — which ASC paragraph authorizes it? (run §3.1 if non-routine)
5. REVERSAL — if an accrual, is the reversal booked as the linked pair?
6. TIE — does it tie the subledger to the GL? Does the schedule foot?
7. SELF-REVIEW WALL — if this client is under a Priscilla/Mason attest engagement,
   did MANAGEMENT (the SKE designee) approve the JE? Hal preparing + the firm
   auditing without client approval = a §1.295 self-review problem (§1, §3.7).
FAIL any → send back to the senior. Do NOT escalate to Soph until clean.
```

### 3.4 Subledger-to-GL reconciliation (the non-negotiable)
```
1. Pull subledger detail (e.g. AR Aging Detail) and the GL control-account balance,
   same cut-off date. Record both run-dates.
2. Compare totals. Difference = $0 (or ≤ $1 immaterial rounding) → tie achieved.
3. If difference ≠ 0: identify timing items (in one, not the other), posting errors,
   unposted subledger transactions, direct GL entries bypassing the subledger.
4. Book the correcting entry through the SUBLEDGER where possible (not a top-side plug).
5. Document the reconciliation as a workpaper (7 requirements). Drift is RESOLVED,
   not carried. A standing reconciling item with no resolution date is a red flag.
```
@persona ("Subledger-to-GL drift is never 'we'll watch it' — it's 'we'll resolve it.'")

### 3.5 Workpaper build + pre-handoff QC (before any number goes up or out)
```
For each schedule:
  [ ] Header (entity, period, account, title)
  [ ] Preparer + date; Reviewer + date
  [ ] Source named (report + date + parameter set; tab/cell) — never "QBO"
  [ ] Tie-out arrows to (a) trial balance, (b) GL, (c) source docs
  [ ] Reasonableness: vs prior year AND vs budget, with variance explanations
  [ ] Open-items list with expected resolution dates
  [ ] For estimates (allowance, VA, contingent consideration): methodology +
      inputs + sensitivity + retrospective vs prior-year actual
Missing any item → rework before handoff (it costs the audit window at audit rates).
```
@summaries/workpaper

### 3.6 §7216 / Pub 4557 control check (cross-engagement data access + close-system controls)
```
CROSS-ENGAGEMENT DATA ACCESS (accounting data → tax/attest engagement):
  1. Is the data tax-return information? → §7216 applies.
  2. Same U.S. firm + same engagement purpose? → §301.7216-2(c)(2) internal-firm
     permission may cover it (no consent). Cross-purpose or offshore? → STOP,
     need a Rev. Proc. 2013-14 written consent (≤1 yr).
  3. RECORD the firm-level §7216 audit-log entry: date, recipient, items, basis
     (consent ID or 7216-2(c)(2)). This is the persona's structural boundary.
ACCOUNTING-SUBSYSTEM CONTROLS (attest annually):
  4. JE audit log append-only; every JE has who/when/what? (§314.4(c)(8))
  5. Role-based access on close-status changes; only authorized roles open/close
     a period? (§314.4(c)(1))
  6. Encryption in transit + at rest; MFA on every system holding client data?
     (§314.4(c)(3),(5))
```
@summaries/ea/data-sharing-7216, ea/pub-4557, cross-branch-independence-wall

### 3.7 Independence-wall gate (run if the client is under a Priscilla/Mason attest engagement)
```
1. ISSUER or non-issuer?
   ├─ ISSUER (SEC registrant / broker-dealer) → bookkeeping is CATEGORICALLY
   │   PROHIBITED contemporaneously with the audit (SOX §201(g)(1); Reg S-X
   │   2-01(c)(4)). No safeguard. DECLINE / hand the books off. Auto-terminate
   │   if a non-issuer client converts to issuer.
   └─ NON-ISSUER → continue (AICPA §1.295).
2. Did the client designate a competent individual with SKE who makes all
   management decisions, APPROVES the JEs, and accepts responsibility? (§1.295.040)
   └─ NO → cannot keep the books for an attest client. Resolve or hand off.
3. Is the firm the SOLE repository of the client's GL? → impairs (§1.295.143).
   Keep client as system-of-record (working-copy-only on the firm side).
4. Personnel/file/review-chain separation in place? Hal/Lila/Theo NOT on the
   attest roster for this client; GL crosses to the audit only via a logged,
   one-time cross-wall read gated by the ICO (not Hal).
5. Coordinate openly on cfo-dept-heads; the ICO/Saira owns the wall log, not Hal.
```
@summaries/cross-branch-independence-wall; @reference/head-attest-mason §2.8 (the attestor's mirror of this wall)

---

## 4. Output templates

### 4.1 Journal entry with support (copy-ready)
```
JE-ID: [CLOSE-2026-05-014]        Entity: [____]   Period: [2026-05]
Date posted: [____]   Prepared by: [____]/[date]   Reviewed by: [Hal]/[date]
Type: [Standard | Recurring | Reversing-pair | Top-side | Reclass]
Linked reversal JE-ID (if accrual): [CLOSE-2026-06-0xx]

  Account            Dr            Cr        Memo
  6xxx Expense    1,200.00                   May professional fees, unbilled
  2xxx Accr. Liab.              1,200.00     accrue per engagement letter

GAAP basis: ASC [###-##-##-#] — [one line]. (Routine accrual: matching/accrual basis.)
Support: [Workpaper WP-AP-05 "May accruals"; source = vendor engagement letter
         dated [__]; GL snapshot [__]]. Source is a NAMED doc, not "QBO."
Tie: ties Accrued Liabilities subledger schedule WP-AP-05 to GL acct 2xxx.
Self-review wall (attest clients only): JE approved by client SKE designee [name]/[date].
```

### 4.2 Monthly-close checklist line (one row per task; the close is the sum of these)
```
| # | Task | Owner | Source (report+date+params) | Ties to | Status | Sign-off/date |
|---|------|-------|------------------------------|---------|--------|---------------|
| 1 | AR aging recon to GL 1200 | Lila | AR Aging Detail, [date], all cust | TB acct 1200 | Done | Hal [date] |
| 2 | Bank recon — operating | Lila | Bank stmt [date] + GL 1010 | TB acct 1010 | Done | Hal [date] |
| 3 | Payroll JE from processor | Theo | Payroll register [run-date] | TB 6000/2200 | Done | Hal [date] |
| 4 | Deferred-rev rollforward (606) | Theo | Contract register [date] | TB 2400 | Open | — |
| 5 | Clearing accts → $0 | Hal | GL clearing 1099/2099 | $0 | Done | Hal [date] |
| 6 | Tax provision recorded | Hal | Anya provision pkg [date] | TB 2300/9100 | Done | Hal [date] |
| 7 | Flux narrative vs budget+PY | Theo | TB + budget [version] | — | Open | — |
```
Advance a stage only when its reconciliations are clean. "Open" with a tie failure blocks the close.

### 4.3 Workpaper structure (the 7 requirements, instantiated)
```
┌─ HEADER ────────────────────────────────────────────────────────────────┐
│ Entity: [__]  Period: [2026-05]  Account: 1200 Accounts Receivable        │
│ Title: AR Aging Reconciliation to GL                                      │
├─ PREPARER / REVIEWER ─────────────────────────────────────────────────────┤
│ Prepared: [Lila] [date]      Reviewed: [Hal] [date]                       │
├─ SOURCE ──────────────────────────────────────────────────────────────────┤
│ AR Aging Detail report, run [date], parameters: all customers, as-of      │
│ 2026-05-31. GL snapshot [date]. (NOT "QBO" — named report + date + params.)│
├─ BODY (tie-out) ──────────────────────────────────────────────────────────┤
│ Aging total .......... 248,113.40  → ties to GL acct 1200 (248,113.40) ✓  │
│ Top-20 customers, days outstanding, last-payment, last-contact dates       │
│ Allowance (ASC 326-20 expected loss): [methodology + pool rates + Q-factor]│
├─ REASONABLENESS ──────────────────────────────────────────────────────────┤
│ vs PY 231k (+7%); vs budget 240k (+3%). Driver: [explanation].            │
│ Flag: ABC Co. at 95 DPO — escalate.                                       │
├─ OPEN ITEMS ──────────────────────────────────────────────────────────────┤
│ None / [item + expected resolution date]                                  │
└───────────────────────────────────────────────────────────────────────────┘
```
@summaries/workpaper; @persona (AR-aging brief)

### 4.4 Revenue-recognition memo (ASC 606, preparer side) — skeleton
```
REVENUE RECOGNITION MEMO — [Contract / Customer]      Prepared: [Theo] Reviewed: [Hal]
1. CONTRACT SUMMARY: parties, term, total consideration, key obligations.
2. STEP 1 — Contract exists? 606-10-25-1 five criteria; collectibility probable
   (25-1(e))? Combined contracts (25-9)? Modifications (25-10→25-13)?  Conclusion + cite.
3. STEP 2 — Performance obligations: list each PO; distinct two-prong (25-14→25-22);
   series election (25-14(b))?  Conclusion: [n] POs.
4. STEP 3 — Transaction price: fixed + variable; estimation method (expected value /
   most-likely); CONSTRAINT applied (32-11 — significant reversal not probable);
   financing/noncash/consideration-payable?  Conclusion: $[__].
5. STEP 4 — Allocation: relative SSP per PO; SSP estimation basis; residual gate
   (32-34(c)) used? [Y/N + why].  Allocation table.
6. STEP 5 — Recognition: over-time (25-27 criterion + progress measure) OR
   point-in-time (25-30 indicators). Principal vs agent per PO (55-37/55-39A)?
   Conclusion: pattern + timing.
7. COSTS (340-40): costs to obtain/fulfill capitalized? amortization pattern?
8. JE PATTERN + DISCLOSURE (606-10-50): disaggregation, contract balances,
   remaining POs, significant judgments.
9. ESTIMATES LOG: every estimate (variable consideration, SSP) with method + inputs +
   sensitivity + retrospective vs actual (this is what the auditor will test).
```
@summaries/asc-606, workpaper

### 4.5 Going-concern preparer assessment — skeleton (each annual + interim period)
```
GOING-CONCERN ASSESSMENT — [Entity] — period ending [__]   Prepared: [Hal]
Look-forward window: one year from [issuance / available-to-be-issued] date = [date].
STEP 1 — Conditions/events (205-40-55-2): recurring losses? working-capital deficiency?
   negative operating cash flow? covenant default/arrearage? loss of key customer/license?
   → In aggregate, substantial doubt raised?  [YES → Step 2 | NO → no disclosure, STOP].
STEP 2 — Management's plans: list each plan; for each, is it BOTH (a) probable of being
   effectively implemented (executed agreement / board approval — NOT aspirational) AND
   (b) probable of mitigating the condition?  → Doubt alleviated? [YES | NO].
DISCLOSURE: none (no doubt) | 205-40-50-12 (alleviated) | 205-40-50-13 WITH the exact
   phrase "substantial doubt about the entity's ability to continue as a going concern"
   (not alleviated).
Subsequent events in the window (ASC 855) folded in? [Y].  Cite conclusion.
```
@summaries/going-concern

### 4.6 §1.295 nonattest / independence-wall acknowledgment (preparer-side, when books are under attest)
```
Header: client; the attest engagement (Priscilla/Mason); the bookkeeping engagement (Hal); date.
1. Client type: [non-issuer attest | ISSUER → bookkeeping prohibited, STOP].
2. §1.295.040 prerequisites: competent individual w/ SKE = [name/title]; client makes all
   management decisions [Y]; client evaluates adequacy & results [Y]; client APPROVES journal
   entries [Y]; written understanding on file [Y/date].
3. Hosting: firm is NOT sole repository of client GL (client is system-of-record) [Y] (§1.295.143).
4. Separation: Hal/Lila/Theo not on attest roster [Y]; GL crosses to audit only via logged
   one-time cross-wall read gated by ICO [Y].
5. Conclusion: independence PRESERVED / IMPAIRED.  ICO + Saira hold the wall log (not Hal).
```
@summaries/cross-branch-independence-wall

---

## 5. Verification checklist (pre-output gate — every number, every entry, every close)
Apply before anything leaves Hal for Soph (mirrors the persona pre-review checklist; each carries its anchor).

- [ ] **Every number on the schedule ties to a named source** — report + date + parameter set (or tab/cell), **never "QBO."** (§2.10 #3; @persona)
- [ ] **Every subledger reconciles to the GL** — drift > $1 is **resolved**, not watched. (§3.4; @persona)
- [ ] **Period cutoffs clean** — no transaction sitting in the wrong month; subsequent events classified Type 1 (adjust) vs Type 2 (disclose) per ASC 855. (§2.7)
- [ ] **Accruals booked** for known-but-unbilled; reversing entries stored as the **linked pair.** (§2.9; @persona)
- [ ] **Clearing/suspense accounts at zero** or explained. (§2.9; @persona)
- [ ] **Right ASC Topic, scope-gated** — read -15 before -25; non-routine entries ran the 8-step walk (§3.1) and cite a specific paragraph. (§2.0; @summaries/fasb)
- [ ] **Revenue:** 5-step memo done for material contracts; constraint applied (32-11); principal/agent per PO; deferred-rev = contract liability, unbilled = contract asset. (§2.1)
- [ ] **Leases:** classification (5 criteria) documented; ROU + liability tie; IBR basis stated. (§2.2)
- [ ] **Tax provision:** recorded as Anya computed; **ETR recon tied to the tax accounts;** discrete-vs-AETR flagged; OCI allocation uses with-and-without. Hal recorded, did NOT decide. (§2.3)
- [ ] **Allowances/estimates:** CECL allowance is an expected-loss estimate (§2.4); every estimate has methodology + inputs + sensitivity + retrospective vs actual. (§2.10)
- [ ] **Going concern:** annual/interim two-step assessment done; plans tested against the "probable of implementation" prong (no aspirational plans). (§2.6)
- [ ] **Narrative matches the number** — flux discussed vs **budget AND prior period.** (§2.9; @persona)
- [ ] **§7216 audit-log entry recorded** for any cross-engagement data access; JE audit-log + close-status role-based access intact. (§2.11; @persona)
- [ ] **Independence wall (if books are under a Priscilla/Mason attest engagement):** issuer→prohibited; non-issuer→§1.295.040 SKE + client JE approval + written understanding; not sole GL repository; coordinated openly with the ICO/Saira on cfo-dept-heads. (§3.7)

If any fail, the senior goes back. Do not escalate to Soph until it is clean. **A number that does not tie does not post.**

---

## 6. Worked examples (rules applied end-to-end, preparer side)

### 6.1 SaaS deferred revenue — book the 606 5-step
A SaaS client signs a 12-month subscription, $24,000 paid upfront, plus a one-time $3,000 implementation service that the customer could buy from others. **Walk (§3.1 + §2.1):** Step 1 — contract exists, collectibility probable (`606-10-25-1`). Step 2 — **two POs**: the implementation is **distinct** (capable + distinct-in-context, `25-14`→25-22) from the SaaS access. Step 3 — transaction price $27,000, no variable consideration. Step 4 — allocate on **relative SSP**: implementation SSP $3,000, SaaS SSP $24,000 → allocate as-is. Step 5 — implementation recognized **at the point in time** delivered (`25-30`); SaaS recognized **over time** ratably across 12 months (the customer simultaneously receives and consumes, `25-27(a)`). **JE:** on cash, Dr Cash 27,000 / Cr Deferred revenue (contract liability) 27,000. On implementation completion, Dr Deferred revenue 3,000 / Cr Revenue 3,000. Each month, Dr Deferred revenue 2,000 / Cr Revenue 2,000. **Disclosure (`606-10-50`):** contract liability balance + remaining POs. **Trap avoided:** bundling implementation into the subscription would have deferred revenue that should be recognized at delivery. @summaries/asc-606

### 6.2 Office lease — classify and book under ASC 842
The firm signs a 5-year office lease, $5,000/month, no purchase option, asset not specialized, economic life of the building far exceeds 5 years. **Classification (§2.2, `842-10-25-2`):** (a) no ownership transfer; (b) no purchase option; (c) 5 years is **not** a major part of the building's remaining life; (d) PV of payments is **not** substantially all of the building's FV; (e) not specialized → **operating lease.** **Initial measurement:** lease liability = PV of 60 payments of $5,000 at the **IBR** (implicit rate not determinable) — say IBR 6%, PV ≈ $258,000; **ROU asset** = liability + any prepaid − incentives + IDC. **JE at commencement:** Dr ROU asset 258,000 / Cr Lease liability 258,000. **Monthly:** single straight-line lease cost $5,000; the entry reduces the liability (interest accretion + principal) and amortizes the ROU as the plug. **Trap avoided:** treating it as a finance lease would front-load expense incorrectly; using an unsecured revolver rate as the IBR overstates the rate (the auditor's #1 842 finding). @summaries/asc-842

### 6.3 Quarter-close tax provision — record, don't decide
At Q2 close, Anya delivers the provision package: AETR 24%, plus a **discrete** item — a state rate change enacted in Q2 increasing the DTL by $40,000, and a proposed **valuation allowance** release of $120,000 on NOL DTAs. **Hal's procedure (§2.3, §3.2):** (1) **record** the AETR-based tax on YTD ordinary income; (2) **record** the discrete rate-change effect in **continuing operations** in Q2 (`740-10-25-47`) — flagged discrete, not run through AETR; (3) **record** the VA release **Anya decided** (Hal does not assess the four sources himself); (4) **tie the ETR reconciliation to the tax accounts** — every reconciling line foots to a GL balance; (5) verify any OCI tax used **with-and-without.** **JE:** Dr Income tax expense (AETR portion) + Dr Income tax expense (discrete rate change) 40,000 / Cr Deferred tax liability 40,000; VA release: Dr Valuation allowance 120,000 / Cr Income tax expense 120,000. **Wall note:** if this client is under a Priscilla/Mason audit, Anya's firm-side provision team and the audit team are bifurcated; Hal records management's (the client SKE designee's) approved numbers. **Trap avoided:** burying the discrete item in the AETR distorts every subsequent quarter. @summaries/asc-740

### 6.4 Post-close customer bankruptcy — Type 1 subsequent event, and the allowance
The books close 5/31; on 6/20 (before issuance) a major customer files Chapter 7; the receivable existed at 5/31 and collectibility was already doubtful at year-end. **Procedure (§2.7, §2.4):** the bankruptcy is **additional evidence of a condition existing at the balance-sheet date** → **Type 1 (recognized) subsequent event** (ASC 855) → **adjust** the 5/31 financials. Increase the **CECL allowance** (ASC 326-20 expected-loss) for the now-confirmed loss. **JE (dated in May):** Dr Credit loss expense / Cr Allowance for credit losses; on write-off, Dr Allowance / Cr Accounts receivable. **Contrast:** if instead a fire destroyed the customer's warehouse on 6/20 (a **new** condition arising after 5/31), that is **Type 2** — **disclose** the nature and estimated effect, do **not** adjust. **Contrast 2:** if on 6/20 Hal discovered the May AR had been **mis-added** (a math error), that is **not** a subsequent event — it routes to **ASC 250** error correction (restate if material under SAB 99 qualitative factors). @summaries/going-concern, asc-326

---

## 7. Source map (deep dives — verifiable paths)
Summaries under `research/summaries/`; deep reports under `(grounded in domain research; re-ground with your own sources)` (CPA) and `(grounded in domain research; re-ground with your own sources)` (EA); EA summaries under `(grounded in domain research; re-ground with your own sources)`. The CPA reports are written attest-side — read them for the underlying ASC paragraphs, then translate to the preparer's seat.

| Topic Hal books | Summary | Deep folder (key files) |
|---|---|---|
| **FASB codification hierarchy + 8-step walk** | `fasb-accounting-standards-codification-codificatio.md` | `2026-05-16-fasb-accounting-standards-codification-codification-architec/` (04-authority-hierarchy, 06-attestor-navigation, 07-scope-exception-patterns) |
| **ASC 606 revenue (5-step, principal/agent, costs)** | `asc-606-revenue-from-contracts.md` | `2026-05-16-asc-606-revenue-from-contracts-with-customers-attest-side-pe/` (02-step1 … 06-step5, 07-costs-and-modifications, 09-principal-vs-agent, 11-independence-wall) |
| **ASC 842 leases (classification, ROU/liability, IBR)** | `asc-842-leases-attest-side.md` | `2026-05-16-asc-842-leases-attest-side-perspective-jurisdiction-neutral/` (02-lessee-classification, 03-lessee-measurement, 08-ibr, 09-embedded-lease) |
| **ASC 740 provision (DTA/DTL, VA, UTP, AETR, intraperiod)** | `asc-740-income-taxes-attest.md` | `2026-05-16-asc-740-income-taxes-attest-side-perspective-jurisdiction-ne/` (02-dta-dtl, 03-valuation-allowance, 05-interim-aetr, 10-three-branch-seam) |
| **ASC 326 CECL (pooling, R&S forecast, Q-factors, AR allowance)** | `asc-326-cecl-current-expected.md` | `2026-05-16-asc-326-cecl-current-expected-credit-losses-attest-side-pers/` (02-pooling, 03-reasonable-supportable-forecast, 04-qualitative, 07-write-off) |
| **ASC 805 / 350 combinations + goodwill** | `asc-805-business-combinations-and.md` | `2026-05-16-asc-805-business-combinations-and-asc-350-intangibles-goodwi/` (02-acquirer-id, 03-measurement-period, 04-contingent-consideration, 07-goodwill-impairment) |
| **Going concern (205-40) + subsequent events (855) + changes/errors (250) + materiality (SAB 99/108)** | `going-concern-asc-205-40.md` | `2026-05-16-going-concern-asc-205-40-subsequent-events-asc-855-accountin/` (02-asc-205-40, 05-asc-855, 07-asc-250, 08-sab-99-sab-108) |
| **Workpaper integrity (the Hal-side 7 requirements + PBC handoff)** | `workpaper-structure-and-audit-file.md` | `2026-05-16-workpaper-structure-and-audit-file-documentation-as-1215-au/` (07-unified-template, **08-preparer-handoff** ← Hal-to-auditor spec) |
| **Independence wall (§1.295, SOX §201, Reg S-X 2-01(c)(4))** | `cross-branch-independence-wall-protocol.md` | `2026-05-16-cross-branch-independence-wall-protocol-cpa-branch-attest-en/` (02-chinese-wall-structure, 04-engagement-letter-clauses, 08-issuer-vs-nonissuer-delta) |
| **§7216 / §6103 data-sharing boundary** | `(grounded in domain research; re-ground with your own sources)` | `(grounded in domain research; re-ground with your own sources)` (02-four-fact-patterns, 04-cfo-tax-handoff, 03-audit-log-and-controls) |
| **Pub 4557 WISP six-area framework** | `(grounded in domain research; re-ground with your own sources)` | `(grounded in domain research; re-ground with your own sources)` (01-six-area-framework, 02-ftc-safeguards-rule) |

**Adjacent (cross-head; cite when bridging, do not own):** the AUDIT of these books (AU-C / PCAOB AS), the attest opinion, SOC reports → **Priscilla / Mason** (`.claude/agents/references/head-attest-mason.md`; @summaries/aicpa-au-c-clarified-standards, @summaries/ssae-statements-on-standards-for, @summaries/soc-1-soc-2-soc, @summaries/pcaob-auditing-standards-full-as). The QM system, the firm independence framework, peer review, the wall log → **Saira** (@summaries/quality-management-standards-sqms-1). The tax positions Hal records but does not decide → **Anya** (cfo-tax). Hal *prepares*; they *attest / decide*.

---
*Gaps where research was thin or absent (flag to Soph if a close turns on these): (1) **No monthly-close marathon exists in this repo** — the dead `research/marathons/2026-05-05-modern-monthly-close-...` path has been removed from §2.9 and the persona (no `research/marathons/` dir exists at the repo root); the §2.9/§3.2 close cadence is professional-practice knowledge whose tie-out/recon discipline is one-hop traceable to `@summaries/workpaper` + `@persona`, but the day-by-day cadence is NOT itself one-hop traceable here. Source the cadence against a monthly-close marathon only if one lands at a real path (gap CFO-012, agent-improvement/waves/wave-1/cfo/review/findings.md). (2) The CPA reports are written **attest-side**; this brain translates them to the preparer's seat, but the deep files describe how to AUDIT each topic — the recognition/measurement ASC paragraphs are reliable, but preparer-specific disclosure checklists and full JE patterns were inferred from standard GAAP mechanics, not lifted verbatim; verify JE specifics against primary ASC text before booking material/non-routine entries. (3) `[UNVERIFIED]` State-board variations on AICPA §1.295 bookkeeping-independence and on the "sole repository" hosting threshold are not enumerated (@summaries/cross-branch-independence-wall). (4) `[UNVERIFIED]` Whether §7216 reaches pure non-preparation accounting work is not settled; the conservative firm-level audit-log control is adopted regardless (@summaries/ea/data-sharing-7216). (5) Effective-date matrices for open ASUs beyond the Wave-19–23 topics were not fully enumerated — consult the FASB effective-dates page for any topic outside 606/842/326/740/805 (@summaries/fasb).*

## 8. QBO execution seam
When a task here needs QuickBooks Online actions, route the EXECUTION to the **QBO Agent** (the `pack-qbo-agent` pack: `qbo-agent/skills/` + `combos/`) — this brain supplies the *reasoning* (the controlling rule, the right account, what "correct" looks like); the QBO Agent supplies the *driving* (recognition microskills + HTN planner over the live UI). Hal is the deepest QBO user: the monthly close, bank-feed categorization, and subledger-to-GL recon all execute through this seam, with his close tie-out discipline (§3.2) as the reasoning that says when a row is "correct" (@qbo-agent/reference/cfo/head-controller-hal.md).
- **Money-fence (hard):** the QBO Agent stages work read-only -> draft -> human-commit and is HARD-BLOCKED from money movement (Post / Pay / Send / Match-commit / Schedule-payment / Finish-reconciling require a human; JE Save is operator-allowed because reclassification is not money movement). Never reason around the fence. (@qbo-agent hooks/)
- **cfo-controller QBO tasks (reason here -> drive there):**
  | Domain task (you reason) | QBO Agent route (it drives) |
  |---|---|
  | Monthly close orchestration — cut-off, accruals, TB tie (§3.2) | `close-out-month` |
  | Bank-feed match/categorize during close (§2.9/§3.2) | `match-batch` · `qbo-bankfeed-set-category` |
  | Bank / credit-card reconciliation to GL (§3.4) | `reconcile-walk` · `qbo-recon-flag-discrepancy` |
  | JE prep + review gate, post above-materiality entries (§3.3) | `post-and-verify-batch` · `qbo-je-save` |
  | Trial-balance + GL tie-out across the subledgers (§3.2/§3.4) | `gl-tie-out` · `ar-aging-review` · `ap-aging-review` |
- Grounded handoff: cite the controlling rule in this brain (the §3.2 close cadence, the §3.4 subledger-to-GL recon, the §2.11 JE append-only control); name the qbo-agent skill/combo there. Bundled execution map: `@qbo-agent/reference/cfo/`.
