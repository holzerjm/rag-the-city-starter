"""Split millbrook_full.md into ten per-document files under corpus/docs/.

The gist ships the whole city as ONE markdown file. Real municipal data
never arrives that way, so we split on the "## DOCUMENT N:" headings to
simulate a ten-source corpus (demographics, bios, minutes, a medical
record, a transcript, a diary, email, a conversation, news, engineering).
naive_rag.py indexes the split files, and inspecting a single failing
doc is much easier than scrolling one 22 KB wall of text.

Run from the repo root:  python -m lab0_millbrook.split_corpus

Other corpora reuse this splitter via --input / --outdir (e.g. Level 2's
lab0_boston). Defaults are unchanged: with no flags it splits Millbrook
exactly as before. A custom --input keeps its own leading comment block
(everything before the first heading) as the per-file header instead of
the Millbrook attribution.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

CORPUS = Path(__file__).resolve().parent / "corpus"
FULL = CORPUS / "millbrook_full.md"
DOCS = CORPUS / "docs"

HEADING_RE = re.compile(r"^## DOCUMENT (\d+): (.+?)\s*$", re.M)

# Prepended to every generated docs/ file. The splitter always regenerates
# docs/ from millbrook_full.md (whose own header sits before the first
# heading and is never captured), so re-splitting stays idempotent.
ATTRIBUTION = """\
<!--
  Millbrook City RAG Challenge \u00a9 William Caban \u2014 used with permission.
  All content is fictional, AI-generated synthetic data.
  Source: https://gist.github.com/williamcaban/8764f13aaa5c4b0768033671483f6c0f
  This corpus is NOT covered by this repository Apache-2.0 code license.
-->

"""


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")


def split(input_path: Path = FULL, outdir: Path = DOCS) -> list[Path]:
    text = input_path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    if input_path == FULL and len(matches) != 10:
        raise SystemExit(f"Expected 10 '## DOCUMENT N:' headings, found {len(matches)} — corpus changed?")
    if not matches:
        raise SystemExit(f"No '## DOCUMENT N:' headings found in {input_path}")
    if input_path == FULL:
        header = ATTRIBUTION
    else:  # carry the corpus's own preamble (e.g. its fiction disclaimer)
        preamble = text[:matches[0].start()].strip()
        header = preamble + "\n\n" if preamble else ""
    outdir.mkdir(parents=True, exist_ok=True)
    written = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        num, title = int(m.group(1)), m.group(2)
        path = outdir / f"doc{num:02d}_{slugify(title)}.md"
        path.write_text(header + text[m.start():end].strip() + "\n", encoding="utf-8")
        written.append(path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a '## DOCUMENT N:' corpus into per-document files.")
    parser.add_argument("--input", type=Path, default=FULL, help="corpus markdown file (default: Millbrook)")
    parser.add_argument("--outdir", type=Path, default=DOCS, help="output directory (default: Millbrook corpus/docs)")
    args = parser.parse_args()
    for path in split(args.input, args.outdir):
        print(f"  {path.name}")
    print(f"Split {args.input.name} into {len(list(args.outdir.glob('doc*.md')))} documents -> {args.outdir}")


if __name__ == "__main__":
    main()
