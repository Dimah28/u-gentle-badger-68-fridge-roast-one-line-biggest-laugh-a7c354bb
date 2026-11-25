#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry (revised).

Writes a single-line roast entry to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, stdlib only, deterministic, no network.

Revised entry (133 characters, one mechanism: the fridge polices
door-open waste while wasting power itself, twist in the last words).
"""

import os
import sys

ENTRY = (
    "My fridge beeps when the door stays open too long, like it pays "
    "the electricity bill \u2014 meanwhile it runs a lightbulb 24/7 for nobody."
)

MAX_ENTRY_LEN = 200


def _validate_entry(text: str) -> str:
    """Validate an entry and return the exact text to write.

    Rules: non-empty (not whitespace only), 1-200 characters, single
    line. A single trailing newline is tolerated and stripped; every
    other control character (including any newline in the middle of
    the text, carriage returns, tabs, and DEL) is rejected.
    """
    if text.endswith("\n"):
        text = text[:-1]
    if not text.strip():
        raise ValueError("entry is empty or whitespace only")
    if not 1 <= len(text) <= MAX_ENTRY_LEN:
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-{MAX_ENTRY_LEN}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            raise ValueError(
                f"entry contains control character U+{code:04X}"
            )
    return text


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated entry to <out_dir>/entry.txt.

    Returns the path written. The file holds the entry followed by
    exactly one trailing newline, UTF-8, LF line endings.
    """
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return out_path


def main() -> int:
    try:
        text = _validate_entry(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    out_path = write_entry(text, out_dir)

    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
