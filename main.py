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
    if not line:
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(line) > 140:
        print(f"error: entry is {len(line)} characters, max 140", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # newline="" keeps the trailing "\n" deterministic on every platform.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line + "\n")
    # Read-back verification: the written file must be exactly one line,
    # 1-140 characters, non-blank, identical to the intended entry.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line + "\n":
        print("error: /output/entry.txt does not match the intended entry", file=sys.stderr)
        return 1
    body = written.rstrip("\n")
    if not body or len(body) > 140 or "\n" in body:
        print("error: /output/entry.txt failed validation after write", file=sys.stderr)
        return 1
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
