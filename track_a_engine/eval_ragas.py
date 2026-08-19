"""RAGAS evaluation skeleton, wired to the Lab 0 questions.json format.

Judges score "RAG Quality & Grounding" out of 4 — RAGAS gives you the
numbers to show them: faithfulness (is the answer grounded in retrieved
context?) and answer correctness (does it match the reference?). This
skeleton feeds it the same {question, expected_answer} records Lab 0
uses, so your Millbrook score and your Boston eval share one format.

RAGAS is heavy, so it lives in requirements-track-a.txt:
    .venv/bin/pip install -r requirements-track-a.txt

Run:  python track_a_engine/eval_ragas.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = REPO_ROOT / "lab0_millbrook" / "questions.json"

try:
    from ragas import EvaluationDataset, evaluate  # noqa: F401
    from ragas.metrics import AnswerCorrectness, Faithfulness  # noqa: F401
except ImportError:
    print("[!] ragas is not installed (it is heavy, so it isn't in the base requirements).")
    print("[!] Install Track A extras:  .venv/bin/pip install -r requirements-track-a.txt")
    sys.exit(1)


def build_records() -> list[dict]:
    """questions.json -> RAGAS records, answered by the naive baseline.

    Swap `naive_rag` for YOUR pipeline — that before/after delta is the
    slide your final presentation wants.
    """
    sys.path.insert(0, str(REPO_ROOT))
    from lab0_millbrook import naive_rag

    records = []
    for q in json.loads(QUESTIONS.read_text(encoding="utf-8")):
        chunks = naive_rag.retrieve(q["question"])
        answer = naive_rag.generate(q["question"], chunks) or ""
        records.append({
            "user_input": q["question"],
            "retrieved_contexts": [c["text"] for c in chunks],
            "response": answer,
            "reference": q["expected_answer"],
        })
    return records


def main() -> None:
    records = build_records()
    dataset = EvaluationDataset.from_list(records)
    # TODO(team): pass your judge LLM/embeddings (RAGAS defaults to OpenAI;
    # point it at a local model via its llm=/embeddings= wrappers).
    result = evaluate(dataset, metrics=[Faithfulness(), AnswerCorrectness()])
    print(result)


if __name__ == "__main__":
    main()
