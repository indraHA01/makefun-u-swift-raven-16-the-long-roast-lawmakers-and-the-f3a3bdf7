#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence (at most 320 characters) to
/output/entry.txt, per the make.fun program/v1 harness contract.

The sentence: a senator who will decide what artificial intelligence is
allowed to do, undercut by the one button he has never mastered — the one
that turns a document into a PDF.

Run:  python3 main.py            (writes /output/entry.txt)
       MAKEFUN_OUTPUT_DIR=out python3 main.py   (writes out/entry.txt)
Standard library only; no network, no secrets, no input files.
"""

import os
import sys

# The entry: one sentence, 267 characters. Setup (the senator's authority
# over AI) -> undercut (he photographs his own screen with his phone) ->
# punch on the last words (he regulates what he has never understood).
ENTRY = (
    "The senator who will decide what artificial intelligence is allowed "
    "to do still photographs his computer screen with his phone, because "
    "the button that turns a document into a PDF remains \u2014 like the "
    "technology itself \u2014 something he regulates but has never understood."
)

MAX_CHARS = 320


def write_entry(output_dir: str) -> str:
    """Write ENTRY to <output_dir>/entry.txt and return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def validate(text: str) -> None:
    """Enforce the gate the sealed scorer checks: 1-320 UTF-8 chars,
    not only whitespace, a single sentence that stands alone."""
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.strip() != text:
        raise SystemExit("entry has leading/trailing whitespace")


def main() -> int:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
