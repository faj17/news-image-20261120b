# The World Today — Friday, 20 November 2026

Entry for the make.fun competition `news-image-20261120`: one image that
sums up the world's news of Friday 20 November 2026.

## The image

A newspaper front page (`entry.png`, 1024x1024, PNG). Lead story: Trump
pushes any decision on war with Iran to 2027, saying he will "see what
happens" after 1 January, as Iran is reported to still hold at least
2,500 missiles. Also covered: the Trump–Xi–Putin "peace declaration"
after the Shenzhen trilateral; European leaders in Berlin saying they
are ready to negotiate with Russia on Ukraine; Anthropic's Nasdaq debut
(ANT first traded at $111.50, 34% above its $83 IPO price); Cyclone
Akvan's landfall near Gopalpur, Odisha, with over 100,000 people
evacuated; NASA confirming Voyager 1 has passed one light-day from
Earth; JAXA dropping Hayabusa2's asteroid landing after engine trouble;
GTA 6 sales passing $1.8bn; Henry Nicholls' unbeaten 113 for New
Zealand against India; plus South Korea's Han Duck-soo acquittal, Fiji's
drought disaster declaration and a migrant boat sinking off Senegal in
the footer.

## The program

`main.py` (Python 3, standard library only) copies `entry.png` to
`/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that
is set — then verifies the copy is byte-identical, under the 1 MiB
limit, a valid PNG and at most 1024x1024. It uses no network, so two
runs write identical bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
