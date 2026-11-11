# Example 1: How many ice cream carts should you run?

A made-up business case, built to teach one real skill: **finding the point where the next dollar stops paying
for itself** (what the show *Return on Token* calls "marginal ROI equals zero"). No coding experience needed to
use it — you can run the whole thing by uploading one CSV into Claude.

## The business case

**Sunny Sadie's Ice Cream Carts** is a seasonal beach-town business that can run 1 to 8 carts. More carts means
more ice cream sold... but every cart you add also competes for the same walk-up crowd as the carts already out
there (we call this *cannibalization* — the same word a marketer uses when a new product eats into an existing
one's sales instead of growing the pie). At some point, the next cart earns less than it costs to run, even
though the *business as a whole* is still profitable.

That "some point" is exactly the question most AI and software spending gets wrong: teams keep adding seats,
agents, or campaigns because the *average* return still looks positive, without ever checking what the *next* one
actually adds.

## What's in this folder

| File | What it is |
|---|---|
| `generate_simulation.py` | Generates the Monte Carlo simulation (pure Python standard library, no installs needed) |
| `ice_cream_cart_simulation.csv` | The generated data: 16,000 simulated days (2,000 per cart count, 1 through 8) |
| `CLAUDE_PROMPT.md` | **Start here if you just want to try it.** The exact prompt to paste into Claude |
| `analyze_results.py` | A reference analysis in plain Python, so you can check Claude's answer, or skip Claude entirely |

## The model, briefly

Each simulated day draws a random temperature, whether it's a weekend, and whether it rains — all of which move
how many customers show up. Each cart earns `(price - cost) x customers`, minus a fixed daily cost (cart rental
plus one staffer). Adding more carts means each cart gets a shrinking slice of the same crowd. Full formula and
all the made-up numbers (price $4.50/cone, cost $0.90/cone, $180/day fixed cost per cart) are commented in
`generate_simulation.py` — change any of them and regenerate with `python3 generate_simulation.py`.

## The answer this specific run gives (already run for you)

| Carts | Mean daily profit | Marginal vs. previous cart |
|---|---|---|
| 1 | $148.67 | — |
| 2 | $231.77 | **+$83.10** |
| 3 | **$268.95** | **+$37.17** |
| 4 | $252.06 | **-$16.88** |
| 5 | $211.99 | -$40.07 |
| 6 | $174.19 | -$37.80 |
| 7 | $97.81 | -$76.39 |
| 8 | $7.67 | -$90.14 |

Total profit is still positive all the way through 8 carts — it's easy to look at that and think "every cart
helps, so why not run all 8?" The real answer is **3 carts**. The 4th cart doesn't just earn less than the first
three — it actively costs the business about $17/day, because it steals customers from the carts you already
have without bringing in enough new ones to cover its own $180 daily cost. Carts 5 through 8 make it worse. This
is the same shape as most "we added more AI seats / ad spend / sales reps and it kept helping" stories: the total
number can still look fine for a while after the real decision point has already passed.

Re-run `analyze_results.py ice_cream_cart_simulation.csv` to reproduce this table yourself, or follow
`CLAUDE_PROMPT.md` to get Claude to produce it (and a chart) from the raw CSV with no code of your own.

## The skill to take to work this week

Pick one thing at your job that you'd assume "more is better": ad spend, support headcount, AI seats, outreach
volume. If you have (or can log) the per-unit cost and the per-unit outcome, run the same five questions from
`CLAUDE_PROMPT.md` against your own numbers instead of this CSV. The question that matters is never "is this
still profitable overall" — it's "is the next one."
