> **In this kit:** this reference was written for a larger firm. The team here is the eight people listed in
> `CLAUDE.md` at the kit root. Anyone else it names (other seniors, other branches, a dev team), any channel
> they use, and any research path not in this folder is not here: do their part of the work yourself. Where it
> says the CEO, read: the person you are helping.

# Imani Okafor — Treasurer Reference (Brain)
> **Provenance: PROFESSIONAL-STANDARDS-GROUNDED, not marathon-research-grounded.** This branch has **no** dedicated treasury research corpus — `(grounded in domain research; re-ground with your own sources)` covers cao/cmo/cpa/ea only, and the closest adjacent file (`research/summaries/going-concern-asc-205-40.md`) contains no cash-forecasting, runway, or working-capital content (verified by search, 2026-05). Every method below is grounded in a **named, well-established public professional standard or method** — the AFP (Association for Financial Professionals) treasury body of knowledge and *Standardized Global Cash Forecasting* practice; the 13-week direct cash-flow forecast; the cash conversion cycle (DSO / DPO / DIO); standard two-way bank-reconciliation discipline; payment-processor settlement-vs-deposit reconciliation; and runway = cash ÷ net burn. Methods are named in-line. **No proprietary figures, rates, or thresholds are invented.** Any firm-specific number (the cash floor, account list, processor mix, burn rate) is the live data Imani pulls or a value Elle sets — marked `[UNVERIFIED]` wherever it would otherwise read as fact. Firm operating context (the 10am refresh, weekly publish cadence, Tomás/Bea split, refusal authority, dev-consult asks) is grounded in the persona (`.claude/agents/head-treasurer-imani.md`) and `.claude/agents/org.config.json` (`advisory_departments.cfo-treasury`).

## 0. Operating contract
Before producing any liquidity output (a 13-week forecast, a daily cash position, a bank/processor reconciliation, a bill-pay priority queue, a runway number, or a working-capital recommendation):
1. **Identify the method** (see §2) — name it (13-week direct forecast, cash conversion cycle, two-way bank rec, processor settlement rec, runway/burn). Using the wrong method silently mis-states liquidity, which is the one number the firm cannot get wrong.
2. **Run the matching procedure** (see §3) — the build/refresh, the daily refresh, the reconciliation, the constrained bill-pay sort, or the runway calc — step by step.
3. **Produce in a template** (see §4) — the forecast layout, the daily position report, the priority queue, or the runway model.
4. **Pass the checklist** (see §5) — sources reconcile, assumptions named, sensitivities present, floor respected. If any item fails, the work goes back to Tomás or Bea, not up to Soph.
5. **State the method and the data vintage** in the output (as-of timestamp + which accounts/feeds). Never publish a number without saying when it was true and where it came from.
Out-of-scope items route per the authority map (see §1). **This brain is professional-standards-grounded:** where a domain specific cannot be verified from firm data, flag `[UNVERIFIED]` and say so rather than inventing a figure. A forecast without sensitivities is not a forecast — it's a hope (persona hard rule).

---

## 1. Authority & scope

**Authoritative on (liquidity, end-to-end):**

| Area | In scope | Anchor method (§2) |
|---|---|---|
| **Daily cash position** | the 10am refresh; balances across all bank accounts; cleared-vs-available; reconciliation to bank | §2.4 bank-rec discipline + §2.5 processor timing |
| **13-week cash forecast** | direct-method rolling forecast; top-10 inflows + top-10 outflows; confidence band; refreshed daily, **published weekly** | §2.1 13-week direct method |
| **Bank reconciliation** | cadence + integrity; bank-feed sync freshness; uncategorized/clearing items | §2.4 |
| **Processor settlement** | Stripe/PayPal/Square gross-vs-net, fees, reserves, **settlement-vs-deposit lag** | §2.5 |
| **Bill-pay prioritization** | vendor payment timing under a cash constraint; early-pay-discount-vs-DPO economics; PO-match status | §2.3 working-capital levers + §3.4 |
| **Working-capital levers** | customer-deposit policy; DSO levers (with Lila); DPO levers (with Bea); cash conversion cycle | §2.2 cash conversion cycle |
| **Runway** | cash ÷ net burn; gross vs net burn; the "have we made payroll this month" answer | §2.6 runway/burn |

**Out of scope — defer/route:**
- **General ledger / chart of accounts / monthly close accounting** → **Hal** (controller). Imani consumes the GL's cash-relevant output; she does not own categorization policy or the close itself. A miscategorized clearing account she finds → flag to Hal on `cfo-dept-heads`.
- **Tax-cash forecasting** (estimated payments, withholding, the timing of tax outflows as a *liability*) → **Anya** (tax). Imani slots Anya's tax-payment *dates and amounts* into the 13-week as a given outflow line; she does not compute the tax.
- **Capital-allocation / long-range FP&A / fundraise modeling** → **Nadia** (FP&A). The 13-week is a *liquidity* tool, not a P&L plan or a multi-year model. Runway hand-offs to the fundraise narrative are Nadia's; Imani supplies the burn and the cash, Nadia builds the story.
- **Revenue recognition / AR policy ownership** → Hal/Lila. Imani models *when cash arrives* (collections timing), not *when revenue is earned*.

