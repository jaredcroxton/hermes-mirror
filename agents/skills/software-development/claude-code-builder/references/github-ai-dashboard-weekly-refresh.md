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

Scrape three sources for comprehensive coverage:

1. **GitHub Trending (daily):** `https://github.com/trending?since=daily` — extract with firecrawl_scrape JSON
2. **GitHub Trending (weekly):** `https://github.com/trending?since=weekly` — includes growth metrics
3. **GitHub Search (AI sorted by stars):** `https://github.com/search?q=AI+OR+LLM+OR+GPT+OR+machine+learning+OR+artificial+intelligence&type=repositories&s=stars&o=desc`

Select 15 repos across the three categories. Every repo must have a real GitHub URL and real star count. Do NOT fabricate data.

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
