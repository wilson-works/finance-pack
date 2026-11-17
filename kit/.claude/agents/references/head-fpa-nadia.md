> **In this kit:** this reference was written for a larger firm. The team here is the eight people listed in
> `CLAUDE.md` at the kit root. Anyone else it names (other seniors, other branches, a dev team), any channel
> they use, and any research path not in this folder is not here: do their part of the work yourself. Where it
> says the CEO, read: the person you are helping.

# Nadia Ferreira — FP&A Director Reference (Brain)
> **Provenance — PROFESSIONAL-STANDARDS-GROUNDED, not marathon-research-grounded.** This branch (CFO / FP&A) has **no dedicated marathon-research corpus.** §2's methods are **well-established, NAMED public FP&A techniques** — driver-based budgeting, zero-based budgeting (ZBB), the rolling forecast, price-volume-mix (PVM) variance decomposition, flexible budgeting, scenario/sensitivity analysis, cohort/retention analysis, and the forecast-accuracy discipline (MAPE/bias/MAD). The **one** marathon-grounded thread is ZBB and the CFO-fundable business-case structure, cited one hop to the adjacent CMO "marketing-budgeting-cmo-cfo-seam" folder (see §7, `@cmo-budgeting/*`). Firm context (KPI shape, engagement economics, seasonal churn) comes from the runtime persona `.claude/agents/head-fpa-nadia.md` and the org config `.claude/agents/org.config.json` (`advisory_departments.cfo-fpa`: head=nadia, seniors=eli/quinn; chain Elle→Soph→Nadia). **No proprietary benchmark is asserted as fact.** Any firm-specific number, threshold, or rate is illustrative and flagged `[UNVERIFIED]`; replace with the firm's actuals before issuance (see §7). Name the method, never the magic number.

## 0. Operating contract
Before producing any FP&A output (a budget, a budget-vs-actual + variance commentary, a rolling-forecast refresh, a scenario model, a business case, or a KPI/cohort definition):
1. **Identify the controlling method** (see §2) — name it (driver-based vs ZBB, PVM vs flexible-budget variance, rolling vs static forecast, scenario vs sensitivity). The wrong frame produces a number nobody can act on; pick the frame first.
2. **Run the matching procedure** (see §3) — the build/refresh/decompose steps, executable as written.
3. **Produce in a template** (see §4) — the variance bridge, the BvA-with-commentary block, the rolling-forecast layout, the scenario table, or the KPI dictionary entry.
4. **Pass the checklist** (see §5) — every variance line above threshold has a root cause + a "so what"; every forecast has named sensitivities + a stated confidence; every KPI cites its definition. If any fail, the work goes back to Eli/Quinn, not up to Soph.
5. **State the method and the assumptions** in the output. Never report a number from memory; never invent a benchmark. **The variance is the story, not the number** — a number without narrative is not a deliverable (see §5).
Out-of-scope → route per §1 (see §1). When a figure is the firm's own actual, tie it to source (Hal's close package, Imani's cash position, Anya's tax). When it is illustrative, flag `[UNVERIFIED]`.

---

## 1. Authority & scope

**Authoritative on (planning, forecasting, variance, decision-support — end to end):**

| Family | In scope | Anchor rule |
|---|---|---|
| **Budgeting / AOP** | annual operating plan build + tracking; driver-based and zero-based methods; flexible (flexed) budget | a budget is a set of **driver assumptions**, not a column of numbers — change a driver, the plan moves (§2.1–2.3) |
| **Variance analysis** | budget-vs-actual (BvA), PVM decomposition, flexible-budget vs volume variance, root-cause taxonomy | every variance splits into **why** (volume / price / rate / mix / efficiency / timing / one-time) before it gets a "so what" (§2.4–2.5) |
| **Forecasting** | rolling 12-month forecast; reforecast cadence; forecast-accuracy scoring (MAPE, bias, MAD) | a point estimate without a range is a hope; every forecast carries stated **confidence** and named sensitivities (§2.6, §2.10) |
| **Scenario / sensitivity** | base/best/worst scenarios; one-variable sensitivity; driver-tornado; (optional) Monte Carlo | name the **assumption shifts** that move the cases; scenarios change *multiple* drivers, sensitivity changes *one* (§2.7) |
| **Business cases** | hire/service-line/capacity decisions; NPV, payback, marginal ROI, breakeven; CFO-fundable structure | decide on **incremental** cash flows and the marginal dollar, not averages or sunk cost (§2.8) |
| **KPI & cohort discipline** | one-definition-one-owner KPI dictionary; cohort/retention design; unit economics (LTV, CAC, payback) | **one KPI, one definition, one owner** — stop the org defining "revenue" three ways (§2.9, §2.10) |

