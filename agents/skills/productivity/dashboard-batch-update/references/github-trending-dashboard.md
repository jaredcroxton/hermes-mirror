# GitHub Trending Dashboard — Session Reference

## Dashboard File
`/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html`

## Batch JSON Pattern
Saved as: `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/batch_YYYYMMDD.json`

Each batch JSON contains:
- `date`: "DD Month YYYY"
- `source`: "GitHub Trending (weekly)"
- `repositories`: Array of 14 repo objects with name, description, total_stars, stars_this_week, language, url, category, why_this_matters, signal
- `hn_signals`: Object (often empty when Firecrawl is unavailable)
- `ph_signals`: Object (often empty when Firecrawl is unavailable)
- `notes`: Free-text notes about scraping limitations

## HTML Template Architecture (Actual)

The dashboard does NOT use a `var BATCHES = {...}` pattern. It uses:

- `const REPOS = [...]` — flat array of all 14 repos for the current week. Each repo has a `signal` field that determines which tab it shows in.
- `const ARCHIVE_WEEK1 = [...]` — previous week's repos in compact format
- `const ARCHIVE_WEEK2 = [...]` — 2 weeks ago
- `const ARCHIVE_WEEK3 = [...]` — 3 weeks ago
- Tabs rendered by filtering REPOS by `signal` prefix:
  - `renderTab('trending', REPOS.filter(r => r.signal.indexOf('Trending today') === 0))`
  - `renderTab('growing', REPOS.filter(r => r.signal.indexOf('Fastest growing') === 0))`
  - `renderTab('starred', REPOS.filter(r => r.signal.indexOf('Most starred') === 0))`

**Update approach:** Rewrite the entire HTML file. Targeted patching is too fragile for the flat REPOS array + archive shift pattern.

## GitHub Trending Scrape Notes

### Primary: Firecrawl
URL: `https://github.com/trending?since=weekly`
Use `mcp_firecrawl_firecrawl_scrape` with JSON format and schema, or markdown format with `maxAge`.

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

When Firecrawl is available: scrape `https://news.ycombinator.com` and `https://www.producthunt.com` and cross-reference repo names.

When Firecrawl is unavailable:
- Use `browser_navigate` to HN front page, scan for repo names in story titles
- PH may not be reachable — note in batch JSON
- Direct repo matches on HN/PH front pages are rare; most weeks return empty hn_signals and ph_signals

## Batch History

| Date | Repos | Top Repo | Top Growth |
|------|-------|----------|------------|
| 20 July 2026 | 14 | OpenCut-app/OpenCut | +12,743/week |
| 13 July 2026 | 15 | openclaw/openclaw | +2,800/week |
| 06 July 2026 | 10 | meetily | +1,409/day |
| 29 June 2026 | 12 | headroom | +16,102/week |
