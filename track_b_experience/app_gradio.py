"""Track B alternative: the same grounded chat in minimal Gradio.

Gradio is not in the base requirements — install it if you prefer it:
    .venv/bin/pip install gradio

Run:  .venv/bin/python track_b_experience/app_gradio.py
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from boston import query as boston_query  # noqa: E402

try:
    import gradio as gr
except ImportError:
    print("[!] gradio is not installed. Fix: .venv/bin/pip install gradio")
    sys.exit(1)


def respond(message: str, history: list) -> str:
    chunks = boston_query.retrieve(message)
    answer = boston_query.answer(message, chunks)
    if answer is None:
        answer = "(model offline — start Ollama: `ollama serve`)"
    cites = "\n".join(f"- {c['dataset']} — rows {c['rows']}" for c in chunks)
    return f"{answer}\n\n**Citations**\n{cites}"


demo = gr.ChatInterface(
    respond,
    title="RAG the City — ask Boston's open data",
    description="Grounded answers with citations from Analyze Boston datasets.",
)

if __name__ == "__main__":
    demo.launch()
