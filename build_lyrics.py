#!/usr/bin/env python3
"""Wrap the lines in lyrics.txt with the .verse and .chorus classes and drop
them into the Exercise 3 block. Edit BLOCKS if you re-split the song."""

import html
import pathlib
import sys

DOC = pathlib.Path("murugavvel_suryaprakash_cw03.html")
SRC = pathlib.Path("lyrics.txt")

# (class, first line, last line) - 1-based, inclusive
BLOCKS = [
    ("verse",  1, 11),
    ("chorus", 12, 16),
    ("verse",  17, 22),
    ("chorus", 23, 26),
    ("verse",  27, 29),
    ("chorus", 30, 35),
]

START, END = "<!-- lyrics:start -->", "<!-- lyrics:end -->"


def main():
    if not SRC.exists():
        sys.exit(f"{SRC} not found - paste the lyrics into it first, one line per line.")

    lines = [ln.strip() for ln in SRC.read_text(encoding="utf-8").splitlines()]
    lines = [ln for ln in lines if ln]
    if not lines:
        sys.exit(f"{SRC} is empty.")

    out = []
    for cls, first, last in BLOCKS:
        chunk = lines[first - 1:last]
        if not chunk:
            continue
        out.append(f'      <div class="{cls}">')
        for ln in chunk:
            out.append(f"        <p>{html.escape(ln)}</p>")
        out.append("      </div>")

    doc = DOC.read_text(encoding="utf-8")
    a, b = doc.index(START), doc.index(END) + len(END)
    doc = doc[:a] + START + "\n" + "\n".join(out) + "\n      " + END + doc[b:]
    DOC.write_text(doc, encoding="utf-8")
    print(f"Inserted {len(lines)} lines across {len(BLOCKS)} blocks into {DOC}.")


if __name__ == "__main__":
    main()
