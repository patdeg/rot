#!/usr/bin/env python3
"""Reference analysis of ice_cream_cart_simulation.csv — the same analysis the
CLAUDE_PROMPT.md asks Claude's Analysis tool to do, written out in plain
Python so you can check Claude's answer against this one (or just run this
if you don't have Claude's Analysis tool handy). Pure standard library.
"""

import csv
import statistics
import sys


def load_profits_by_cart_count(path: str) -> dict:
    by_count = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            n = int(row["num_carts"])
            by_count.setdefault(n, []).append(float(row["total_daily_profit"]))
    return by_count


def percentile(sorted_values, p):
    k = (len(sorted_values) - 1) * p
    f, c = int(k), min(int(k) + 1, len(sorted_values) - 1)
    if f == c:
        return sorted_values[f]
    return sorted_values[f] + (sorted_values[c] - sorted_values[f]) * (k - f)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "ice_cream_cart_simulation.csv"
    by_count = load_profits_by_cart_count(path)

    print(f"{'carts':>5} {'mean':>10} {'p10':>10} {'p50':>10} {'p90':>10} {'marginal_vs_prev':>18}")
    prev_mean = None
    best_n, best_mean = None, float("-inf")
    for n in sorted(by_count):
        values = sorted(by_count[n])
        mean = statistics.mean(values)
        p10 = percentile(values, 0.10)
        p50 = percentile(values, 0.50)
        p90 = percentile(values, 0.90)
        marginal = "" if prev_mean is None else f"{mean - prev_mean:+.2f}"
        print(f"{n:>5} {mean:>10.2f} {p10:>10.2f} {p50:>10.2f} {p90:>10.2f} {marginal:>18}")
        if mean > best_mean:
            best_mean, best_n = mean, n
        prev_mean = mean

    print(f"\nBest expected total daily profit: {best_n} cart(s), ${best_mean:,.2f}/day.")
    print("The 'right' number of carts is where the NEXT cart's marginal profit "
          "goes negative, not where total profit is still positive — that is "
          "usually a much smaller number than 'as many as the budget allows.'")


if __name__ == "__main__":
    main()
