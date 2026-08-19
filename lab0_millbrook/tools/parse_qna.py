"""Parse the vendored "Testing and Evals QnA.md" into questions.json.

The gist's QnA file is regular enough to parse with two regexes:
  ## CHALLENGE CATEGORY <n>: <NAME>          -> category
  ### QUESTION <id> (Difficulty: <level>)    -> one question block
Each block carries **Question:**, **Expected Answer:**, and a bulleted
"Wrong Answers a RAG might give" list — which is exactly what an
LLM-as-judge needs (lab0_millbrook/judge.py consumes this output).

Run from the repo root:  python lab0_millbrook/tools/parse_qna.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

QNA_PATH = Path(__file__).resolve().parents[1] / "corpus" / "testing_and_evals_qna.md"
OUT_PATH = Path(__file__).resolve().parents[1] / "questions.json"

CATEGORY_RE = re.compile(r"^## CHALLENGE CATEGORY \d+: (.+?)\s*$", re.M)
QUESTION_RE = re.compile(r"^### QUESTION (\w+) \(Difficulty: (\w+)\)\s*$", re.M)


def _field(block: str, label: str) -> str:
    """Grab the text of a **label:** field up to the next bold field."""
    m = re.search(rf"\*\*{label}:\*\*\s*(.+?)(?=\n\*\*|\n---|\Z)", block, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip().strip('"') if m else ""


def _wrong_answers(block: str) -> list[str]:
    m = re.search(r"\*\*Wrong Answers a RAG might give:\*\*\s*\n(.*?)(?=\n---|\Z)", block, re.S)
    if not m:
        return []
    return [ln.lstrip("- ").strip() for ln in m.group(1).splitlines() if ln.strip().startswith("-")]


def parse(text: str) -> list[dict]:
    questions = []
    # Walk category sections in order; each holds its own QUESTION blocks.
    cat_starts = [(m.start(), m.group(1).title()) for m in CATEGORY_RE.finditer(text)]
    for i, (start, category) in enumerate(cat_starts):
        end = cat_starts[i + 1][0] if i + 1 < len(cat_starts) else len(text)
        section = text[start:end]
        q_matches = list(QUESTION_RE.finditer(section))
        for j, qm in enumerate(q_matches):
            q_end = q_matches[j + 1].start() if j + 1 < len(q_matches) else len(section)
            block = section[qm.start():q_end]
            questions.append({
                "id": qm.group(1),
                "category": category,
                "difficulty": qm.group(2),
                "question": _field(block, "Question"),
                "expected_answer": _field(block, "Expected Answer"),
                "wrong_answers": _wrong_answers(block),
            })
    return questions


def main() -> None:
    questions = parse(QNA_PATH.read_text(encoding="utf-8"))
    OUT_PATH.write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    cats = sorted({q["category"] for q in questions})
    print(f"Wrote {len(questions)} questions across {len(cats)} categories -> {OUT_PATH}")
    for c in cats:
        print(f"  {c}: {sum(1 for q in questions if q['category'] == c)}")


if __name__ == "__main__":
    main()
