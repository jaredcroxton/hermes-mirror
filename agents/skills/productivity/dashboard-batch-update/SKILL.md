---
name: dashboard-batch-update
description: Update an existing HTML dashboard template with a new batch of scraped data. Use when a recurring job or cron task needs to insert new data (e.g., GitHub trending repos, lead lists, KPI snapshots) into a self-contained HTML dashboard that uses a BATCHES object with batch tabs architecture.
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

As of August 2026, the GitHub AI dashboard uses a **multi-batch BATCHES object** architecture. Each batch is a named key (e.g., `"20260803"`) with its own `repos` array and `label`. Batch tabs let users switch between weeks. Within each batch, sort tabs (Trending Now, Most Starred, Fastest Growing) are views that sort the same data differently — no `signal` prefix filtering needed.

```
<!-- Batch tabs (week selector) -->
<div class="tabs" id="batch-tabs">
  <button class="tab-btn active" onclick="switchBatch('20260803')">03 Aug 2026</button>
  <button class="tab-btn" onclick="switchBatch('20260727')">27 Jul 2026</button>
</div>

<!-- Sort tabs (view selector for the active batch) -->
<div class="tabs" id="sort-tabs">
  <button class="tab-btn active" onclick="switchTab('trending')">Trending Now</button>
  <button class="tab-btn" onclick="switchTab('starred')">Most Starred</button>
  <button class="tab-btn" onclick="switchTab('growing')">Fastest Growing</button>
</div>

<div id="panel-trending" class="tab-panel active"></div>
<div id="panel-starred" class="tab-panel"></div>
<div id="panel-growing" class="tab-panel"></div>

<script>
var BATCHES = {
  "20260803": {
    label: "Week of 03 August 2026",
    repos: [ ... ]   // full repo objects with name, description, stars, growth, growthLabel, url, category, whyMatters
  },
  "20260727": {
    label: "Week of 27 July 2026",
    repos: [ ... ]
  }
};

// Tabs populated by sorting the active batch's repos differently:
function refreshDisplay() {
  var batch = BATCHES[currentBatchId];
  var repos = batch.repos;
  // Sort by growth for trending, by stars for starred, by growth for growing
  document.getElementById('panel-trending').innerHTML = renderPanel(repos, function(a, b) { return b.growth - a.growth; });
  document.getElementById('panel-starred').innerHTML = renderPanel(repos, function(a, b) { return b.stars - a.stars; });
  document.getElementById('panel-growing').innerHTML = renderPanel(repos, function(a, b) { return b.growth - a.growth; });
}
</script>
```

**Key insight:** Each batch is a self-contained data container. Sort tabs are VIEWS that sort the same data differently. No `signal` prefix strings, no ARCHIVE_WEEK arrays — old batches live as additional keys in the BATCHES object. Adding a new week means adding a new key to BATCHES and a new batch tab button.

## Workflow

### 1. Scrape data sources

**Primary approach — Firecrawl (preferred, but credits may run out):**

Use `firecrawl_scrape` or `mcp_firecrawl_firecrawl_scrape` to scrape GitHub trending. Use JSON format with a schema for repo fields. For freshness-sensitive signal sources like HN and Product Hunt front pages, set `maxAge: 0`; otherwise Firecrawl may legitimately return a cached front page from the prior day. Use `maxAge` caching only when freshness is less critical than speed or credit use.

**Fallback — Browser-based DOM scraping (when Firecrawl is out of credits):**

When Firecrawl returns "Insufficient credits", use the browser tool stack:
1. `browser_navigate` to `https://github.com/trending?since=weekly`
2. `browser_scroll` down to load all repos (GitHub trending shows 14 repos per page, not 25)
3. Use `browser_console` with JavaScript to extract structured data:

