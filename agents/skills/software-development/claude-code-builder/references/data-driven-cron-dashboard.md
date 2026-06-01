# Data-Driven Cron Dashboard Pattern

Build pattern for dashboards that refresh weekly from external data sources.

## Architecture

Three-layer separation:

1. **Research agent** scrapes live data into JSON (repos.json)
2. **Build agent** consumes JSON and produces monolithic HTML dashboard
3. **Cron scheduler** runs weekly to refresh data and rebuild

## Step 1: Scrape fresh data

Delegate to a research subagent:

```text
Goal: Scrape GitHub for top 15 AI repos (5 trending, 5 most starred, 5 fastest growing).
Output: /Users/jc/Desktop/hermes_builds/<project>/repos.json
Schema: [{name, description, stars, growth, category, url, why, signal}]
```

Key rules:
- Every repo MUST have a real GitHub URL and real star count
- Do NOT fabricate data
- Skip repos Jared already knows (he will tell you which)
- Every "why" field personalised to Jared's context
- Include "signal" field (X trending, HackerNews #N, ProductHunt #N, or null)

## Step 2: Build dashboard

Delegate to Bob Builder via kanban or delegate_task:

```text
Goal: Build PerformOS/Performlytics-styled HTML dashboard from repos.json.
Output: /Users/jc/Desktop/hermes_builds/<project>/dashboard.html
Mode: LOCAL ARTIFACT ONLY. No GitHub push. No Vercel deploy.
```

Features:
- Category dropdown filter
- Per-card: name, description, stars, growth, GitHub link, signal badge, "Why this matters"
- Relevant/Not relevant checkbox per repo → localStorage
- Last-updated timestamp
- Archive section for future weeks

## Step 3: Cron

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

After every dashboard build, run:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('<dashboard path>')
c = p.read_text()
c = c.replace('\u2014', '-').replace('&mdash;', '-')
p.write_text(c)
print('Remaining:', c.count('\u2014') + c.count('&mdash;'))
PY
```

Count must be zero before delivering to Jared.

## Weekly archive

Before overwriting repos.json, copy to:

```text
/Users/jc/Desktop/hermes_builds/<project>/archive/repos_YYYY-MM-DD.json
```

Dashboard should show archive section if archive files exist.

## Relevance voting

Checkbox per repo stored in localStorage keyed by repo name. Persists across weekly refreshes. If a repo reappears, it keeps its vote.

## Example: GitHub AI Dev Dashboard

Code: `~/Desktop/hermes_builds/github-ai-dashboard/`
Cron: `f02f4a756e4f` (Monday 4 p.m.)
Brand: Performlytics
