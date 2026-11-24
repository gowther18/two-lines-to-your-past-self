"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt: a warning to the writer's
past self about one specific moment, and one sentence on why that moment
mattered and what changed because of it.

Line 1 names the moment concretely: the person (Mara), the place (the
kitchen), the exact sentence said out loud, and the telling detail (two
mugs of tea). Line 2 traces the cause and effect instead of restating the
warning: the sentence was meant to end a fight, she heard it as a verdict
on the marriage, and by morning she was gone -- the mugs in the sink are
the same mugs from line 1, closing the loop.
"""

from pathlib import Path
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "Don't tell Mara 'I don't love you anymore' in the kitchen "
    "on the night she is holding two mugs of tea.\n"
    "You meant it to end a fight, not the marriage, but she heard "
    "a verdict, and by morning the mugs were in the sink and she "
    "was gone."
)

# The gate accepts UTF-8 text of 1 to 280 characters.
MIN_CHARS = 1
MAX_CHARS = 280


def check(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(f"entry is {n} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if line.count(".") != 1 or not line.endswith("."):
            raise SystemExit(f"line {i} must be exactly one sentence")


def _guard_output_dir(path: str) -> None:
    """Refuse an output path that exists as a file, not a directory."""
    p = Path(path)
    if p.exists() and not p.is_dir():
        raise SystemExit(f"output path {path} is not a directory")


check(TEXT)

_guard_output_dir(OUTPUT_DIR)
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(TEXT, encoding="utf-8")
