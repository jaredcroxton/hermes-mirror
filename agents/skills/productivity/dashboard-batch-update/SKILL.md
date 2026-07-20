---
name: dashboard-batch-update
description: Update an existing HTML dashboard template with a new batch of scraped data. Use when a recurring job or cron task needs to insert new data (e.g., GitHub trending repos, lead lists, KPI snapshots) into a self-contained HTML dashboard file that uses a flat REPOS array + archive arrays pattern.
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

The GitHub AI dashboard uses a flat REPOS array + archive arrays pattern, NOT a BATCHES object. The actual structure:

```
<div class="tab-nav">
  <button class="tab-btn active" onclick="switchTab('trending')">Trending Today</button>
  <button class="tab-btn" onclick="switchTab('growing')">Fastest Growing</button>
  <button class="tab-btn" onclick="switchTab('starred')">Most Starred</button>
  <button class="tab-btn" onclick="switchTab('archive')">Archive</button>
</div>

<div class="tab-panel active" id="tab-trending"><div class="card-grid" id="grid-trending"></div></div>
<div class="tab-panel" id="tab-growing"><div class="card-grid" id="grid-growing"></div></div>
<div class="tab-panel" id="tab-starred"><div class="card-grid" id="grid-starred"></div></div>
<div class="tab-panel" id="tab-archive"><!-- archive sections --></div>

<script>
const REPOS = [ ... ];  // flat array, all repos. Each has a "signal" field like "Trending today #1"

const ARCHIVE_WEEK1 = [ ... ];  // previous week's repos, compact format
const ARCHIVE_WEEK2 = [ ... ];
const ARCHIVE_WEEK3 = [ ... ];

// Tabs populated by filtering REPOS by signal prefix:
renderTab('trending', REPOS.filter(r => r.signal.indexOf('Trending today') === 0));
renderTab('growing', REPOS.filter(r => r.signal.indexOf('Fastest growing') === 0));
renderTab('starred', REPOS.filter(r => r.signal.indexOf('Most starred') === 0));
</script>
```

**Key insight:** The tabs are VIEWS onto a single flat REPOS array, not separate data containers. Each repo has a `signal` field that determines which tab it appears in. The archive is a separate data structure with compact entries.

## Workflow

### 1. Scrape data sources

**Primary approach — Firecrawl (preferred, but credits may run out):**

Use `firecrawl_scrape` or `mcp_firecrawl_firecrawl_scrape` to scrape GitHub trending. Use `maxAge` for cached data.

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

Read the full HTML file. Identify:
- The current REPOS array (flat array of all repos with `signal` fields)
- The ARCHIVE_WEEK1, ARCHIVE_WEEK2, ARCHIVE_WEEK3 arrays
- The timestamp in the header
- The archive section titles and date labels

### 4. Update the HTML — full file rewrite

Because the REPOS array is a single flat array that feeds all three tabs via `signal` prefix filtering, targeted patching is error-prone. **Rewrite the entire HTML file** using `write_file`:

1. Replace the REPOS array with the new batch's repos
2. Shift old REPOS data into ARCHIVE_WEEK1 (compact format: name, stars, growth, date)
3. Shift old ARCHIVE_WEEK1 to ARCHIVE_WEEK2
4. Shift old ARCHIVE_WEEK2 to ARCHIVE_WEEK3 (add a new archive section div if needed)
5. Update the timestamp in `.timestamp` and `.section-header` to the current date
6. Update the repo count in the timestamp text

**Archive chip format:**
```javascript
{"name": "owner/repo", "stars": 12345, "growth": "+X,XXX stars/week", "date": "DD Month"}
```

Keep all CSS and tab-switching JavaScript unchanged.

### 5. Verify

After writing, read the file back and verify:
- The new REPOS array contains 14 repos with correct `signal` prefixes
- ARCHIVE_WEEK1 now holds last week's repos (compact format)
- ARCHIVE_WEEK2 and ARCHIVE_WEEK3 are shifted correctly
- The timestamp is updated to the current date
- The archive section titles match the shifted dates
- Tab nav buttons are unchanged (always the same four tabs)

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

- **Firecrawl may run out of credits.** Always have the browser-based DOM scraping fallback ready. The `browser_navigate` + `browser_console` with JavaScript extraction pattern is proven and reliable for GitHub trending.
- **GitHub trending page shows 14 repos, not 25.** The `querySelectorAll('article')` returns exactly 14 articles on the trending page. Don't expect 25 or try to scroll-infinite-load more — there aren't any more.
- **Use href for repo names, not textContent.** The `h2 > a` textContent has whitespace artifacts (e.g., `"Nutlope /\n\n      hallmark"`). Extract the clean name from the href attribute: `href.replace(/^\//, '')`.
- **Rewrite the entire HTML file, don't patch.** The flat REPOS array + archive shift pattern makes targeted patching too fragile. A full `write_file` is safer and the file is small (~20KB).
- **Keep the CSS and JS identical.** Only the REPOS array, ARCHIVE arrays, and timestamp text change. Don't touch the styles or tab-switching logic.
- **Archive entries are compact.** Not full repo objects. Just `name`, `stars`, `growth`, `date` for the archive chips.
- **HN and PH cross-reference is best-effort.** When Firecrawl search is also unavailable, cross-reference is limited to front-page-only scanning via browser. Note this in the batch JSON's `notes` field.
- **Match the existing format exactly.** The `growth` field format is `"+X,XXX stars this week"` or `"+X,XXX stars/week"` in archives. The `signal` field format is `"Trending today #N"`, `"Fastest growing #N"`, or `"Most starred #N"`.
