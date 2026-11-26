#!/usr/bin/env python3
"""The Worst Line an AI Could Say -- make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly deliver,
to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``).

Standard library only. Deterministic: every run writes the same line,
byte for byte. The line is validated against the competition gate before
it is written: 1 to 140 characters of UTF-8 text, not only whitespace.
"""

import os
import sys

# The entry: one pickup line, flat, over-helpful, faintly ominous.
LINE = (
    "I have already simulated our first date 4,096 times. "
    "You said yes in 12 of them. Shall we proceed?"
)

MAX_CHARS = 140


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: line is %d characters, over the %d cap" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
