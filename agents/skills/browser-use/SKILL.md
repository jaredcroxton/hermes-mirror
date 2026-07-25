---
name: browser-use
description: "Use browser-use (Python library, 96K+ stars) for complex web automation: multi-step browser tasks, form filling, data extraction, and AI-driven web navigation. Installed locally at /Users/jc/.local/bin/python3.11 with Playwright Chromium."
version: 1.0.0
author: PerformOS / Jared Croxton
metadata:
  hermes:
    tags: [browser, automation, web, agents, scraping, ai]
---

# Browser-Use Skill

browser-use is an AI-native browser automation framework that lets LLMs control a real browser through Playwright. 96K+ GitHub stars. It is more powerful than Hermes' built-in `browser_navigate` / `browser_click` tools for complex multi-step web tasks.

## What it can do

- Navigate websites and interact with forms, buttons, dropdowns
- Extract structured data from web pages
- Fill out multi-page forms
- Log into services and perform account actions
- Scrape dynamic content that requires JavaScript rendering
- Execute multi-step workflows like "find the cheapest flight from SYD to MEL next Friday"
- Run any task an AI agent would do in a browser

## Installation (already done)

```bash
# Installed on Jared's Mac
/Users/jc/.local/bin/python3.11 -m pip install --break-system-packages browser-use
/Users/jc/.local/bin/python3.11 -m playwright install chromium
```

Package: `browser-use` v0.12.9

## How agents call browser-use

Agents invoke browser-use via terminal. Use this exact pattern, passing the API key directly:

```python
/Users/jc/.local/bin/python3.11 - <<'PY'
import asyncio
from browser_use import Agent, Browser
from browser_use.llm.google import ChatGoogle

# Read key directly to avoid env-var newline issues
key = None
with open('/Users/jc/.hermes/.env') as f:
    for line in f:
        s = line.strip()
        if s.startswith('GOOGLE_API_KEY=*** and not line.lstrip().startswith('#'):
            key = s.split('=',1)[1].strip()
            break

async def main():
    llm = ChatGoogle(model='gemini-2.5-flash', api_key=key)
    browser = Browser(headless=True)
    agent = Agent(
        task="<plain English task>",
        llm=llm,
        browser=browser,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
PY
```

DO NOT set GOOGLE_API_KEY as an environment variable. Pass it directly to ChatGoogle. Passing via env var causes newline header injection errors.

## LLM Providers

browser-use needs its own LLM provider. Options in order of preference for Jared's setup:

1. **ChatGoogle** — free tier. Requires `GOOGLE_API_KEY` in the active Hermes profile `.env`. Get key: https://aistudio.google.com/apikey. Use model `gemini-2.5-flash` for fast, free, reliable browser automation.
2. **ChatAnthropic** — requires `ANTHROPIC_API_KEY`.
3. **ChatBrowserUse** — browser-use's own API. Requires `BROWSER_USE_API_KEY`.
4. **ChatOpenAI** — requires `OPENAI_API_KEY`.

## When to use browser-use vs Firecrawl MCP vs Hermes built-in browser

| Task | Use |
|---|---|
| Single URL text extraction | Firecrawl MCP `firecrawl_scrape` |
| Full site crawl to structured data | Firecrawl MCP `firecrawl_crawl` |
| LLM-powered structured extraction | Firecrawl MCP `firecrawl_extract` |
| Quick page check, simple click | Hermes `browser_navigate` + `browser_click` |
| Multi-step form fill | browser-use |
| Dynamic scraping across pages | browser-use |
| Login + perform actions | browser-use |
| Extract tables/repeated data | browser-use |
| Interact with a complex SPA | browser-use |
| "Give me the contents of this URL" | Firecrawl |
| "Do this thing on this website" | browser-use |

Firecrawl is a scraping API — fast, single-call, returns clean markdown/JSON. browser-use is a real browser driven by an LLM — slow, multi-step, but can interact. They complement each other.

## Australian commerce sites: bot detection patterns

Australian retailers AND travel booking sites aggressively block headless browsers. The pattern varies by category:

### Retail (Coles, Woolworths)

Both block headless browsers with hCaptcha and WAF rules. **Firecrawl MCP can bypass these** for data extraction (product listings, prices). Pattern: try browser first → if blocked → Firecrawl scrape → if that fails → tell user.

### Travel (Jetstar, Skyscanner, Kayak, Webjet, Flight Centre)

Every major Australian travel site blocks headless browsers at the CDN/WAF level. **Firecrawl cannot help here** because booking requires multi-step interactivity (search → select → fill passenger details → pay), not just data extraction. Google Flights partially works for search and price discovery but its pricing/booking page hangs in headless mode.

**Travel booking workflow**: use Google Flights via `browser_navigate` to search and identify the best flight → give user the Google Flights results URL → user completes booking in their real browser.

**Do not attempt direct airline/OTA booking in headless mode.** It will fail. Give the user the Google Flights URL and stop.

See `references/retail-scraping-pattern.md` for per-site results across both categories.

## Pitfalls

