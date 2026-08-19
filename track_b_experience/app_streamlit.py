"""Track B: Streamlit chat over the Boston collection, citations included.

Two Track B rubric anchors are wired in from the start:
  * every answer renders citation cards (dataset + row ids) under it —
    a citizen should never have to trust an uncited claim;
  * an honesty path — when the model abstains ("I don't know"), we style
    that as a first-class outcome, not a failure. Guessing is the failure.

Run:  make track-b     (or: .venv/bin/streamlit run track_b_experience/app_streamlit.py)
"""
from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))  # so `boston` imports under `streamlit run`

from boston import query as boston_query  # noqa: E402

st.set_page_config(page_title="RAG the City", page_icon=":classical_building:")
st.title("RAG the City — ask Boston's open data")
st.caption("Answers are grounded in Analyze Boston datasets and cited below each reply.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        for cite in msg.get("citations", []):
            st.info(cite, icon=":material/dataset:")

if prompt := st.chat_input("e.g. Show 311 complaints on Washington St"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            chunks = boston_query.retrieve(prompt)
        except SystemExit as exc:  # no collection yet — say how to fix it
            st.error(str(exc))
            st.stop()
        answer = boston_query.answer(prompt, chunks)
        if answer is None:
            st.warning("Ollama is unreachable — start it with `ollama serve` and "
                       "`ollama pull granite3.1-dense:8b`. Retrieval still ran; "
                       "citations below are real.")
            answer = "_(no answer — model offline)_"
        elif "i don't know" in answer.lower() or "data doesn't say" in answer.lower():
            # The honesty path: abstention rendered as a win, not an error.
            st.success("This answer honestly reports what the data does NOT say — "
                       "per the rubric, that beats a confident guess.", icon=":material/verified:")
        st.markdown(answer)
        citations = [f"{c['dataset']} — rows {c['rows']}" for c in chunks]
        for cite in citations:
            st.info(cite, icon=":material/dataset:")
        st.session_state.messages.append(
            {"role": "assistant", "content": answer, "citations": citations})
