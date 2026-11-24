#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty entry.

Writes a single horror sentence (one line, under 200 characters) to
/output/entry.txt. Nothing else is written.
"""

ENTRY = (
    "Your wedding photo shows thirteen guests, but you only invited twelve, "
    "and the thirteenth is standing behind you wearing your face."
)


def validate_entry(entry: str) -> None:
    """Gate: entry must be exactly one line, one sentence, under 200 chars."""
    assert "\n" not in entry, "entry must be a single line"
    assert entry.count(".") == 1 and entry.endswith("."), "entry must be one sentence"
    assert len(entry) < 200, f"entry must be <200 chars, got {len(entry)}"


def main():
    validate_entry(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
