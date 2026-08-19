"""Level 2 intro — The Fort Point Files (Boston-shaped Millbrook variant).

Splits lab0_boston/corpus/fortpoint_full.md into per-document files, builds
the Boston chroma index alongside (not replacing) the Millbrook one, prints
the scenario, and suggests five questions whose failures are worth watching.

Run:  make lab0-boston     (or: python -m lab0_boston.intro)
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

from lab0_millbrook import naive_rag
from lab0_millbrook.split_corpus import split

HERE = Path(__file__).resolve().parent
FULL = HERE / "corpus" / "fortpoint_full.md"
DOCS = HERE / "corpus" / "docs"
QUESTIONS = HERE / "questions.json"
COLLECTION = "fortpoint_naive"
WIDTH = 78

DISCLAIMER = (
    "The Fort Point Files is a work of fiction created for RAG education. "
    "Characters, businesses, documents, and all numbers are invented; Boston "
    "place names are used fictitiously. Inspired by the Millbrook City RAG "
    "Challenge by William Caban (used with permission)."
)

SCENARIO = (
    "The Northern Avenue Bridge — a 1908 swing bridge over the Fort Point "
    "Channel, a short walk from Saturday's venue — has been closed to vehicles "
    "since 1997 and fenced off from everyone since December 2014. That much is "
    "real. Everything else here is fiction: a 2026 reopening study, a council "
    "docket, a bakery on Sleeper Street, a water taxi dodging debris, and "
    "eleven documents shaped exactly like the Analyze Boston data you'll index "
    "on Saturday — 311 rows, an inspection report, a budget CSV that disagrees "
    "with its own narrative, minutes, a weekly paper, a trilingual transcript, "
    "a property record, an engineering assessment, bios, and a diary."
)

# The five try-these questions (ids into questions.json) with failure teasers.
SUGGESTED: list[tuple[str, str]] = [
    ("1A", "two Fitzgeralds — watch it merge the councilor and the engineer into one person"),
    ("2B", "the answer (~15 years) is written in NO chunk — it needs date arithmetic across documents"),
    ("3A", "the budget CSV says $4,200,000, the narrative says $3.65M — the baseline will confidently pick one"),
    ("4A", "the inspection report has violation codes, not causes — the right answer is 'the data doesn't say'"),
    ("9A", "counting 311 rows that a fixed-size chunker just sliced in half — the tabular-chunking failure"),
]


def _wrap(text: str) -> str:
    return textwrap.fill(text, WIDTH, initial_indent="  ", subsequent_indent="  ")


def main() -> None:
    print("LEVEL 2 — THE FORT POINT FILES")
    print("=" * WIDTH)
    print(_wrap(SCENARIO))
    print()
    print(_wrap(DISCLAIMER))
    print()
    print("Splitting the corpus:")
    for path in split(FULL, DOCS):
        print(f"  {path.name}")
    print("\nBuilding the Boston index (collection: %s)..." % COLLECTION)
    coll = naive_rag.build_index(docs_dir=DOCS, collection=COLLECTION)
    print(f"  {coll.count()} chunks indexed.")

    questions = {q["id"]: q for q in json.loads(QUESTIONS.read_text(encoding="utf-8"))}
    print("\nTRY THESE FIVE (each hides a failure the naive baseline walks into):")
    for qid, teaser in SUGGESTED:
        q = questions[qid]
        print(f'\n  [{qid} · {q["category"]}]')
        print(_wrap(q["question"]))
        print(_wrap(f"-> expect trouble: {teaser}"))

    print("\n" + "=" * WIDTH)
    print('Ask anything:   make lab0-boston-ask Q="What is the condition rating of the swing span?"')
    print("Score all 24:   make lab0-boston-score")
    print("Your goal Saturday is EXCELLENT — pick which failure you'll kill first.")


if __name__ == "__main__":
    main()
