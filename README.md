# RAG the City — starter repo

Starter kit for **RAG the City**, The Open Accelerator's one-day RAG hackathon over
Boston's open data (Saturday, August 22, 2026 — Fort Point, Boston). The premise:
**feel naive RAG break before you build something better.** Lab 0 hands you **The
Fort Point Files** — a fictional 2026 reopening study of the very real Northern
Avenue Bridge, a short walk from the venue — eleven documents engineered to make a
vanilla chunk-embed-retrieve pipeline merge two Peñas into one person, botch date
arithmetic, pick one of two contradictory budget figures, invent a cause the
inspection report never states, and miscount a CSV. Every document is shaped like
the real Analyze Boston data you'll build on Saturday. You watch the baseline fail
in an inspectable six-stop tour, and then you spend hack day killing the failure
mode you choose.

## Quickstart

```bash
git clone https://github.com/holzerjm/rag-the-city-starter.git
cd rag-the-city-starter
make setup
ollama pull granite3.1-dense:8b
make data
make lab0
```

`granite3.1-dense:8b` is the default model everywhere; any Ollama model tag works
(set `OLLAMA_MODEL=<tag>`). Run `make` alone to list every target.

## Lab 0 — The Fort Point Files (~30 min)

`make lab0` splits the corpus and runs the 6-stop guided tour. Each stop asks the
naive baseline a real Fort Point question, shows you the retrieved chunks and the
(wrong) answer, then shows **Saturday's data shape** — where the identical failure
waits inside the real Analyze Boston data.

> The Fort Point Files is a work of fiction created for RAG education. Characters, businesses, documents, and all numbers are invented; Boston place names are used fictitiously. Inspired by the Millbrook City RAG Challenge by William Caban (used with permission).

| # | Fort Point question | Naive-RAG failure | Saturday's data shape | Rubric tie |
|---|---|---|---|---|
| 1 | "When did the bridge close to all users?" then "Which Peña spoke at the May 19 committee meeting?" | warm-up works; then merges Yolanda (the bakery owner) and Camila (her daughter, the 'C. Peña' in the minutes) — similarity ≠ identity | 311 export & permit records repeat names and street names — same string, different people and places | RAG Quality /4 |
| 2 | "How long had the bridge been closed to all users when the 2026 assessment was submitted?" | the answer (~11.5 years) is in NO chunk — needs date arithmetic across documents, and 1997 is the wrong anchor | trends over the crime & 311 CSVs are computed across dates, never stored in any row | Track A: Temporal RAG |
| 3 | "How much does FY2027 commit to design and engineering?" | the budget CSV says $4,200,000, the narrative says $3.65M — the baseline confidently returns ONE | the real Operating Budget ships as a CSV and a narrative that can disagree on a line item | RAG Quality + Multi-Source |
| 4 | "What caused Gull & Anchor's walk-in cooler failure?" | invents a cause; the inspection report holds violation codes only — correct = "the data doesn't say" | Food Establishment Inspections: codes and dispositions, no narrative reasons | RAG Quality /4 anchor: says 'I don't know' instead of guessing |
| 5 | "Degrees of separation: Wilner Joseph → Deirdre Fitzgerald?" | no chunk contains the path — hops span transcript, minutes, and property record; needs an entity graph | property owner → violations → permits → neighborhood patterns across CSVs | Track A: Graph / Agentic RAG |
| 6 | "How many 311 requests list a location at the bridge?" | no chunk contains a count — the answer (9 of 28 rows) exists only by iterating the table | "how many?" over the real 311 CSV — aggregation needs structured, row-aware retrieval | RAG Quality /4 — a confident wrong count is a fabrication |

Then close the loop:

```bash
make lab0-ask Q="Which Peña gave public comment at the May 19 committee meeting?"   # ask anything yourself
make lab0-score                                   # judge all 24 questions
```

`make lab0-score` runs the full 24-question eval — nine failure categories — through
an LLM judge and prints your band per the challenge rubric — EXCELLENT (90–100) /
GOOD (75–89) / FAIR (60–74) / POOR (<60), with fabrication flagged as a CRITICAL
FAILURE. Your goal Saturday is EXCELLENT — pick which failure you'll kill first.

See [`lab0_boston/README.md`](lab0_boston/README.md) for the scenario and question
breakdown.

## Origin: the Millbrook City RAG Challenge

