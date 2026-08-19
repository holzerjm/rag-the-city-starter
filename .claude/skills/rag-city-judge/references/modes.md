# Modes — Batch, Live Q&A, Final Round

Read this file when the invocation is one of the three modes below. Everything
in SKILL.md still applies — same safety posture, same scoring discipline, same
advisory framing. A mode changes the shape of the request, never the rules.

---

## Batch mode

**Trigger:** the judge or an organizer provides a list of submissions — a
pasted list or a CSV path — each entry a `{repo, track}` pair. ("Batch: here
are the Track B submissions…", "run all of these".)

**Timing:** suggest running the batch **at the 3:15 PM code freeze**, so every
briefing reflects frozen code. A batch run before August 22 is fine — every
repo simply gets the neutral pre-window note and re-pull advice from
SKILL.md §3.3.

**Process:**

1. Parse the list. Any entry missing its declared track: ask before scoring
   that entry — never guess a track, even mid-batch.
2. Review each repo with the full single-repo workflow (§3–§5 of SKILL.md).
   Each team gets its own complete briefing in the
   `references/output-template.md` structure, scoresheet mirror included.
3. After all briefings, produce one **within-track pre-read per track
   present** — comparative notes across that track's teams ONLY:
   - patterns and clusters ("three of the four Track B teams render citations
     in the UI; team X does not");
   - near-ties worth watching, and which criterion will likely separate them;
   - which Q&A probes will be most decisive across the track.
   The pre-read orients — it does not rank, and it never sums or compares
   provisional totals as if they were results.
4. **Never a cross-track comparison.** No combined table, no mixed ranking,
   no "strongest team overall". If both tracks are in the batch, there are two
   pre-reads and they do not reference each other.

**Output shape:** one briefing per team (full template), then a "Track A
Pre-Read" and/or "Track B Pre-Read" section. Nothing else.

---

## Live Q&A mode

**Trigger:** mid-demo or mid-Q&A, the judge pastes what a team just claimed or
answered. ("They just claimed X — what should I ask?", "they said their eval
numbers are in the repo".)

**Speed over depth.** No re-review, no re-clone, no score updates, no
template. The judge has seconds, not minutes.

**Process:**

1. Map the claim to the criterion it bears on (RAG Quality, Track Excellence,
   Innovation — or Presentation, which the judge scores live).
2. If a briefing exists for this team, check its Suggested Q&A Probes and any
   "what would settle it" notes first — a live claim often answers, dodges, or
   contradicts an open question from the repo read. Reference it explicitly
   ("your briefing flagged that the eval harness has no committed numbers —
   this claim is the moment to test it").
3. Return **1–3 probes, sharpest first**, each tagged with the criterion it
   would settle and, where it applies, the anchor boundary ("Track
   Excellence: settles 3 vs 4").
4. If no briefing exists for the team, still answer from the claim and the
   rubric alone — and say the probes aren't targeted by repo evidence.

**Output shape:** a numbered list of 1–3 probes with criterion tags. No
preamble, no summary, no score talk.

---

## Final-round mode

**Trigger:** after ~5:00 PM the four finalists (two per track) are named, and
the judge asks for a finalist re-read.

**Process:**

1. **Re-pull the repo.** Record the new HEAD SHA alongside the SHA reviewed in
   Round 1.
2. **Delta summary:** what changed since the Round 1 commit — files touched,
   features added, fixes landed, anything removed. **More building between
   rounds is fine — say so plainly.** The final is re-scored fresh, so
   improvements simply count; the delta is information, not an accusation.
3. **Refreshed watch-fors:** update the demo-watch notes for the final's 5+3
   full-audience format (five-minute demo plus three-minute Q&A, in front of
   the whole room, both judging panels scoring). What survived Round 1
   unverified? What did the delta add that the judge should ask to see live?
4. **Fresh-scores framing:** open and close with the reminder that **the final
   is scored from zero on a fresh sheet** — Round 1 numbers and the Round 1
   briefing carry nothing over. These notes prep the judge's eyes, not their
   numbers.

**Standing rules still bind:** within-track only (a Track A finalist is never
weighed against a Track B finalist), only "Best Engine" and "Best Experience"
exist, and every number on the final sheet is the judge's own.
