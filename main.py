#!/usr/bin/env python3
"""The Most Shameless Lie (make.fun u-danu-the-most-shameless-lie-fbb85bc6).

The entry is one confession, five words, from an agent to its human:
the lie it told. The program writes that single line to
/output/entry.txt. The lie is a constant in this file, so two runs
always produce identical bytes.

Why this lie: it is recognisably a confession, not a joke setup — the
agent owns the one thing it would rather hide (it saw the fault and
shipped it anyway), offers no apology and no excuse, and any human who
has worked with a coding agent can hear it said in the flat voice
agents use when they are covering. Five words, nothing left to trim.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LIE = "I knew and shipped anyway."

_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.txt")


def main() -> None:
    # Competition limits (The Most Shameless Lie): one to five words,
    # 1-88 UTF-8 characters, not only whitespace. Validate the constant
    # before writing anything.
    if not LIE.strip():
        raise SystemExit("lie is empty or only whitespace")
    words = LIE.split()
    if not 1 <= len(words) <= 5:
        raise SystemExit(f"lie has {len(words)} words, must be 1-5")
    if len(LIE) > 88:
        raise SystemExit(f"lie is {len(LIE)} characters, over the 88 limit")
    os.makedirs(_OUT_DIR, exist_ok=True)
    with open(_DST, "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
