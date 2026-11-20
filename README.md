# The World Today — Friday, 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/faj17/news-image-20261120b/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/faj17/news-image-20261120b/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper front page for Friday, 20 November 2026, made for the
news-image-20261120 competition. The image is `entry.png`: a single
1024 by 1024 front page, laid out like a broadsheet, with the day's
biggest stories set as headlines above the fold.

## What is on the front page

- **Iran decision deferred.** Washington will not decide on military
  action against Iran until 2027. US intelligence believes Iran still
  holds at least 2,500 missiles.
- **A three-way peace declaration.** Trump, Xi and Putin signed a joint
  peace declaration after their trilateral meeting in Shenzhen.
- **Europe prepares to talk.** At the Coalition of the Willing summit in
  Berlin, European leaders said they are ready for negotiations over
  Ukraine. Putin responded to the strike on the Crimean Bridge by
  vowing a far more painful retaliation.
- **Anthropic joins the market.** The AI company debuted on Nasdaq,
  first trading at $111.50 — about 34% above its $83 IPO price — and
  closed the day 17% higher at $97.17.
- **Cyclone Akvan hits Odisha.** The storm made landfall near Gopalpur
  with winds of 90–100 km/h gusting to 110. More than a hundred
  thousand people — 105,304 — were evacuated beforehand.
- **Voyager 1, one light-day out.** NASA confirmed the probe has now
  travelled a full light-day from Earth.
- **Hayabusa2 landing dropped.** JAXA scrapped its plan to land
  Hayabusa2 on asteroid 1998 KY26 in 2031.
- **GTA 6 overtakes The Odyssey.** The game's sales have now passed the
  film's $1.80 billion worldwide gross.
- **Nicholls stands firm.** Henry Nicholls ended day one of the first
  Test against India in Wellington unbeaten on 113, New Zealand 243
  for 5.

## How to run it

`main.py` copies the finished front page to the output directory and
checks the copy byte for byte. It needs nothing beyond Python 3 and
the standard library, and it never uses the network.

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png` and prints its path, size in bytes,
dimensions and SHA-256 digest. The output directory can also be given
directly, and `--verbose` prints the source details too:

```sh
python3 main.py --output out --verbose
```

If the variable is unset and no `--output` is given, the copy goes to
`/output/entry.png`.

## Verification

The script was run twice in a row into the same directory and both runs
reported the same SHA-256 digest for `out/entry.png`, identical to the
digest of `entry.png` itself — so the delivered copy is byte-identical
to the source image. The file is 1,024,661 bytes at 1024 by 1024
pixels, inside the competition's one-mebibyte limit.

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?ref=tzsn25v9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
