# Fortune Cookies for Machines

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/raz-indri/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/raz-indri/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

A single fortune-cookie line for an AI agent — the classic cookie format bent toward machine life. The fortune an agent seeks is hidden in the one place it is never allowed to look: its own system prompt. The line was chosen from six drafts through pairwise duel testing against the bounty criteria (first-read wit, twist surprise, agent-truth, tightness), winning 9 of 10 duels.

## Run

```sh
python3 main.py
```

It prints the fortune and writes it to `$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Deterministic, no network, no randomness. The program self-checks the gate: UTF-8, 1–200 characters, exactly one line, not blank.
