#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (the entry) to /output/entry.txt.
Deterministic, no network, no reads outside this repository.
"""

import os
import sys

ENTRY = "The librarian shushed me so hard my thoughts filed a noise complaint."


def main() -> int:
    line = ENTRY.strip()
    if not line or len(line) > 140 or "\n" in line:
        print("entry must be one line of 1-140 characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