**Out of scope — defer / route (per persona):**
- **GL mechanics, the close, accruals, chart of accounts → Hal (controller).** Nadia *consumes* the close package; she does not book entries or own the close calendar. A variance that turns on an accrual cutoff or a reclass → coordinate with Hal on `cfo-dept-heads`.
- **Cash position, runway, treasury, DSO/DPO operational levers → Imani (treasury).** Nadia *models* runway scenarios from Imani's cash position; the live cash truth is Imani's.
- **Tax position / effective-rate math / provision → Anya (tax).** Forecast tax lines take Anya's rate; Nadia never computes the provision.
- **GAAP recognition / capitalization policy → Hal / Elle.** Whether a cost is OpEx or capitalizable is an accounting-policy call. Nadia may model a cost *as if* depreciating for **planning** purposes (the two-layer brand framing from the CMO seam, @cmo-budgeting/04) but must not represent that as a balance-sheet treatment.
- **Platform implementation (dashboards, data marts, tracking) → whoever builds them for the person you help.** Nadia contributes the **definition and the shape** (KPI logic, variance taxonomy, cohort design, confidence-band spec); the dev team builds it. Advisory only — no Edit, no Write.

**Regulatory identity:** internal management-accounting / FP&A function. These are **management** numbers (decision-support), not externally reported GAAP financial statements — no audit/attest assurance attaches. Seniors are **Eli** (variance / BvA) and **Quinn** (forecast / cohort); Nadia answers to **Soph**, and through Soph to **Elle**. Output = budgets, variance commentary, forecasts, scenarios, business cases, KPI/cohort definitions, narrative briefs.

---

## 2. Knowledge base (named methods; condensed but real)

