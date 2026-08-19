# Track B Review Lens — "The Experience" (User Experience & Citizen Usability)

Apply this lens ONLY when the team declared Track B. It maps the Track B anchor language in `rubric.md` to things you can find in a repo. Remember the event page's own words: "The RAG pipeline can use standard approaches — LangChain + ChromaDB is completely fine." **Never mark a Track B team down for a standard pipeline** — the split-card note says a beautiful app is never marked down for using a standard pipeline. Pipeline plainness is priced into their track choice; what you are grading is the experience.

A caveat before scoring anything: UX is ultimately judged live, hands-on ("Hand me the phone" is the guide's strongest probe). The repo shows you what the team *built toward*; the live demo shows whether it lands. Score conservatively from code and route uncertainty into demo-watch notes and probes.

## What each anchor level looks like in code

### Signals of a 4 — "Intuitive and genuinely delightful … Visual, conversational, accessible, and honest about its sources"

The anchor names four qualities; look for each:

- **Visual**: charts, maps, or infographics generated from query results — Plotly/Folium/Leaflet/Mapbox/deck.gl/Recharts in the render path, a heatmap for 311 clusters, not just markdown text.
- **Conversational**: multi-turn state — chat history carried into follow-ups, clarifying questions, "tell me more" affordances; not a one-shot search box.
- **Accessible**: `aria-*` attributes, semantic landmarks, `alt` text, visible focus/keyboard handling, contrast-conscious tokens, reduced-motion queries, large-text options, voice input; an accessibility audit doc is a named bonus.
- **Honest about its sources**: citations rendered IN the interface — dataset name, link back to data.boston.gov, data freshness ("Last updated: …"), confidence display. The event page's Trust & Transparency card is the template. Sources living only in a JSON log or terminal print is not "honest about its sources" at the 4 level.
- An **abstention path in the UI**: what does the user see when the data can't answer? A designed "I don't know / here's what I'd need" state supports both this criterion's honesty language and RAG Quality.
- Other 4-level signals the event page names: progressive disclosure (simple answer first, details on demand), multilingual (auto-detect + response in the user's language — Boston is diverse: Spanish, Haitian Creole, Chinese), personalization ("my neighborhood" / saved address), mobile-first responsive layout, "share this answer", voice in/out.

### Signals of a 3 — "Clean interface, logical flow. A non-technical person could use it with some guidance."

- A coherent web UI (Streamlit/Gradio/Chainlit/React) with clear labels, a sensible layout, example prompts or onboarding hints, loading states; sources shown at least somewhere in the UI.

### Signals of a 2 — "Functional but plain. Needs explaining before someone could use it on their own."

- A default-widget UI with no guidance: unlabeled input box, answers as plain paragraphs, no examples, no state for errors or empty results; sources absent or as raw file paths.

### Signals of a 1 — "Raw text output. Confusing, and requires technical knowledge to operate."

- CLI-only or notebook-only interaction; the user must edit code or run scripts to ask a question; no source display at all. (This is a 1 *for Track B* — the same repo could be fine in Track A. Track choice is the lens.)

## Where these things typically live

- UI code: `app.py`, `ui/`, `frontend/`, `pages/`, `components/`, `streamlit_app.py`, templates.
- Citation rendering: the answer-display component — is retrieval metadata (dataset, URL, date) carried all the way to the screen?
- Accessibility: grep the frontend for `aria-`, `alt=`, `tabindex`, `role=`, `prefers-` (color-scheme / reduced-motion), `@media`; a `lighthouse`/audit report file.
- Multilingual: i18n libs, locale files, language-detection calls, translated prompt templates.
- Mobile/responsive: viewport meta, breakpoints, flex/grid layouts, PWA manifest.
- README screenshots/GIFs and the demo video are legitimate UX evidence — cite them like files.

## Q&A probe patterns (adapt to THIS repo's weak spots; the guide's arsenal has the canonical four)

1. "Hand me the phone — or the laptop. Can I use it cold, right now?" (thirty unassisted seconds; needing the team to steer is the 3 anchor's "with some guidance", not a 4)
2. "Where does this answer show its source and how fresh the data is?" ("honest about its sources" is written into the 4 anchor — trust cues belong in the interface, not the repo)
3. "Ask it something the data can't answer — what does a resident SEE?" (the abstention path as a designed UI state, not a stack trace)
4. "Your neighbor who's never heard of RAG asks about their street's 311 complaints — what do they see, and would they trust it?" (visual, conversational, honest — all three should be visible in the answer)
5. "What did you deliberately leave out to keep it simple?" (great UX is editing; teams that can name their cuts designed the experience)
