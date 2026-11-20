#!/usr/bin/env python3
"""The World Today -- Friday, 20 November 2026.

Entry for make.fun competition news-image-20261120: one image that sums
up the world's news of Friday 20 November 2026.

The image is a newspaper front page, drawn for this day from the stories
reported on 20 November 2026:

  * Lead: Trump pushes any decision on war with Iran to 2027, saying
    he will "see what happens" after 1 January; US intelligence is
    reported to assess Iran still holds at least 2,500 missiles.
  * After the Shenzhen trilateral, Trump, Xi and Putin issue a "peace
    declaration": a nuclear war cannot be won and must never be fought,
    with dialogue on nuclear risks and more refined petroleum supply.
    Xi calls the talks "fruitful"; Putin calls them a "success".
  * European leaders at the Berlin Coalition of the Willing summit say
    they are ready to negotiate with Russia on ending the war in
    Ukraine, with Europe and Kyiv at the table. Putin vows a "far more
    painful" response to Ukraine's strike on the Crimean Bridge, and
    Russian drones damage the Dutch and Austrian embassies in Kyiv.
  * Anthropic's Nasdaq debut: ANT first trades at $111.50, 34% above
    its $83 IPO price, and closes 17% higher at $97.17. The $81.3bn
    offering, the largest IPO ever, closes on 20 November.
  * Cyclone Akvan makes landfall near Gopalpur, Odisha, around noon,
    winds 90-100 km/h gusting to 110; over 100,000 people evacuated
    to 1,224 shelters, with a zero-casualty target.
  * NASA confirms Voyager 1 has passed one light-day from Earth.
  * JAXA drops Hayabusa2's planned 2031 landing on asteroid 1998
    KY26 after ion-engine trouble; a flyby of 2015 BM510 in April
    2028 instead.
  * GTA 6 sales pass The Odyssey's $1.80bn global run.
  * Henry Nicholls scores an unbeaten 113 as New Zealand reach 243
    for five on day one of the first Test against India in Wellington.
  * Also: South Korea's Supreme Court overturns ex-PM Han Duck-soo's
    conviction; Fiji declares a national disaster over drought;
    dozens missing after a migrant boat sinks off Senegal.

The program itself is deliberately small and deterministic: it copies the
image the repository holds to the output path, then verifies the copy is
byte-identical to the source. Two runs therefore write identical bytes.
It uses only the Python standard library and touches no network.

Run locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
import sys

# The image lives next to this program in the repository.
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(REPO_DIR, "entry.png")

# The grader sets MAKEFUN_OUTPUT_DIR; the competition rules name /output.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def sha256_of(path):
    """Return the lowercase hex SHA-256 of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path):
    """Return (width, height) of a PNG from its IHDR chunk, or None."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def main():
    if not os.path.isfile(SOURCE):
        print("error: entry.png is missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    size = os.path.getsize(OUTPUT)
    if size > 1048576:
        print("error: entry.png exceeds the 1 MiB limit", file=sys.stderr)
        return 1
    dims = png_dimensions(OUTPUT)
    if dims is None:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if dims[0] > 1024 or dims[1] > 1024:
        print("error: entry.png exceeds 1024x1024", file=sys.stderr)
        return 1
    if sha256_of(SOURCE) != sha256_of(OUTPUT):
        print("error: copy differs from source", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT, size, sha256_of(OUTPUT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
