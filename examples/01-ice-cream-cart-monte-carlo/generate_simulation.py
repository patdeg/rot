#!/usr/bin/env python3
"""Generate a Monte Carlo simulation CSV for a made-up small business decision.

The business: Sunny Sadie's Ice Cream Carts, a seaside town with room for
1 to 8 carts. Each cart earns money from ice cream sales, which depend on
weather, weekday vs. weekend, and random luck. Each *additional* cart also
steals a little territory from the carts already running (cannibalization),
so the average cart gets a little less busy every time you add one.

This is the business-case version of "the last slice of pizza is worth
less than the first": the question is not "should we run carts?" (yes), it
is "how many carts before the next one is not worth it?" That is a marginal
-ROI-equals-zero decision, and it is exactly the kind of question a Monte
Carlo simulation is built for: run the uncertain day many times, at every
cart count, and look at what the *next* cart actually adds on average.

Pure standard library, no pip installs needed. Deterministic with --seed.
"""

import argparse
import csv
import random
import statistics

PRICE_PER_CONE = 4.50
VARIABLE_COST_PER_CONE = 0.90
FIXED_COST_PER_CART_PER_DAY = 180.0  # cart rental + one staffer, one day

MIN_CARTS = 1
MAX_CARTS = 8


def cannibalization_factor(num_carts: int) -> float:
    """Each cart beyond the first overlaps territory with the others.

    1 cart keeps 100% of its natural draw. By 8 carts, each cart is down to
    about half its solo draw, because carts are now close enough together
    that customers split between them instead of each cart drawing fresh
    customers.
    """
    return 1.0 / (1.0 + 0.12 * (num_carts - 1))


def simulate_one_day(num_carts: int, rng: random.Random) -> dict:
    is_weekend = rng.random() < (2.0 / 7.0)
    rain = rng.random() < 0.15

    temp_f = rng.gauss(78, 8)
    temp_f = max(55.0, min(105.0, temp_f))

    # Hotter days and weekends draw more walk-up customers per cart.
    base_customers = max(0.0, (temp_f - 60.0) * 5.2)
    if is_weekend:
        base_customers *= 1.35
    if rain:
        base_customers *= 0.30

    # Cart-to-cart noise: some carts just have a better or worse day.
    noise = max(0.0, rng.gauss(1.0, 0.18))

    customers_per_cart = base_customers * cannibalization_factor(num_carts) * noise

    revenue_per_cart = customers_per_cart * PRICE_PER_CONE
    variable_cost_per_cart = customers_per_cart * VARIABLE_COST_PER_CONE
    profit_per_cart = revenue_per_cart - variable_cost_per_cart - FIXED_COST_PER_CART_PER_DAY

    return {
        "num_carts": num_carts,
        "is_weekend": int(is_weekend),
        "rain": int(rain),
        "temp_f": round(temp_f, 1),
        "customers_per_cart": round(customers_per_cart, 1),
        "revenue_per_cart": round(revenue_per_cart, 2),
        "profit_per_cart": round(profit_per_cart, 2),
        "total_daily_profit": round(profit_per_cart * num_carts, 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials-per-cart-count", type=int, default=2000,
                         help="simulated days per cart-count scenario (default: 2000)")
    parser.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    parser.add_argument("--out", default="ice_cream_cart_simulation.csv",
                         help="output CSV path (default: ice_cream_cart_simulation.csv)")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    fieldnames = ["trial_id", "num_carts", "is_weekend", "rain", "temp_f",
                  "customers_per_cart", "revenue_per_cart", "profit_per_cart",
                  "total_daily_profit"]

    rows_written = 0
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        trial_id = 0
        for num_carts in range(MIN_CARTS, MAX_CARTS + 1):
            for _ in range(args.trials_per_cart_count):
                trial_id += 1
                row = simulate_one_day(num_carts, rng)
                row["trial_id"] = trial_id
                writer.writerow(row)
                rows_written += 1

    print(f"Wrote {rows_written} rows ({MAX_CARTS - MIN_CARTS + 1} cart-count scenarios "
          f"x {args.trials_per_cart_count} simulated days each) to {args.out}")

    # Quick sanity summary, so you can see the diminishing-returns shape
    # without opening the CSV. Re-simulate cheaply by cart count for this
    # printout (keeps the function above the single source of truth).
    print("\ncart_count  mean_daily_profit  (quick check, not the full analysis)")
    rng2 = random.Random(args.seed)
    for num_carts in range(MIN_CARTS, MAX_CARTS + 1):
        profits = [simulate_one_day(num_carts, rng2)["total_daily_profit"]
                   for _ in range(args.trials_per_cart_count)]
        print(f"{num_carts:>10}  {statistics.mean(profits):>18,.2f}")


if __name__ == "__main__":
    main()
