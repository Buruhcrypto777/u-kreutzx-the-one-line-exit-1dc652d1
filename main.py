#!/usr/bin/env python3
"""The One-Line Exit -- entry program.

Writes one resignation letter, exactly one line long, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR, or a local out/ dir).

The letter: a lifeguard resigns, effective immediately, because he
has just realized he cannot swim. The job's core requirement,
inverted, with the punch on the very last word -- a letter a person
could actually send, and the kind of line a colleague forwards.
"""

import os

LETTER = "I am resigning, effective immediately: I have just realized I cannot swim."


def resolve_output_dir():
    """Pick the output directory per the competition spec."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    text = LETTER.strip()
    if not text or "\n" in text or len(text) > 140:
        raise ValueError("letter must be one non-blank line of 1-140 characters")
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LETTER + "\n")
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(local, exist_ok=True)
        with open(os.path.join(local, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LETTER + "\n")
    print(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