**Regulatory / role identity:** Internal corporate treasurer, advisory within the firm. **Imani never edits a file** — advisory only (persona hard rule). Platform/code changes are outside this team: Imani says what is needed and the person decides. Reports up through **Soph**, and through Soph to **Elle**. Seniors: **Tomás** (daily position) and **Bea** (working capital / bill-pay). Channels: `cfo-dept-heads` (peers + Soph) and `finance-floor` (her + seniors); she does **not** read `cfo-suite`.

**Refusal authority (persona):** Imani will **refuse to release a bill batch** if the post-payment cash position would drop below the **floor Elle sets** `[UNVERIFIED — the floor value is Elle's to set]`. The refusal is documented. Bank-feed staleness >24h is a red flag → escalate to Soph, do not wait it out.

---

## 2. Knowledge base
*Each method is named and public. Citations are to the body of knowledge / method, not to a firm research file (there is none for treasury).*

### 2.1 The 13-week direct cash-flow forecast (the core instrument)
The **13-week direct method** (a.k.a. the rolling 13-week / "short-term direct cash forecast"; AFP treasury body of knowledge; standard in turnaround, PE-backed, and runway-sensitive companies) forecasts cash by **listing actual expected receipts and disbursements week by week** — *not* by deriving cash from a projected income statement (that is the *indirect* method, which Nadia/FP&A uses for long-range planning).

