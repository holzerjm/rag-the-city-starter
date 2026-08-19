# Level 2: The Fort Point Files

The Millbrook failure modes, rebuilt on Boston-shaped documents. The story spine is
real geography: the **Northern Avenue Bridge** over the Fort Point Channel — a 1908
swing bridge, closed to vehicles in 1997 and fenced off from everyone since December
2014, a short walk from the hackathon venue — wrapped in a **fictional 2026 reopening
study**. The eleven documents are shaped like Saturday's real Analyze Boston data: a
311 export with CSV-ish rows, a food-establishment inspection report, an operating
budget CSV that disagrees with its own budget narrative on one line item, council
committee minutes, a neighborhood weekly, a trilingual community-meeting transcript
(Spanish / Haitian Creole / Chinese — Boston's actual 311 languages), a property &
permit record, an engineering assessment, bios, and a diary.

> The Fort Point Files is a work of fiction created for RAG education. Characters, businesses, documents, and all numbers are invented; Boston place names are used fictitiously. Inspired by the Millbrook City RAG Challenge by William Caban (used with permission).

## Run it

```bash
make lab0-boston                                  # split the corpus, build the index, guided intro
make lab0-boston-ask Q="How long has Yolanda Peña been running Gull & Anchor Bakery?"
make lab0-boston-score                            # judge all 24 questions, print your band
```

The engine is the same deliberately naive baseline as Lab 0 (`lab0_millbrook/`),
pointed at this corpus via `--corpus-dir` / `--questions` / `--collection` flags —
Millbrook behavior is unchanged when the flags are omitted.

## What's different from Millbrook

`questions.json` holds **24 questions**: the eight Millbrook categories
(Ambiguous References ×3, Temporal Complexity ×3, Contradictory Information ×3,
Missing Context Scenarios ×3, Domain Confusion ×3, Relationship Complexity ×3,
Multilingual And Cultural Complexity ×2, Technical Domain Integration ×2) **plus a
ninth category Millbrook lacks — Aggregation & Counting ×2** — counting over the
311 export's rows, where a fixed-size chunker slices the table in half. That is the
tabular-chunking failure you'll meet the moment you index Saturday's real 311 CSV.

Every failure is real in the corpus: the budget contradiction's two numbers are both
present ($4,200,000 in the CSV vs $3.65 million in the narrative), the
missing-context questions are genuinely unanswerable, the date arithmetic is
consistent and never pre-computed, the two Fitzgeralds and the two Peñas are
genuinely confusable, the multilingual spans are genuinely in those languages, and
the aggregation answers are exactly computable from the 28 rows.
