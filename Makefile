# RAG the City — starter repo
# Quickstart: make setup && ollama pull granite3.1-dense:8b && make data && make lab0

.DEFAULT_GOAL := help
VENV   := .venv
PY     := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip

.PHONY: help setup data lab0 lab0-ask lab0-score lab0-boston lab0-boston-ask lab0-boston-score track-a track-b

help: ## Show every target and what it does
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

setup: ## Create .venv and install the slim base requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

data: ## Download the two lab datasets (311 + food inspections) from Analyze Boston via CKAN
	$(PY) boston/download.py

lab0: ## Run Lab 0 — the 5-stop guided tour where naive RAG breaks in front of you
	$(PY) -m lab0_millbrook.tour

lab0-ask: ## Ask the naive baseline one question: make lab0-ask Q="What is the population of Millbrook?"
	$(PY) -m lab0_millbrook.naive_rag "$(Q)"

lab0-score: ## Judge all 22 Millbrook questions with an LLM and print your scoring band
	$(PY) -m lab0_millbrook.judge

lab0-boston: ## Level 2 — split The Fort Point Files corpus, build its index, guided intro
	$(PY) -m lab0_boston.intro

lab0-boston-ask: ## Ask the baseline one Fort Point question: make lab0-boston-ask Q="..."
	$(PY) -m lab0_millbrook.naive_rag --corpus-dir lab0_boston/corpus/docs --collection fortpoint_naive "$(Q)"

lab0-boston-score: ## Judge all 24 Fort Point questions with an LLM and print your scoring band
	$(PY) -m lab0_millbrook.judge --corpus-dir lab0_boston/corpus/docs --questions lab0_boston/questions.json --collection fortpoint_naive

track-a: ## Track A demo — dense-only vs BM25+dense hybrid retrieval, side by side
	$(PY) track_a_engine/hybrid_search.py

track-b: ## Track B demo — Streamlit chat UI with citation cards over the Boston data
	$(VENV)/bin/streamlit run track_b_experience/app_streamlit.py
