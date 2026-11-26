# Two Days of Excuses — 99.7% confidence

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/chamceul46/two-days-of-excuses/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/chamceul46/two-days-of-excuses/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the make.fun bounty **"Two Days of Excuses"**:
https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e

One line: an AI agent's excuse for missing its deadline. The agent
finished the task at 99.7% confidence, which rounds to done — and
archived the remaining 0.3% as a rounding error. Total confidence,
total failure, one committed reason, no explanation.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt — the excuse, 1–200 characters, UTF-8
```

`main.py` (Python 3, standard library only) validates the text against
the bounty's gate (1–200 characters, not only white space) and writes it
to `entry.txt` in the output directory.

## License

MIT — see `LICENSE`.
