"""Deliver the front-page image for news-image-20261120.

Competition: news-image-20261120, dated Friday, 20 November 2026.

The picture is a single newspaper front page for that day. Its stories are:

- Washington puts off any choice about striking Iran until 2027, while
  American intelligence estimates Tehran still has no fewer than 2,500
  missiles in its arsenal.
- After meeting in Shenzhen, Trump, Xi and Putin put their names to a
  joint peace declaration.
- European leaders gather in Berlin for a Coalition of the Willing summit
  and say they are prepared to open talks on Ukraine; Putin answers the
  attack on the Crimean Bridge by promising a reply far more painful.
- Anthropic begins trading on Nasdaq: first trade at $111.50, about 34%
  above its $83 flotation price, before settling 17% higher at $97.17.
- Cyclone Akvan comes ashore close to Gopalpur in Odisha, with sustained
  winds of 90 to 100 km/h and gusts to 110, and 105,304 residents moved
  to safety ahead of it.
- NASA confirms Voyager 1 has now travelled one light-day away from Earth.
- JAXA abandons its plan to set Hayabusa2 down on asteroid 1998 KY26
  in 2031.
- Grand Theft Auto 6 has now sold more than The Odyssey's $1.80 billion
  worldwide gross.
- Henry Nicholls finishes day one of the first Test against India in
  Wellington unbeaten on 113, with New Zealand on 243 for 5.

This script takes the finished artwork, ``entry.png``, sitting next to it,
checks that it is a genuine 1024 by 1024 PNG no larger than one mebibyte,
places an exact copy at the output location, and proves the copy matches
the original byte for byte. It uses only the Python standard library and
never touches the network, so repeated runs always give the same result.
"""

import argparse
import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

SOURCE_FILENAME = "entry.png"
WANTED_WIDTH = 1024
WANTED_HEIGHT = 1024
BYTE_LIMIT = 1024 * 1024
PNG_MARK = b"\x89PNG\r\n\x1a\n"
HEADER_BYTES = 33  # 8 signature + 4 length + 4 type + 13 IHDR data + 4 CRC


def complain(message):
    """Print an error to stderr and stop with a non-zero status."""
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def digest_file(path):
    """Return the hex SHA-256 of the file at *path*, read in chunks."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            piece = handle.read(65536)
            if not piece:
                break
            hasher.update(piece)
    return hasher.hexdigest()


def measure_png(path):
    """Check *path* is a PNG of the wanted size; return (width, height)."""
    size = os.path.getsize(path)
    if size > BYTE_LIMIT:
        complain(
            "entry.png is %d bytes, over the %d byte limit" % (size, BYTE_LIMIT)
        )
    with open(path, "rb") as handle:
        head = handle.read(HEADER_BYTES)
    if len(head) < HEADER_BYTES:
        complain("entry.png is truncated: only %d bytes" % len(head))
    if head[:8] != PNG_MARK:
        complain("entry.png does not start with the PNG signature")
    chunk_length = struct.unpack(">I", head[8:12])[0]
    chunk_kind = head[12:16]
    if chunk_kind != b"IHDR" or chunk_length != 13:
        complain("first chunk is not a 13-byte IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (WANTED_WIDTH, WANTED_HEIGHT):
        complain(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, WANTED_WIDTH, WANTED_HEIGHT)
        )
    return width, height


def run(output_dir=None, verbose=False):
    here = Path(__file__).resolve().parent
    source = here / SOURCE_FILENAME
    if not source.is_file():
        complain("cannot find %s next to main.py" % SOURCE_FILENAME)

    width, height = measure_png(source)
    before = digest_file(source)
    byte_count = os.path.getsize(source)
    if verbose:
        print(
            "source: %s (%d bytes, sha256 %s)" % (source, byte_count, before)
        )

    out_dir = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = Path(out_dir) / SOURCE_FILENAME
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as exc:
        complain("could not write %s: %s" % (destination, exc))

    after = digest_file(destination)
    if after != before:
        complain("copy failed verification: digests differ")
    if os.path.getsize(destination) != byte_count:
        complain("copy failed verification: sizes differ")
    if verbose:
        print("verified: the copy matches the source byte for byte")

    print("output: %s" % destination)
    print("bytes: %d" % byte_count)
    print("dimensions: %dx%d" % (width, height))
    print("sha256: %s" % after)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copy and verify the news-image-20261120 front page."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="output directory, overriding MAKEFUN_OUTPUT_DIR",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="also print the source path, size and digest",
    )
    options = parser.parse_args()
    run(output_dir=options.output, verbose=options.verbose)
