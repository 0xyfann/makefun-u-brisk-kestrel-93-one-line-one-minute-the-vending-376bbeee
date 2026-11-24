#!/usr/bin/env python3
"""Vending Machine Pickup Line — one line, one minute.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only.
"""

import os

LINE = (
    "Are you exact change? Because every time you walk by, my slot "
    "lights up and my coil won't let go."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
