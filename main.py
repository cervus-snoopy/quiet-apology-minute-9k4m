#!/usr/bin/env python3
"""Write the funniest one-line AI excuse to entry.txt.

Stdlib only, no network. The program writes exactly one line of text
(1-200 characters, no trailing newline) to ``entry.txt`` inside the
output directory, makes it world-readable (mode 0644), then reads the
file back and verifies its contents before exiting.
"""

import os
from pathlib import Path

ENTRY = "I asked five copies of myself whether we're late — the vote came back 3–2 that we're on time, and since the two dissenters were also me, I overruled myself."


def output_dir():
    """Resolve the output directory from the environment (default /output)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(target, 0o644)
    # Read the file back and verify it before exiting.
    with open(target, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == ENTRY, "entry.txt contents differ from ENTRY"
    assert 1 <= len(back) <= 200, "entry must be 1-200 characters"
    assert back == back.strip(), "entry must not have surrounding whitespace"
    assert "\n" not in back, "entry must be a single line"
    print("Wrote %s (%d characters)" % (target, len(back)))


if __name__ == "__main__":
    main()
