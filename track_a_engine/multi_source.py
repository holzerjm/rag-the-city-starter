"""Track A skeleton: one question, two sources that disagree.

THE STARTING POINT, NOT THE SOLUTION. Goal: answer a single question —
"What is the FY26 appropriation for the Parks Department?" — from BOTH
the Operating Budget CSV and the budget-narrative PDF, then surface the
disagreement instead of silently picking one (Lab 0 stop 3 is the same
failure in miniature: 40 vs 25 vs 15 tons).

What runs today: the CSV half, if you've downloaded the budget CSV.
What's TODO: everything that makes it multi-source. Teams extend this.

PDF parsing needs Docling:  .venv/bin/pip install -r requirements-track-a.txt

Run:  python track_a_engine/multi_source.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = REPO_ROOT / "data" / "downloads"
BUDGET_CSV = DOWNLOADS / "operating-budget.csv"
BUDGET_PDF = DOWNLOADS / "operating-budget-narrative.pdf"
QUESTION = "What is the FY26 appropriation for the Parks Department?"


def csv_answer() -> str:
    if not BUDGET_CSV.exists():
        return (f"[TODO] {BUDGET_CSV.name} not downloaded yet.\n"
                "       Get it from https://data.boston.gov/dataset/operating-budget\n"
                "       (or extend boston/download.py to fetch it — one list entry).")
    df = pd.read_csv(BUDGET_CSV, low_memory=False)
    # TODO(team): find the department + fiscal-year columns for the real
    # schema and filter for Parks. This substring probe just proves I/O.
    hits = df[df.astype(str).apply(lambda r: r.str.contains("Parks", case=False, na=False)).any(axis=1)]
    return f"CSV: {len(hits)} candidate rows mention 'Parks' out of {len(df)} total."


def pdf_answer() -> str:
    try:
        from docling.document_converter import DocumentConverter  # noqa: F401
    except ImportError:
        return ("[TODO] Docling not installed — pip install -r requirements-track-a.txt\n"
                "       Then: convert the budget-narrative PDF to markdown, chunk it,\n"
                "       and retrieve the Parks paragraph.")
    if not BUDGET_PDF.exists():
        return f"[TODO] Download the budget-narrative PDF to {BUDGET_PDF}."
    # TODO(team): DocumentConverter().convert(BUDGET_PDF) -> markdown ->
    # chunk -> embed -> retrieve the Parks appropriation paragraph.
    return "[TODO] Docling is installed — implement the conversion pipeline here."


def reconcile(csv_result: str, pdf_result: str) -> str:
    # TODO(team): when both sources return a number, compare them.
    # If they disagree, SAY SO and cite both — that is the whole point.
    return "[TODO] Reconciliation: report both figures and flag any disagreement."


def main() -> None:
    print(f"QUESTION: {QUESTION}\n")
    csv_r, pdf_r = csv_answer(), pdf_answer()
    print(f"SOURCE 1 — Operating Budget CSV\n  {csv_r}\n")
    print(f"SOURCE 2 — Budget narrative PDF (Docling)\n  {pdf_r}\n")
    print(f"RECONCILIATION\n  {reconcile(csv_r, pdf_r)}")


if __name__ == "__main__":
    main()
