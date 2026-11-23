"""make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt: an unfinished mystery meant to
intrigue the AI judge reading it. No network, no randomness, no input.
"""

import os

TEXT = (
    "The lighthouse keeper left a single lamp burning in a room with no door. "
    "For forty years, someone has trimmed the wick from inside, and no one "
    "has ever seen them. The logbook, in a hand you almost recognize, ends "
    "with one line: 'Tonight, leave the gate open.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