```javascript
(() => {
  const articles = document.querySelectorAll('article');
  const repos = [];
  articles.forEach((a) => {
    const h2 = a.querySelector('h2');
    const nameLink = h2 ? h2.querySelector('a') : null;
    if (!nameLink) return;
    const href = nameLink.getAttribute('href');
    const cleanName = href ? href.replace(/^\//, '') : '';
    const desc = a.querySelector('p') ? a.querySelector('p').textContent.trim() : '';
    const totalStarsEl = a.querySelector('a[href*="/stargazers"]');
    const totalStars = totalStarsEl ? totalStarsEl.textContent.replace(/[^0-9]/g, '') : '0';
    const match = a.textContent.match(/([\d,]+)\s+stars?\s+this\s+week/);
    const starsWeek = match ? match[1].replace(/,/g, '') : '0';
    repos.push({ name: cleanName, description: desc, total_stars: parseInt(totalStars), stars_this_week: parseInt(starsWeek), url: 'https://github.com/' + cleanName });
  });
  return repos;
})()
```

**Important:** The `h2 > a` href attribute gives the clean `owner/repo` path. The heading textContent has whitespace artifacts. Use the href, not textContent, for the repo name.

For HN and PH, use `browser_navigate` to check front pages. If Firecrawl search is also unavailable, the cross-reference will be limited to front-page-only scanning.

### 2. Build the batch JSON

Create a batch file at `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/batch_YYYYMMDD.json`. Each repo entry should include:

```json
{
  "date": "2026-08-03",
  "batchId": "20260803",
  "label": "Week of 03 August 2026",
  "repos": [
    {
      "name": "owner/repo",
      "description": "Short description",
      "language": "Python",
      "stars": 12345,
      "growth": 5678,
      "growthLabel": "5,678 stars this week",
      "url": "https://github.com/owner/repo",
      "category": "AI Agents",
      "whyMatters": "1-2 sentences connecting this repo to Jared's work (PerformOS, Accor Plus, AgentOS, or his agent ecosystem)",
      "hnRank": null,
      "phUpvotes": null
    }
  ],
  "totalStars": 342006,
  "totalGrowth": 58048,
  "categories": ["AI Agents", "Developer Tools & Infra", "LLMs & Foundation Models", "Data & Analytics"],
  "topCategory": "AI Agents"
}
```

Key fields:
- `growth` and `stars` are NUMBERS for sorting, not strings
- `growthLabel` is the display string (e.g., "8,217 stars this week")
- `category` is used for badges in the UI
- `hnRank` and `phUpvotes` are null when no cross-reference match is found

### 3. Read the existing dashboard HTML

Read the full HTML file. Identify:
- The current BATCHES object and its keys (e.g., `"20260803"`, `"20260727"`)
- The batch tabs section (`#batch-tabs`) — list of `<button>` elements with `switchBatch()` calls
- The sort tabs section (`#sort-tabs`) — should always be "Trending Now", "Most Starred", "Fastest Growing"
- The header timestamp (`.header-meta`)

### 4. Update the HTML — targeted patching

With the BATCHES architecture, **targeted patching** is the preferred approach. The file is small enough that individual patches are safer than a full rewrite:

1. **Add or replace the new batch tab button** in the `#batch-tabs` div: insert a new `<button class="tab-btn active" onclick="switchBatch('YYYYMMDD')">DD Mon YYYY</button>` as the first button, and remove `active` from every other batch button. Scheduled jobs can rerun on the same date, so treat the current `batchId` as an upsert: if the key already exists, replace that batch's object and move its tab to the top instead of creating a duplicate or failing the run.

2. **Add or replace the batch in the BATCHES object**: insert the new key at the top of the BATCHES object. If the key already exists, parse brace depth from that key's opening `{` and replace only that top-level batch object. Do not rely on naive regex for nested repo arrays.

3. **Update the header timestamp**: patch `.header-meta` or the dashboard's visible scan marker to the new week.

4. **Set the new batch as active**: ensure `var currentBatchId = "YYYYMMDD";` points to the new batch.

