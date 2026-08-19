# RAG the City — starter repo

Starter kit for **RAG the City**, The Open Accelerator's one-day RAG hackathon over
Boston's open data (Saturday, August 22, 2026 — Fort Point, Boston). The premise:
**feel naive RAG break before you build something better.** Lab 0 hands you a tiny
fictional city (Millbrook) with ten documents engineered to make a vanilla
chunk-embed-retrieve pipeline conflate people, botch dates, pick one of three
contradictory numbers, and invent a dead couple's backstory — then maps every one of
those failures onto the real Analyze Boston datasets you'll build on Saturday. You
watch the baseline fail in an inspectable, 30-minute tour, and then you spend hack
day killing the failure mode you choose.

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

## Lab 0 — feel naive RAG break (~30 min)

`make lab0` runs a 5-stop guided tour. Each stop asks the naive baseline a real
Millbrook question, shows you the retrieved chunks and the (wrong) answer, then
shows the **Boston twin** — the same failure waiting inside Saturday's data.

| # | Millbrook question | Naive-RAG failure | Boston twin (Saturday's data) | Rubric tie |
|---|---|---|---|---|
| 1 | "What is the population of Millbrook?" then "Dr. Okafor treated a patient — what condition, what relationship?" | warm-up works; then conflates TWO different Dr. Okafors | "Show 311 complaints on Washington St" — Washington St exists in Roslindale, Dorchester, downtown… similarity ≠ identity | RAG Quality /4 |
| 2 | "How long has Ahmed Al-Rashid run his bakery?" | answer (30 yrs) is in NO chunk — needs date arithmetic | "Is crime in Roxbury getting better or worse over the last 3 years?" | Track A: Temporal RAG |
| 3 | "What is Bridge 7's load capacity?" | corpus holds 40 (original), 25 (current), 15 (restriction) tons — baseline confidently returns ONE | Operating Budget CSV vs Budget-narrative PDF give different numbers for one line item | RAG Quality + Multi-Source |
| 4 | "What happened to Isabella Romano's parents?" | invents a backstory; correct = grounded abstention ("parents deceased", nothing more) | "Why was this restaurant's license suspended?" — inspections data has violation codes, not narrative reasons; right answer is "the data doesn't say" | RAG Quality /4 anchor: "says 'I don't know' instead of guessing" |
| 5 | "Degrees of separation: Ahmed Al-Rashid → Dr. Kwame Okafor?" | no chunk contains the path — needs entity graph | "Property owner → violations → permits → neighborhood patterns" | Track A: Graph/Agentic |

Then close the loop:

```bash
make lab0-ask Q="What is the population of Millbrook?"   # ask anything yourself
make lab0-score                                          # judge all 22 questions
```

`make lab0-score` runs the full 22-question eval through an LLM judge and prints
your band per the challenge rubric — EXCELLENT (90–100) / GOOD (75–89) /
FAIR (60–74) / POOR (<60), with fabrication flagged as a CRITICAL FAILURE.
Your goal Saturday is EXCELLENT — pick which failure you'll kill first.

## Level 2: The Fort Point Files (`lab0_boston/`)

The same failure modes rebuilt on Boston-shaped documents. The spine is real
geography — the **Northern Avenue Bridge** over the Fort Point Channel, closed to
vehicles since 1997 and fenced off from everyone since December 2014, a short walk
from the venue — wrapped in a fictional 2026 reopening study. Eleven documents are
shaped like Saturday's real data: a 311 export with CSV-ish rows, a food-inspection
report, a budget CSV that disagrees with its own budget narrative on one line item,
council committee minutes, a neighborhood weekly, a trilingual meeting transcript
(Spanish / Haitian Creole / Chinese — Boston's actual 311 languages), a property &
permit record, an engineering assessment, bios, and a diary. The 24 eval questions
keep Millbrook's eight categories and add a ninth Millbrook lacks —
**Aggregation & Counting** over the 311 rows, the tabular-chunking failure.

> The Fort Point Files is a work of fiction created for RAG education. Characters, businesses, documents, and all numbers are invented; Boston place names are used fictitiously. Inspired by the Millbrook City RAG Challenge by William Caban (used with permission).

```bash
make lab0-boston                                  # split the corpus + build index + guided intro
make lab0-boston-ask Q="How long has Yolanda Peña been running Gull & Anchor Bakery?"
make lab0-boston-score                            # judge all 24 questions
```

See [`lab0_boston/README.md`](lab0_boston/README.md) for the scenario and question
breakdown. The engine is the Millbrook baseline pointed at the Boston corpus via
`--corpus-dir` / `--questions` / `--collection`; Millbrook defaults are untouched.

## Repo map

```
lab0_millbrook/        Lab 0: the Millbrook corpus and the naive baseline
  corpus/millbrook_full.md      vendored corpus (see attribution below)
  corpus/docs/                  the corpus split into 10 per-document files
  split_corpus.py               splitter (run automatically on first index)
  naive_rag.py                  the deliberately naive baseline + CLI
  tour.py                       the 5-stop guided tour        (make lab0)
  judge.py                      LLM judge over all 22 questions (make lab0-score)
  questions.json                22 eval questions, 8 categories (generated)
  boston_parallels.json         the 5-stop Millbrook→Boston mapping (data)
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
