# Australian Retail and Travel Site Blocking Patterns

## The pattern

Australian retail and travel sites use aggressive bot detection. Headless browsers (both Hermes built-in browser and browser-use/Playwright) are blocked by all major players. Firecrawl MCP often succeeds on the same pages because it routes through API-level access that bypasses browser fingerprinting.

## Blocked sites (confirmed 01 June 2026)

| Site | Blocker | Error |
|------|---------|-------|
| Coles | Imperva / hCaptcha | Iframe wall with hCaptcha challenge |
| Woolworths | Edge/WAF | "Access Denied" at the door |
| Jetstar | Akamai CDN | `net::ERR_HTTP2_PROTOCOL_ERROR` |
| Skyscanner | Custom captcha | "Are you a person or a robot?" |
| Kayak | Custom bot page | "What is a bot?" |
| Expedia | Custom captcha | "Show us your human side..." |
| Flight Centre | Redirect | 404 on direct search URL |
| Webjet | Redirect | 404 on direct search URL |

## What works

### Google Flights
- **Search:** Works. Can navigate, select dates, see results, compare prices.
- **Pricing/booking page:** Hangs at "Getting prices." The pricing API call fails in headless mode.
- **Calendar pricing grid:** Works. Dates with prices render correctly.

### Firecrawl MCP
- **Coles:** Full product search results extracted. Same URL blocked by browser → works via Firecrawl.
- **Woolworths:** Full product search results extracted. Same URL blocked by browser → works via Firecrawl.
- Method: `POST https://api.firecrawl.dev/v1/scrape` with `{"url": "...", "formats": ["markdown"], "onlyMainContent": true}`

## What would unlock these sites

Residential proxies (Browserbase Scale plan, ~$200/month) and advanced stealth (`BROWSERBASE_ADVANCED_STEALTH=true`). These route through real residential IPs and spoof browser fingerprints. Without these, Australian retail and travel sites are a wall for headless browsers.

## Technique: Firecrawl fallback

When a site blocks the browser:

1. Try `browser_navigate` first.
2. If blocked (captcha, access denied, HTTP2 error), immediately pivot to Firecrawl MCP.
3. Use the same URL. Firecrawl often succeeds where the browser fails.
4. Parse the markdown output for structured data.

DO NOT loop retrying the browser on blocked sites. One attempt, then Firecrawl.
