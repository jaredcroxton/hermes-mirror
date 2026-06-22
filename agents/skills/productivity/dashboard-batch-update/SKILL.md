---
name: dashboard-batch-update
description: Update an existing HTML dashboard template with a new batch of scraped data. Use when a recurring job or cron task needs to insert new data (e.g., GitHub trending repos, lead lists, KPI snapshots) into a self-contained HTML dashboard file that uses a BATCHES object pattern.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [dashboard, batch-update, scrape, html, patch, cron, data-pipeline]
    related_skills: [claude-design, html-leads-dashboard, native-mcp]
---

# Dashboard Batch Update

Use this skill when the task is to update an **existing** HTML dashboard file with a new batch of data — not to build a new dashboard from scratch.

Typical trigger: a cron job or scheduled task that scrapes a data source (GitHub trending, HN, PH, APIs), builds a batch JSON, and inserts it into an HTML dashboard template as a new tab.

## Expected Dashboard Template Pattern

The target HTML file is expected to follow this structure:

```
<div class="tab-nav">
  <button class="tab-btn active" onclick="switchTab('batchN')">Label N</button>
  <button class="tab-btn" onclick="switchTab('batchN-1')">Label N-1</button>
  ...
</div>

<div class="tab-panel active" id="batchN"></div>
<div class="tab-panel" id="batchN-1"></div>
...

<div class="timestamp" id="last-updated">Last updated: DATE</div>

<script>
var BATCHES = {
  'batchN': [ ... ],
  'batchN-1': [ ... ],
};

function switchTab(tab) { ... }
function renderTab(tab) { ... }

renderTab('batchN');
renderTab('batchN-1');
</script>
```

## Workflow

### 1. Scrape data sources

Use `firecrawl_scrape` to scrape the primary data source (e.g., GitHub trending). Use `maxAge: 300` for near-fresh data. Scrape secondary sources (HN, Product Hunt) in parallel for cross-signal badges.

For GitHub trending, the scrape returns the full page. Parse the markdown to extract: repo name, description, total stars, stars-this-week growth, and URL. The growth number is shown as "X,XXX stars this week" on the trending page.

### 2. Build the batch JSON

Create a batch file at the expected path (e.g., `batch_YYYYMMDD.json`). Each repo entry should include:

```json
{
  "name": "owner/repo",
  "description": "Short description",
  "stars": 12345,
  "growth": "+X,XXX this week",
  "url": "https://github.com/owner/repo",
  "why": "1-2 sentences connecting this repo to Jared's work (PerformOS, Accor Plus, AgentOS, or his agent ecosystem)",
  "signal": "Trending #N this week"
}
```

Also include a `cross_signals` object noting any HN ranking or Product Hunt upvotes for repos that appear on those platforms.

### 3. Read the existing dashboard HTML

Read the full HTML file to understand the current structure. Use `read_file` with pagination if the file is large. Identify:
- The current batch keys (e.g., `batch4`, `batch3`, `batch1`)
- The tab nav structure
- The BATCHES object location
- The renderTab calls at the bottom
- The timestamp format

### 4. Patch the HTML — four surgical edits

Use `patch` (mode=replace) for each edit. Do NOT rewrite the entire file.

**Edit 1 — Tab nav:** Add the new tab button first (newest first), shift others down. Mark the new tab as `active`, others not.

**Edit 2 — Tab panels:** Add the new `<div class="tab-panel active" id="batchN"></div>` first, shift others down (remove `active` from old top batch).

**Edit 3 — BATCHES object:** Insert the new batch data as the first entry in the BATCHES object (before the current top batch). Use the full JSON array.

**Edit 4 — renderTab calls:** Add `renderTab('batchN');` as the first renderTab call.

**Edit 5 — Timestamp:** Update the timestamp to the current date.

### 5. Verify

After patching, read the file back and verify:
- The new batch key appears in the BATCHES object
- The new tab button exists and is active
- The new tab panel div exists
- The renderTab call includes the new batch
- The timestamp is updated

## Cross-signal badge logic

After scraping GitHub trending, check HN and Product Hunt front pages for the same repos:

- **HN:** If a trending repo appears on the HN front page, note its rank and points (e.g., "HN #3, 305 points")
- **Product Hunt:** If a trending repo has a PH launch, note its rank and upvotes (e.g., "PH #1, 383 upvotes")
- If no direct matches, note related products on those platforms that align with the trend

Add these as `signal` fields on relevant repos or in the `cross_signals` section of the batch JSON.

## References

- `references/github-trending-dashboard.md` — session-specific details for the GitHub trending dashboard: file paths, batch history, scrape notes for GitHub/HN/PH, and HTML anchor patterns for patching.

## Pitfalls

- **Do not rewrite the entire HTML file.** Use targeted `patch` calls. Rewriting risks losing existing data or breaking the template structure.
- **Read the full file before patching.** The file may be paginated. Use `offset` and `limit` to read all sections.
- **Match the existing JSON format exactly.** If existing batches use `"growth": "+X,XXX this week"`, use the same format. Don't switch to different field names or structures.
- **Keep the newest batch first.** The tab nav and BATCHES object should have the newest batch as the first entry.
- **Test the patch diff.** After each patch, verify the diff looks correct — especially that you're inserting before the right anchor string.
- **Firecrawl rate limits.** When scraping multiple sources in parallel, they generally complete fine, but if one fails, retry individually.
- **GitHub trending page structure.** The trending page embeds star counts and growth in the markdown output. Parse carefully — the growth number appears as "X,XXX stars this week" near each repo entry.
