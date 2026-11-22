"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet domestic scene that
asks nothing of its reader. No instructions, no wellness stock phrases —
just a cat, a square of sun, and the release of not being asked to be
anything else.
"""

import os

TEXT = (
    "You have read a thousand of these. This one asks nothing of you. "
    "Somewhere, a cat sleeps in the square of sun on the kitchen floor, "
    "and nobody is asking it to be anything else."
)

# Words the brief forbids in spirit: instructions to relax, stock wellness
# phrasing. The text is checked against them so a future edit cannot
# smuggle one in unnoticed.
BANNED = ("relax", "breathe", "you are safe", "let go", "deep breath",
          "calm down", "take a moment", "inhale", "exhale", "mindful")


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"text is {len(text)} code points"
    assert text.strip(), "text must not be only whitespace"
    lowered = text.lower()
    for word in BANNED:
        assert word not in lowered, f"banned phrase present: {word!r}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