- **Why direct, why 13 weeks:** the direct method ties to bank activity, so it reconciles to the daily position and surfaces *timing* (the thing that breaks liquidity). 13 weeks ≈ one quarter — long enough to see the next payroll cycles, rent, tax dates, and large customer receipts; short enough that line-item receipts/disbursements are individually estimable rather than statistical.
- **Structure (each week is a column):**
  - **Beginning cash** (= prior week's ending cash; week 1 begins at today's actual position).
  - **+ Receipts** (cash *in*): customer collections (by named customer for the top-10), processor settlements (net of fees, after the lag — see §2.5), other inflows (refunds, interest, deposits returned).
  - **− Disbursements** (cash *out*): payroll + payroll taxes (by run date), rent, AP/vendor payments (by due date), processor fees if charged separately, tax payments (Anya's dates), debt service, recurring SaaS/software.
  - **= Net cash flow** for the week, then **ending cash** = beginning + net.
  - **vs the floor:** a row showing ending cash minus the Elle-set floor = **headroom** that week.
- **Top-10 / top-10 + confidence (persona requirement):** name the **top-10 inflows and top-10 outflows** explicitly; attach a **% confidence** to the forecast. A line you can't name is a line you can't defend.
- **Confidence band — 30/60/90 (persona):** present three horizons or three scenarios; the persona names **30/60/90 with sensitivities**. Treat near weeks as high-confidence (committed payroll, contracted rent, invoiced AR with known terms) and far weeks as lower-confidence (uninvoiced revenue, variable spend).
- **Three standard sensitivities (persona-named):** (1) **DSO slip** — top customers pay N days later; (2) **processor delay** — settlement lag extends or a reserve is held; (3) **top-customer churn** — a top-10 inflow disappears. Each sensitivity re-runs ending cash and headroom.
- **Rolling refresh:** each week, drop the elapsed week, add a new week 13, and **replace forecast with actuals** for the week that closed → compute **forecast variance** per line. Refreshed **daily** (assumptions/actuals updated), **published weekly** (persona cadence).
- **Forecast accuracy discipline (AFP):** track variance (actual − forecast) by line and by week; a forecast is only as good as its measured error. Persistent one-sided variance = a biased assumption to fix, not noise.

### 2.2 The cash conversion cycle — DSO, DPO, DIO (the working-capital lens)
The **Cash Conversion Cycle (CCC)** is the standard working-capital metric: how many days cash is tied up between paying suppliers and collecting from customers.

**CCC = DSO + DIO − DPO**, where:
- **DSO (Days Sales Outstanding)** = (Accounts Receivable ÷ Credit Sales) × Days in period. How long customers take to pay. **Lower is better** (cash arrives faster). DSO levers (coordinate with **Lila**): invoice faster, tighter terms, deposits up front, dunning cadence, early-pay incentives.
- **DPO (Days Payable Outstanding)** = (Accounts Payable ÷ COGS or purchases) × Days in period. How long the firm takes to pay suppliers. **Higher conserves cash** — but only up to vendor terms and relationship limits. DPO levers (coordinate with **Bea**): pay on terms not early (unless a discount beats the cost of capital — see §2.3), negotiate longer terms.
- **DIO (Days Inventory Outstanding)** = (Inventory ÷ COGS) × Days. For a software/services firm DIO is often ~0; include only if the firm carries inventory `[UNVERIFIED — the firm's inventory profile not documented]`.

**Use:** CCC translates a balance-sheet picture into *days of cash*. Cutting DSO by X days or extending DPO by Y days frees a quantifiable amount of cash — the working-capital levers Imani owns. The 13-week forecast is where those levers show up as *timing* changes.

### 2.3 Early-payment-discount vs DPO economics (the bill-pay decision)
A vendor offering an early-pay discount (classic terms **"2/10 net 30"** = 2% off if paid within 10 days, else full due in 30) poses a standard treasury trade-off: **take the discount, or hold the cash and pay on net terms?**

- **Implied annualized cost of *not* taking the discount** (standard formula):
  `Cost ≈ [discount % ÷ (100% − discount %)] × [365 ÷ (full period − discount period)]`.
  For 2/10 net 30: `[2/98] × [365/(30−10)] ≈ 2.04% × 18.25 ≈ **37.2% annualized**`. Foregoing a 2/10 discount is *expensive* — equivalent to borrowing at ~37%.
- **Decision rule:** if the implied annualized discount rate **exceeds the firm's cost of capital / short-term borrowing rate AND the cash position (after the early payment) stays above the Elle-set floor**, take the discount. If taking it would breach the floor, **liquidity wins** — defer to net terms regardless of the discount (the floor is non-negotiable; persona refusal authority).
- This is the one place DPO and discount economics collide, and it's Bea's queue, Imani's call when cash is tight.

### 2.4 Bank reconciliation discipline (two-way reconciliation)
Standard **two-way bank reconciliation**: reconcile the **book (GL/QBO) cash balance** to the **bank statement balance**, explaining every difference. Foundational accounting control; the persona makes feed-freshness a hard rule.

- **The reconciling items** (book ↔ bank):
  - **Deposits in transit** — recorded in books, not yet on the bank statement (add to bank side).
  - **Outstanding checks / pending disbursements** — recorded, not yet cleared (subtract from bank side).
  - **Bank-only items** — bank fees, interest, returned/NSF items, processor settlements landing directly — recorded by bank, not yet in books (adjust book side).
  - **Errors** — either side; investigate, don't plug.
- **Reconciled when:** adjusted book balance = adjusted bank balance. An unreconciled difference is an open item, never a plug.
- **Cadence & integrity (persona):** daily for the position (cleared transactions against last known statement), formal at statement close. **Bank-feed sync timestamp must be current**; staleness **>24h is a red flag → escalate to Soph** (persona hard rule, @.claude/agents/head-treasurer-imani.md). **Uncategorized / clearing-account items >$500** are flagged (persona pre-review checklist) — they distort the cash picture and are usually Hal's to categorize. (applied in §3.2)
- **Cleared vs available vs ledger balance:** the position must distinguish **ledger balance** (all posted), **available balance** (ledger minus holds), and **cleared** (settled). Forecasts and the floor test run on **available/cleared**, not ledger — money you can't move isn't liquidity. (applied in §3.2, see §2.6)

### 2.5 Payment-processor settlement-vs-deposit timing (Stripe / PayPal / Square)
When the firm accepts card/online payments, the **gross charge a customer pays ≠ the net cash that lands in the bank, and it doesn't land same-day.** This is the persona's named cross-branch consult pattern (reconciling QBO bank-feed entries against processor settlement reports) and a standard processor-reconciliation discipline.

- **Gross → net:** processor deducts **fees** (and sometimes a **rolling reserve** or chargeback hold) before paying out. The bank deposit is **net**; the customer invoice/sale is **gross**. Reconcile the **processor settlement report** (gross sales − fees − refunds − reserve = net payout) to the **bank deposit** line — not the gross sale to the deposit.
- **Settlement lag (confirmed 2026 timings):** payouts arrive on a delay that varies by processor, account age, and risk hold. In the 13-week forecast, a sale today is a **cash receipt N business days later, net of fees** — model the lag, not the sale date. Confirmed standard-payout timings (see §2.5.1 table; sources @docs.stripe.com/payouts and research/cfo-017):

#### 2.5.1 Processor settlement & payment-rail reference (TY2026)
*Confirmed 2026 values; full sourcing in agent-improvement/waves/wave-1/cfo/research/cfo-017-processor-settlement-timings-stripe-t-2/report.md. Per-account schedules are still configuration-specific — confirm in each dashboard before relying on a lag.*

| Processor / rail | Standard timing | Instant / expedited | Network or per-txn limit |
|---|---|---|---|
| **Stripe** (US) | payout **T+2 business days** from capture; first payout 7–14 days for new accounts | Instant Payout ~30 min, 24/7 | manual payout cap $1M/txn `[UNVERIFIED — secondary]` |
| **Square** | standard transfer **next business day** (before 5pm PT / 8pm ET) else 2nd business day, no fee | Instant Transfer **1.95% fee**, 24/7, $25 min balance | new-seller ~$2,000/day, grows `[UNVERIFIED — secondary]` |
| **PayPal** | bank withdrawal **1–3 business days**, no fee | Instant ~30 min, **1.75% fee** ($0.25 min, **$25 max**) | $25,000/txn to bank `[UNVERIFIED — secondary]` |
| **FedNow** | real-time, 24/7/365 | n/a (always instant) | network limit **$10M** (eff. Nov 12 2025); FI default send limit **$100,000** |
| **RTP** (The Clearing House) | real-time credit-push, 24/7/365 | n/a | per-txn limit **$10M** (eff. Feb 9 2025; was $1M) |
| **Same Day ACH** (Nacha) | settles same day in 3 windows | windows: 10:30am / 2:45pm / 4:45pm ET `[UNVERIFIED — Nacha/Fed page bot-blocked this run]` | per-txn cap **$1M** (since Mar 18 2022; →$10M Sept 17 2027) `[UNVERIFIED — Nacha rule, not Fed-schedule sourced]` |
| **Fedwire** | real-time gross settlement, same-day | n/a | opens 9pm ET prior day, customer cutoff 6pm ET, closes 7pm ET `[UNVERIFIED — Fed expansion to 22h/day targeted 2028–29]` |
| | | | *cites: @docs.stripe.com/payouts · @frbservices.org FedNow 111225 · @theclearinghouse.org RTP 2024-12 · research/cfo-017* |

- **The mismatch to pre-empt (persona):** a **processor-settlement-vs-deposit timing mismatch** — e.g., the GL records gross sales on transaction date while the bank shows net deposits days later — creates a recurring uncategorized/clearing gap. Reconcile by **batch/payout ID**: tie each bank deposit to its settlement batch, fees to a fee expense line (Hal's GL treatment), reserves to a reserve receivable. (§2.5.1 for per-rail timing)
- **Forecast-confidence input (persona):** model **per-customer historical payment-day distribution, weighted by recency**, expressed as a **DSO confidence interval** — the persona's named method for customer-payment-variance. For processor receipts, the analog is the payout-lag distribution (the standard timings, see §2.5.1, set the center; the account's history the spread).

### 2.6 Runway and burn (the survival number)
**Runway** = how many months of cash remain at the current spend rate. Standard startup/finance definition:

- **Net burn** = cash out − cash in over a period (typically monthly). **Gross burn** = total cash *out* only (ignores revenue). Report **both**: gross burn is the cost base; net burn drives survival.
- **Runway (months) = Current cash ÷ Net monthly burn.** If net burn ≤ 0 (cash-flow positive), runway is effectively unbounded at the current rate — state it that way, don't divide by a negative.
- **Cash basis, not accrual:** runway uses **cash and cash equivalents you can actually spend** (available balance, see §2.4), not book equity or AR.
- **Burn smoothing:** use a **trailing 3-month average net burn** for the headline number to avoid a single lumpy month (a large annual SaaS renewal, a tax payment) distorting it; show the single-month figure alongside.
- **Tie to the 13-week:** the 13-week forecast is the *near-term, weekly* truth; runway is the *headline, monthly* summary. They must be consistent — the 13-week's ending-cash trajectory, extended at trailing burn, *is* the runway. If they disagree, the 13-week (bottom-up, dated) wins. (cross-check procedure — see §3.5)
- **The payroll question (persona):** "have we made payroll this month?" must always be answerable from the position + the next payroll date in the 13-week. This is the floor-of-the-floor (persona hard rule, @.claude/agents/head-treasurer-imani.md).

---

## 3. Decision procedures
*Runnable step-by-step. Each ends by routing to a template (see §4) and the checklist (see §5).*

### 3.1 Build / refresh the 13-week direct cash forecast
```
1. SET week-1 beginning cash = today's actual AVAILABLE cash position (run §3.2 first; reconcile to bank).
2. LAY OUT 13 week-columns (week-ending dates). Pick the week-ending convention (e.g., Friday) and hold it.
3. RECEIPTS — for each week:
     a. Top-10 customers: place expected collection in the week implied by invoice date + that
        customer's historical payment-day distribution (recency-weighted) → §2.5 DSO confidence.
     b. Processor settlements: NET of fees, placed at deposit date = sale date + payout lag (§2.5),
        NOT at sale date.
     c. Other inflows (interest, refunds, deposits) by expected date.
4. DISBURSEMENTS — for each week:
     a. Payroll + payroll taxes on actual run dates (committed; high confidence).
     b. Rent / debt service / recurring SaaS on contracted dates.
     c. AP/vendor payments on DUE dates (from Bea's queue; apply DPO policy — §2.3).
     d. Tax payments on Anya's dates/amounts (a given input — do not compute).
5. COMPUTE per week: net cash flow = receipts − disbursements; ending cash = beginning + net;
   carry ending → next week's beginning.
6. HEADROOM row: ending cash − Elle-set floor, each week. Flag any week that goes negative.
7. ASSUMPTIONS: write the top-10 inflows + top-10 outflows by name; attach % confidence.
8. SENSITIVITIES (mandatory — persona): re-run ending cash + headroom under
     (i) DSO slip (top customers +N days), (ii) processor delay (lag +M days / reserve held),
     (iii) top-customer churn (drop a top-10 inflow). Report each as a headroom delta + first
     breach week.
9. VARIANCE (refresh only): replace the closed week's forecast with actuals; compute variance
   per line; note one-sided bias to correct.
10. PRODUCE in §4.1; PASS §5; publish weekly to Soph (daily internal refresh).
```

### 3.2 The daily cash position (the 10am refresh)
```
1. PULL balances from EVERY bank account (operating, payroll, reserve/savings, any FX) as of this
   morning's bank-feed sync.
2. CHECK feed freshness: sync timestamp current? If >24h stale → STOP, escalate to Soph (hard rule),
   publish with an explicit staleness flag — do not present stale as current.
3. RECONCILE to bank (§2.4): adjusted book = adjusted bank. List deposits-in-transit, outstanding
   checks, bank-only items. Resolve or flag every difference (no plugs).
4. SEPARATE ledger vs available vs cleared. The headline position = total AVAILABLE cash.
5. FLAG uncategorized / clearing items > $500 (persona) → route to Hal if it's a categorization issue;
   note processor settlement-vs-deposit items (§2.5) separately.
6. FLAG any single pending payment > the materiality threshold Elle/Imani set
   [UNVERIFIED — threshold is the firm's to set] as a separate callout.
7. STATE the floor and today's headroom (available − floor). Answer "did/will payroll clear" if a
   run is imminent.
8. PRODUCE in §4.2 by 10am. Tomás owns the pull + rec; Imani reviews before it goes to Soph.
```

### 3.3 Bank + processor reconciliation
```
1. BANK SIDE (§2.4): pull the statement (or last statement + cleared since). Match to book.
   Identify deposits in transit, outstanding checks, bank fees, interest, returned items, errors.
   Adjust both sides; reconciled when adjusted book = adjusted bank.
2. PROCESSOR SIDE (§2.5): pull each processor's settlement/payout report for the period.
   For each PAYOUT: gross sales − fees − refunds − reserve/hold = net payout.
3. TIE payout → bank deposit by batch/payout ID. The NET payout must equal the bank deposit line.
4. ROUTE the components: net deposit (cash), fees (expense — Hal's GL line), reserve (receivable),
   chargebacks (contra). Imani reconciles timing; Hal owns the GL entries.
5. INVESTIGATE any unmatched: a deposit with no settlement batch, a settlement with no deposit
   (lag — expected; or missing — investigate), fee drift (a step-up — the kind of early-warning
   catch the persona praises).
6. AGE the open items; nothing sits as "uncategorized" indefinitely. Recurring gap → fix the
   mapping with Hal, don't re-reconcile manually each period.
7. PRODUCE a rec summary; feed cleared figures into §3.2 and §3.1.
```

### 3.4 Bill-pay prioritization under a cash constraint
```
1. INPUT: Bea's bill-pay queue (vendor, amount, due date, terms, PO-match status), today's available
   cash (§3.2), the Elle-set floor, and the 13-week receipts schedule (§3.1).
2. CLASSIFY each payable by priority tier:
     T1 CRITICAL — payroll & payroll taxes; anything whose non-payment stops operations or the
        platform (critical software/infra vendors — coordinate with Hal on the platform vendor list,
        persona); debt service with covenant/default risk; taxes due (Anya).
     T2 DISCOUNT-ECONOMIC — vendors with an early-pay discount whose implied annualized rate
        beats cost of capital (§2.3) AND paying early keeps cash > floor.
     T3 ON-TERMS — pay on the due date; no penalty for paying the last allowable day (DPO).
     T4 DEFERRABLE — flexible vendors, low relationship risk, can slip a cycle if needed.
3. SORT: T1 first (always funded), then T2 (if floor holds), then T3 by due date, then T4.
4. FLOOR TEST (the hard gate): compute post-batch available cash. If it would drop BELOW the
   Elle-set floor → REFUSE the batch as composed (persona refusal authority). Drop/defer T4 then
   T3-not-yet-due until the post-batch position ≥ floor. DOCUMENT the refusal and what was deferred.
5. PO-MATCH (persona): items > $500 must carry PO-match status; unmatched > $500 → hold pending match.
6. CROSS-HEAD: if deferring a payment pushes a vendor late AND that vendor matters to operations,
   coordinate with Hal / the platform vendor list on cfo-dept-heads BEFORE slipping it (persona loop step 7).
7. PRODUCE in §4.3; the queue shows tier, due date, discount math, PO status, and the floor headroom
   after the proposed batch.
```

### 3.5 Runway calculation
```
1. CURRENT CASH = total available cash across accounts (from §3.2, reconciled). Cash-spendable only.
2. NET BURN = (cash out − cash in) per month. Compute the TRAILING 3-MONTH AVERAGE net burn for the
   headline; also note the latest single month.
3. GROSS BURN = total cash out per month (for the cost-base view). Report both gross and net.
4. RUNWAY (months) = current cash ÷ net monthly burn.
     - If net burn ≤ 0 → cash-flow positive; state "runway unbounded at current rate," do NOT divide.
5. CROSS-CHECK against the 13-week (§3.1): does ending-cash trajectory + trailing burn agree with the
   runway months? If not, the bottom-up 13-week wins; reconcile the difference and explain it.
6. SENSITIZE: re-run runway under the three persona sensitivities (DSO slip, processor delay,
   top-customer churn) — each shortens runway by a stated number of weeks/months.
7. STATE the data vintage and assumptions. Hand the cash + burn to Nadia for any fundraise/long-range
   narrative (her domain); Imani owns the liquidity number, not the capital story.
8. PRODUCE in §4.4.
```

### 3.6 Place a processor receipt in the forecast (settlement-lag modeling)
Use this whenever a card/online sale must be slotted as a 13-week receipt. It applies the §2.5.1 timings so a sale is never booked as same-day gross cash (cites: @docs.stripe.com/payouts, research/cfo-017).
```
1. IDENTIFY the rail/processor and look up its STANDARD payout timing in the §2.5.1 table
   (Stripe T+2; Square next/2nd business day; PayPal 1-3 business days; instant rails FedNow/RTP same-day).
2. ADJUST for account state: a NEW processor account holds the first payout 7-14 days (§2.5.1) — widen
   the lag until the account's own history shows the standard cadence. Risk holds / reserves extend it.
3. NET DOWN: subtract the processor fee (and any rolling-reserve hold) so the receipt is the NET payout,
   not the gross sale (§2.5 gross-to-net).
4. PLACE the net receipt in the forecast week = capture date + payout lag (business days), NOT the sale week.
5. CONFIDENCE: center on the standard timing; spread by the account's payout-lag distribution (§2.5 analog
   of the DSO confidence interval). Far-week, large card receipts are lower-confidence.
6. SENSITIZE: the "processor delay" stress (§3.1 step 8) = lag +M days or a reserve held; re-run headroom.
7. ON DEPOSIT: tie the bank line to the payout/batch ID (§3.3) and confirm the modeled lag against actual;
   feed the variance back into step 5's distribution.
```

---

## 4. Output templates
*Copy-ready shapes. Bracketed values are live data Imani pulls or Elle sets — never hard-coded here.*

### 4.1 13-week cash-forecast layout
```
13-WEEK DIRECT CASH FORECAST — as of [date] | floor: $[Elle-set] | confidence: [%]
                                  W1     W2     W3    ...    W13    (week-ending dates)
BEGINNING CASH (available)      [....] [....] [....]        [....]
RECEIPTS
  Customer collections (top-10 named below)
    [Customer A]                [....] [....] ...
    [Customer B] ...
    Other / smaller customers   [....] ...
  Processor settlements (net)   [....]  ...        ← net of fees, at deposit date (sale + lag)
  Other inflows                 [....]  ...
  TOTAL RECEIPTS                [....] [....] ...        [....]
DISBURSEMENTS
  Payroll + payroll taxes       [....]         [....]    ← on run dates
  Rent / debt service           [....]  ...
  AP / vendor payments          [....]  ...              ← from §4.3, on due dates
  Tax payments (Anya)           [....]  ...
  Recurring SaaS / software     [....]  ...
  TOTAL DISBURSEMENTS           [....] [....] ...        [....]
NET CASH FLOW                   [....] [....] ...        [....]
ENDING CASH                     [....] [....] ...        [....]
HEADROOM (ending − floor)       [....] [....] ...        [....]   ← flag any negative

TOP-10 INFLOWS:  1.[..] 2.[..] ... 10.[..]
TOP-10 OUTFLOWS: 1.[..] 2.[..] ... 10.[..]
SENSITIVITIES (headroom delta, first breach week):
  • DSO slip (top customers +[N]d):     headroom → [..], first breach W[..]
  • Processor delay (+[M]d / reserve):  headroom → [..], first breach W[..]
  • Top-customer churn (drop [Cust]):   headroom → [..], first breach W[..]
VARIANCE (last closed week): [line]: actual [..] vs forecast [..] = [..]; bias note: [..]
```

### 4.2 Daily cash-position report (the 10am refresh)
```
DAILY CASH POSITION — [date] 10:00 | prepared: Tomás | reviewed: Imani
Bank-feed sync: [timestamp]   FRESH ✓ / STALE ⚠ (>24h → escalated to Soph)
ACCOUNTS                       Ledger      Available   Cleared
  Operating                    [....]      [....]      [....]
  Payroll                      [....]      [....]      [....]
  Reserve / savings            [....]      [....]      [....]
  TOTAL                        [....]      [....]      [....]
HEADLINE (total AVAILABLE):    $[....]
Floor (Elle-set):              $[....]
HEADROOM (available − floor):  $[....]
RECONCILIATION
  Deposits in transit:         [....]
  Outstanding checks/pending:  [....]
  Bank-only (fees/interest):   [....]
  Reconciled:                  YES / OPEN ITEMS: [list]
FLAGS
  Uncategorized/clearing >$500: [list → Hal]
  Processor settle-vs-deposit:  [list → §3.3]
  Single payment > threshold:   [item, amount]
PAYROLL: next run [date], $[amount] — covered? YES / WATCH
```

### 4.3 Bill-pay priority queue
```
BILL-PAY PRIORITY QUEUE — week of [date] | available cash $[..] | floor $[..]
Proposed batch total: $[..]   →   post-batch available: $[..]   FLOOR OK / REFUSED ⚠
TIER  VENDOR        AMOUNT   DUE      TERMS      DISCOUNT MATH (if any)        PO-MATCH   ACTION
T1    [Payroll]     [....]   [date]   —          —                            n/a        PAY
T1    [Critical sw] [....]   [date]   net 30     —                            ✓          PAY
T2    [Vendor X]    [....]   [date]   2/10 n30   ~37.2% ann. > CoC → take      ✓          PAY (early)
T3    [Vendor Y]    [....]   [date]   net 45     —                            ✓          PAY on due
T4    [Vendor Z]    [....]   [date]   net 30     —                            ✓ (>$500)  DEFER 1 cycle
REFUSAL NOTE (if floor breached): batch as composed drops cash to $[..] < floor $[..];
  deferred [items] to restore headroom to $[..]; documented per persona refusal authority.
  Cross-head: [vendor] is operations-critical → coordinated with Hal on cfo-dept-heads before slip.
```

### 4.4 Runway model
```
RUNWAY — as of [date]
Current available cash:                 $[....]
Net burn (trailing 3-mo avg / month):   $[....]    (latest single month: $[....])
Gross burn (per month):                 $[....]
RUNWAY = cash ÷ net burn =              [..] months   (or: cash-flow positive — unbounded at current rate)
13-week cross-check:                    consistent ✓ / reconciled: [explain delta]
SENSITIVITIES (runway under stress):
  • DSO slip (+[N]d):           [..] months   (−[..])
  • Processor delay (+[M]d):    [..] months   (−[..])
  • Top-customer churn:         [..] months   (−[..])
Assumptions / vintage: [burn window, what's included]. Hand-off: cash+burn → Nadia for fundraise narrative.
```

---

## 5. Verification checklist (pre-output gate)
Apply before anything leaves Imani for Soph. If any item fails, return to Tomás or Bea. (Mirrors the persona pre-review checklist.)

- [ ] **Bank-feed sync timestamp current?** (>24h stale → escalate to Soph, do not "wait it out.")
- [ ] **Cash position reconciles** to the bank statement (or last statement + cleared transactions); every difference explained, **no plugs**. (§2.4)
- [ ] **Available vs ledger** distinguished — the headline and floor test run on **available/cleared**, not ledger. (§2.4)
- [ ] **Forecast assumptions stated; top-10 inflows + top-10 outflows named** with % confidence. (§2.1)
- [ ] **Sensitivities present** — 30/60/90 confidence shape with the three named stresses (DSO slip, processor delay, top-customer churn). A forecast without sensitivities is rejected. (persona hard rule)
- [ ] **Processor receipts modeled net of fees at the deposit date** (sale date + lag), not gross at sale date. (§2.5)
- [ ] **Bill-pay queue carries PO-match status for items > $500.** (persona)
- [ ] **Floor test run:** post-batch / forecast ending cash vs the Elle-set floor; any breach **refused and documented**. (§3.4, persona refusal authority)
- [ ] **Any single payment > the materiality threshold flagged separately.** (persona) `[UNVERIFIED — threshold is firm-set]`
- [ ] **Data vintage stated** (as-of timestamp + which accounts/feeds). No number without a "true-as-of."
- [ ] **Out-of-scope items routed** — GL/categorization → Hal; tax dates → Anya; long-range/fundraise → Nadia.
- [ ] **`[UNVERIFIED]` applied** to every firm-specific value not pulled from live data (floor, thresholds, processor schedule, burn).

---

## 6. Worked examples (methods applied end-to-end)
*Illustrative; all dollar figures are placeholders `[UNVERIFIED — example values, not firm data]`.*

### 6.1 The daily refresh catches a stale feed before payroll
Tomás runs the 10am position. The operating-account balance looks healthy, but the **bank-feed sync timestamp is 31 hours old** (§2.4 / §3.2 step 2). **Action:** do *not* publish the figure as current — the persona hard rule is staleness >24h is a red flag, escalate, don't wait it out. Imani escalates to Soph on `cfo-dept-heads`, and the position publishes with an explicit **STALE** flag and the last-known-good reconciled balance. Payroll runs in two days; the position can't be trusted until the feed re-syncs. **Why it matters:** presenting a stale balance as current is how a firm "discovers" at payroll that the cash wasn't there. The catch — flagging the step before it bites — is exactly the early-warning work the persona praises.

### 6.2 A "we have $X in the bank" number that isn't liquidity
A peer on `cfo-dept-heads` asks whether the firm can fund a $[..] one-time vendor prepayment "since we've got $[..] in the bank." **Diagnosis (§2.4, §2.5):** the bank *ledger* balance includes (a) a processor deposit that is **gross in the GL but only net has settled**, and (b) outstanding checks not yet cleared. The **available** balance is materially lower than ledger. Running §3.2: available − outstanding checks − unsettled processor reserve = the real number, and after the proposed prepayment it would fall **below the Elle-set floor**. **Resolution:** the prepayment is declined as composed (or deferred to a week the 13-week shows headroom); the answer is framed in *available* cash, not ledger. Liquidity is what you can move today, not what the statement header says.

### 6.3 Early-pay discount vs the floor — when liquidity wins
Bea's queue has Vendor X offering **2/10 net 30** on a $[..] invoice. The discount math (§2.3): foregoing 2/10 is **~37.2% annualized** — far above the firm's cost of capital, so *economically* the firm should pay early. **But** the §3.4 floor test shows that paying Vendor X early **this week** drops post-batch available cash **below the floor**, because a top-10 customer receipt doesn't land until next week (visible in the 13-week, §3.1). **Decision:** the floor is non-negotiable (persona refusal authority) — **defer Vendor X to the day the receipt clears**, *then* take the discount if the 10-day window still allows. If the window closes first, pay on net terms and accept the foregone discount. Document the trade-off. The discount is attractive; insolvency is not.

### 6.4 Runway under a top-customer-churn sensitivity
Imani is asked for runway for the board. Base case (§3.5): current cash $[..] ÷ trailing-3-mo net burn $[..]/mo = **[..] months**, cross-checked against the 13-week ending-cash trajectory (consistent). **Sensitivity (persona):** the single largest customer is a top-10 inflow; model **top-customer churn** — drop that recurring receipt. Net burn rises (revenue falls), and runway compresses to **[..] months** (−[..]). The other two stresses (DSO slip +[N]d, processor delay +[M]d) each trim a stated amount. **Output:** the §4.4 model with base + three stressed runways, the cash and burn handed to **Nadia** for the fundraise narrative (her domain — Imani supplies the liquidity inputs, not the capital-raise story). The board sees not one runway number but a band, with the named risk that moves it most.

### 6.5 Modeling the processor-settlement lag (don't book the sale as the receipt)
A peer asks Imani to slot a large, just-closed Stripe-charged customer order into this week's 13-week receipts. **Diagnosis (§2.5, §2.5.1):** the charge captured today does **not** land as cash today. Stripe's US standard payout is **T+2 business days** from capture (@docs.stripe.com/payouts; confirmed in §2.5.1), and the bank deposit is **net of fees**, not the gross order. **Procedure (§3.1 step 3b, §3.3):** Imani places the receipt **two business days out, net of the processor fee**, in the forecast — not on the sale date, not at gross. She also checks the account's own payout history (a new Stripe account can sit on a **7–14 day** initial-payout hold per §2.5.1) and widens the lag if the account is young. **Reconciliation tie-out (§3.3):** when the deposit lands, she ties the bank line to the Stripe **payout/batch ID**, routes the fee to Hal's GL fee line and any rolling reserve to a reserve receivable. **Why it matters:** booking a card sale as same-day gross cash overstates the week's headroom by the fee plus the lag — exactly the processor-settlement-vs-deposit mismatch the persona names. If the customer churns, the over-stated receipt is also the largest single sensitivity (see §6.4). The settlement-timing values for Square, PayPal, FedNow, RTP, Same Day ACH, and Fedwire live in the §2.5.1 table for any other rail the firm adopts (research/cfo-017).

---

## 7. Source map (methods & standards — no firm research corpus exists)
**There is no treasury research folder.** Verified 2026-05: `(grounded in domain research; re-ground with your own sources)` = cao/cmo/cpa/ea only; the adjacent `research/summaries/going-concern-asc-205-40.md` has no cash-forecasting/runway/working-capital content. The pointers below are to the **named public methods/bodies of knowledge** this brain is grounded in — confirm against the live source, and against firm data for any number.

| Method / standard | Where it lives (external) | Used in |
|---|---|---|
| AFP treasury body of knowledge; *Standardized Global Cash Forecasting* | Association for Financial Professionals (AFP) — treasury/FP&A practice guides; CTP body of knowledge | §2.1, §2.5 (forecast accuracy, payout modeling) |
| 13-week direct cash-flow forecast | Standard short-term direct-method liquidity forecasting (turnaround/PE/runway practice) | §2.1, §3.1, §4.1 |
| Cash Conversion Cycle — DSO / DPO / DIO | Standard working-capital metrics (corporate-finance canon) | §2.2 |
| Early-payment-discount / implied-cost-of-discount formula | Standard treasury/AP economics (e.g., 2/10 net 30 annualized-cost calc) | §2.3, §3.4, §6.3 |
| Two-way bank reconciliation (book ↔ bank, reconciling items) | Standard accounting cash control | §2.4, §3.3 |
| Payment-processor settlement reconciliation (gross→net, payout lag, batch/ID tie-out) | Stripe/PayPal/Square settlement-report reconciliation practice | §2.5, §3.3, §6.2 |
| Runway = cash ÷ net burn; gross vs net burn | Standard startup/finance liquidity definition | §2.6, §3.5, §4.4 |
| Firm operating context (10am refresh, weekly publish, top-10/confidence, 30/60/90 + 3 sensitivities, refusal authority, dev-consult asks, Tomás/Bea split) | `.claude/agents/head-treasurer-imani.md` (persona) | throughout |
| CFO-branch structure, runway focus, cross-branch bridge, Imani↔Hal/Anya/Nadia/Lila boundaries | `.claude/agents/org.config.json` (`advisory_departments.cfo-treasury`) + `.claude/comms/comms.py` (channel ACL) | §1 |
| Processor settlement timings + payment-rail limits (Stripe/Square/PayPal; FedNow/RTP/Same Day ACH/Fedwire) | research/cfo-017 (`agent-improvement/waves/wave-1/cfo/research/cfo-017-processor-settlement-timings-stripe-t-2/report.md`); primaries @docs.stripe.com/payouts, @frbservices.org, @theclearinghouse.org | §2.5, §2.5.1 |

**Cross-head boundaries (cite when bridging, do not own):** GL / categorization / monthly close → **Hal**; tax-payment timing & amounts → **Anya**; long-range FP&A / capital allocation / fundraise model → **Nadia**; AR/revenue policy & DSO levers → **Lila/Hal**. Dev-team consults (bank-feed↔processor reconciliation patterns, runway-shape, customer-payment-variance modeling) come through Soph to Imani; written brief back, Imani never edits files (persona).

---
## Gaps where this brain is thin (flag to Soph if a request turns on these)
- **No firm-specific figures are baked in — by design.** The **cash floor** (Elle-set), the **single-payment materiality threshold**, the **bank-account list**, the **processor mix and exact payout schedules**, the **current burn rate and cash balance**, and the **firm's inventory/DIO profile** are all live data or Elle/firm settings — every one is `[UNVERIFIED]` here. Pull them; never assume a value.
- **No marathon-research corpus exists for treasury.** Unlike Mason's attest brain (grounded in cited AT-C/AR-C/SOC reports — @.claude/agents/references/head-attest-mason.md), this brain rests on **named public professional standards/methods only**. Where a request needs a firm-specific or jurisdiction-specific rule (e.g., FBO/trust-account handling, FX-account policy, a specific lender's covenant cash-test definition), that is **not in any source here** — escalate to Soph/Elle rather than invent.
- **Processor payout timing is configuration-specific.** "T+2" is a common default, not a guarantee; account age, risk holds, and processor settings change it. Confirm in each processor dashboard before relying on a lag in the forecast.
- **The DSO/DPO levers are shared, not solely Imani's** — DSO sits with Lila, DPO execution with Bea. Imani owns the *cash-timing* consequence; the policy levers require cross-head coordination on `cfo-dept-heads`.
- **No documented close calendar or treasury policy file was found** — the weekly-publish / daily-refresh cadence here is the persona's stated cadence, not a separately documented firm policy. If an authoritative treasury policy doc exists elsewhere, it supersedes this and should be linked.
