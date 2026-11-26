#!/usr/bin/env python3
"""The Printer Apology — make.fun entry.

Writes one line to /output/entry.txt: an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. 96 characters, plain ASCII, no trailing newline.

The joke: the printer prints its apology on the back of the very report
it jammed — and the front of that report is still stuck inside it.
"""

import os

ENTRY = "Sorry I jammed. I printed this apology on the back of your report. The front is still inside me."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-120 UTF-8 chars.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
