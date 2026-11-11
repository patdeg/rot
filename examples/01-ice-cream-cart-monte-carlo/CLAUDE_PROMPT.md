# The prompt: paste this into Claude

This is written for **Claude.ai's Analysis tool** (sometimes called the code-execution or REPL tool — the feature
that lets Claude write and run real code against a file you upload, instead of guessing at numbers). Turn it on in
Settings if you don't see it, then:

1. Start a new chat.
2. Upload `ice_cream_cart_simulation.csv` (16,000 simulated days, 8 cart-count scenarios — see `README.md` for
   where the numbers come from).
3. Paste the prompt below, exactly, right under the upload.

You do not need to know Python, pandas, or anything about Monte Carlo simulation to run this. That is the point.

---

```
I run a small seasonal business and I'm trying to decide how many ice cream carts to put on the street. I had an
analyst run a Monte Carlo simulation: 2,000 simulated days for each possible cart count from 1 to 8, accounting for
weather, weekends, rain, and some cart-to-cart luck. The attached CSV has one row per simulated day, with columns:
trial_id, num_carts, is_weekend, rain, temp_f, customers_per_cart, revenue_per_cart, profit_per_cart,
total_daily_profit.

Please:

1. For each value of num_carts (1 through 8), compute the mean, p10, median, and p90 of total_daily_profit.
2. Compute the marginal profit of each additional cart: mean(total_daily_profit at n) minus mean(total_daily_profit
   at n-1).
3. Tell me the cart count where that marginal number first goes negative — that's the point where the next cart
   stops paying for itself, even though total profit might still look positive for a cart or two after that.
4. Make one chart: total expected daily profit on the y-axis, number of carts on the x-axis, with the
   profit-maximizing point marked.
5. In plain English, no jargon: how many carts should I run, and what's the one-sentence reason — not "more carts
   means more sales," the real reason.
```

---

## Why this prompt, not a bigger one

- It gives Claude the file and the exact columns, so it doesn't have to guess at the schema.
- It asks for the mean **and** the spread (p10/median/p90) on purpose — a business decision made only on the
  average hides how bad (or good) a specific real day could be. This is the same "don't just look at the average"
  idea behind the show's own "holdout test" questions.
- Step 3 is the actual business question. Steps 1-2 are just the arithmetic that answers it. If you only remember
  one line from this whole exercise, remember step 3's framing: find where the *next* dollar (or cart) stops
  paying, not where you're still "in the black" overall.

## Try it on your own numbers next

Once this works, the real exercise is swapping in your own situation: replace "carts" with "ad campaigns,"
"support agents," "AI seats," or "sales reps," replace the simulated columns with your own logged cost and outcome
data, and ask Claude the same five questions. Real companies have found real money this way by testing one more
unit of spend against the last one, instead of assuming "more must be better" — see the `README.md` in this folder
for the idea in more detail.
