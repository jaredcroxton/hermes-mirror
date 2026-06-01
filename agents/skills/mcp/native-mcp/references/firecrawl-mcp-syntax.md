# Firecrawl MCP — Call Syntax Reference

Source: session 01 Jun 2026

## Connection
- **STDIO:** `npx -y firecrawl-mcp` (via Hermes MCP config in `config.py`)
- **mcporter:** available but scrape param resolution is buggy — see below

## Tool names (namespaced)
All tools are called as `firecrawl.<toolname>`:
- `firecrawl.firecrawl_scrape` — single URL scrape
- `firecrawl.firecrawl_map` — site URL map
- `firecrawl.firecrawl_search` — web search with optional extraction
- `firecrawl.firecrawl_crawl` — full site crawl

## Scrape tool schema
```
function firecrawl_scrape(
  url: string,           // required
  formats?: "markdown" | "html" | "rawHtml" | "screenshot" | "links" | "summary" | "changeTracking" | "branding" | "json",
  jsonOptions?: object,
  screenshotOptions?: object,
  parsers?: "pdf",
  // optional: pdfOptions, onlyMainContent, includeTags, excludeTags, waitFor, ...
)
```

## mcporter call syntax — KNOWN BUG

| Pattern | Result |
|---------|--------|
| `mcporter call firecrawl firecrawl_scrape "https://x.com" "markdown"` | ❌ "Invalid URL" |
| `mcporter call firecrawl firecrawl_scrape --params '{"url":"https://x.com"}'` | ❌ "expected string, received undefined" |

**Root cause:** firecrawl_scrape via mcporter has a parameter resolution bug — the SDK param is `url` but mcporter's generic call wrapper does not resolve it from either positional or JSON form.

**Workaround:** Use `web_extract` instead for page content. Same quality, no auth, instant.

## When to use what

| Task | Tool | Notes |
|------|------|-------|
| Read one article/page | `web_extract` | Fast, no setup |
| Read 5+ pages at once | `web_extract` (batch of 5) | One call |
| JS-rendered content | `browser_navigate` + `browser_snapshot` | Needs auth session |
| Pricing/product data | `web_extract` first | Firecrawl as backup if blocked |

## Known blocking pages (WAF / bot detection)
- Coles: hCaptcha
- Woolworths: WAF block
- Jetstar: Akamai bot detection
- Skyscanner: captcha
- Kayak: bot redirect
- Webjet / Flight Centre: 404
- Expedia: blocked
- Gmail / Google: requires authenticated session (headless gets login page)
