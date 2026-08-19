"""Lab 0 guided tour — watch naive RAG break, one lesson per stop.

The default tour is The Fort Point Files: six stops, ~30 minutes, driven
by lab0_boston/tour_stops.json. Each stop runs real corpus questions
through the naive baseline so you can watch it break, then explains WHAT
JUST HAPPENED, shows the ground truth, and points at the matching shape
inside Saturday's real Analyze Boston data.

The original tour — the Millbrook City RAG Challenge by William Caban,
the challenge this lab was rebuilt from — runs via its own stops file
(boston_parallels.json, single source of truth shared with the pre-hack
page): that's make lab0-millbrook. The Makefile passes explicit --stops
/ --corpus-dir / --collection for BOTH editions.

A stops file is either a JSON list of stops (the original Millbrook
format, framed with MILLBROOK_META below) or an object with "title",
"intro", "shape_label", "outro" (lines), "next_steps" (lines), and
"stops". Each stop may carry "questions" (or the legacy singular
"millbrook_question"), "failure", "expected", "data_shape" (or the
legacy "boston_twin"), "rubric_tie", and "ask_command".

Run:  make lab0     (or: python -m lab0_millbrook.tour)
"""
from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

from lab0_millbrook import naive_rag

FORTPOINT_STOPS = naive_rag.REPO_ROOT / "lab0_boston" / "tour_stops.json"
WIDTH = 78

# Framing applied when the stops file is a plain JSON list — the original
# Millbrook format used by boston_parallels.json.
MILLBROOK_META = {
    "title": "THE ORIGINAL — MILLBROOK CITY RAG CHALLENGE",
    "intro": "William Caban's fictive-city challenge: the corpus Lab 0 was rebuilt "
             "from. Millbrook is fiction; the failure modes are real. Five stops, "
             "each mapped to its Boston twin.",
    "shape_label": "ON SATURDAY THIS LOOKS LIKE",
    "outro": [
        "Also hiding in this corpus: domain confusion ('PE License' =",
        "Professional Engineer, not gym class) and multilingual code-",
        "switching (Arabic/Spanish/Mandarin/Italian). Boston twin: 311",
        "requests arrive in Spanish, Haitian Creole, and Chinese.",
    ],
    "next_steps": [
        "Next: make lab0-millbrook-score  — judge all 22 questions and get your band.",
        "Your goal Saturday is EXCELLENT — pick which failure you'll kill first.",
    ],
}


def _wrap(label: str, text: str) -> str:
    body = textwrap.fill(text, WIDTH, initial_indent="  ", subsequent_indent="  ")
    return f"{label}\n{body}"


def run_stop(stop: dict, total: int, meta: dict, docs_dir: Path, collection: str) -> None:
    print("\n" + "=" * WIDTH)
    print(f"  STOP {stop['stop']}/{total}")
    print("=" * WIDTH)
    questions = stop.get("questions") or stop["millbrook_question"]
    for q in (questions if isinstance(questions, list) else [questions]):
        naive_rag.ask(q, docs_dir=docs_dir, collection=collection)
    print()
    print(_wrap("WHAT JUST HAPPENED", stop["failure"]))
    if stop.get("expected"):
        print()
        print(_wrap("GROUND TRUTH", stop["expected"]))
    shape = stop.get("data_shape") or stop.get("boston_twin")
    if shape:
        print()
        print(_wrap(meta["shape_label"], shape))
    print()
    print(f"RUBRIC TIE: {stop['rubric_tie']}")
    if stop.get("ask_command"):
        print(f"TRY IT YOURSELF: {stop['ask_command']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Lab 0 guided tour over a stops file.")
    parser.add_argument("--stops", type=Path, default=FORTPOINT_STOPS,
                        help="stops JSON file (default: Fort Point's tour_stops.json)")
    parser.add_argument("--corpus-dir", type=Path, default=naive_rag.DOCS_DIR,
                        help="split docs directory (default: Fort Point)")
    parser.add_argument("--collection", default=naive_rag.COLLECTION,
                        help="chroma collection name (default: fortpoint_naive)")
    args = parser.parse_args()

    data = json.loads(args.stops.read_text(encoding="utf-8"))
    if isinstance(data, list):  # original Millbrook stops format
        meta, stops = MILLBROOK_META, data
    else:
        meta, stops = data, data["stops"]
    print(meta["title"])
    print(textwrap.fill(meta["intro"], WIDTH))
    for stop in stops:
        run_stop(stop, len(stops), meta, args.corpus_dir, args.collection)
    print("\n" + "=" * WIDTH)
    for line in meta.get("outro", []):
        print(f"  {line}")
    print("=" * WIDTH)
    print()
    for line in meta.get("next_steps", []):
        print(line)


if __name__ == "__main__":
    main()
