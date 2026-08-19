# rag-city-judge

A Claude Code skill that acts as an advisory AI co-judge for TOA's **RAG the
City** hackathon. Give it a team's repo (URL or local path) and their declared
track (A — Engine, or B — Experience) and it produces a Judge Briefing:
eligibility pre-check, provisional 1–4 scores against the official rubric
anchors with file-level evidence, demo-watch notes, tailored Q&A probes, a
red-flag scan, and a scoresheet-mirror transfer aid. It works on any base —
official starter fork or a team's own repo — and does static review only: it
never runs the team's code. The briefing is advisory: Presentation is scored
live only, and the judge's own integers on the printed scoresheet always
govern.

## Setup — zero install

The skill lives at `.claude/skills/rag-city-judge/` in the starter repo, so
cloning the repo and running Claude Code inside it is the whole setup:

    git clone https://github.com/holzerjm/rag-the-city-starter.git
    cd rag-the-city-starter
    claude

(Alternatively, copy this directory into any project's `.claude/skills/`, or
into `~/.claude/skills/` to have it available everywhere.)

## Example prompts

Single review:

- "Judge this Track A submission: <repo URL>"
- "Score this submission — Track B: <repo URL>"
- "Prep me for this demo: <repo URL>, Track A"

Batch (one briefing per team + a within-track pre-read per track — best run
at the 3:15 PM code freeze):

- "Batch: here are the Track B submissions: <repo1>, <repo2>, <repo3>"
- "Judge these repos: <CSV path with repo,track columns>"

Live Q&A (mid-demo — fast probes, no re-review):

- "They just claimed their hybrid search beats naive RAG — what should I ask?"
- "Team said the eval numbers are in the repo. Probe?"

Final round (post-5:00 PM — re-pull, delta since Round 1, fresh-score prep):

- "Re-read <repo URL> for the final round — what changed since this
  afternoon?"
