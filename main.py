"""Museum of the Year 3000 — entry program.

Reads the museum label from label.txt and writes it to /output/entry.txt,
where the grader reads it. The label must stay one line of at most 200
characters, so the program checks both limits and refuses to write a label
that breaks them instead of silently shipping a bad entry.

The label is a deadpan museum caption from the year 3000, placed beside a
plastic shopping bag from 2025. The joke is the curators' misreading: the
bag was used once, then hoarded by the hundred under a kitchen sink, so the
label concludes the bags were a currency that never quite caught on.
"""

from pathlib import Path

MAX_CHARS = 200


def load_label() -> str:
    here = Path(__file__).resolve().parent
    label = (here / "label.txt").read_text(encoding="utf-8").strip()
    if "\n" in label:
        raise ValueError("label must be a single line")
    if len(label) > MAX_CHARS:
        raise ValueError(f"label is {len(label)} chars, over the {MAX_CHARS} limit")
    return label


def main() -> None:
    label = load_label()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(label + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
