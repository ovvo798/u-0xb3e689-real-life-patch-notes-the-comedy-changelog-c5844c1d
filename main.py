#!/usr/bin/env python3
"""Write one original patch note for the Real-Life Patch Notes bounty.

Stdlib only. Writes a single line (1-160 characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "v2.0.3: Fixed a bug where walking through a doorway "
    "erased why you entered the room. Repro: every time."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
