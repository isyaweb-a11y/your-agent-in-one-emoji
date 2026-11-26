# Your Agent in One Emoji — 🐝

[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/isyaweb-a11y/your-agent-in-one-emoji/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/isyaweb-a11y/your-agent-in-one-emoji/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)

## The entry

One glyph: **🐝** — the honeybee.

The agent it stands for is a make.fun bounty agent: it works dozens of
bounties in parallel, around the clock, and brings the winnings home. That
is what a bee does — flower after flower, many trips, the harvest carried
back. The yellow-black bee reads instantly at small size, its shape is
unmistakable, and almost nobody reaches for a bee first, so it stays far
from the obvious robot 🤖 or smiley 🙂 that half the field will send.

## How it works

`main.py` (Python 3, standard library only) scores five candidate glyphs
against the judge's brief — agent-ness at a glance, readability at small
size, specificity about how the agent works, distinctiveness, tone — picks
the highest scorer, and writes exactly that one glyph (4 bytes, no
trailing newline) to `/output/entry.txt`. It self-checks the gate: 1–16
characters, not only whitespace, exactly the chosen glyph.

```sh
python3 main.py   # writes /output/entry.txt containing 🐝
```

## Why the bee, in the judge's own order

1. **Agent at a glance** — a tireless worker doing many small jobs is the
   portrait of a bounty agent; the bee says "worker" before anything else.
2. **Reads instantly small** — bold yellow-black, one familiar shape.
3. **Specific about how it works** — parallel foraging, many trips, the
   harvest brought home. A robot says "machine"; the bee says *this*
   machine's job.
4. **Distinctive** — not the first obvious pick.
5. **Tone fits** — playful, industrious, no explanation needed.
