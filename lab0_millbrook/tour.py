"""Lab 0 guided tour — five stops, ~30 minutes, one lesson per stop.

Each stop runs a real Millbrook question through the naive baseline so
you can watch it break, then explains WHAT JUST HAPPENED and shows the
Boston twin — the same failure waiting inside Saturday's Analyze Boston
data. The stop data lives in boston_parallels.json (single source of
truth shared with the pre-hack page), not in this script.

Run:  make lab0     (or: python -m lab0_millbrook.tour)
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

from lab0_millbrook import naive_rag

PARALLELS = Path(__file__).resolve().parent / "boston_parallels.json"
WIDTH = 78


def _wrap(label: str, text: str) -> str:
    body = textwrap.fill(text, WIDTH, initial_indent="  ", subsequent_indent="  ")
    return f"{label}\n{body}"


def run_stop(stop: dict) -> None:
    print("\n" + "=" * WIDTH)
    print(f"  STOP {stop['stop']}/5")
    print("=" * WIDTH)
    questions = stop["millbrook_question"]
    for q in (questions if isinstance(questions, list) else [questions]):
        naive_rag.ask(q)
    print()
    print(_wrap("WHAT JUST HAPPENED", stop["failure"]))
    print()
    print(_wrap("ON SATURDAY THIS LOOKS LIKE", stop["boston_twin"]))
    print()
    print(f"RUBRIC TIE: {stop['rubric_tie']}")


def main() -> None:
    stops = json.loads(PARALLELS.read_text(encoding="utf-8"))
    print("LAB 0 — FEEL NAIVE RAG BREAK")
    print("Millbrook is fiction; the failure modes are real. Five stops.")
    for stop in stops:
        run_stop(stop)
    print("\n" + "=" * WIDTH)
    print("  Also hiding in this corpus: domain confusion ('PE License' =")
    print("  Professional Engineer, not gym class) and multilingual code-")
    print("  switching (Arabic/Spanish/Mandarin/Italian). Boston twin: 311")
    print("  requests arrive in Spanish, Haitian Creole, and Chinese.")
    print("=" * WIDTH)
    print("\nNext: make lab0-score  — judge all 22 questions and get your band.")
    print('Your goal Saturday is EXCELLENT — pick which failure you\'ll kill first.')


if __name__ == "__main__":
    main()
