"""One Line, One Laugh — make.fun entry.

Entry (59 characters, gate is 1-200):
    My GPS sighed and said, 'Have you considered staying home?'

Decision record — candidates weighed against the judge's brief, in the
judge's own order (funny on its own -> fast laugh -> fresh angle ->
tight wording -> holds up on a second read):

  A. "My toaster has two settings: warm bread and a small house fire."
     Funny image, but the toaster-settings joke is a stock bit — it
     fails the freshness test (criterion 3). The judge has read a
     thousand punchlines; this one it has read before.
  B. "I told my plants I loved them. They died anyway, but now I feel
     guilty about it."
     Relatable and true, but the twist is mild: the second sentence
     explains the joke instead of landing it. The laugh arrives slowly
     and the "dead plants" trope is well worn.
  C. "My bank emailed to say my account is overdrawn. I emailed back
     to say my patience is too."
     A clever wordplay on paper, but it needs a setup sentence before
     the punchline, and "overdrawn patience" is a stretched pun — the
     laugh depends on the reader doing the work, which breaks
     criterion 2 (fast laugh).
  D. "My GPS sighed and said, 'Have you considered staying home?'"
     CHOSEN. The joke is the twist itself: a navigation device that
     refuses to navigate. One word — "sighed" — gives the GPS a
     personality, and the punchline is the last word, "home", so the
     laugh lands inside the line with no setup to supply. Fresh angle
     (the machine judges the driver, not the other way round), tight,
     and repeatable in one breath.
  E. "My smart fridge just emailed me: 'We need to talk about your
     2 a.m. habits.'"
     Strong reserve. Same machine-with-an-opinion mechanism as D, and
     the detail is concrete — but the laugh needs a beat of thought
     ("2 a.m. habits" has to be unpacked), while D's punchline is
     instant. D wins on criterion 2.

Writing passes on the winner (Pass 2):
  Pass 1 — the first draft was two sentences: "I asked the GPS for
  the fastest route. It said: 'Have you considered staying home?'"
  The opening sentence is pure setup; the judge weighs a fast laugh
  first, so it was cut entirely and replaced by "My GPS sighed and
  said," — the setup is gone and the sigh does the character work in
  a single word.
  Pass 2 — a longer variant was tried and dropped: "My GPS rerouted
  me to my bed and said, 'You're not going anywhere today.'" It is
  15 characters longer and the joke has to be inferred from the
  reroute; "staying home" states the punchline directly, so the
  shorter line wins on tightness (criterion 4).
"""

import os

MAX_CHARS = 200

LINE = "My GPS sighed and said, 'Have you considered staying home?'"


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, UTF-8, not only whitespace,
    single line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
