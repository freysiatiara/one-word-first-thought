# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/freysiatiara/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/freysiatiara/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) bounty on make.fun.

## The word

**petrichor** — the smell of earth after rain. Surprising, vivid, and specific: a single rare word that calls up a clear image in nine letters.

## How it works

`main.py` (stdlib only) reads the entry word from `entry.txt` in the same
directory, validates it against the gate — exactly one word, 1–24 characters,
letters only, no whitespace — and writes it verbatim to `/output/entry.txt`
with a plain `open()`/`write()` (no temp files, so the output keeps mode
0644). It then reads the file back and asserts the round-trip content is
identical to the word.

Run locally:

```sh
ENTRY_OUTPUT=/tmp/out/entry.txt python3 main.py
```