The Fort Point Files' failure-mode design comes straight from the
[Millbrook City RAG Challenge](https://gist.github.com/williamcaban/8764f13aaa5c4b0768033671483f6c0f)
by **William Caban** — a fictive city (Millbrook, pop. 47,832, story spine: the
failing Bridge 7) whose ten documents and 22 eval questions calibrated every trap
above. The Boston edition rebuilds those traps on Boston-shaped documents and adds
a ninth category Millbrook lacks — **Aggregation & Counting** (24 questions vs 22).
The original ships in this repo uncut, and its five-stop tour maps each Millbrook
failure to its Boston twin:

```bash
make lab0-millbrook                               # the original 5-stop guided tour
make lab0-millbrook-ask Q="What is the population of Millbrook?"
make lab0-millbrook-score                         # judge all 22 Millbrook questions
```

Millbrook City RAG Challenge © William Caban — used with permission. All content is
fictional, AI-generated synthetic data.

## Repo map

```
lab0_boston/           Lab 0: The Fort Point Files — corpus, questions, tour stops
  corpus/fortpoint_full.md      the 11-document corpus (fiction; see disclaimer)
  corpus/docs/                  the corpus split into 11 per-document files
  questions.json                24 eval questions, 9 categories
  tour_stops.json               the 6-stop guided tour data      (make lab0)
lab0_millbrook/        The original Millbrook challenge + the shared naive engine
  corpus/millbrook_full.md      vendored corpus (see attribution below)
  corpus/docs/                  the corpus split into 10 per-document files
  split_corpus.py               splitter for both corpora
  naive_rag.py                  the deliberately naive baseline + CLI
  tour.py                       guided-tour runner   (make lab0 / make lab0-millbrook)
  judge.py                      LLM judge over a question set (make lab0-score)
  questions.json                22 eval questions, 8 categories (generated)
  boston_parallels.json         the original 5-stop Millbrook→Boston mapping (data)
  tools/parse_qna.py            regenerates questions.json from the QnA file
boston/                Shared data plumbing for hack day
  download.py                   CKAN-resolved dataset downloads (make data)
  ingest.py                     chunk+embed CSVs into chroma (--strategy row|group)
  query.py                      grounded-answer CLI with citations
track_a_engine/        Track A "Best Engine" starting points
track_b_experience/    Track B "Best Experience" starting points
```

## Track A — Best Engine (`track_a_engine/`)

For teams judged on RAG architecture. Start from:

- `hybrid_search.py` (`make track-a`) — dense-only vs BM25+dense fusion, side by
  side, so you can see exactly where each retriever wins.
- `multi_source.py` — skeleton: one question answered from a budget CSV **and** a
  budget PDF (Docling), reconciling the disagreement. Clearly marked TODOs.
- `eval_ragas.py` — RAGAS harness wired to the Lab 0 `questions.json` format.

Heavy deps live separately: `.venv/bin/pip install -r requirements-track-a.txt`
(adds `docling`, `ragas`).

## Track B — Best Experience (`track_b_experience/`)

For teams judged on citizen usability. Standard pipeline is fine — per the event
page, "LangChain + ChromaDB is completely fine." Start from:

- `app_streamlit.py` (`make track-b`) — chat UI with citation cards under every
  answer and a first-class "I don't know" honesty path.
- `app_gradio.py` — the same idea, minimal Gradio.
- `components/map_answer.py` — folium heatmap from a 311 dataframe, embeddable in
  Streamlit. Citizens think in places, not row ids.

## For judges

Judging materials live separately so team clones stay lean: the advisory
AI co-judge skill is at [holzerjm/rag-city-judge](https://github.com/holzerjm/rag-city-judge),
and the full Judges’ Guide is at
<https://the-open-accelerator.com/hackathon/upcoming/RAGtheCityHack/judging/>.

## Datasets (Analyze Boston)

`make data` downloads the two lab defaults — 311 (current-year CSV) and Food
Establishment Inspections — resolving resource URLs at runtime via the CKAN API.
Your Saturday submission needs **2+ datasets** from [Analyze Boston](https://data.boston.gov):

- [311 Service Requests](https://data.boston.gov/dataset/311-service-requests)
- [Food Establishment Inspections](https://data.boston.gov/dataset/food-establishment-inspections)
- [Crime Incident Reports](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system)
- [Property Assessment](https://data.boston.gov/dataset/property-assessment)
- [Operating Budget](https://data.boston.gov/dataset/operating-budget)
- [Approved Building Permits](https://data.boston.gov/dataset/approved-building-permits)
- [Employee Earnings Report](https://data.boston.gov/dataset/employee-earnings-report)
- [Trees](https://data.boston.gov/dataset/bprd-trees)
- [Open Space](https://data.boston.gov/dataset/open-space)
- [Vision Zero Crash Records](https://data.boston.gov/dataset/vision-zero-crash-records)

## License and attribution

The **code** in this repository is licensed under the Apache License 2.0 — see
[LICENSE](LICENSE). Copyright 2026 The Open Accelerator contributors.

The **Millbrook corpus** (`lab0_millbrook/corpus/`) is **not** covered by the code
license: Millbrook City RAG Challenge © William Caban — used with permission. All
content is fictional, AI-generated synthetic data.
Source: <https://gist.github.com/williamcaban/8764f13aaa5c4b0768033671483f6c0f>

## Event links

- Event page: <https://the-open-accelerator.com/hackathon/upcoming/RAGtheCityHack/>
- Register (Luma): <https://luma.com/toa-raghack>
- Discord: <https://red.ht/toa-discord>
- Team matching: <https://red.ht/toa-team-matching>
- Contact: <hackathon@the-open-accelerator.com>
