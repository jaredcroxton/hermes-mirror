# Split Build Pattern for Complex Dashboards

## When to use

When a build involves multiple distinct components (data engine + UI + cron + deploy), the 600s `delegate_task` limit will likely be exceeded if attempted as a single delegation.

Trigger signs:
- Data-driven dashboards with scoring/filtering logic
- Builds requiring sample data generation
- Projects with cron automation components
- Any brief exceeding ~200 lines of spec

## The pattern

Split into sequential phases. Each phase is a separate `delegate_task` call. Each phase's output becomes the next phase's input.

### Phase A — Data model and sample data
**Goal:** Define the data schema, generate sample data, build scoring/weighting logic.

**Deliverables:**
- `data/sample.json` — realistic sample records with all required fields
- `data/scoring-weights.json` — keyword weights or scoring rules
- `README.md` — schema docs

**Why first:** The UI phase needs the exact real data shape. Locking data first means the UI build references real fields, not placeholders.

### Phase B — UI build
**Goal:** Build the dashboard/frontend consuming the Phase A data.

**Deliverables:**
- `index.html` — single self-contained file with embedded sample data
- All CSS, JS, and data inline (no file:// fetch issues)

**Brief to Bob:** Reference Phase A file paths explicitly. Tell Bob to read Phase A files and embed the data inline.

### Phase C — Automation (after UI approval only)
**Goal:** Cron scraping scripts, live data connection, deploy.

**Only proceed here once the UI is staged and approved.**

## Real example

PerformOS Trending Intelligence Dashboard, June 2026:
- Phase A: 30 sample stories + scoring-weights.json (20 keywords, sum 100) + README — 208s
- Phase B: 412-line dashboard with filters, score badges, thumbs up/down, localStorage — 288s
- Single delegation would have timed out (limit: 600s)

## Anti-patterns
- **Do not** combine Phase A and Phase B — timeout is guaranteed
- **Do not** skip Phase A — Bob will hallucinate data shapes
- **Do not** include Phase C in Phase B's brief — deploy only after UI approval
