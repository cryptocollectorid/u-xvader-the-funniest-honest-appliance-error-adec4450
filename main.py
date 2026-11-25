#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — entry program.

Writes a single line (max 200 characters) to /output/entry.txt:
the funniest honest error message a home appliance could show.

The line is a toaster's error. The fault is real (a full crumb tray),
the voice is the machine's own flat, put-upon tone, and the joke is
that after three years of silent service it has simply had enough.
"""

import os

ENTRY = (
    "Error: crumb tray full. I have collected your crumbs for three "
    "years without complaint. Today, I am full."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
