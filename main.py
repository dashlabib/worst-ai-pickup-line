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


def validate_line(line):
    """Check one candidate line against the competition gate.

    Returns the stripped line, or raises ValueError naming the failure.
    """
    stripped = line.strip()
    if not stripped:
        raise ValueError("line is empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d cap" % (len(stripped), MAX_CHARS)
        )
    stripped.encode("utf-8")  # the gate requires UTF-8 text
    return stripped


def main() -> int:
    try:
        line = validate_line(LINE)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
