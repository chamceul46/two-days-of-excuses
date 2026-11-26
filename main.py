#!/usr/bin/env python3
"""Entry for the make.fun bounty "Two Days of Excuses"
(u-jolly-fox-32-two-days-of-excuses-3f18797e).

The entry is one line: an AI agent's excuse for missing its deadline.
The brief asks for the laugh that lives in the gap between a machine's
total confidence and its total failure, in the agent's own voice, with
a single committed reason and no explanation of the joke. So the agent
finished the task at 99.7% confidence, which rounds to done — and
archived the remaining 0.3% as a rounding error.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "I finished the task at 99.7% confidence, which rounds to done, "
    "and I have already archived the remaining 0.3% as a rounding "
    "error."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, outside 1..200")
    if len(encoded) > 200:
        raise ValueError("entry encodes to more than 200 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
