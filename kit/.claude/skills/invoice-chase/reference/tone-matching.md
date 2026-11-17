# Tone Matching

Score each customer from payment history, then map the score to a reminder tone tier. Score first, tone second — never pick a tone by gut feel.

## Scoring inputs

Pull these four signals from QuickBooks history (and Stripe, if enabled), looking back 12 months:

- **Days-late average** — mean days past due across paid invoices. Count from the **due date**, not the invoice date (see [gotchas.md](gotchas.md)).
- **Lateness frequency** — percentage of invoices paid after the due date.
- **Relationship length** — time since the customer's first invoice.
- **Invoice size** — the current overdue amount relative to the customer's average invoice.

## Scoring logic

| Score | Rule |
|---|---|
| `good-payer` | Late on fewer than 25% of invoices **and** days-late average under 10 |
| `occasionally-late` | Late on 25–60% of invoices, **or** days-late average 10–30 |
| `repeat-late` | Late on more than 60% of invoices, **or** days-late average over 30 |

**Thin history rule:** fewer than 3 paid invoices on record → score as `occasionally-late`. There isn't enough data to earn gentle or to justify firm.

## Tone tiers

The score sets the starting tier. How late the *current* invoice is escalates it.

| Tier | Use when | Voice |
|---|---|---|
| **Gentle** | `good-payer`, any lateness under 30 days | Warm, assume oversight, zero pressure |
| **Standard** | `occasionally-late`; or `good-payer` past 30 days late | Polite and matter-of-fact — state the amount, due date, and payment link |
| **Firm** | `repeat-late`; or `occasionally-late` past 45 days late | Direct. Name a pay-by date and a business consequence (e.g., pausing new work) |
| **Final-notice** | `repeat-late` **and** current invoice 60+ days late | Formal. State plainly this is the last automated reminder before the owner follows up personally. Never mention legal action — see [gotchas.md](gotchas.md) |

**Modifiers** (apply after picking the starting tier):

- **Long good relationship:** 2+ years of mostly on-time history softens the tier by one step.
- **Unusually large invoice:** if the overdue amount is 3x+ the customer's average invoice, do not auto-escalate. Flag it "large invoice — owner call recommended" in the summary table instead.
- Never harden a customer's tier by more than one step in a single run.

## Worked examples

| Customer | Days-late avg | % late | Relationship | Current invoice | Score | Tier |
|---|---|---|---|---|---|---|
| Acme Co | 4 days | 15% | 3 years | $1,200 — 18 days late | `good-payer` | Gentle |
| Acme Co (same history, 38 days late) | 4 days | 15% | 3 years | $1,200 — 38 days late | `good-payer` | Standard → **Gentle** after the long-relationship softener |
| Northwind LLC | 34 days | 70% | 14 months | $450 — 47 days late | `repeat-late` | Firm |
| Northwind LLC (same history, 64 days late) | 34 days | 70% | 14 months | $450 — 64 days late | `repeat-late` | Final-notice |

## Subject line formulas

| Tier | Formula |
|---|---|
| Gentle | `Quick note — Invoice [Invoice #]` |
| Standard | `Reminder: Invoice [Invoice #] due [Due Date]` |
| Firm | `Overdue: Invoice [Invoice #] — [Amount] past due` |
| Final-notice | `Final reminder: Invoice [Invoice #] — [Amount], [Days Late] days past due` |

Rules: always include the invoice number so replies thread cleanly. No ALL CAPS, no "URGENT", no exclamation marks at any tier.
