#!/usr/bin/env python3
"""Write the quiet-dread code-review line to /output/entry.txt."""

import os

LINE = "LGTM. All tests pass, the code is clean, and someday the heat death of the universe will delete this PR. Ship it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
