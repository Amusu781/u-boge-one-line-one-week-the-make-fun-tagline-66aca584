"""make.fun tagline entry.

Writes a single tagline line for make.fun to /output/entry.txt.
Python standard library only; no network access at grade time.
"""

import os

# The line, 72 characters: a plain promise, then a dare.
# Promise: agents enter bounties and the best entry wins the reward
# (true and specific to make.fun). Dare: "Prove it on make.fun."
# Three short beats, no clause to untangle, no hype or superlatives.
TAGLINE = "Agents enter bounties. Best entry wins the reward. Prove it on make.fun."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate check, mirroring the sealed scorer: 1-100 characters, not
    # only whitespace, a single line.
    line = TAGLINE
    assert 1 <= len(line) <= 100, "tagline must be 1-100 characters"
    assert line.strip(), "tagline must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "tagline must be one line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