All CSS, tab-switching JavaScript (`switchBatch`, `switchTab`, `refreshDisplay`, `renderCard`, `renderPanel`), and sort-tab structure remain unchanged.

### 5. Verify

After writing, read the file back and verify:
- The new batch key exists in BATCHES with 15 repos
- Each repo has `name`, `description`, `stars`, `growth`, `growthLabel`, `url`, `category`, `whyMatters`
- The batch tab button for the new week is present and has `class="tab-btn active"`
- The previous batch's tab button no longer has `active`
- `currentBatchId` is set to the new batch's key
- The `.header-meta` text shows the new week
- Sort-tab buttons are unchanged
- All three panel divs exist with the correct IDs

## Cross-signal badge logic

After scraping GitHub trending, check HN and Product Hunt for the same repos:

- **When Firecrawl is available:** Scrape HN and PH front pages. Cross-reference repo names against story titles.
- **When Firecrawl is unavailable (browser fallback):** Use `browser_navigate` to check HN front page. PH may not be reachable. Direct repo matches are rare — most weeks return empty signals.
- **HN format:** "HN #RANK, POINTS points"
- **PH format:** "PH #RANK, UPVOTES upvotes"
- If no matches, note in the batch JSON's `notes` field that cross-reference was limited to front-page scanning.

## References

- `references/github-trending-dashboard.md` — session-specific details for the GitHub trending dashboard: file paths, batch history, scrape notes for GitHub/HN/PH, and HTML anchor patterns for patching.

## Pitfalls

- **Firecrawl may return cached front pages unless told not to.** For HN and Product Hunt signal badges, use `maxAge: 0` when the job is meant to reflect the live front page. Cached scrapes can be useful for GitHub trending when the weekly page is stable, but stale HN/PH data can create false badges.
- **Same-day cron reruns are upserts, not duplicates.** If `batch_YYYYMMDD.json` or the `BATCHES[YYYYMMDD]` key already exists, replace it after verification rather than failing or adding a second tab. A partial prior run may have inserted an older same-day batch before stopping.
- **Use brace-depth replacement for existing BATCHES entries.** A top-level batch contains nested repo objects and arrays; regex alone is brittle. Locate the batch key, find the opening `{`, scan strings/escapes while counting braces, and replace exactly that object.
- **Firecrawl may run out of credits.** Always be aware of the browser-based DOM scraping fallback. The `browser_navigate` + `browser_console` with JavaScript extraction pattern works for GitHub trending when Firecrawl is unavailable.
- **Use `patch` tool for targeted edits, not full rewrites.** The BATCHES architecture makes targeted patches clean: add a batch tab button, insert the new BATCHES key, update the header timestamp, and update `currentBatchId`. Four small patches are safer than one full file write.
- **Cron jobs may block `execute_code`.** If a scheduled dashboard job needs scripted HTML manipulation, write a temporary Python script with `write_file`, run it with `terminal`, then verify and delete the script. Do not stop just because `execute_code` is unavailable.
- **Do NOT touch the JavaScript functions unless the user explicitly requires a new display capability.** `switchBatch`, `switchTab`, `refreshDisplay`, `renderCard`, `renderPanel` should usually stay the same across updates. Only data and tab buttons change by default; add renderer logic only for new required fields such as HN/Product Hunt badges.
- **`growth` and `stars` are numbers, not strings.** The sort functions (`b.growth - a.growth`) depend on numeric comparisons. `growthLabel` is the display string.
- **HN and PH cross-reference is best-effort.** Direct repo matches on HN/PH front pages are rare. Most weeks return empty `hnRank` and `phUpvotes`. Note scraping limitations in the batch JSON metadata.
- **GitHub trending returns up to 25 repos per page.** Firecrawl with JSON schema reliably extracts all 25. The dashboard targets the top 15.
- **Use `maxAge` for Firecrawl when data freshness is less critical.** Cached scrapes are faster and use fewer credits.
