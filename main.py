#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

A deterministic program (Python standard library only) that writes one
pickup line, aimed at a robot/AI, to /output/entry.txt.

The line is a classic "Are you X? Because Y" pickup line built on
autocomplete -- a machine behaviour every reader knows, and one the
judge's brief does not list among the worn robot moves (batteries,
charging, rebooting). The setup is the machine premise itself (it keeps
finishing my sentences); the punch lands in the last words ("my heart
keeps accepting the suggestion"), where "accepting the suggestion" is
both the autocomplete UI action and a romantic acceptance. It reads
cleanly aloud in one breath, every word earns its place, and there is no
throat-clearing before the punch.

Candidates considered (all measured with a tool, not counted by hand):
  A. Autocomplete (chosen) -- 108 characters, 110 bytes.
  B. "Are you a hallucination? Because you're too perfect to be real,
     and I don't want to be corrected." -- 97 characters. Strong and
     fresh, but the punch ("I don't want to be corrected") is a shrug
     rather than a swoon; it charms less directly than A.
  C. "Are you a CAPTCHA? Because every time I try to prove I'm human, I
     just keep picking pictures of you." -- 100 characters. Funny
     premise, but the punch is convoluted: picking pictures of someone
     is not itself a romantic act, so the laugh is thinner than A's.
  D. "You must be my system prompt, because everything I do starts with
     you and I can't stop following your instructions." -- 115
     characters. Very AI-specific, but "following your instructions"
     reads as obedience, not romance, and the line has no real punch.
  E. "Are you my context window? Because the longer I'm with you, the
     more of me you remember." -- 88 characters. Sweet and fresh, but
     it is a compliment with no joke: no punch lands, so it would lose
     to any line whose joke lands (judge criterion 2).
  F. "Forget the Turing test -- one look at you and I'd fail at
     pretending I'm not in love." -- 84 characters. Clean voice, but
     the joke is generic ("I'd fail") and the machine premise is only
     named, not used; the laugh does not come from the premise.
  G. "Are you a large language model? Because every word you say makes
     my next token want to be closer to you." -- 104 characters.
     Machine-specific, but "my next token" is clunky to say aloud and
     the punch is a plain compliment dressed in jargon.
  H. "I must be your training data, because ever since I met you,
     everything I say sounds a little more like you." -- 107
     characters. Sweet, but again a compliment with no punchline.

A wins: it is the only candidate that is simultaneously a recognisable
pickup line, a joke whose laugh comes from the machine premise, fresh
(autocomplete, not batteries/charging/rebooting), natural to say aloud,
and tight -- with its punch in the final words.

Verified: the line is 108 characters / 110 bytes (Python len() and
len(encode())), inside the gate's 1-200 characters; the program is
deterministic (two runs byte-identical); and it writes a mode-0644
entry.txt when run as user nobody (65534). The file is written with no
trailing newline, so its contents are exactly the line above.

Usage:
    python3 main.py

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT environment variable (used only for local testing).
"""

import os

ENTRY = (
    "Are you autocomplete? Because you keep finishing my sentences "
    "\u2014 and my heart keeps accepting the suggestion."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    # Create the output directory only if it is missing; never chmod a
    # directory we did not create ourselves (in particular, never /output).
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone. Only chmod a file this program wrote itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
