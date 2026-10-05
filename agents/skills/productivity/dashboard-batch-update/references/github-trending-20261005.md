# GitHub Trending Dashboard Batch - 05 October 2026

## What changed

The scheduled dashboard job successfully used Firecrawl MCP to scrape:
- `https://github.com/trending?since=weekly`
- `https://news.ycombinator.com`
- `https://www.producthunt.com`

Firecrawl returned structured JSON, but the MCP tool wrapped the payload as a JSON string with `metadata` and `json`. The useful repo data was under `result.json.repos`.

## Dashboard shape observed

The live dashboard at `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html` still used:
- `#signal-tabs`
- `currentSignal`
- `signalRepos(repos)`
- one grid `#repo-grid`

It did not use the newer pure sort-tab/panel architecture. For this shape, each new repo needed `bucket: "Trending Today"` so the default active tab displayed all 15 current repos.

## Generator alignment

The directory contained `refresh_dashboard.py`. Updating only `dashboard.html` would leave the dashboard vulnerable to being overwritten by stale generator data. The run updated:
- `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/batch_20261005.json`
- `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/repos.json`
- `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html`
- the `SELECTED` block in `refresh_dashboard.py`

## Cross-signal result

HN and Product Hunt front pages were checked. No direct matches were found for the top 15 GitHub trending repositories, so `hnRank`, `hnPoints`, `phRank`, and `phUpvotes` stayed null and `signalBadges` stayed empty.

## Verification pattern used

After writing files:
1. Parse `dashboard.html`, extract `var BATCHES`, and validate `BATCHES[batchId].repos.length == 15`.
2. Validate `stars` and `growth` are numbers.
3. Validate each repo has `name`, `description`, `stars`, `growth`, `growthLabel`, `url`, `category`, `whyMatters`, and `why_this_matters`.
4. Confirm `var currentBatchId = "20261005"`.
5. Confirm the active batch tab exists.
6. Run `python3 -m py_compile refresh_dashboard.py` after patching its `SELECTED` block.
7. Open the local dashboard file in a browser, confirm no console errors, and inspect the visible hero date, repo count, first cards, and archive controls.

## Durable lesson

For this dashboard class, the safe update is not only a JSON insertion. It is a four-part consistency update: batch JSON, rendered HTML, active tab/current batch, and generator source if present.
