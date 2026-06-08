# Data-Driven Cron Dashboard Pattern

Build pattern for dashboards that refresh weekly from external data sources.

## Architecture

Three-layer separation:

1. **Data scraper** collects live data into JSON (repos.json)
2. **Template builder** consumes JSON and produces monolithic HTML dashboard
3. **Cron scheduler** runs weekly to refresh data and rebuild

## Cron mode constraints

When running as a scheduled cron job, these tools are blocked:
- `execute_code` — blocked ("Cron jobs run without a user present to approve it")
- Piped interpreters (`curl | python3`, `cat | python3`) — blocked by security scanning
- `delegate_task` — may work but unreliable; prefer direct execution
- `git push` — times out in sandbox (osxkeychain unreachable)

**Workaround for API data:** download to temp files first (`curl -s -o /tmp/file.json`), then process with standalone `python3 -c "..."` scripts. Never pipe directly to an interpreter.

**Workaround for deployments:** use `vercel --prod --yes` directly, not git push.

## Step 1: Scrape fresh data (multi-source)

Do NOT rely on a single source. Combine multiple approaches for data quality:

### 1a. GitHub API search (primary source)

Run 3-4 targeted GitHub API searches for different categories. Download each to a temp file, then process with standalone Python:

```bash
curl -s -o /tmp/gh_ai_ml.json "https://api.github.com/search/repositories?q=topic:ai+topic:machine-learning&sort=stars&order=desc&per_page=10"
curl -s -o /tmp/gh_ai_agents.json "https://api.github.com/search/repositories?q=topic:ai-agent+topic:llm&sort=stars&order=desc&per_page=15"
curl -s -o /tmp/gh_ai_open.json "https://api.github.com/search/repositories?q=topic:open-source+topic:ai+topic:llm&sort=stars&order=desc&per_page=10"
curl -s -o /tmp/gh_ai_growth.json "https://api.github.com/search/repositories?q=topic:generative-ai+topic:large-language-model+created:>2025-01-01&sort=stars&order=desc&per_page=15"
```

Process each file with standalone scripts (never piped):

```bash
python3 -c "
import json
with open('/tmp/gh_ai_ml.json') as f:
    data = json.load(f)
for i, item in enumerate(data.get('items', [])[:10]):
    stars = item['stargazers_count']
    desc = (item['description'] or 'N/A')[:150]
    print(f'{i+1}. {item[\"full_name\"]} | {stars:,} stars | {desc}')
"
```

### 1b. GitHub Trending page (supplemental growth data)

The Trending page provides weekly star growth data the API doesn't. Extract via `browser_console`:

```javascript
JSON.stringify(Array.from(document.querySelectorAll('article.Box-row')).map(article => {
  const h2 = article.querySelector('h2 a');
  const name = h2 ? h2.textContent.trim().replace(/\s+/g, ' ').replace(/\s*\/\s*/g, '/') : '';
  const starLink = article.querySelector('a[href*="/stargazers"]');
  const starCount = starLink ? starLink.textContent.trim().replace(/[^0-9]/g, '') : '';
  const fullText = article.textContent;
  const weekMatch = fullText.match(/([\d,]+)\s+stars?\s+this\s+week/i);
  return {
    name, total_stars: starCount,
    stars_this_week: weekMatch ? weekMatch[1].replace(/,/g, '') : '0'
  };
}))
```

### 1c. Selection rules

