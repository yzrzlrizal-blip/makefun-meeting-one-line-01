#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library, deterministic: the same line on every run.
"""

import os
import sys

LINE = "We are here because no one read the email, and the email said we didn't need to be here."


def check(line: str) -> None:
    # The sealed gate: UTF-8 text, 1 to 200 characters, not only white space.
    if not line or not line.strip():
        sys.exit("entry must not be empty or only white space")
    if len(line) > 200:
        sys.exit("entry must be at most 200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")


def main() -> None:
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            sys.exit("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
