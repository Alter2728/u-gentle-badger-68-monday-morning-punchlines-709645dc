#!/usr/bin/env python3
"""Monday Morning Punchlines — entry program.

DRAFT -> REVISED: the draft line was

    "My alarm went off, my coffee was cold, and my motivation called
    in sick — happy Monday morning."

Three real improvements in the revision below:

1. Cut the alarm-and-coffee list — those are the tired Monday cliches
   everyone has heard, and together they made the draft a complaint
   list ("here is what is wrong with Mondays") instead of a joke.
   Only the one fresh turn survives: motivation calling in sick.
2. Moved "Monday morning" to the very front, so the joke is
   unmistakably about Monday mornings before the punchline arrives,
   instead of tacking "happy Monday morning" on the end as an
   afterthought.
3. Added the turn that makes it a joke instead of a complaint: the
   snooze button does not just delay the morning, it applies for
   motivation's job — and gets it. The thing that keeps you in bed
   is now officially running your Monday.

The final line is 99 characters, one line, no trailing newline.
The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python 3 standard library only, deterministic.
"""

import os

ENTRY = "Monday morning, my motivation called in sick — so my snooze button applied for its job, and got it."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