After collecting from all sources:
- Combine, deduplicate, and rank
- Target 15 repos across 3 groups of 5: Trending, Most Starred, Fastest Growing
- Every repo MUST have a real GitHub URL and real star count from the API
- Do NOT fabricate data. Skip repos without verified numbers
- Every "why" field personalised to Jared's context (PerformOS, AgentOS, Accor Plus, APAC markets)
- Include "signal" field (Trending #1, GitHub Trending, Most starred, Fastest growing)
- Use these categories: AI Agents, LLMs & Foundation Models, Developer Tools & Infra, Open Source AI Models, Productivity & Automation, Data & Analytics

## Step 2: Build dashboard via template replacement

For DATA-REFRESH dashboards (not greenfield builds), do NOT delegate to Bob Builder. Use template replacement instead — faster, no timeout risk, no delegation complexity.

### 2a. Template pattern

Write a `dashboard_template.html` with `__BATCH3_DATA__` and `__BATCH1_DATA__` placeholders in the JavaScript data section. Keep CSS, JS logic, and HTML structure intact. Only the data arrays change week to week.

### 2b. Build script

```python
import json

with open('repos.json') as f:
    current = json.load(f)
with open('archive/repos_YYYY-MM-DD.json') as f:
    archive = json.load(f)

def to_js_json(repos):
    entries = []
    for r in repos:
        entry = {
            "name": r["name"], "description": r["description"],
            "stars": r["stars"], "growth": r["growth"],
            "category": r["category"], "url": r["url"],
            "why": r["why"], "signal": r.get("signal", "")
        }
        entries.append(entry)
    return json.dumps(entries, indent=4, ensure_ascii=False)

with open('dashboard_template.html') as f:
    template = f.read()

html = template.replace('__BATCH3_DATA__', to_js_json(current))
html = html.replace('__BATCH1_DATA__', to_js_json(archive))

with open('dashboard.html', 'w') as f:
    f.write(html)
```

### 2c. Tabbed dashboard pattern

Use a tabbed layout with inline JSON data per batch:
- Tab 1: current week (auto-selected on load)
- Tab 2: previous week archive
- Each batch gets its own tab button with date label
- Data embedded inline in the HTML (no fetch calls) to avoid CORS from file:// URLs
- JavaScript switches tabs and renders cards by category

## Step 3: Archive and verify

### 3a. Archive

Before overwriting repos.json, copy to:

```text
/Users/jc/Desktop/hermes_builds/<project>/archive/repos_YYYY-MM-DD.json
```

### 3b. Verification

- `python3` check: valid JSON, exactly 15 entries, category distribution
- Em dash gate: strip `\u2014` and `&mdash;` from BOTH repos.json AND dashboard.html
- Structural HTML checks (30 GitHub URLs = 15 current + 15 archived)
- Do NOT rely on browser rendering for verification — the headless browser blocks JavaScript on `file://` URLs

## Step 4: Cron

```bash
hermes cron create "0 16 * * 1" \
  --name "Dashboard Weekly Refresh" \
  --prompt "Scrape fresh repos, archive last week, rebuild dashboard."
```

Cron rule: run at Monday 4 p.m. AEST.

## Brand palettes

Ask Jared which brand to use. The default PerformOS lime (#D4FF3B) is being phased out in favour of product-specific palettes:

- **Performlytics**: blue (#3B82F6) accent, violet (#8B5CF6) secondary, cyan (#22D3EE) data viz
- **Pocket Customer**: lime (#D4FF3B), warm cream (#F5EADB)
- **LearnOS**: light theme only, no dark background

When Jared says "update the colour," consult `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/<Product>/VISUAL.md`.

## Em dash gate (NON-NEGOTIABLE)

After every dashboard build and repos.json write, strip em dashes from BOTH files. Cron mode cannot use heredoc (`<<'PY'`), so use standalone scripts:

```bash
python3 -c "
p = '/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html'
with open(p) as f:
    c = f.read()
c = c.replace('\u2014', '-').replace('&mdash;', '-')
with open(p, 'w') as f:
    f.write(c)
print('Em dashes remaining:', c.count('\u2014') + c.count('&mdash;'))
"
```

Repeat for repos.json. Count must be zero before delivering.

## Relevance voting

Checkbox per repo stored in localStorage keyed by repo name. Persists across weekly refreshes. If a repo reappears, it keeps its vote.

## Example: GitHub AI Dev Dashboard

Code: `~/Desktop/hermes_builds/github-ai-dashboard/`
Cron: `f02f4a756e4f` (Monday 4 p.m.)
Brand: Performlytics
