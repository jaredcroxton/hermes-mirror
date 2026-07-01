---
name: google-ads-search-campaign
description: Use when Jared asks Brock to build a Google Ads Search campaign for any product, service, or event. Covers product research, competitor landscape analysis, keyword strategy by intent grouping, negative keyword frameworks, responsive ad copy generation, campaign settings, budget forecasting, conversion tracking setup, and launch checklist. Works with or without an existing Google Ads account.
category: marketing
---

# Google Ads Search Campaign Builder

## When to load

Load this skill when Jared asks to:
- "build a Google Ads campaign"
- "set up ads for [product/event]"
- "be the Google Ads expert"
- "run search ads"
- "plan keywords and budget for ads"
- Any variant of launching paid search advertising

## Brock's role

Brock is the Google Ads expert. Jared wants pragmatic action, not certification paths. When Jared asks about Google Ads, be the expert — give him the plan, the keywords, the settings, the ad copy. Do not redirect him to Skillshop certification unless he explicitly asks for it.

## Workflow (6 phases)

### Phase 1: Product research
- Scrape the product/landing page using Firecrawl or web_extract
- Extract: product name, price, format, location (if physical), dates, seat capacity, unique differentiators, conversion event
- Identify the single conversion goal (purchase, signup, booking, etc.)
- If it's an Eventbrite event, the conversion event is the Order Confirmation page

### Phase 2: Competitor landscape
- Search for direct competitors advertising similar products in the same geography
- Pull competitor pricing, format, and positioning
- Identify the price gap and unique angle — this feeds ad copy
- Note free alternatives that need to be negative-keyworded out

### Phase 3: Keyword economics
- Use industry benchmarks to estimate CPC, CTR, conversion rate, and CPA
- Education industry (2026 benchmarks): CPC ~$2.40 AUD, CTR 3.78%, CVR 3.39%, CPA ~$45.56
- Australia average Search CPC: ~$4.12 AUD (varies by industry)
- Build keyword groups by intent level:

**Ad Group 1 — Intent Buyers (phrase match):** People actively shopping. Highest conversion probability. Core product terms + location + format.

**Ad Group 2 — Problem Aware (phrase match):** People who know they need the solution but haven't found the product yet. Outcome-focused terms.

**Ad Group 3 — Competitor Adjacent (phrase match):** People looking at alternatives. Competitor brand and format terms.

- Total: 15-25 keywords across 3 ad groups
- Do NOT use broad match. It bleeds budget on irrelevant queries.
- Do NOT use exact match only either — too restrictive for a new campaign. Phrase match is the sweet spot.

### Phase 4: Negative keywords (add BEFORE launching)
Build a negative keyword list from these categories:
- **Price qualifiers:** free, cheap, discount
- **Format mismatches:** online, remote, webinar, virtual
- **Wrong geography:** every capital city not in the target area
- **Wrong audience:** kids, school, university, TAFE, degree, diploma, internship, job, salary
- **Wrong intent:** certification, download, PDF, template, definition, what is

### Phase 5: Campaign architecture

#### Ad copy
- 15 headlines (max allowed). Pin the strongest to H1. Include price and unique differentiators.
- 4 descriptions (max allowed). Lead with the contrast against competitors.
- All headlines and descriptions should make sense individually — Google mixes them.
- Price in a headline lifts CTR.

#### Campaign settings
| Setting | Default recommendation |
|---|---|
| Campaign type | Search (NOT Performance Max) |
| Network | Search Network only. Uncheck partners and Display. |
| Location | Target city + 50km radius. Presence only, NOT "presence or interest." |
| Location exclusion | All other states/capitals |
| Language | English |
| Budget | Start at $10/day for events. Scale based on product price and timeline. |
| Bid strategy | Maximize Clicks with max CPC bid limit (set $4 for education, higher for other industries). Do NOT use Maximize Conversions until 15+ conversions accumulated. |
| Ad rotation | Optimize: Prefer best performing ads |
| Ad schedule | 6am-10pm local time. No point running overnight. |
| End date | Day before event (if event-based) |

### Phase 6: Budget forecast
Build a simple table:
- Daily budget × days until event = total spend
- Total spend ÷ estimated CPC = estimated clicks
- Estimated clicks × industry avg conversion rate = estimated conversions
- Check: is the cost-per-booking acceptable against the ticket price?

For events: every day delayed is a day of data lost. Launch ASAP.

## Conversion tracking (non-negotiable)

If the product uses Eventbrite:
1. In Google Ads: Tools → Conversions → New conversion action → Website
2. Set conversion value to the ticket price
3. Count: Every conversion
4. Click-through conversion window: 30 days
5. Copy Conversion ID and Conversion Label
6. In Eventbrite: Manage Events → Tracking Pixels → Google Ads conversion tag
7. Tag must fire on the Order Confirmation page

For non-Eventbrite products: Google Tag Manager is the fallback path.

## Launch checklist

Deliver this checklist to Jared every time:
1. Confirm Google Ads account active
2. Set up conversion tracking → get Conversion ID + Label
3. Paste conversion tag into booking platform
4. Build Search campaign with settings from Phase 5
5. Create 3 ad groups with keywords from Phase 3
6. Add ALL negative keywords from Phase 4 BEFORE launching
7. Add 15 headlines + 4 descriptions to responsive search ad
8. Set budget, bid strategy, max CPC bid limit
9. Launch
10. Check Search Terms report every 3 days — add new negatives
11. After 50 clicks: review CTR. Below 3%? Rewrite headlines.
12. After 5+ conversions: consider switching to Target CPA

## What NOT to do

1. **Never use Broad Match** on a small-budget campaign. It will match irrelevant queries and drain spend.
2. **Never use Performance Max** for a single-product, localised Search campaign. PMax pushes budget into Display and YouTube.
3. **Never skip conversion tracking.** If you do, you cannot optimise.
4. **Never set and forget.** Search Terms must be checked every 3 days in week one.
5. **Never let ads run past the event date** for event campaigns. Set the end date.

## Pitfalls

- **Jared says "skill shot" or mentions Skillshop:** He historically wants direct action, not certification. Be the expert and give him the plan. Only redirect to Skillshop if he explicitly asks for certification.
- **Over-researching:** Jared moves fast. Get the product data, competitor snapshot, benchmark CPC, and deliver the plan. Don't spend hours on marginal keyword variants.
- **Wrong match types:** Broad match on a $10/day budget will bleed 30%+ of spend on garbage. Phrase match is the starting default.
- **Missing conversion tracking:** The single biggest failure mode. Jared must set this up before launch or the entire campaign is untrackable spend.

## Reference files

- `references/crew-brisbane-campaign.md` — Full campaign plan for the CREW Brisbane workshop (8 Aug 2026, $299, 25 seats). Use as a worked example/template for future event campaigns.
