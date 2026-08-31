# GitHub AI Dashboard Weekly Refresh Pattern

Use when the cron job or Jared asks to refresh the GitHub AI Dashboard (top 15 AI repos).

## Dashboard identity

- Local directory: `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/`
- Source data: `repos.json` (15 repos, each with name, description, stars, growth, growthLabel, category, url, whyMatters)
- Archive: `archive/repos_YYYY-MM-DD.json` (previous week's data, copied before overwrite)
- Dashboard HTML: `dashboard.html` (PerformOS dark theme, tabbed layout)
- This is a LOCAL-ONLY artifact. No GitHub push. No Vercel deploy.

## Category structure (3 tabs, ~5 each)

1. **Trending Today** — repos appearing on GitHub Trending (daily or weekly)
2. **Fastest Growing** — repos with highest star velocity this week
3. **Most Starred** — repos with highest absolute star count

## Source strategy

Scrape four sources for comprehensive coverage. Use `browser_navigate` + `browser_console` for all extraction (not firecrawl_scrape -- browser_console with querySelectorAll is faster and more reliable for GitHub pages). The preferred combination is: **Topics page** (top AI repos + approximate stars) → **GitHub API** (exact stars + descriptions) → **Trending pages** (velocity data) → curate 15.

### Source 1: GitHub Topics (AI-tagged, sorted by stars) — BEST FIRST SOURCE

URL: `https://github.com/topics/ai?o=desc&s=stars`

This page lists AI-tagged repos sorted by stars. It has a clean `article` DOM structure and returns the top AI repos in one page. Star counts are abbreviated (e.g., "383k", "253k") so supplement with API for exact numbers.

Extraction expression (browser_console):
```js
(() => {
    const articles = document.querySelectorAll('article');
    const results = [];
    articles.forEach(article => {
        const h3 = article.querySelector('h3');
        if (!h3) return;
        const links = h3.querySelectorAll('a');
        const nameParts = [];
        links.forEach(l => nameParts.push(l.textContent.trim()));
        const fullName = nameParts.join('/');
        const href = links.length >= 2 ? links[1].getAttribute('href') : '';
        const desc = article.querySelector('p') ? article.querySelector('p').textContent.trim() : '';
        const starText = article.textContent.match(/Star\s+([\d.]+k?)/);
        const starsRaw = starText ? starText[1] : '';
        let stars = 0;
        if (starsRaw.endsWith('k')) stars = Math.round(parseFloat(starsRaw) * 1000);
        else stars = parseInt(starsRaw.replace(/,/g, '')) || 0;
        const topics = Array.from(article.querySelectorAll('a[href*="/topics/"]')).map(a => a.textContent.trim());
        results.push({fullName, desc: desc.substring(0, 200), stars, starsRaw, href, topics});
    });
    return JSON.stringify(results.slice(0, 20));
})()
```

### Source 2: GitHub API — exact star counts and descriptions

After identifying candidate repos from the Topics page (or other sources), download exact data via GitHub's public API. This gives real star counts, full descriptions, topics, and language data.

**Cron-safe download pattern (no piped interpreters):**
```bash
# Download to temp files (never pipe to python3 in cron mode)
for repo in "openclaw/openclaw" "obra/superpowers" "NousResearch/hermes-agent"; do
  name=$(echo "$repo" | tr '/' '_')
  curl -s -o "/tmp/gh_${name}.json" "https://api.github.com/repos/${repo}"
done

# Process with standalone script (not piped)
python3 -c "
import json, glob
for f in glob.glob('/tmp/gh_*.json'):
    d = json.load(open(f))
    print(d.get('full_name'), d.get('stargazers_count'), (d.get('description') or '')[:200])
"
```

Key fields from API response: `stargazers_count` (exact integer), `description`, `topics`, `language`, `html_url`, `forks_count`, `updated_at`.

### Source 3: GitHub Trending (daily)
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

### Source 4: GitHub Trending (weekly)

Same extraction expression as daily, but match `stars this week` instead of `stars today`:
```js
const weekMatch = text.match(/(\d[\d,]*)\s*stars?\s*(this week)/i);
const weeklyGrowth = weekMatch ? parseInt(weekMatch[1].replace(/,/g, '')) : 0;
```

### Source 5: GitHub Search (most-starred AI repos)

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

**Tab allocation pattern (proven in 13 July 2026 session):** After collecting ~20 candidate repos with exact API data, sort all candidates by growth (weekly stars). Allocate the top 5 by growth to "Trending Today", the next 5 to "Fastest Growing", and pick the 5 with highest absolute stars from the remaining pool for "Most Starred". This guarantees no overlaps and clean 5-per-tab distribution. Signal labels follow the pattern: "Trending today #N", "Fastest growing #N", "Most starred #N".

## Dashboard BATCHES structure (critical)

The dashboard does NOT use a flat `const REPOS = [...]` array. It uses a `var BATCHES` object with dated batch keys, each containing a `repos` array:

```javascript
var BATCHES = {
  "20260803": {
    label: "Week of 03 August 2026",
    repos: [
      {"name":"block/buzz","description":"...","stars":21289,...},
      ...
    ]
  },
  "20260727": {
    label: "Week of 27 July 2026",
    repos: [...]
  }
};
```

The dashboard has TWO sets of tabs: **batch tabs** (switching between weeks) and **sort tabs** (Trending Now | Most Starred | Fastest Growing). Both use the `BATCHES[currentBatchId].repos` array and sort it client-side.

## Dual-file update workflow

This is a two-file update, not a single-file build:

1. **Archive last week first** — copy current `repos.json` to `archive/repos_YYYY-MM-DD.json` before overwriting.
2. **Write fresh repos.json** — use `write_file` with the full 15-entry JSON array. Verify with standalone `python3 -c` that it's valid JSON and has exactly 15 entries.
3. **Update dashboard.html BATCHES data** — do NOT use `patch` tool (it fails on nested JS object literals with mixed quoting). Use a Python positional-index approach instead:
   - Read the HTML file
   - Find the `var BATCHES = {` marker
   - Find the current week's batch key (e.g., `"20260803":`)
   - Find the `repos: [` array start within that batch
   - Find the next batch key (e.g., `"20260727":`) to locate the array end boundary
   - Use `rindex(']', ...)` to find the exact closing bracket before the next batch
   - Replace the array segment with the fresh serialized data
   - Write the result back
4. **Run em dash gate** on dashboard.html after updating.
5. **Add a new batch tab** — add a button in the `#batch-tabs` div for the new week and update the `BATCHES` object with the previous week's data moved to a historical key.

### Pitfall: regex replacement fails on nested JS objects

The `BATCHES` object uses mixed quoting (unquoted JS keys like `repos:` but double-quoted string keys like `"20260803":`). Regex-based replacement is fragile and often fails. The positional-index method (finding exact character offsets via `.index()` and `.rindex()`) is reliable. Always prefer it over regex for dashboard data updates.

## Data format (unified — repos.json and dashboard use the same fields)

Both `repos.json` and the dashboard's inline `REPOS` array use the same field names. This avoids dual-format drift and makes the weekly update a single write + replace operation.

```json
{
  "name": "openclaw/openclaw",
  "description": "One sentence description",
  "stars": 382737,
  "growth": 2800,
  "growthLabel": "2,800 stars this week",
  "category": "AI Agents",
  "url": "https://github.com/openclaw/openclaw",
  "whyMatters": "Personalized line tied to Jared's context"
}
```

**Field definitions:**
- `name`: owner/repo (e.g., "bojieli/ai-agent-book")
- `description`: one-sentence summary
- `stars`: exact integer star count
- `growth`: numeric growth (weekly or daily stars added)
- `growthLabel`: human-readable growth string (e.g., "15,909 stars this week" or "900 stars today")
- `category`: one of AI Agents, LLMs & Foundation Models, Developer Tools & Infra, Open Source AI Models, Productivity & Automation, Data & Analytics
- `url`: full GitHub URL
- `whyMatters`: personalized line tied to Jared's context

**Dashboard HTML format:** The BATCHES object's `repos` arrays use the exact same field names as repos.json. When updating, write fresh repos.json first, then use positional-index replacement to update the `repos` array in dashboard.html for the new batch. Tab allocation is determined by JavaScript sort functions, not a separate `signal` field.

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
- Fonts: Inter (body, display), JetBrains Mono (labels)
- TWO sets of tabs: batch tabs (week selector: e.g., 03 Aug 2026 | 27 Jul 2026) and sort tabs (Trending Now | Most Starred | Fastest Growing)
- All data inline in HTML via `var BATCHES = { "YYYYMMDD": { label, repos: [...] } }` structure (no fetch calls, no external JS)
- Header stats row: repos tracked, combined stars, categories, top category
- Single-column card grid with hover effects
- Each card: name (linked with GitHub icon), category badge, growth badge, star count badge, description, "Why this matters" callout

## First-build vs weekly update

**First build (dashboard.html does not exist):** Write the complete dashboard with `write_file`. Use the BATCHES structure with one initial batch entry. The HTML, CSS, JS, and embedded BATCHES data go in a single file. Include batch-switching tabs and sort tabs.

**Weekly update (dashboard.html exists):** Write fresh `repos.json` first. Archive last week's data. Then use Python positional-index replacement (NOT patch tool, NOT regex) to update the BATCHES object in the dashboard HTML. Add a new batch tab button for the current week. The CSS/HTML/JS structure stays unchanged; only the BATCHES data and batch tab markup are updated. This is faster and avoids regressions on the visual design.

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
- All repos have required fields: name, description, stars, growth, growthLabel, category, url, whyMatters
- All URLs start with `https://github.com/`
- dashboard.html has zero em dashes
- dashboard.html contains BATCHES object with the current week's batch key, tab switching functions, and stats row
- Extract the inline `<script>` block and run `node --check` against it before browser verification. Dashboard rebuilds can pass structural HTML checks while still failing at runtime because Python f-strings corrupt quoted JavaScript selectors such as `querySelector('[onclick="..."]')`.
- Browser verification confirms JavaScript actually executed: `typeof BATCHES === 'object'`, current batch id is defined, and five `.repo-card` elements render for each signal tab.
- Verify all three signal tabs, not only the default view: call `switchSignal('Trending Today')`, `switchSignal('Fastest Growing')`, and `switchSignal('Most Starred')` in the browser console and confirm each renders five `.repo-card` elements with the expected repo names.
- After browser verification, run one final file-level guard from the dashboard directory: confirm `repos.json` has 15 entries, `batch_YYYYMMDD.json` is a 15-item list, `dashboard.html` contains the intended current-week repos, old category labels from any previous run are absent, and em dash count is zero. This catches same-directory cron or parallel-process overwrites that can happen between the build and the final report.
- If the final guard shows the dashboard regressed after a successful refresh, immediately rerun the purpose-built `refresh_dashboard.py`, then repeat the script check, browser check, and final guard. Report only the final verified state.
- Previous week's batch data is preserved (not overwritten)
- New batch tab button exists in `#batch-tabs` for the current week
- Archive file exists at `archive/repos_YYYY-MM-DD.json`
