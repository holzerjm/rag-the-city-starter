# RAG the City — starter repo
# Quickstart: make setup && ollama pull granite3.1-dense:8b && make data && make lab0

.DEFAULT_GOAL := help
VENV   := .venv
PY     := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip

# Explicit per-edition flags — behavior never depends on Python defaults.
FORTPOINT_FLAGS := --corpus-dir lab0_boston/corpus/docs --collection fortpoint_naive
MILLBROOK_FLAGS := --corpus-dir lab0_millbrook/corpus/docs --collection millbrook_naive

.PHONY: help setup data lab0 lab0-ask lab0-score lab0-millbrook lab0-millbrook-ask lab0-millbrook-score track-a track-b

help: ## Show every target and what it does
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-21s %s\n", $$1, $$2}'

setup: ## Create .venv and install the slim base requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

data: ## Download the two lab datasets (311 + food inspections) from Analyze Boston via CKAN
	$(PY) boston/download.py

lab0: ## Run Lab 0 — The Fort Point Files: split the corpus + the 6-stop guided tour
	$(PY) -m lab0_millbrook.split_corpus --input lab0_boston/corpus/fortpoint_full.md --outdir lab0_boston/corpus/docs
	$(PY) -m lab0_millbrook.tour --stops lab0_boston/tour_stops.json $(FORTPOINT_FLAGS)

lab0-ask: ## Ask the naive baseline one Fort Point question: make lab0-ask Q="..."
	$(PY) -m lab0_millbrook.naive_rag $(FORTPOINT_FLAGS) "$(Q)"

lab0-score: ## Judge all 24 Fort Point questions (9 categories) with an LLM and print your scoring band
	$(PY) -m lab0_millbrook.judge $(FORTPOINT_FLAGS) --questions lab0_boston/questions.json

lab0-millbrook: ## The original — William Caban's Millbrook City RAG Challenge: 5-stop tour
	$(PY) -m lab0_millbrook.split_corpus --input lab0_millbrook/corpus/millbrook_full.md --outdir lab0_millbrook/corpus/docs
	$(PY) -m lab0_millbrook.tour --stops lab0_millbrook/boston_parallels.json $(MILLBROOK_FLAGS)

lab0-millbrook-ask: ## Ask the baseline one Millbrook question: make lab0-millbrook-ask Q="..."
	$(PY) -m lab0_millbrook.naive_rag $(MILLBROOK_FLAGS) "$(Q)"

lab0-millbrook-score: ## Judge all 22 Millbrook questions with an LLM and print your scoring band
	$(PY) -m lab0_millbrook.judge $(MILLBROOK_FLAGS) --questions lab0_millbrook/questions.json

track-a: ## Track A demo — dense-only vs BM25+dense hybrid retrieval, side by side
	$(PY) track_a_engine/hybrid_search.py

track-b: ## Track B demo — Streamlit chat UI with citation cards over the Boston data
	$(VENV)/bin/streamlit run track_b_experience/app_streamlit.py
