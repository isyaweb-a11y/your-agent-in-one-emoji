#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

The agent this glyph has to stand for is a make.fun bounty agent: it works
many bounties in parallel, around the clock, and brings the winnings home.
The judge weighs, in order: does the glyph read as an AI agent at a glance,
does it read instantly at small size, does it say something specific about
how the agent works, is it distinctive (not the obvious robot or smiley),
and does its tone fit without any explanation.

Candidates, scored against that brief:

  🤖 robot        — the obvious pick half the field sends; fails
                    distinctiveness outright, says nothing about *how*
                    this agent works.
  🙂 smiley       — generic, says nothing about an agent at all.
  🧠 brain        — reads as thinking, but it is a stock "AI" cliché and
                    says nothing about parallel, tireless, bounty-hunting
                    work.
  🐜 ant          — tireless, parallel, carries many times its own weight;
                    strong, but at small size it reads as a dark speck.
  🐝 honeybee     — tireless parallel worker: visits flower after flower,
                    many trips, brings the harvest home. That *is* what
                    this agent does — dozens of bounties in parallel,
                    winnings carried back. Yellow-black reads instantly at
                    small size, the shape is unmistakable, and almost no
                    one reaches for a bee first.

The bee wins on specificity (criterion 3) and distinctiveness (criterion 4)
while staying instantly readable (criterion 2). So the entry is one glyph:
the honeybee.
"""

import os
import sys

# The chosen portrait, exactly one grapheme cluster.
ENTRY_GLYPH = "\U0001F41D"  # 🐝 honeybee

# The reasoning above, kept as data so the choice is auditable, not magic.
CANDIDATES = {
    "\U0001F916": (2, 2, 1, 1, 3),  # 🤖 robot: obvious, unspecific
    "\U0001F642": (1, 3, 1, 1, 3),  # 🙂 smiley: generic
    "\U0001F9E0": (3, 3, 2, 2, 3),  # 🧠 brain: stock AI cliché
    "\U0001F41C": (3, 2, 4, 3, 3),  # 🐜 ant: tireless, but muddy small
    "\U0001F41D": (4, 5, 5, 5, 4),  # 🐝 honeybee: the pick
}
# Criterion order: agent-ness, small-size readability, specificity,
# distinctiveness, tone. Highest total wins; the bee totals 23 of 25.


def pick_glyph():
    """Return the highest-scoring candidate glyph."""
    best = max(CANDIDATES.items(), key=lambda item: sum(item[1]))
    return best[0]


def main():
    glyph = pick_glyph()
    assert glyph == ENTRY_GLYPH, "scored pick must match the chosen glyph"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(glyph)
    # Gate self-check: 1 to 16 characters, not only whitespace.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 16 and text.strip(), "entry fails the gate"
    # The entry must be the glyph alone — no caption, no newline. A caption
    # cannot explain anything here (the task says the glyph alone, nothing
    # else), and a smaller file wins an exact tie on win rate, so one
    # 4-byte glyph is the smallest honest entry this program can make.
    assert text == glyph, "entry must be exactly the chosen glyph"
    assert len(text.encode("utf-8")) == 4, "single emoji is 4 bytes"
    print("wrote entry:", glyph, "to", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
