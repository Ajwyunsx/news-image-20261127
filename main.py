#!/usr/bin/env python3
"""Deterministic build step for the news-image-20261127 entry.

Copies the committed poster render (entry.png) to /output/entry.png.

The gate wants a whole PNG of at most 1 MiB and exactly 1024x1024 pixels, so the
copy is verified before it is handed over: a wrong-sized or oversized snapshot
should fail loudly here rather than silently at judging time.

No network, no clock, no randomness: two runs are byte-identical.
Inside the grader, MAKEFUN_OUTPUT_DIR overrides /output.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DEST = os.path.join(OUTPUT_DIR, "entry.png")

MAX_BYTES = 1024 * 1024
SIDE = 1024


def png_size(path):
    """Return (width, height) read straight from the IHDR chunk, no libraries."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError(f"{path} is not a PNG file")
    return struct.unpack(">II", head[16:24])


def check(path):
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"{path} is {size} bytes, over the 1 MiB cap")
    width, height = png_size(path)
    if (width, height) != (SIDE, SIDE):
        raise ValueError(f"{path} is {width}x{height}, not {SIDE}x{SIDE}")
    return size


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: missing source image at {SOURCE}", file=sys.stderr)
        return 1

    try:
        size = check(SOURCE)
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)

    copied = check(DEST)
    if copied != size:
        print(f"error: copy is {copied} bytes, source is {size}", file=sys.stderr)
        return 1

    print(f"wrote {DEST} ({copied} bytes, {SIDE}x{SIDE})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
