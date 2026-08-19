# RAG the City — Official Rubric Anchors, Red-Flag Caps, and Eligibility Checklist

> **Source of truth: the published event page.** If this file and the live page disagree, the live page wins.
> Event page: https://the-open-accelerator.com/hackathon/upcoming/RAGtheCityHack/#judging
> Judges' guide: https://the-open-accelerator.com/hackathon/upcoming/RAGtheCityHack/judging/

Every project is scored out of **16** — four criteria, each scored **1–4** (whole integers only, no halves) and weighted equally. Three criteria are identical for both tracks. The fourth, **Track Excellence**, is judged against the team's own track's column only.

---

## Criterion 1 · RAG Quality & Grounding (/4) — both tracks

| Score | Anchor (verbatim) |
|-------|-------------------|
| **4** | Every answer grounded in specific data with clear citations. Retrieval is precise and comprehensive — and it says “I don't know” instead of guessing. |
| **3** | Most answers are accurate and cited. Retrieval reliably finds the relevant data. |
| **2** | Broadly right, but citations are thin or inconsistent. Retrieval misses obvious matches. |
| **1** | Answers are often wrong or hallucinated. No citations. |

## Criterion 2 · Track Excellence (/4) — track-specific

This is the one criterion that changes by track. **Judges score you against your own track's column only** — a terminal app is never marked down for looking like a terminal, and a beautiful app is never marked down for using a standard pipeline.

### Track A · The Engine — RAG Architecture & Technical Innovation

| Score | Anchor (verbatim) |
|-------|-------------------|
| **4** | Sophisticated architecture — hybrid search, multi-source orchestration, agentic retrieval, or a real evaluation pipeline. Measurably better than naive RAG, and they can show the numbers. |
| **3** | Proper chunking, vector store, and retrieval pipeline. Handles edge cases sensibly. |
| **2** | A working pipeline, but straight off the quickstart. Little beyond the tutorial. |
| **1** | Basic RAG — stuffs all the data into one prompt. No error handling. |

### Track B · The Experience — User Experience & Citizen Usability

| Score | Anchor (verbatim) |
|-------|-------------------|
| **4** | Intuitive and genuinely delightful. A non-technical resident would use this unprompted. Visual, conversational, accessible, and honest about its sources. |
| **3** | Clean interface, logical flow. A non-technical person could use it with some guidance. |
| **2** | Functional but plain. Needs explaining before someone could use it on their own. |
| **1** | Raw text output. Confusing, and requires technical knowledge to operate. |

## Criterion 3 · Innovation (/4) — both tracks

| Score | Anchor (verbatim) |
|-------|-------------------|
| **4** | A genuinely new approach — something the judges haven't seen before. |
| **3** | Novel combination of data sources, or a creative application of RAG techniques. |
| **2** | A familiar approach, applied competently to a new dataset. |
| **1** | Standard LangChain tutorial implementation. |

## Criterion 4 · Presentation (/4) — both tracks, **live-only**

Never scored from the repo. Included here so the demo-watch notes can point at the right anchors.

| Score | Anchor (verbatim) |
|-------|-------------------|
| **4** | Compelling story, live demo with real queries, explains WHY not just WHAT. The audience is engaged and it lands inside the time limit. |
| **3** | Good demo flow. Explains the problem and the solution clearly. |
| **2** | The demo works, but the story is thin or the pitch runs over time. |
| **1** | Unclear demo, technical jargon, hard to follow. |

---

## Scoring mechanics (from the judges' guide, #mechanics)

- Integers 1–4 on every criterion. No halves, no 2.5s, no "3+". Averaging across judges provides the granularity.
- Score immediately after each demo, before the next team — against the anchors, not against other teams.
- A team's Round 1 result is the average of its 2–3 judges' 16-point totals. Sheets are independent; don't converge.
- Tracks are lanes: never compare a Track A team to a Track B team, in either round.
- The final is re-scored from scratch on a fresh sheet. Round 1 scores do not carry over.
- Tie-break: judges confer, comparing the tied teams' **Track Excellence** scores first, then **RAG Quality**.
- A 3 is a good score; reserve 4s for work that genuinely hits the anchor's full description.
- Anchors describe what was actually seen, not what the team says the system could do.

## Red-flag score caps (from the judges' guide, #redflags)

None of these are new rules — each is already priced into the anchors or the published ground rules.

| Red flag | Effect |
|----------|--------|
| Fabricated answers, no citation — specifics that cannot be traced to a dataset when asked | **Caps RAG Quality at 1** (the 1 anchor verbatim: "wrong or hallucinated, no citations") |
| A canned recording passed off as live | **Caps Presentation** (the 4 anchor's "live demo with real queries" is out of reach) **and undermines RAG Quality** — score what was actually seen |
| Private or scraped data (no PII, no credentialed sources) | **Flag to organizers — eligibility call, not a scoring judgment** |
| Code visibly not written today (months-old commits, imported product) | **Flag to organizers — eligibility call, not a scoring judgment** |
| Refusing off-script queries / steering back to rehearsed prompts | **Caps RAG Quality at 2** — "precise and comprehensive" retrieval can't be credited if it couldn't be tested, and the 3 anchor's "reliably finds the relevant data" is equally unverifiable on rehearsed-only queries |
| Confident answers where honest ones were due | **Anchor guidance, RAG Quality** — graceful "I don't know" beats confident invention; abstention is a feature of the 4 anchor |

House rule from the guide: **score the rubric; escalate the rest.** The eligibility flags (private data, stale code) belong to the organizers — note what you saw, keep scoring, raise it at the tally. Never zero a team on your own authority.

## Eligibility checklist (event page #rules + judges' guide #eligibility)

Due before the **3:15 PM code freeze** on Saturday, August 22:

1. **Public repository** (GitHub, GitLab, etc.) with the working code.
2. **Recorded 2-minute demo video** showing the solution in action — how it works and why it answers a real question.
3. **Declared track** — A (Engine) or B (Experience). One track per team, locked at 10:45 AM, no switching after.
4. **List of the datasets used** — minimum two, from Analyze Boston (data.boston.gov) or the approved supplementary sources (data.mass.gov, data.gov, MBTA Developer Portal, Cambridge Open Data, MassGIS, Boston Public Library, Massachusetts Data Hub, Boston Public Health Data).

Standing ground rules behind them:

- **Fresh code only.** All code, design, and assets created during the hackathon; open-source libraries, public datasets, and APIs welcome — the core solution built on the day. Build window: **10:45 AM – 3:15 PM ET**.
- **Public data only.** No scraped private data, no PII, no credentialed sources.
- **Grounded answers.** A system that can't show its sources scores a 1 on RAG Quality. Citations are not a bonus — they're the point.
- **Live, honest demos.** Real queries in front of the judges; graceful "I don't know" beats confident invention.

Eligibility calls go to the organizers, not judges: note it, keep scoring the rubric, raise it at the tally, or email hackathon@the-open-accelerator.com.

## Prizes — for reference

Exactly two awards exist, decided in the final: the Track A winner ("**Best Engine**") and the Track B winner ("**Best Experience**"). No overall champion, no side prizes. Never invent other awards in a briefing.
