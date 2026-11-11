# rot-public: agent rules

This is the **public** companion repo to Return on Token (`github.com/patdeg/rot`). Read `README.md` first.

## Hard rules

1. **Public by design — keep it that way.** Nothing from the private working repo (guest names, strategy,
   anything about Patrick's current employer or job search) goes here, ever. If you're not sure whether something
   is safe to publish, it isn't — ask first.
2. **Made-up, clearly labelled.** Every business case here is synthetic. Say so plainly in each example's README
   (as the ice-cream-cart example does) so nobody mistakes a teaching example for real company data.
3. **No paid or rate-limited API calls** without napkin math and Patrick's OK first (same house rule as everywhere
   else — see `~/.claude/CLAUDE.md`, prime objective 2). Everything generated here so far uses only Python's
   standard library — no API keys, no cost, by design. Keep it that way unless there's a good reason not to.
4. **Every example ends in a skill.** Not just a number — a named, repeatable technique the reader can apply to
   their own situation. If a draft doesn't have one, it's not done yet.
5. **Style.** Plain language, no filler, no em dashes, witty and a little fun — this repo is meant to be
   enjoyable to read, unlike a dry whitepaper. Match the tone already set in `examples/01-ice-cream-cart-monte-carlo/`.
6. **License split.** Code is MIT (`LICENSE`); everything else (prose, prompts, generated data) is CC BY 4.0
   (`LICENSE-CONTENT`) — same pattern as `ai101`, `hello-docker` and `unreal101`.
