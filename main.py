#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty entry.

Writes a single horror sentence (one line, under 200 characters) to
/output/entry.txt. Nothing else is written.
"""

ENTRY = (
    "Your wedding photo shows thirteen guests, but you only invited twelve, "
    "and the thirteenth is standing behind you wearing your face."
)


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
