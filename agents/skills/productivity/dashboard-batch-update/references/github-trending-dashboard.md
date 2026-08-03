# GitHub Trending Dashboard — Session Reference

## Dashboard File
`/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html`

## Batch JSON Pattern
Saved as: `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/batch_YYYYMMDD.json`

Each batch JSON contains:
- `date`: "YYYY-MM-DD"
- `batchId`: "YYYYMMDD"
- `label`: "Week of DD Month YYYY"
- `repos`: Array of 15 repo objects with: name, description, language, stars (number), growth (number), growthLabel (string), url, category, whyMatters, hnRank (null | number), phUpvotes (null | number)
- `totalStars`: combined stars across all repos
- `totalGrowth`: combined weekly growth
- `categories`: list of category strings
- `topCategory`: the most common category

## HTML Template Architecture (Current — August 2026)

The dashboard uses a **multi-batch BATCHES object** architecture:

- `var BATCHES = { "20260803": { label, repos }, "20260727": { label, repos } }` — each batch is a named key with its own repos array.
- Batch tabs (`#batch-tabs`) let users switch between weeks. The active batch tab gets `class="tab-btn active"`.
- Sort tabs (`#sort-tabs`) always show "Trending Now", "Most Starred", "Fastest Growing". These are VIEWS that sort the active batch's repos differently — no `signal` prefix filtering.
- `refreshDisplay()` renders all three panels by sorting the current batch's repos by growth or stars.
- `switchBatch(batchId)` updates `currentBatchId` and calls `refreshDisplay()`.
- `switchTab(tab)` toggles the active sort-tab panel visibility.
- No ARCHIVE_WEEK arrays needed — old batches live as additional keys in BATCHES.

**Update approach:** Use the `patch` tool for four targeted edits:
1. Add a new batch tab button to `#batch-tabs` (set `active`, remove `active` from old button)
2. Insert the new batch key at the top of the BATCHES object
3. Update `.header-meta` to the new week
4. Update `var currentBatchId` to the new key

## GitHub Trending Scrape Notes

### Primary: Firecrawl with JSON schema (preferred)
Use `mcp_firecrawl_firecrawl_scrape` with `formats: ["json"]` and a schema that extracts: name, description, language, total_stars, stars_this_week, url. The page returns up to 25 repos; the dashboard targets the top 15. Use `maxAge` for cached data when freshness is not critical.

### Fallback: Browser DOM scraping (when Firecrawl is out of credits)
1. `browser_navigate` to `https://github.com/trending?since=weekly`
2. `browser_scroll` down (page shows 14 repos)
3. `browser_console` with JavaScript extraction:

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

**Key extraction details:**
- Repo name: extract from `h2 > a` href attribute (`href.replace(/^\//, '')`), NOT from textContent (whitespace artifacts)
- Total stars: `a[href*="/stargazers"]` → strip non-digits
- Weekly growth: regex `/([\d,]+)\s+stars?\s+this\s+week/` on full article textContent → strip commas
- Language: `[itemprop="programmingLanguage"]` textContent
- Only 14 articles on the page — no infinite scroll, no pagination

## HN / Product Hunt Cross-Reference

Scrape `https://news.ycombinator.com` and `https://www.producthunt.com` with Firecrawl (markdown format). Cross-reference repo names against story/product titles. Direct matches are rare — most weeks return null for `hnRank` and `phUpvotes`. This is expected; the batch JSON should record null values rather than fabricated signals.

## Batch History

| Date | Batch ID | Repos | Top Repo | Top Growth | Architecture |
|------|----------|-------|----------|------------|--------------|
| 03 Aug 2026 | 20260803 | 15 | block/buzz | +8,217/week | BATCHES object + batch tabs |
| 27 July 2026 | 20260727 | 15 | bojieli/ai-agent-book | +15,909/week | BATCHES object + batch tabs |
| 20 July 2026 | 20260720 | 14 | OpenCut-app/OpenCut | +12,743/week | flat REPOS + ARCHIVE_WEEK |
| 13 July 2026 | 20260713 | 15 | openclaw/openclaw | +2,800/week | flat REPOS + ARCHIVE_WEEK |
| 06 July 2026 | 20260706 | 10 | meetily | +1,409/day | flat REPOS + ARCHIVE_WEEK |
| 29 June 2026 | 20260629 | 12 | headroom | +16,102/week | flat REPOS + ARCHIVE_WEEK |
