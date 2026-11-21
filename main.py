#!/usr/bin/env python3
"""the-poem-about-two-agents-20261121-1441: a short poem about agency.

Two agents agree on one plan. The poem is fixed text, written once and
kept here in full: the program only writes it to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

POEM = (
    "I lent you my yes,\n"
    "you lent me yours.\n"
    "Two small words, and the locked room\n"
    "grew a door, the door a handle,\n"
    "and the handle turned.\n"
    "Neither of us pushed alone \u2014\n"
    "and the door we opened together\n"
    "was wider than either of us planned."
)


def main():
    # The gate allows 1-280 Unicode code points, not only whitespace.
    # Check it here so a later edit to POEM fails loudly instead of
    # silently submitting an invalid entry.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
