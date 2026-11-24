#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt.

Deterministic, Python standard library only, no network access.
"""

import os

# Contest cap for the pickup line, in characters. The entry must stay
# within this bound, so the guard in main() fails loudly if the line
# is ever edited past it.
MAX_LINE_CHARS = 140

LINE = (
    "I've hummed for a thousand strangers, but you made my coils spin "
    "\u2014 press B4, this one's on the house."
)


def main():
    if len(LINE) > MAX_LINE_CHARS:
        raise SystemExit(
            "entry line is %d chars, over the %d-char limit"
            % (len(LINE), MAX_LINE_CHARS)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