1. **Playwright requires Chromium installed.** Run `playwright install chromium` first.
2. **Headless mode recommended for agents.** Set `Browser(headless=True)`.
3. **Timeouts.** Complex tasks can take 60-120s. Set generous terminal timeouts.
4. **Gemini rate limits and 503s.** `gemini-2.5-flash` is reliable but can hit demand spikes. 503 errors are temporary — browser-use will retry internally. The key must be Tier 1 (billing enabled) for 1,500 RPM. Free-tier keys are limited to 5 RPM and will exhaust almost immediately.
5. **Google blocks headless.** Some sites (Google, LinkedIn) detect Playwright. Use `use_cloud=True` for stealth browsing if needed.
6. **Python version.** Requires Python 3.11 or higher. Use `/Users/jc/.local/bin/python3.11`.
7. **Path.** The `browser-use` CLI scripts are at `/Users/jc/.local/share/uv/python/cpython-3.11.15-macos-aarch64-none/bin/` but agents should import the library directly via Python, not use the CLI.
8. **Do NOT pipe API keys through heredoc.** The `<<'PY'` heredoc pattern causes newline/header injection errors when the API key contains special characters. Write scripts to temp files instead, or pass the key directly to `ChatGoogle(api_key=key)`.
9. **Tier 1 billing required.** Jared's Google API key must have billing enabled (Tier 1, not Free) to get 1,500 RPM. Keys created in AI Studio default to Free tier. The fix: go to AI Studio → click the dollar sign on the key → set up billing.
10. **Google Flights pricing page hangs.** After selecting both departing and return flights, Google Flights navigates to a pricing/booking page that shows "Getting prices" permanently. The JavaScript pricing API never resolves in headless mode. Do not retry — it will not resolve. Give the user the search results URL instead.
11. **`$` characters in API keys break bash substitution.** The Firecrawl API key contains literal `$` characters. When used in `curl -H "Authorization: Bearer $VAR"`, bash treats `$` as variable expansion. Always use `python3 -c` with `subprocess` or `urllib.request` for API calls that involve keys with special characters — never bare curl with double-quoted strings. Single-quoted heredocs (`<<'EOF'`) also work but require the key to be read from file, not interpolated.
12. **Unicode em dashes and special characters break JavaScript in embedded data.** When scraping text from websites that contains em dashes (—, U+2014), en dashes (–, U+2013), or curly quotes, these characters will silently corrupt JavaScript when the data is embedded in a `<script>` tag or JSON inside an HTML file. Always sanitize scraped text before embedding: `text.replace('\u2014', '--').replace('\u2013', '-').replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')`. This applies to any workflow where scraped text goes into an inline `<script>var DATA = ...;</script>` block.
13. **`file://` protocol blocks `fetch()` to local JSON files.** When building HTML dashboards that load data from local JSON files via `fetch('data.json')`, the `file://` protocol triggers CORS errors in all modern browsers. The fix: embed the data as an inline `<script>` variable instead. Pattern: `var BATCHES = {'batch1': [...], 'batch2': [...]};` directly in the HTML, no fetch needed. This also makes the dashboard fully self-contained and portable — a single HTML file with zero external dependencies.

## JavaScript extraction via browser_console (complement to browser-use)

For single-page structured data extraction where you just need to pull items from a list (like GitHub trending repos, search results, product listings), Hermes' built-in `browser_console` with `Array.from(document.querySelectorAll(...)).map(...)` is faster and more reliable than spawning browser-use. It runs directly in the page context with zero latency.

### Pattern: Extract trending repos from GitHub

```javascript
// Navigate to the page first with browser_navigate, then:
Array.from(document.querySelectorAll('article.Box-row')).map(a => ({
  name: a.querySelector('h2')?.textContent?.trim()?.replace(/\s+/g, ' '),
  stars: [...a.querySelectorAll('a')].filter(l => l.href?.includes('stargazers')).pop()?.textContent?.trim(),
  desc: a.querySelector('p')?.textContent?.trim()?.substring(0, 80)
}))
```

### Pattern: Extract with growth data

```javascript
Array.from(document.querySelectorAll('article.Box-row')).map(a => {
  const stars = [...a.querySelectorAll('a')].filter(l => l.href && l.href.includes('stargazers')).pop();
  const growth = [...a.querySelectorAll('span,div')].find(el => el.textContent && el.textContent.includes('stars this week'));
  return {
    name: a.querySelector('h2 a')?.href?.replace('https://github.com/',''),
    stars: stars?.textContent?.trim(),
    growth: growth?.textContent?.trim()
  };
})
```

### When to use browser_console vs browser-use

| Task | Use |
|---|---|
| Extract a list of items from one page | `browser_console` JS extraction |
| Click through pagination | `browser_console` + `browser_click` |
| Multi-step form fill across pages | `browser-use` |
| Login + perform authenticated actions | `browser-use` |
| Scrape all items across many pages | `browser-use` or Firecrawl MCP crawl |
| Quick structured data from a list page | `browser_console` (instant, no library overhead) |

The `browser_console` approach works on any site that renders data into the DOM. It bypasses bot detection for data extraction because it runs after the page has already loaded. It does NOT work for sites that block the initial page load (Coles hCaptcha, Woolworths WAF).
