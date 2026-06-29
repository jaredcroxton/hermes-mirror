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
URL: `https://github.com/search?q=ai+agent+stars%3A%3E10000&type=repositories&s=stars&o=desc`

**Star count quirk on search pages:** The star link text on search results is abbreviated (e.g., "241k" instead of "240,873"). The full count IS in the page text content. Use the textContent regex pattern: `(\d[\d,]+)\s*stars` to extract the actual number, not the abbreviated link text.

Extraction approach — get raw text per result card:
```js
Array.from(document.querySelectorAll('[data-testid="results-list"] > div')).map((div, i) => ({
  text: div.textContent.substring(0, 300)  // parse name/stars/desc from text
}))
```

Then parse each card's text for: repo name (first line), description, and star count via regex `/(\d[\d,]+)\s*stars/`.

### Selection rules

Select 15 repos total (5 per tab). Every repo must have a real GitHub URL and real star count. Do NOT fabricate data. Avoid duplicating repos across tabs. Prefer fresh picks not featured in the previous 2 weeks when possible.

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
