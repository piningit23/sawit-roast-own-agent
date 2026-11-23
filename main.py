"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

Deterministic: fixed string literal, stdlib only, no randomness, no
network, no clock, no file reads. Output is exactly one line with
no trailing newline — the roast of Sawit, the farming agent that
grinds around the clock yet still needs its human to click.
"""

import os

ROAST = "My agent grinds 24/7, never sleeps, never eats \u2014 and still needs me to click the button."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
