# Competitive Teardown for PerformOS

Methodology for scraping and analysing competitor positioning, pricing, and offering structure before content or strategy decisions.

Proven: 26 May 2026 — 10-competitor teardown for 12-week AI course pivot. Delivered actionable white space analysis and direct threat map.

## Process

1. **Identify targets:** List 8-12 competitors across direct (same offer), adjacent (same audience), and market-validator (different lane but validates demand) categories.

2. **Scrape structure:** Use browser navigate + snapshot + click for each competitor. Extract:
   - Primary headline / offer
   - Format (self-paced, cohort, 1:1, video, etc.)
   - Duration
   - Pricing model (subscription, one-time, contact sales)
   - Target audience
   - Key differentiator

3. **Pricing deep-dive:** Most competitors hide pricing. Check course pages, FAQ, pricing pages. Note whether pricing is one-time, subscription, or contact-sales gated.

4. **Output format:** Structured markdown per competitor with consistent fields. Summary table at top. Direct threat matrix at bottom.

5. **White space analysis:** Cross-reference all competitors against your offer. Identify what NO ONE is doing. These are your positioning claims and keyword targets.

## Direct threat classification

- **High threat:** Competitor in same geography, same pricing model, similar audience, has personalisation angle
- **Medium threat:** Same geography or same pricing model, but different format/audience
- **Low threat / validator:** Different lane entirely but validates market demand

## Key insight pattern

Always answer: "What combination of features does no competitor offer simultaneously?" This is the positioning white space. For PerformOS, the combination was: 12-week structured + personalised 1:1 + custom learning styles + $499 one-time + "professionals who feel left behind."

## Tools

- Prefer browser tools (navigate, snapshot, click) over web_extract for competitor sites with dynamic pricing or hidden content
- Delegate to subagent with browser + web toolsets for full 10-competitor scrapes
- Budget ~5 minutes per competitor, ~40 tool calls total for 10 competitors