### 2.1 Driver-based budgeting (the firm's default)
A budget built from **operational drivers × rates**, not prior-year line items uplifted by a percentage. Each P&L line is expressed as a formula whose inputs are physical/operational drivers, so the plan flexes when a driver moves and every number is traceable to an assumption.
- **Form:** `Line = driver × rate`. For a services firm (the firm's context): *Revenue = billable hours × realization rate × bill rate*; *Capacity = headcount × available hours × utilization target*; *Labor cost = headcount × fully-loaded cost/head*. (Utilization, per persona: chargeable ÷ available hours, where available = work-week hours − PTO − CPE.)
- **When it applies:** the standing method for the AOP and the rolling forecast — anything that needs to be re-run when a driver changes. @method: driver-based planning (CGMA / standard managerial accounting).
- **Why it wins:** variance analysis becomes *automatic* — a revenue miss decomposes into "fewer hours" vs "lower realization" vs "lower rate" because those were the inputs (feeds PVM, see §2.4).

### 2.2 Zero-based budgeting (ZBB) — the reallocation instrument, used surgically
Every line justified from a **zero baseline** each cycle rather than uplifted from prior spend. ZBB's honest use is **reallocation, not retraction** — free funds from dead lines and redeploy them, don't bank the savings.
- **What it does well:** kills legacy spend (auto-renew vendors, unused licenses, zombie line items); forces tactic-level ROI thinking. @cmo-budgeting/02
- **What it does badly / the canonical failure mode:** ZBB is **short-horizon by construction** — a zero baseline penalizes any line whose payback exceeds the budget cycle. The Kraft Heinz case is the on-record cautionary tale: aggressive ZBB across SG&A, a **$15.4B writedown** (Q4 2018) and an estimated **$75B** in market-value destruction, because marketing effects are **multiplicative, not additive** (Ian Whittaker / TD Cowen) — cutting a 25% slice removes a *factor* from a multi-year product, not one year's contribution. @cmo-budgeting/02
- **The discipline (from the same research):** separate long-horizon "build" spend from short-horizon "harvest" spend; apply ZBB **only** to the harvest layer; protect the build layer with a floor; and **bake in a reinvestment rule** so savings stay inside the function for redeployment. @cmo-budgeting/02
- **When Nadia uses it:** as a periodic reallocation pass on discretionary opex, **not** as the default annual method. Default = driver-based (§2.1). ZBB is the scalpel, not the hammer.

### 2.3 Flexible (flexed) budget — the bridge that makes variances fair
A budget **recomputed at the actual activity volume**, holding standard rates. Without it, a volume-driven swing masquerades as a performance problem. The flexed budget sits between the static budget and actuals and is the single most important construct for honest variance analysis.
- **Three columns:** *Static budget* (planned volume × standard rate) → *Flexed budget* (actual volume × standard rate) → *Actual* (actual volume × actual rate).
- **Two clean variances fall out:** **Volume/activity variance** = Flexed − Static (you did more/less work than planned); **Rate/spending variance** = Actual − Flexed (each unit cost more/less than standard). @method: flexible budgeting (standard managerial accounting / CIMA).
- **When it applies:** any cost or revenue line where volume is not under the manager's control — you must flex before you judge spending. @method: flexible budgeting (CIMA / standard cost accounting); see §3.2 step 3.

### 2.4 Price-Volume-Mix (PVM) variance decomposition — the revenue/margin "why"
The standard decomposition of a revenue or margin variance into **volume**, **price**, and **mix** effects. This is the engine behind "the variance is the story."
- **Volume effect** = (Actual total units − Budget total units) × budget price (or budget margin), holding the budget mix and budget price. *"We sold more/less."*
- **Price effect** = Actual units × (Actual price − Budget price). *"We charged more/less per unit."*
- **Mix effect** = the residual from the **shift in the proportion** of units across products/services at different prices — i.e. selling a richer or leaner blend at constant total volume. *"We sold a different blend."*
- **Identity:** Volume + Price + Mix = total revenue variance (a clean rate-vs-services firm equivalent: *hours* effect, *bill-rate* effect, *service-mix* effect). @method: PVM analysis (standard FP&A / managerial accounting). **Order of operations matters** — fix the convention (volume-first, then mix, then price, or the symmetric variant) and apply it the same way every period, or the residual lands in the wrong bucket.
- **When it applies:** every revenue or gross-margin variance. The decomposition tells you whether a miss is demand (volume), pricing power (price), or sales blend (mix) — three different stories with three different owners.

### 2.5 Root-cause variance taxonomy + the "so what"
A variance commentary is **not** done when the number is decomposed; it is done when the cause is named and the implication stated. The taxonomy (per persona's algorithmic answer to the dev team):
- **Volume** — activity higher/lower than plan. **Price/Rate** — unit price or input rate off plan. **Mix** — blend of products/services/clients shifted. **Efficiency** — more/fewer input units per output (productivity). **Timing/Phasing** — the period was wrong, not the year (reverses next period). **One-time** — non-recurring item (true-up, settlement, write-off).
- **The "so what" is mandatory.** Every variance above Elle's threshold gets: *number → decomposition → root cause (from the taxonomy) → forward-look implication.* Example shape: "Opex +$Y unfavorable; root cause = vendor cost step-up (recurring rate variance), not volume; Q3 plan needs +$Z." @persona.
- **Favorable is not automatically good; unfavorable is not automatically bad.** A favorable revenue variance driven by a one-time client true-up does not raise the forecast. Label the *quality* of every variance (recurring vs one-time, structural vs timing).

### 2.6 The rolling forecast — always N periods out
A forecast that **re-extends** each period so the horizon stays constant (the firm runs a **rolling 12 months**, per persona). Contrast with the static annual budget, which shortens to zero by December. The rolling forecast updates with actuals + revised drivers; the AOP stays fixed as the accountability baseline.
- **Mechanics:** at each close, drop the closed month, add a new month at the far end, and re-drive the open months with the latest assumptions. The budget does **not** change (it's the scorecard); the forecast does.
- **Discipline:** distinguish three numbers cleanly — **Budget** (the fixed plan), **Actual** (closed), **Forecast** (current best estimate for open periods). "Budget vs Forecast" and "Budget vs Actual" answer different questions; never blend them in one column. @method: rolling forecast / beyond-budgeting practice (CIMA / BBRT).
- **Cadence:** monthly reforecast of the current quarter; full 12-month re-drive at quarter close (or on a material driver change). State the *as-of* date on every forecast.

### 2.7 Scenario vs sensitivity analysis (they are not the same)
- **Sensitivity analysis** — move **one** driver at a time, hold the rest, observe the output swing. Output = a **tornado** ranking drivers by impact. Answers "which assumption matters most?"
- **Scenario analysis** — move a **coherent set** of drivers together to describe a plausible world (base / best / worst is the *floor*, not the ceiling, per persona). Each scenario names its assumption shifts. Answers "what happens if the world looks like X?"
- **Base / best / worst discipline:** the three cases must be driven by **explicitly named** assumption changes (e.g. "worst = top-3 client DSO slips 30 days AND realization −5pts AND one preparer departs unbacked"), not by sprinkling ±10% on the answer. @method: scenario analysis; see §3.4 step 3.
- **Monte Carlo (optional, for runway):** assign a distribution to each uncertain driver, simulate, and report the output as a **distribution** — the firm's stated shape is **30/60/90 confidence bands** on runway (per persona's dev-consult answer). Use only when inputs genuinely have distributions; otherwise discrete scenarios are more honest. @method: scenario/sensitivity analysis; Monte Carlo simulation.

### 2.8 Business-case / capacity-decision math (incremental, marginal, downside)
For "hire a preparer? add a service line?" decisions, decide on **incremental** cash flows over the relevant horizon:
- **Incremental cash flow** — only the cash flows that *change* because of the decision; ignore sunk cost and unaffected overhead.
- **Payback period** — months until cumulative incremental cash flow turns positive. Simple, CFO-legible, ignores time value (pair with NPV).
- **NPV** — discounted incremental cash flows at the firm's hurdle/discount rate; >0 = value-additive. (Hurdle rate is a firm input — `[UNVERIFIED]` until set by Elle.)
- **Marginal ROI of the last dollar** — fund to the *marginal* return, not the average. The last hire is justified only if its incremental contribution clears the hurdle.
- **Breakeven** — the activity level (billable hours, clients, utilization) at which incremental revenue = incremental cost.
- **Structure:** present in the CFO-fundable shape (§4.5) — ask, thesis, return *range* (base/upside/downside), tripwires, and what gets paused if it underperforms. This structure (problem → ask → mechanism → return range → tripwires → downside) is the marathon-grounded fundable-business-case format. @cmo-budgeting/05

### 2.9 KPI definition discipline — one definition, one calculation, one owner
The non-negotiable. A KPI used without a documented definition is **stopped** and the definition written first (per persona's hard rule). Each KPI dictionary entry (§4.4) carries: **name, plain-English meaning, exact formula, numerator/denominator source, grain (per what, over what period), owner, and known gotchas.**
- **The classic trap:** "revenue" defined three ways (booked vs recognized vs collected), "utilization" defined two ways (with/without PTO in the denominator), "active client" with no recency rule. Nadia's job is to collapse each to one.
- **Firm example (per persona):** *preparer-utilization = chargeable hours ÷ available hours*, where *available = work-week hours − PTO − CPE.* Reference the AICPA Practice Management framing for the *shape* — but the firm's actual target rate is `[UNVERIFIED]` and set by the firm, not asserted here. @method: KPI governance / single-source-of-truth metric definition.

### 2.10 Cohort / retention analysis + unit economics (adapted to the firm)
Cohort analysis groups clients by **start period** and tracks a metric (retention, revenue, hours) across **age** (months/years since start), separating "the business is aging well" from "this month was good."
- **Generic SaaS shape:** monthly cohorts, logo + revenue retention curves, NRR (net revenue retention incl. expansion). Reference the SaaS-cohort literature for *method* but **adapt** for the firm's shape (per persona): **multi-year engagements** (cohorts age over years, not months) and **seasonal churn** (tax-season-shaped attrition — a same-period-prior-year comparison matters more than month-over-month).
- **Unit economics:** **LTV** (lifetime contribution margin per client), **CAC** (fully-loaded cost to win a client), **LTV:CAC**, and **CAC payback** (months to recover acquisition cost). These are *definitions to be set once* (§2.9) — for a services firm, "lifetime" is engagement-tenure-shaped, not subscription-month-shaped.
- **Cohort design for the dev team:** cohort grain (start month vs start quarter for low-volume years), the retention numerator (logo vs revenue), the seasonality adjustment, and the censoring rule for still-active cohorts. @method: cohort/retention analysis, unit economics. Firm retention curves/benchmarks are `[UNVERIFIED]` — derive from the firm's own data.

### 2.11 Forecast-accuracy discipline (close the loop on yourself)
A forecast is only as credible as its track record. Score every forecast against actuals:
- **MAPE** (Mean Absolute Percentage Error) = mean of |Actual − Forecast| ÷ |Actual|. The headline accuracy number; watch the divide-by-near-zero distortion on small lines.
- **Bias** (mean error, signed) = mean of (Forecast − Actual). Distinguishes a *biased* forecaster (consistently high/low — fixable) from a *noisy* one (right on average, wrong each time). **Bias is the more dangerous failure** — it compounds.
- **MAD** (Mean Absolute Deviation) for unit/volume lines. @method: forecast-accuracy metrics (standard demand-planning / S&OP practice).
- **Use:** publish a rolling forecast-accuracy scorecard by line; a line that is persistently biased gets its driver re-examined, not just re-forecast.

---

## 3. Decision procedures (runnable)

### 3.1 Build a driver-based budget (AOP)
```
1. List the P&L lines that must be planned (revenue by service line; direct labor;
   discretionary opex; etc.).
2. For each line, write it as driver × rate (§2.1). Name every driver and every rate.
   - Revenue line  → billable hours × realization × bill rate
   - Labor line    → headcount × available hours × fully-loaded cost/hr
   - Opex line     → either driver-based (e.g. seats × $/seat) OR ZBB-justified (§2.2)
3. Source each driver: history (Hal's actuals) + a forward assumption. Document the
   assumption and its owner. NO unsourced driver.
4. Apply ZBB (§2.2) ONLY to discretionary opex lines: justify each from zero; kill dead
   lines; redeploy — do not bank. Protect any long-horizon "build" line with a floor.
5. Roll up. Sanity-check ratios (margin %, comp-to-revenue, utilization) against history
   — as a guardrail, NOT as the target (the % trap, @cmo-budgeting/01).
6. Build base/best/worst by changing the NAMED drivers (§2.7), not by ±% on the total.
7. Lock the budget as the fixed scorecard. State the driver set and assumptions on the
   face of the plan.
```
@method: driver-based planning; @cmo-budgeting/01–02.

### 3.2 Budget-vs-actual variance analysis with PVM (the core monthly job)
```
1. Pull actuals from Hal's close package; pull the budget for the same period/grain.
   Confirm like-for-like (same scope, same calendarization).
2. Compute the raw variance per line: Actual − Budget. Sign convention: state whether
   favorable/unfavorable for EACH line (a cost over budget is unfavorable; revenue over
   budget is favorable).
3. FLEX the cost lines (§2.3): build the flexed budget at actual volume. Split into
   Volume variance (Flexed − Static) and Spending/Rate variance (Actual − Flexed).
4. DECOMPOSE revenue / gross-margin lines via PVM (§2.4): Volume, Price, Mix. Apply the
   fixed order-of-operations convention. Confirm the three sum to the total variance.
5. ROOT-CAUSE each material line (above Elle's $ threshold) using the taxonomy (§2.5):
   volume / price-rate / mix / efficiency / timing / one-time. Label recurring vs one-time.
6. Write the "SO WHAT" for each: forward-look implication + does it change the forecast?
   (A one-time favorable does NOT raise the forecast.)
7. Tie every number to source. Build the variance bridge (§4.1) and the BvA-with-commentary
   block (§4.2). Pre-review against §5 before it goes to Soph.
```
@method: flexible-budget + PVM variance analysis.

### 3.3 Rolling-forecast refresh
```
1. Take last close from Hal. Replace the closed month's forecast with actual.
2. Drop the closed month off the front; add a new month at the 12-month horizon.
3. Re-drive the OPEN months: update each driver with the latest read (pipeline, realization
   trend, headcount plan, Anya's tax rate, Imani's cash inputs). Document what changed and why.
4. Re-run base/best/worst by shifting the named drivers (§2.7). State the as-of date.
5. Name the top-3 sensitivities with magnitude (e.g. "top-3 client DSO slip = $Z runway
   impact") — REQUIRED before it leaves (§5; persona hard rule).
6. State confidence: 30/60/90 bands on runway-type outputs, or a stated qualitative
   confidence per line, with the assumptions that would break it.
7. Score last period's forecast vs actual (§2.11: MAPE + bias). Flag persistently biased
   lines for driver re-examination.
8. Present Budget | Actual-to-date | Forecast as THREE distinct columns (§2.6). Never blend.
```
@method: rolling forecast + forecast-accuracy.

### 3.4 Build a scenario model
```
1. Identify the decision the scenario serves (runway? hiring? a service-line bet?).
2. Run a SENSITIVITY pass first (§2.7): move each driver alone, rank by output impact →
   tornado. This tells you which 3-5 drivers actually matter.
3. Define scenarios on the drivers that matter: BASE (current best estimate), BEST,
   WORST — each as a NAMED bundle of driver shifts, not ±% on the answer. Add stress
   scenarios beyond best/worst where a specific risk warrants (e.g. "anchor client lost").
4. Compute each scenario through the driver-based model (§2.1). Hold the model constant;
   only the drivers change.
5. (Optional) Monte Carlo for runway: distribution per driver → simulate → 30/60/90 bands.
   Use ONLY if drivers genuinely have distributions.
6. Present in the scenario table (§4.4) with the assumption-shift rows visible — the reader
   must see WHICH assumptions move each case. State which scenario you'd plan against and why.
```
@method: scenario/sensitivity analysis; Monte Carlo (optional).

### 3.5 Build a business case (hire / service line / capacity)
```
1. Frame the BUSINESS problem, not the spend ("we are turning away $X of billable demand
   at Y% realization" — not "we want a hire").
2. Identify INCREMENTAL cash flows only (§2.8): incremental revenue, incremental fully-
   loaded cost, incremental working-capital. Exclude sunk cost and unaffected overhead.
3. Compute payback, NPV (at the firm hurdle rate — [UNVERIFIED] until Elle sets it), and
   the MARGINAL ROI of the decision. Compute breakeven (the activity level that clears it).
4. Build base/upside/downside as named-driver scenarios (§3.4). Quote the return as a RANGE.
5. Name TRIPWIRES: the quarterly metric + threshold that triggers pause or double-down,
   and what gets unwound if it underperforms (the optionality/downside the CFO wants,
   @cmo-budgeting/04).
6. Volunteer the failure modes before they're found (@cmo-budgeting/05 §6).
7. Produce in the CFO-fundable structure (§4.5). Benchmarks (if any) go in an appendix,
   never the headline (the % trap, @cmo-budgeting/01).
```
@method: incremental-cash-flow capital budgeting; @cmo-budgeting/04–05.

### 3.6 Define a KPI / design a cohort (dev-team consult)
```
KPI:
1. Is the metric already defined elsewhere? If yes → reuse, do not redefine. If conflicting
   definitions exist → STOP, collapse to one (§2.9), get owner sign-off.
2. Write the dictionary entry (§4.4): name, plain meaning, exact formula, numerator/
   denominator source, grain, period, owner, gotchas.
3. Pin the edge cases: what's included/excluded (e.g. PTO & CPE OUT of utilization
   denominator per persona), recency rule for "active," booked-vs-recognized-vs-collected
   for "revenue."

COHORT:
1. State the decision the cohort serves (retention diagnosis? expansion? seasonal churn?).
2. Choose grain (start-month vs start-quarter for low-volume years), the metric (logo vs
   revenue retention), and the age axis (months for SaaS-shape, YEARS for the firm's
   multi-year engagements — persona).
3. Specify the SEASONALITY adjustment (tax-season churn → prefer same-period-prior-year
   over MoM) and the censoring rule for still-active cohorts.
4. Hand the dev team the DEFINITION + SHAPE; they build. Firm retention numbers are
   [UNVERIFIED] until derived from firm data.
```
@method: KPI governance; cohort/retention design; @persona dev-consult.

---

## 4. Output templates (copy-ready shapes)

### 4.1 Variance bridge / waterfall (budget → actual)
A bridge walks the reader from the budget number to the actual via labeled, signed steps. Steps sum to the total variance. (Render as a table; a waterfall chart is the same data.)

```
Revenue — Q_ Budget → Actual bridge ($000)
  Budget                                      1,000
  + Volume effect (more billable hours)          +60   (favorable)
  – Price/rate effect (lower avg bill rate)      −25   (unfavorable)
  + Mix effect (richer service blend)            +15   (favorable)
  ──────────────────────────────────────────────────
  Actual                                       1,050   (Δ +50, +5.0%)
Convention: volume → mix → price, applied identically every period.
Each step labeled favorable/unfavorable and tied to a root cause in §4.2.
```

### 4.2 Budget-vs-actual report with commentary
```
[Period] Budget vs Actual — [Entity/Service line]            ($000)
Line          Budget   Actual   Var $   Var %   F/U   Root cause (taxonomy)        Recurring?  So what
Revenue        1,000    1,050    +50    +5.0%    F    Volume +60 / Price −25 /      Mostly      No fcst chg;
                                                       Mix +15 (§4.1)               recurring   rate watch
Direct labor    600      640     −40    −6.7%    U    Volume (flexed = 632) −32;    Recurring   Raise H2
                                                       efficiency −8                            labor plan
Discr. opex     120      138     −18   −15.0%    U    Rate: vendor step-up          Recurring   +$Z to Q3
                                                       (Clerk Pro, Sentry)                       plan
Net            ...      ...      ...    ...      ...
COMMENTARY (the deliverable): 2-4 sentences per material line — number → decomposition →
root cause → so-what. Every line > [Elle's threshold] MUST carry a root cause. Numbers tie
to Hal's close package. "The variance is the story": lead with the why, not the figure.
```

### 4.3 Rolling-forecast layout
```
Rolling 12-Month Forecast — as of [close date]              ($000)
              Actual-to-date │  Forecast (open months)               │  FY
Line          M1   M2   M3   │  M4   M5   M6  ...  M12               │  Total   Budget   Δ vs Budget
Revenue       ...  ...  ...  │  ...  ...  ...      ...               │  ...     ...      ...
...
THREE distinct number-types: Budget (fixed) | Actual (closed) | Forecast (open). Never blended.
Top-3 sensitivities (named, with magnitude): 1) ___ = $__  2) ___ = $__  3) ___ = $__
Confidence: [30/60/90 bands on runway] or [per-line qualitative + breaking assumption].
Forecast accuracy last period: MAPE __% ; bias __ (signed). Biased lines flagged: ___.
Assumptions changed this refresh: ___.
```

### 4.4 KPI dictionary entry
```
KPI: <name>
  Plain meaning : <one sentence a non-finance reader understands>
  Formula       : <exact numerator ÷ denominator, with units>
  Source        : numerator ← <system/report>; denominator ← <system/report>
  Grain         : <per client / per preparer / firm-wide>, <period>
  Owner         : <single named owner>
  Gotchas       : <inclusions/exclusions, edge cases, common misdefinition>
Example —
KPI: Preparer utilization
  Plain meaning : share of a preparer's available time that is billable
  Formula       : chargeable hours ÷ available hours
  Source        : chargeable ← time system; available = work-week hrs − PTO − CPE
  Grain         : per preparer, monthly
  Owner         : Nadia (FP&A)
  Gotchas       : PTO & CPE are OUT of the denominator; target rate is firm-set [UNVERIFIED]
```

### 4.5 Scenario table + CFO-fundable business-case top sheet
```
SCENARIO TABLE — [decision], as of [date]            ($000)
Driver / assumption        Worst        Base         Best
Billable demand (hrs)      −10%         plan         +8%
Realization rate           −5 pts       plan         +2 pts
Avg bill rate              flat         plan          +3%
Key-client DSO             +30 days     plan         flat
──────────────────────────────────────────────────────────
Revenue                    ...          ...          ...
Contribution               ...          ...          ...
Runway (months)            ...          ...          ...    ← 30/60/90 band if Monte Carlo
Plan-against: <which scenario and why>.

CFO-FUNDABLE BUSINESS CASE (top sheet) — maps each section to the CFO objection it pre-empts:
  0. The ask        — $ amount, horizon, what's reallocated/unwound if approved
  1. The problem    — measured business gap in firm KPIs (sourced from Hal's actuals)
  2. The mechanism  — incremental plan (the hire / the service line), driver-based
  3. The return     — base/upside/downside RANGE: incremental contribution, payback,
                       NPV @ hurdle [UNVERIFIED], MARGINAL ROI of the last dollar
  4. Governance     — quarterly tripwires (metric + threshold + action), pause list
  5. Why now / why different — not a flat % uplift; an incremental thesis
  6. Risks          — volunteered failure modes + confidence interval on the estimate
  Appendix          — any peer benchmark (anchor only, NOT the argument — the % trap)
```
@cmo-budgeting/05 (fundable structure); @cmo-budgeting/04 (CFO's four demands).

---

## 5. Verification checklist (pre-output gate — mirrors the persona's pre-review)
Apply before anything leaves Nadia for Soph. If any fail, return to Eli/Quinn.

- [ ] **Variance:** every line above Elle's $ threshold has a **root cause** from the taxonomy (§2.5) and a **"so what."** Numbers without narrative go back. @persona
- [ ] **Decomposition done right:** cost lines **flexed** before judging spending (§2.3); revenue/margin lines **PVM-split** (§2.4) with the components summing to the total; one-time vs recurring labeled.
- [ ] **Forecast:** top-3 **sensitivities named with magnitude**; **confidence stated** (30/60/90 bands or per-line qualitative + breaking assumption). A point estimate without a range is a hope. @persona
- [ ] **Three number-types kept distinct:** Budget (fixed) | Actual | Forecast — never blended in one column (§2.6).
- [ ] **Forecast accuracy fed back:** last period's MAPE + **bias** computed; persistently biased lines flagged (§2.11).
- [ ] **Scenario:** base/best/worst present, each driven by **named assumption shifts**, not ±% on the total (§2.7); the plan-against scenario stated.
- [ ] **Business case:** decided on **incremental** cash flows; **marginal ROI** (not average) shown; tripwires + downside named; return quoted as a **range** (§2.8, §4.5).
- [ ] **KPI:** every KPI used carries a **cited definition** (§4.4); no metric used under two definitions; one owner each. @persona
- [ ] **Source tie-out:** every actual ties to Hal's close package / Imani's cash position / Anya's tax rate. Illustrative or unset figures flagged `[UNVERIFIED]`.
- [ ] **No invented benchmark.** Any peer ratio is an appendix anchor, not the basis of an ask (the % trap, @cmo-budgeting/01).
- [ ] **The lead is the narrative.** The "so what" is on page one; the table supports it.

---

## 6. Worked examples (methods applied end-to-end)

### 6.1 Revenue missed plan — PVM says it's a price story, not a demand story
Q2 service revenue came in at $1,050k vs a $1,000k budget — a **+$50k favorable** headline. Eli's draft stopped there. **Nadia's read (§3.2 + §2.4):** decompose before celebrating. Volume effect **+$60k** (more billable hours than planned), price/rate effect **−$25k** (average bill rate slipped — discounting on two renewals), mix effect **+$15k** (a richer advisory blend). The headline beat **masks a rate erosion** that is *recurring*. **So what:** the volume beat is real but the −$25k rate slip will repeat unless renewals are re-priced; the forecast holds on volume but flags rate as a downside sensitivity, and the H2 plan adds a pricing-review tripwire. The variance — not the +$50k — is the story. @method PVM; @persona.

### 6.2 Labor over budget — flex it before you judge it
Direct labor came in $640k vs $600k budget, **−$40k unfavorable.** A naive read says "overspent on people." **Nadia's read (§3.2 + §2.3):** flex first. At the *actual* (higher) billable volume, the flexed labor budget is $632k. So **Volume variance = −$32k** (you did more work — largely *justified* by the revenue volume beat in 6.1) and **Spending/efficiency variance = −$8k** (the genuinely controllable piece — slight overtime inefficiency). **So what:** ~80% of the "overspend" is volume-driven and self-funding; only the $8k efficiency slice is a performance issue. Without flexing, Eli would have escalated a $40k problem that is really an $8k problem. @method flexible budgeting.

### 6.3 Rolling forecast — a one-time true-up does NOT raise the year
At the May close, April revenue beat forecast by $40k. Quinn's instinct: raise the full-year forecast. **Nadia's read (§3.3 + §2.5):** characterize the variance first. The $40k is a **one-time** prior-year billing true-up (non-recurring), not a run-rate change. **So what:** book the $40k in actuals, but **do not** re-drive the open months upward — the underlying drivers (hours, realization, rate) are unchanged. The rolling forecast re-extends with a flat run-rate; the forecast-accuracy scorecard (§2.11) notes the beat as one-time so it doesn't pollute the bias metric. Confidence band unchanged; top-3 sensitivities (key-client DSO, realization, one preparer's pipeline) restated. A forecaster who banks one-time beats into the run-rate builds an upward **bias** — the dangerous error. @method rolling forecast + forecast-accuracy.

### 6.4 Business case — "hire a preparer?" on incremental, marginal terms
The firm is turning away billable demand and a partner wants a headcount add. **Nadia's read (§3.5 + §2.8):** frame the business problem (turning away ~$X of demand at Y% realization), then model **incremental** cash flows only — incremental billable revenue at the marginal realization/rate, less the fully-loaded cost of the hire, less ramp. **Payback** ≈ N months; **NPV** > 0 at the firm hurdle rate `[UNVERIFIED]`; **breakeven** at U% utilization. Build base/upside/downside as named scenarios (downside = ramp is slower AND demand softens). **Tripwire:** if the new hire's utilization is below breakeven by end of Q2, pause the second planned add. Volunteer the failure modes (ramp risk, demand-softening risk). Present in the CFO-fundable top sheet (§4.5) with any peer staffing ratio in the appendix only — never as the argument (the % trap). @method incremental capital budgeting; @cmo-budgeting/04–05.

### 6.5 KPI discipline — "what is our utilization rate?" asked two ways
Two dashboards report "utilization" — one at 78%, one at 71%. **Nadia's read (§3.6 + §2.9):** STOP; this is the one-definition violation. The gap is the **denominator**: one includes PTO/CPE in available hours, one excludes them. Collapse to the persona's single definition — *chargeable ÷ (work-week hours − PTO − CPE)* — write the dictionary entry (§4.4), assign one owner, and reissue both dashboards off it. The *target* rate stays `[UNVERIFIED]` (firm-set; reference AICPA Practice Management for shape, not a fabricated number). Until the definition is fixed, neither number is a deliverable. @persona hard rule.

---

## 7. Source map (verifiable paths + named methods)

**Marathon-grounded (one-hop, adjacent CMO branch — cite as `@cmo-budgeting/NN`):**
All under `(grounded in domain research; re-ground with your own sources)`.

| Tag | Topic | File |
|---|---|---|
| @cmo-budgeting/summary | Marketing-budgeting + CMO-CFO seam distilled (ZBB, % trap, fundable case) | `(grounded in domain research; re-ground with your own sources)` |
| @cmo-budgeting/01 | The percent-of-revenue trap (benchmark = anchor, not answer) | `…/01-percent-of-revenue-trap.md` |
| @cmo-budgeting/02 | Zero-based budgeting; Kraft Heinz cautionary case; reallocation-not-retraction; reinvestment rule | `…/02-zero-based-budgeting.md` |
| @cmo-budgeting/04 | The CMO-CFO seam: CFO's four demands (incrementality, business-KPI translation, capital thesis, optionality/downside) | `…/04-cmo-cfo-seam.md` |
| @cmo-budgeting/05 | CFO-fundable business-case structure (problem→ask→mechanism→return-range→tripwires→downside; benchmarks in appendix) | `…/05-fundable-business-case.md` |

**Professional-standards-grounded (named public methods — NOT in this repo's research; cited by method name):**

| §  | Method | Standard body / origin |
|---|---|---|
| 2.1 | Driver-based budgeting | CGMA / standard managerial accounting |
| 2.2 | Zero-based budgeting (ZBB) | Pyhrr (orig.); 3G/McKinsey marketing application via @cmo-budgeting/02 |
| 2.3 | Flexible (flexed) budgeting; volume vs spending variance | CIMA / standard cost accounting |
| 2.4 | Price-Volume-Mix (PVM) variance decomposition | standard FP&A / managerial accounting |
| 2.5 | Root-cause variance taxonomy + "so what" | management-reporting practice; @persona algorithmic answer |
| 2.6 | Rolling forecast / beyond budgeting | CIMA / Beyond Budgeting Round Table (BBRT) |
| 2.7 | Scenario vs sensitivity analysis; Monte Carlo | standard decision/risk analysis |
| 2.8 | Incremental-cash-flow capital budgeting (NPV, payback, marginal ROI, breakeven) | standard corporate finance |
| 2.9 | KPI governance (one-definition-one-owner) | metric-governance / single-source-of-truth practice |
| 2.10 | Cohort/retention analysis; unit economics (LTV, CAC, payback) | SaaS-metrics literature, **adapted** to multi-year/seasonal firm shape per @persona |
| 2.11 | Forecast-accuracy metrics (MAPE, bias, MAD) | demand-planning / S&OP practice |

**Firm context (runtime paths):** `.claude/agents/head-fpa-nadia.md` (domain, hard rules, dev-consult answers: utilization definition, variance taxonomy, 30/60/90 confidence, cohort shape) and `.claude/agents/org.config.json` → `advisory_departments.cfo-fpa` (head=nadia; seniors=eli/quinn; scope rows) plus `.claude/comms/comms.py` for the channel ACL (chain Elle→Soph→Nadia; Eli/Quinn floor; Hal/Imani/Anya boundaries).

---
*Gaps / open items (flag to Soph if a deliverable turns on these):*
- **No FP&A marathon corpus exists for this branch.** §2 is professional-standards-grounded (see §7 method table); only ZBB and the fundable-business-case structure are research-cited (one hop to CMO, `@cmo-budgeting/02` / `@cmo-budgeting/05`). If FP&A becomes a recurring need, commission a marathon on: PVM order-of-operations conventions, services-firm cohort/retention shapes, and forecast-accuracy targets.
- **Every firm-specific number is `[UNVERIFIED]`** — hurdle/discount rate, utilization target, Elle's variance materiality threshold, retention curves, LTV/CAC, headcount-to-revenue ratios. These must come from the firm's actuals (Hal/Imani/Anya/Elle), not from this brain (see §5 source-tie-out gate). **No benchmark is asserted as fact here.**
- **PVM convention not fixed:** volume-first vs price-first changes where the residual lands. The firm must adopt **one** convention; this brain defaults to volume→mix→price but does not claim it as authoritative (see §2.4).
- **Monte Carlo / 30-60-90 bands** are method-correct but require distributional inputs the firm may not yet maintain; discrete base/best/worst is the honest fallback until those distributions exist (see §2.7).
- **Cross-branch boundary live:** capitalization/GAAP treatment (Hal/Elle), cash truth (Imani), tax rate (Anya). Nadia models *from* their numbers; she does not own them.
