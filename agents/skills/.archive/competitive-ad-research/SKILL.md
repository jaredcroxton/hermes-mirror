---
name: competitive-ad-research
description: Use when Jared asks Brock to research competitor Facebook/Instagram advertising — Ad Library searches, competitive intelligence for CREW workshops, PerformOS products, or Accor Plus positioning. Covers multi-tool research workflow (browser → web search → Firecrawl), competitor profiling, and strategic implications reporting.
category: marketing
---

# Competitive Ad Research

## When to load

Load this skill when Jared asks to:
- "search Facebook Ad Library for..."
- "what ads are competitors running..."
- "competitive intelligence on [X] training/workshop..."
- "who's advertising [X] in Australia..."
- "find top performing ads for..."
- Research competitor advertising strategy
- "what does [competitor product] cost..." or "how does [competitor] pricing work..."
- "what's [competitor's] data compliance / privacy policy..."
- Research a competitor AI tool, SaaS product, or platform for pricing, features, or compliance

## Research workflow

### Phase 1: Facebook Ad Library (browser)
1. Navigate with query params pre-built: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AU&q=...&search_type=keyword_unordered&sort_data[mode]=total_impressions&sort_data[direction]=desc`
2. Expect the first navigation to return an empty snapshot — Facebook is JS-heavy. Wait, scroll, then use browser_vision to see what rendered.
3. Facebook bot detection WILL eventually block browser automation. Expect this. When it happens, the page goes blank (empty snapshot, element_count=0).
4. You typically get 2-3 successful page loads before blocking kicks in. Prioritise the most important searches first.

### Phase 2: Web search fallback
When Facebook blocks the browser, pivot to web_search with targeted queries:
- `Facebook ads "in person" "AI training" Australia workshop Claude Code`
- `"[topic]" workshop Brisbane in-person paid training [year]`
- `[competitor name] Facebook ad library [topic] impressions Australia`
- Search for competitor names + "Facebook" + "ad" + the topic
- Use `site:facebook.com` operator for Facebook posts and pages

Web search often surfaces Facebook posts and pages that the Ad Library browser approach misses.

### Phase 3: Deep scrape competitor pages
Once competitors are identified, use web_extract or Firecrawl scrape on their actual websites (not Facebook) to get pricing, format, dates, trainer bios, and positioning. Facebook pages themselves cannot be scraped by Firecrawl — they block it.

### Phase 4: Firecrawl agent (optional, patience required)
Firecrawl agent can autonomously research Facebook Ad Library but takes 2-5+ minutes. Poll every 15-30 seconds with firecrawl_agent_status. Facebook often blocks it too — don't rely on it as the primary method. If it's still "processing" after 3-4 minutes, move on.

## What to capture for each competitor

For event/training competitors:
- Advertiser name and page/URL
- Price (incl. GST status)
- Format (in-person/online, duration, capacity)
- Date and location
- Trainer/credibility signals
- Content/curriculum summary
- Unique positioning angle
- Refund/cancellation policy
- Whether they're running active Facebook ads

For product competitors:
- Advertiser and product name
- Price point
- Key differentiators claimed in ads
- Target audience signals in ad copy
- Visual style of creative (from screenshots)

## Output format

Jared wants structured competitive reports with:
1. Direct competitors first (same format, same geography)
2. Adjacent competitors second (different format or geography)
3. Strategic implications section — what this means for CREW/PerformOS positioning
4. Tables for comparison data
5. Lead with the competitive insight, not the methodology
6. A recommended next step at the end

## Pitfalls

- Facebook Ad Library blocks browser automation after 2-3 page loads. Plan for this — get the most important searches done first.
- Firecrawl cannot scrape facebook.com URLs. Don't try.
- Don't spend more than 5-6 minutes on Facebook Ad Library. The web search fallback typically yields better results faster.
- The Facebook Ad Library sort-by-impressions is useful but actual impression counts aren't shown — only relative ordering.
- Internal products (CREW) won't appear in Ad Library. That's expected — you're researching the competitive landscape, not verifying your own ads.
- Be thorough on competitor pricing and positioning — this is what feeds Jared's strategic decisions.
- **Firecrawl/web_search outage fallback**: When Firecrawl or web_search return credit-exhausted errors, pivot to browser tools (browser_navigate → browser_snapshot → browser_console). For SPAs that redirect or hide content behind login, look for the API/platform documentation site (e.g., platform.kimi.ai instead of kimi.com) — these often have public pricing and policy pages. Use browser_console with `document.querySelector('main')?.innerText` to extract full page text when snapshots are truncated. The `execute_code` tool with `web_search` from `hermes_tools` can also work when the direct `web_search` tool fails.

## Reference files

- `references/crew-competitive-landscape-2026-07.md` — Current competitive snapshot for CREW workshop positioning: Spruik, Team 400, Brisbane Claude Masterclass, Net101, Get AI Ready, Claude Code Community Australia, and adjacent competitors. July 2026.
- `references/kimi-k3-pricing-compliance-2026-07.md` — Kimi K3 API pricing, consumer subscription tiers, data compliance analysis (Singapore-based, model training clause), and competitive positioning vs Claude/DeepSeek. July 2026.
