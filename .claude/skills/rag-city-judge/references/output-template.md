# Judge Briefing — Output Template

Produce the briefing in exactly this structure. Fill every section; where evidence is missing, write "Cannot verify from repo" rather than guessing.

---

```markdown
# Judge Briefing — {Team name or repo name}

| | |
|---|---|
| **Declared track** | {A — The Engine / B — The Experience} |
| **Repo** | {URL or local path} |
| **Commit reviewed** | {short SHA + commit date, or "working tree (no git history)"} |
| **Reviewed** | {date} · Static review only — code was read, not executed |

## Eligibility Pre-Check

> Advisory only. Eligibility calls belong to the organizers — never treat a flag here as a disqualification. Note it, keep scoring, raise it at the tally.

| Item | Status | Evidence |
|------|--------|----------|
| Public repository with working code | Pass / Flag / Cannot verify | {…} |
| 2-minute demo video submitted | Pass / Flag / Cannot verify | {usually lives outside the repo — check the submission form} |
| Declared track (locked 10:45 AM) | Pass / Flag / Cannot verify | {stated where?} |
| 2+ datasets from Analyze Boston or approved supplementary sources | Pass / Flag / Cannot verify | {which datasets, found where} |
| Fresh-code signal (commits within Aug 22, 10:45 AM–3:15 PM ET build window) | Pass / Flag / Cannot verify | {commit-time summary; note pre-event scaffolding or wholesale imports} |

{If anything is Flag or Cannot verify: one line per item on what to raise with organizers at the tally.}

## Provisional Scores — PROVISIONAL & ADVISORY

> Scored from the repo only, against the verbatim anchors. Presentation is not scored here — it is live-only. Your own 1–4 integers on the printed scoresheet govern.

### RAG Quality & Grounding — {1–4}/4
- **Anchor matched:** "{quote the anchor verbatim}"
- **Evidence:** {file:line references}
- **What would move it +1 / −1:** {…}

### Track Excellence ({Track A: RAG Architecture & Technical Innovation / Track B: User Experience & Citizen Usability}) — {1–4}/4
- **Anchor matched:** "{quote the anchor verbatim — from the declared track's column only}"
- **Evidence:** {file:line references}
- **What would move it +1 / −1:** {…}

### Innovation — {1–4}/4
- **Anchor matched:** "{quote the anchor verbatim}"
- **Evidence:** {file:line references}
- **What would move it +1 / −1:** {…}

**Provisional subtotal: {n}/12** (Presentation /4 is scored live, bringing the sheet to /16)

{If the repo alone could not distinguish two anchor levels on any criterion, say so here and point to the Q&A probe that would settle it live.}

## Presentation — Watch-For Notes (not scored from the repo)

- {2–4 bullets: what to watch for in THIS team's live demo — e.g., "the README promises a live map; confirm the demo shows it with a real query", "eval numbers are claimed but not committed; ask to see them run", time-limit risks, canned-demo risk}

## Suggested Q&A Probes

{3–5 questions targeting THIS repo's specific weak spots or unverifiable claims. Tag each with the criterion it would settle, e.g. "(Track Excellence: settles 3 vs 4)".}

1. {…}
2. {…}
3. {…}

## Red-Flag Scan

{One line per red flag from rubric.md: Clear / Flagged, with evidence. If flagged, restate the cap (e.g., "caps RAG Quality at 1") or "escalate to organizers" for eligibility flags.}

## Strengths & Critical Improvement

**Two strengths:**
1. {…}
2. {…}

**One critical improvement:** {the single change that would most raise their score, tied to an anchor}

## One-Line Verdict

{One sentence: where this submission sits and what will decide it live.}

## Scoresheet Mirror

> **Transfer aid — your call on every number.** This block mirrors the printed
> scoresheet's order. The `*` marks this briefing's provisional suggestion on
> the three repo-scorable criteria; the checkboxes, Presentation, TOTAL, and
> the verdict line stay blank for you.

    TEAM: {team}                          JUDGE: ______________________
    ROUND: {1 / Final}                    TRACK: {A — Engine / B — Experience}

    RAG Quality & Grounding               [ ] 1   [ ] 2   [ ] 3   [ ] 4
    Track Excellence ({Track A: RAG Architecture & Technical Innovation / Track B: User Experience & Citizen Usability})
                                          [ ] 1   [ ] 2   [ ] 3   [ ] 4
    Innovation                            [ ] 1   [ ] 2   [ ] 3   [ ] 4
    Presentation — score live             [ ] 1   [ ] 2   [ ] 3   [ ] 4

    TOTAL: ____ /16

    One-line verdict: _______________________________________________________

{When filling this block in, append `*` to the provisionally suggested integer
on each of the three repo-scorable rows — e.g. `[ ] 3*` — and nowhere else.
Presentation keeps its "— score live" label and gets no mark; TOTAL and the
verdict line are always left blank.}

---
*This briefing is decision support, produced by static repo review only. It is advisory: your own 1–4 integer scores on the printed scoresheet govern, Round 1 and the final are scored fresh and independently, and Track A and Track B teams are never compared. Scoresheet: https://the-open-accelerator.com/hackathon/upcoming/RAGtheCityHack/judging/scoresheet/*
```
