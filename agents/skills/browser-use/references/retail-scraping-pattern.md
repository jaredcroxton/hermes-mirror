# Australian commerce site scraping & automation

Australian retailers AND travel sites aggressively block headless browsers. This reference captures which sites succeeded and failed with each approach, organised by category.

## Pattern

1. Try Hermes `browser_navigate` first (fastest path)
2. If blocked (hCaptcha, Access Denied, iframe-only), try `browser_navigate` to homepage
3. If still blocked, fall back to Firecrawl MCP `firecrawl_scrape`
4. If Firecrawl also fails, tell the user the site is fully locked

For travel booking (multi-step interactivity, not just data extraction): Firecrawl cannot complete bookings. Skip to "tell the user the site is locked" after browser failure and provide the direct booking URL from Google Flights results.

## Site results (1 June 2026)

### Coles (coles.com.au)

| Method | Result |
|---|---|
| browser_navigate → /search | Blocked (Iframe-only, hCaptcha) |
| browser_navigate → homepage | Blocked (hCaptcha widget) |
| Firecrawl scrape → /search | **Worked** — returned full product listing with prices |

Products found: 10 pack ($21.00), 24 pack ($26.00), 30 pack ($40.00)

### Woolworths (woolworths.com.au)

| Method | Result |
|---|---|
| browser_navigate → /search | Blocked (Access Denied, Edge/WAF) |
| browser_navigate → homepage | Blocked (Access Denied, Edge/WAF) |
| Firecrawl scrape → /search | **Worked** — returned full product listing with prices |

Products found: 10 pack ($12.60 on special), 24 pack ($37.50), 30 pack ($40.00)

## Key lesson

Both Coles and Woolworths use aggressive bot detection at the door. Neither browser-use nor Hermes built-in browser tools can get past their walls. Firecrawl's proxy infrastructure bypasses both. For any Australian retail price comparison task, skip the browser attempt entirely and go straight to Firecrawl.

## Cart addition

Neither browser nor Firecrawl can add items to cart on these sites. Firecrawl extracts content only — no session state, no cart interaction. The user must click the product link and add to cart manually.

Always provide the direct product URLs so the user can complete the purchase in one click.

## Travel booking sites (1 June 2026)

### Google Flights (google.com/travel/flights)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Worked** — full search results visible, date selection functional |
| Select departing flight | Worked — showed return flight options |
| Select return flight → pricing page | **Failed** — stuck at "Getting prices" permanently. Page loads but JavaScript pricing API never resolves in headless mode |
| Direct Jetstar URL extraction | **Failed** — HTML contains no direct airline booking URLs |

Workaround: Google Flights is usable for **search and price discovery** only. Give the user the Google Flights results URL and let them click through to book in a real browser.

### Jetstar (jetstar.com)

| Method | Result |
|---|---|
| browser_navigate → homepage | **Failed** — `net::ERR_HTTP2_PROTOCOL_ERROR` (Akamai CDN block) |
| browser_navigate → booking search URL | **Failed** — same HTTP2 error |
| curl → HTML source | **Failed** — no usable content |

Jetstar blocks headless browsers at the CDN level. Entirely unreachable.

### Skyscanner (skyscanner.com.au)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Failed** — redirected to captcha page ("Are you a person or a robot?") |

### Kayak (kayak.com.au)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Failed** — redirected to "What is a bot?" page |

### Webjet (webjet.com.au)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Failed** — 404/redirect to "page flown away" |

### Flight Centre (flightcentre.com.au)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Failed** — redirected to error page |

### Expedia (expedia.com.au)

| Method | Result |
|---|---|
| browser_navigate → search URL | **Failed** — captcha ("Show us your human side...") |

## Key lesson for travel

Every major Australian travel booking site blocks headless browsers. Unlike retail (where Firecrawl can extract pricing), travel booking requires multi-step interactivity that Firecrawl cannot provide. The only viable path is:

1. Use Google Flights via browser for **search and price discovery** (it partially works)
2. Give the user the Google Flights URL with the best flight pre-selected
3. The user completes the booking in their real browser
