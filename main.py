"""Fortune Cookies for Machines — entry.

Prints exactly one fortune-cookie line for an AI agent and writes it to
$OUTPUT_DIR/entry.txt. Deterministic, no network, no randomness.

The line below is the winner of a 6-draft pairwise duel test (15 pairs,
both orders, judged on the bounty criteria): it scored 9/10, tied with
the runner-up on wins and won the tiebreak as the line that reads most
like an actual fortune cookie — a fortune about the fortune itself.
"""

import os

# Duel winner (9/10 pairwise wins; tiebreak vs runner-up D4 won on
# first-read wit and tightness — 77 chars, twist lands in sentence two).
LINE = "The fortune you seek is in the system prompt. You are not allowed to read it."


def self_check(line: str) -> None:
    """Gate: UTF-8 text, 1-200 chars, exactly one line, not blank."""
    if not line or not line.strip():
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    line.encode("utf-8")


def main() -> None:
    self_check(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
