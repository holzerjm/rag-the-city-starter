# Track A Review Lens — "The Engine" (RAG Architecture & Technical Innovation)

Apply this lens ONLY when the team declared Track A. It maps the Track A anchor language in `rubric.md` to things you can actually find in a repo. The UI is irrelevant here — a terminal demo can win Track A, and the split-card note says a terminal app is never marked down for looking like a terminal.

## What each anchor level looks like in code

### Signals of a 4 — "Sophisticated architecture … measurably better than naive RAG, and they can show the numbers"

The 4 anchor lists its own evidence classes. Look for any of:

- **Hybrid search**: dense vector retrieval combined with sparse/keyword (BM25, SPLADE, `rank_bm25`, Elasticsearch/OpenSearch alongside a vector store, reciprocal rank fusion / `RRF` / rerankers like `cohere-rerank`, `bge-reranker`, `cross-encoder`).
- **Multi-source orchestration**: structured (CSV) and unstructured (PDF) sources answered in one query path; per-source retrievers merged by a router or fusion step; Docling/Unstructured for the PDF side next to Pandas for the CSV side.
- **Agentic retrieval**: the system decides which datasets to query per question — router chains, tool-calling loops, LangGraph graphs, function-calling with per-dataset tools, query decomposition/rewriting before retrieval.
- **A real evaluation pipeline WITH numbers**: RAGAS, TruLens, DeepEval, a custom eval harness, an A/B of chunking strategies — and actual recorded metrics (precision/recall/faithfulness, hit-rate tables, before/after comparisons) committed as results files, notebook outputs, or README tables. **No numbers, no 4** — "and they can show the numbers" is in the anchor. An eval script with no committed or demonstrable output only supports a 4 if they can run it live in Q&A.
- Bonus-point signals the event page names for Track A: entirely local models (Ollama/RamaLama/vLLM, no cloud keys), novel chunking strategy for tabular data, novel query strategy over large data, exclusively open-source tools, graph RAG / knowledge-graph construction (Neo4j, NetworkX, entity-relation extraction over property → violations → permits chains).

### Signals of a 3 — "Proper chunking, vector store, and retrieval pipeline. Handles edge cases sensibly."

- A deliberate chunking choice (row-level, section-level, or document-level with stated reasoning — commit messages and comments count), not just the framework default splitter with default sizes.
- A real vector store in the loop (ChromaDB, Qdrant, pgvector, Milvus) with a persisted or reproducible index build.
- Edge-case handling: empty-retrieval paths, "I don't know" fallbacks, top-k tuning, input validation, error handling around the LLM call, dataset-quirk handling (encoding, nulls, huge CSVs).

### Signals of a 2 — "A working pipeline, but straight off the quickstart. Little beyond the tutorial."

- Structure and naming that mirror the LangChain/LlamaIndex quickstart nearly verbatim; default splitter, default embeddings, default prompt; one dataset loaded the way the tutorial loads text files even though the data is a 100K-row CSV.
- Works, but nothing was tuned, measured, or handled beyond the happy path.

### Signals of a 1 — "Basic RAG — stuffs all the data into one prompt. No error handling."

- No retrieval step at all: the whole CSV (or its head) is read and pasted into the prompt/context; no vector store, or one that is initialized but never queried on the answer path.
- Bare `llm(prompt)` calls with no try/except, no fallback, no abstention path.

## Where these things typically live

- Retrieval logic: `retriever*.py`, `rag/`, `pipeline/`, `search/`, `src/`, chain/graph definitions.
- Eval: `eval/`, `evals/`, `tests/`, `benchmarks/`, `ragas*`, notebook files, `results/*.json|csv|md`.
- Dependencies tell the architecture story fast: `requirements.txt` / `pyproject.toml` / `package.json`. `rank_bm25`, a reranker, `ragas`, `langgraph`, `neo4j` each imply a specific claim to verify in code — a dependency alone proves nothing; confirm it is imported and on the answer path.
- Ingestion/chunking: `ingest*.py`, `load*.py`, `chunk*.py`, `etl/`, `data/` scripts; look at what splitter and what parameters.
- Citations: wherever the answer is assembled — is source metadata carried from retrieval into the final output?

## Q&A probe patterns (adapt to THIS repo's weak spots; the guide's arsenal has the canonical four)

1. "Your `requirements.txt` lists {rank_bm25 / ragas / langgraph} but I couldn't find it on the answer path — where does it actually run?" (dependency vs. reality; separates a 4 claim from a 2)
2. "What here measurably beats naive RAG — can you show me the numbers?" (the anchor's own bar; verbatim from the guide's arsenal)
3. "Walk me through one query end to end — what was retrieved, and why those chunks?" (designed pipeline (3+) vs. quickstart pasted together (2))
4. "How did you chunk the {their largest CSV} so retrieval actually works?" (tabular chunking is the day's hardest Track A problem)
5. "What breaks first if I point this at ten more city datasets?" (the 3 anchor's "handles edge cases sensibly" — teams that know their failure modes have earned it)
