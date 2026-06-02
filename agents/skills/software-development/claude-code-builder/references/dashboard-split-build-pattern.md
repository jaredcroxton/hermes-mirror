# Dashboard Split-Build Pattern

When a full dashboard build with data engine + UI exceeds the 600s `delegate_task` timeout (common for complex greenfield builds with Taste bundle), split into two phases:

## Phase A: Data Engine (Bob)

Build the data model, scoring logic, and sample data. No UI.

Deliverables:
- `data/sample.json` — realistic sample stories/data with full schema
- `data/scoring-weights.json` — keyword weights, scoring rules
- `README.md` — schema documentation

This phase uses `toolsets: ["file","terminal"]` only. No browser, no design load. Completes in 200-210s.

## Phase B: Dashboard UI (Bob)

Read the data files from Phase A. Build the full HTML dashboard with all features.

Deliverables:
- `index.html` — single monolithic file, all CSS/JS inline, data embedded

This phase uses `toolsets: ["file","terminal"]` and loads the Taste bundle (claude-design + popular-web-designs) during Phase 1 Blueprint. Completes in 280-340s.

## Delegation pattern

```python
# Phase A
delegate_task(
    goal="Build Phase A data engine files...",
    context="You are Bob Builder... TASK: Build Phase A...",
    toolsets=["file","terminal"]
)

# Phase B
delegate_task(
    goal="Build Phase B dashboard UI...",
    context="You are Bob Builder... Data files already exist at ~/Desktop/hermes_builds/<project>/data/...",
    toolsets=["file","terminal"]
)
```

## Why this works

The 600s limit is per subagent call, not per build. Splitting into two calls keeps each under the limit. Bob inherits the file state from Phase A since both write to the same workspace directory.

## When to use

Trigger when:
- The build brief includes both a data model AND a UI
- The user asks for 30+ data items with scoring logic
- The brief mentions "world-class design" or requires the Taste bundle
- The full build would realistically take more than 300s

Not needed for:
- Simple dashboards with <10 items
- Static pages with no data model
- Enhancement tasks on existing files
