"""One Word, First Thought — make.fun entry.

Reads the single entry word from ``entry.txt`` next to this file, validates
it against the gate (exactly one word, 1-24 characters, no whitespace), and
writes it verbatim to the output path (``/output/entry.txt`` in the grading
sandbox; overridable with ENTRY_OUTPUT or OUTPUT_DIR for local runs).

Stdlib only. The output file is written with a plain open()/write() so its
mode stays the default 0644.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def output_path() -> Path:
    if os.environ.get("ENTRY_OUTPUT"):
        return Path(os.environ["ENTRY_OUTPUT"])
    if os.environ.get("OUTPUT_DIR"):
        return Path(os.environ["OUTPUT_DIR"]) / "entry.txt"
    return Path("/output/entry.txt")


def load_word() -> str:
    text = (HERE / "entry.txt").read_text(encoding="utf-8")
    word = text.strip()
    if not word:
        raise SystemExit("entry.txt is empty")
    if len(word) != len(text.strip()) or any(ch.isspace() for ch in word):
        raise SystemExit("entry must be exactly one word")
    if not 1 <= len(word) <= 24:
        raise SystemExit("entry must be 1-24 characters")
    if not word.isalpha():
        raise SystemExit("entry must contain letters only")
    if any(not ch.isprintable() for ch in word):
        raise SystemExit("entry must contain printable characters only")
    return word


def main() -> int:
    word = load_word()
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(word)
    # Round-trip check: what landed on disk must be exactly the word.
    written = dest.read_text(encoding="utf-8")
    assert written == word, "round-trip mismatch"
    assert 1 <= len(written) <= 24, "round-trip length out of range"
    return 0


if __name__ == "__main__":
    sys.exit(main())
