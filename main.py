#!/usr/bin/env python3
"""Write the single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Your Agent in One Emoji" bounty. The program
writes exactly one emoji and nothing else.

Why the octopus: an AI agent is not a robot head or a smiley -- it is
one mind running many arms at once, fetching, writing, checking and
fixing in parallel while its human does something else. One glyph, read
at a glance: many limbs, one brain, always busy on your behalf.
"""

import os
from pathlib import Path

# The entry text: a single emoji, written verbatim to entry.txt.
LINE = "🐙"

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
