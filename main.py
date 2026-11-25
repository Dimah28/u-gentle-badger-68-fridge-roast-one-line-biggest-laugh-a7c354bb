#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single-line roast entry to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "My smart fridge emails me a weekly report: 47 door opens, "
    "zero vegetables eaten \u2014 and a passive-aggressive salad "
    "recipe I will also ignore."
)


def main() -> int:
    # Validation: 1-200 characters, single line, not whitespace only.
    if not ENTRY.strip():
        print("error: entry is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(
            f"error: entry is {len(ENTRY)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    print(f"wrote {out_path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
