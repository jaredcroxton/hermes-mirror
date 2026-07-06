# GitHub AI Dashboard Weekly Refresh Pattern

Use when the cron job or Jared asks to refresh the GitHub AI Dashboard (top 15 AI repos).

## Dashboard identity

- Local directory: `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/`
- Source data: `repos.json` (15 repos, each with name, description, stars, growth, category, url, why, signal)
- Archive: `archive/repos_YYYY-MM-DD.json` (previous week's data, copied before overwrite)
- Dashboard HTML: `dashboard.html` (PerformOS dark theme, tabbed layout)
- This is a LOCAL-ONLY artifact. No GitHub push. No Vercel deploy.

## Category structure (3 tabs, ~5 each)

1. **Trending Today** — repos appearing on GitHub Trending (daily or weekly)
2. **Fastest Growing** — repos with highest star velocity this week
3. **Most Starred** — repos with highest absolute star count

## Source strategy

Scrape three sources for comprehensive coverage. Use `browser_navigate` + `browser_console` for all extraction (not firecrawl_scrape — browser_console with querySelectorAll is faster and more reliable for GitHub pages).

### Source 1: GitHub Trending (daily)
URL: `https://github.com/trending?since=daily`

Extraction expression (browser_console):
```js
JSON.stringify(Array.from(document.querySelectorAll('article.Box-row')).map(article => {
  const h2 = article.querySelector('h2');
  const link = h2 ? h2.querySelector('a') : null;
  const href = link ? link.getAttribute('href') : '';
  const name = href.replace(/^\//, '');
  const desc = article.querySelector('p') ? article.querySelector('p').textContent.trim() : '';
  const starLink = article.querySelector('a[href*="/stargazers"]');
  const starsText = starLink ? starLink.textContent.trim().replace(/[^0-9]/g, '') : '0';
  const text = article.textContent;
  const todayMatch = text.match(/(\d[\d,]*)\s*stars?\s*today/);
  const todayGrowth = todayMatch ? parseInt(todayMatch[1].replace(/,/g, '')) : 0;
  return {name, description: desc, stars: parseInt(starsText) || 0, todayGrowth, url: 'https://github.com/' + name};
}))
```

### Source 2: GitHub Trending (weekly)
URL: `https://github.com/trending?since=weekly`

Same extraction expression as daily, but match `stars this week` instead of `stars today`:
```js
const weekMatch = text.match(/(\d[\d,]*)\s*stars?\s*(this week)/i);
const weeklyGrowth = weekMatch ? parseInt(weekMatch[1].replace(/,/g, '')) : 0;
```

### Source 3: GitHub Search (most-starred AI repos)

**Preferred URL:** `https://github.com/search?q=llm+OR+gpt+OR+%22ai+agent%22+OR+%22large+language+model%22&type=repositories&s=stars&o=desc`

This OR-based query returns 1M+ results with top repos sorted by stars. Broader and more predictable than topic-filtered queries (which return too few results) or `stars:>10000` (which misses emerging repos).

**Search page DOM is DIFFERENT from Trending pages.** `article.Box-row` selectors do NOT work on search result pages. Search results use a different layout with h3 headings and list-items for metadata. The data IS there but extraction requires more iteration than trending pages.

**Star count quirk on search pages:** The star link text on search results is abbreviated (e.g., "226k" instead of "226,393"). The full count IS visible in the `browser_snapshot` accessibility labels like `link "226393 stars" [ref=e95]` -- the text in the `link` label is the full number. However, `browser_console` extraction via `a[href*="/stargazers"]` returns the abbreviated link text ("226k"), NOT the full number.

**Reliable extraction approach for search pages -- two-stage:**

Stage 1: Use `browser_console` to get repo names (from h3 > a links):
```js
JSON.stringify(Array.from(document.querySelectorAll('h3 a')).slice(0, 15).map(a => {
  const fullName = a.textContent.trim().replace(/\s+/g, '');
  return { fullName, url: 'https://github.com/' + fullName };
}).filter(r => r.fullName.includes('/')))
```

Stage 2: Use `browser_snapshot` with `full=true` to read the full star counts. The snapshot labels include unabbreviated counts like `link "226393 stars"`. Manually transcribe these into the repos.json entries.

**If multiple extraction attempts fail (common on search pages),** do not give up. The `browser_console` approach with different selectors (`h3 a`, `a[href*="/stargazers"]`, parent-tree traversal) needs iteration. After 2-3 failed attempts, fall back to the snapshot method: `browser_snapshot(full=true)` and manually extract repo names and full star counts from the accessibility tree.

### Selection rules

Select 15 repos total (5 per tab). Every repo must have a real GitHub URL and real star count. Do NOT fabricate data. Avoid duplicating repos across tabs. Prefer fresh picks not featured in the previous 2 weeks when possible.

**Deduplication across sources:** Repos often appear in both daily and weekly trending (e.g., strix appeared as #3 trending today AND #2 fastest growing this week). Assign each repo to ONE tab only. Priority order for assignment:
1. If a repo has both daily and weekly growth, put it in Trending Today (daily signal is fresher)
2. If a repo only has weekly growth (not in daily), put it in Fastest Growing
3. If a repo only has absolute star count (from search), put it in Most Starred

**Repos appearing in previous week's archive:** Check the archived `repos_YYYY-MM-DD.json` from last week. If a repo appears there with the same signal, prefer a different repo for this week unless it genuinely improved its position (e.g., moved from #5 to #1 in the same category).

**Category diversity target:** Across all 15 repos, aim for representation from 3+ categories. If one category dominates (e.g., 10 of 15 are "AI Agents"), swap 1-2 repos for strong alternatives in underrepresented categories.

## Data format (repos.json entry)

```json
{
  "name": "owner/repo",
  "description": "One sentence description",
  "stars": 12345,
  "growth": "+1,234 stars this week",
  "category": "AI Agents",
  "url": "https://github.com/owner/repo",
  "why": "Personalized line tied to Jared's context (PerformOS, AgentOS, private AI, business AI, APAC markets)",
  "signal": "Trending today"
}
```

Categories: AI Agents, LLMs & Foundation Models, Developer Tools & Infra, Open Source AI Models, Productivity & Automation, Data & Analytics

Signal values: "Trending today", "Fastest growing #N", "Most starred top N"

## Archive step (mandatory)

Before overwriting repos.json:
```bash
mkdir -p /Users/jc/Desktop/hermes_builds/github-ai-dashboard/archive
cp /Users/jc/Desktop/hermes_builds/github-ai-dashboard/repos.json \
   /Users/jc/Desktop/hermes_builds/github-ai-dashboard/archive/repos_$(date +%Y-%m-%d).json
```

## Dashboard HTML structure

- PerformOS dark theme: #0A0A0A background, #F5EADB cream text, #D4FF3B lime accent
- Fonts: Archivo (display), Inter (body), JetBrains Mono (labels)
- 4-tab layout: Trending Today | Fastest Growing | Most Starred | Archive
- All data inline in HTML (no fetch calls, no external JS)
- Archive tab shows previous week's repos as chips with date, name, stars, growth
- Responsive grid: `repeat(auto-fill, minmax(380px, 1fr))`
- Each card: name (linked), stars, category badge, description, growth badge, "Why this matters" section

## Em dash gate (cron-safe)

After writing dashboard.html, strip em dashes using standalone python3 via terminal (NOT execute_code, NOT piped heredoc):

```bash
python3 -c "
content = open('/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html').read()
content = content.replace('\u2014', '-').replace('&mdash;', '-')
open('/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html', 'w').write(content)
print('Em dashes remaining:', content.count('\u2014') + content.count('&mdash;'))
"
```

## Verification

- repos.json is valid JSON with exactly 15 entries
- All repos have required fields: name, description, stars, growth, category, url, why
- All URLs start with `https://github.com/`
- dashboard.html has zero em dashes
- dashboard.html contains REPOS array, ARCHIVE array, and tab switching function
- Archive file exists with previous week's data
