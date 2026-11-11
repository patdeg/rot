# rot — Return on Token: try-it-yourself examples

Companion repo to **Return on Token**, a video and newsletter series about one question: *what does AI (and data,
and any other spend) actually return for what it costs?* — YouTube **@ReturnOnToken**, LinkedIn group "Return on
Token", and the newsletter at **returnontoken.substack.com**.

This repo is the hands-on half: small, made-up business cases — a lot of them food-themed, because food is an
easy thing to picture a margin on — that you can actually run, usually by pasting one file into Claude. No prior
Monte Carlo, statistics, or coding background assumed. Every example ends with one real skill you can take to
work this week.

Private, sensitive project material (guest notes, strategy, anything about Patrick's own employer or job search)
lives in a separate, non-public repo and never ends up here — this one is deliberately safe to share with anyone.

## Examples

| # | Example | Skill it teaches |
|---|---|---|
| 1 | [ice-cream-cart-monte-carlo](examples/01-ice-cream-cart-monte-carlo/) | Finding the point where the *next* unit of spend stops paying for itself (marginal ROI = 0), using a Monte Carlo simulation and Claude's Analysis tool |

More examples will be added as the show covers more ground (holdout tests, cost-per-query chargebacks, capacity
planning, and others — see the show's own idea list for what's coming).

## How to use any example here

Each example folder is self-contained: a README explaining the business case, a CSV (or a script that generates
one), and a `CLAUDE_PROMPT.md` with the exact text to paste into [Claude](https://claude.ai) alongside the file.
Turn on Claude's **Analysis tool** (Settings -> Features, or ask Claude how) so it can actually run code against
the data instead of describing it from memory — that's what makes "upload a CSV, get a real answer" work.

## License

Code (the `.py` scripts) is MIT — see `LICENSE`. Everything else (READMEs, prompts, generated example data) is
CC BY 4.0 — see `LICENSE-CONTENT`. Same split as this repo's sibling teaching projects, `ai101`, `hello-docker`
and `unreal101`.
