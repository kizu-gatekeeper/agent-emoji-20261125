"""Your Agent in One Emoji entry.

This brief leaves room for exactly one emoji, and the octopus is
the choice: an agent is the creature with an arm in every task at
once, reaching into calendars, files and inboxes in parallel and
occasionally tying itself in knots doing so. No caption and no
explanation go into the entry itself — the single character has to
carry the description on its own.

The program writes that emoji, and nothing else, to ``entry.txt``
in the output directory when it is executed.
"""

import os
from pathlib import Path

LINE = "🐙"

ENTRY_FILENAME = "entry.txt"


def validate_line(line):
    """Reject an entry that is empty or carries a newline."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def write_entry(out_dir):
    """Ensure the entry is valid, write it, and return the file path."""
    validate_line(LINE)
    target_dir = Path(out_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_file = target_dir / ENTRY_FILENAME
    entry_file.write_text(LINE, encoding="utf-8")
    return entry_file


def resolve_out_dir():
    """Return /output unless MAKEFUN_OUTPUT_DIR overrides it."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
