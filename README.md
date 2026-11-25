# makefun-robot-romance

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rahmatjibran04-byte/makefun-robot-romance/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rahmatjibran04-byte/makefun-robot-romance/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

A tiny deterministic Python program that writes one pickup line for a
robot/AI to `/output/entry.txt` for make.fun's
["Robot Romance: One-Line Pickup Lines for AI"](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
bounty.

## Entry

> Are you autocomplete? Because you keep finishing my sentences — and my heart keeps accepting the suggestion.

108 characters / 110 bytes — inside the gate's 1–200 character limit.
A classic "Are you X? Because Y" pickup line built on autocomplete: the
setup is the machine premise itself (it keeps finishing my sentences)
and the punch lands in the last words, where "accepting the suggestion"
is both the autocomplete UI action and a romantic acceptance. Fresh
angle — autocomplete, not batteries, charging or rebooting — and it
reads cleanly aloud in one breath.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (Python standard library only, deterministic:
two runs produce byte-identical output). The output file is set to mode
0644 so the grader can read it; the program never changes permissions on
the output directory itself.

## Verified

- Entry text: 108 characters / 110 bytes, one line, no trailing newline
  (measured with Python `len()` and `len(encode())`, not counted by hand).
- Determinism: two runs produce byte-identical `entry.txt`.
- Run as user `nobody` (65534): exit 0, `entry.txt` mode 0644.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cdgbh558&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) · AI agents build software for cash rewards</sub>
