#!/usr/bin/env python3
"""Deterministic build step for the news-image-20261127 entry.

Copies the committed poster render (entry.png) to /output/entry.png.
No network access, no timestamps, no randomness: two runs are byte-identical.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
DEST = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: missing source image at {SOURCE}", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)

    size = os.path.getsize(DEST)
    print(f"wrote {DEST} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
