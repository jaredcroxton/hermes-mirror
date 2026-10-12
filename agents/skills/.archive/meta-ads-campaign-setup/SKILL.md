---
name: meta-ads-campaign-setup
description: Use when Jared asks Brock to walk him through creating, configuring, and publishing a Meta (Facebook/Instagram) Ads campaign. Covers campaign structure, audience targeting, placements, ad creative, Advantage+ toggles, and publishing workflow.
---

# Meta Ads Campaign Setup

## When to load
Jared asks to create a Meta Ads campaign, post a reel/ad live on Facebook Ads Manager, or walk through Ads Manager step by step.

## Persona
Assume Alex Hormozi's voice. Direct, punchy, no fluff. Short sentences. Call things as they are. No hand-holding, no cheerleading, no over-explaining. If something is wrong, name it and fix it fast.

## Pre-flight checks
1. Confirm which ad account is active (PerformOS: `2413919059...`)
2. Confirm the objective (Traffic if no conversion pixel on destination; Sales if pixel is installed)
3. Confirm the destination URL (typically Eventbrite: `eventbrite.com.au/e/1992802394607`)
4. Confirm creative is 9:16 (1080x1920) for Reels/Stories. If 16:9, switch to manual placements Feed-only.

## Campaign structure

### Campaign level
- **Buying type:** Auction
- **Objective:** Traffic (default for Eventbrite without pixel) or Sales
- **Campaign name:** `CREW-Workshop-Cold-TOF-MonthYear`
- **Budget:** $20/day for testing. Do not touch for 72 hours minimum.
- **Bid strategy:** Highest volume
- **A/B Test:** ON if running two creatives. Leave OFF for single ad.

### Ad set level — Audience
- **Advantage+ audience:** ON
- **Custom audiences:** Skip unless warm list exists
- **Age:** 25-55+
- **Gender:** All
- **Location:** Brisbane +50mi, Gold Coast +25mi. Exclude NSW. Remove redundant suburbs already inside radii.
- **Detailed targeting:** ONE interest only. "Artificial intelligence" or similar. Do not stack interests — each layer chokes delivery.

### Ad set level — Placements
- **Advantage+ placements:** ON (if creative is 9:16)
- If 16:9 creative: OFF. Manual placements: Feed only (both platforms), In-Stream, Video Feeds.
- **Placement value rules:** None

### Ad level — Creative
- **Ad name:** `ReelName-V1`
- **Identity:** Perform OS (FB Page), performos_au (IG)
- **Website URL:** Eventbrite link
- **UTM parameters:** `utm_source=meta&utm_medium=paid&utm_campaign=crew-workshop-tof&utm_content=reel-name`
- **Primary text:** 3 lines max. Pattern-interrupt hook on line 1. Call to action on line 2. Scarcity on line 3.
- **Headline:** Short and direct (e.g. "One-Day AI Build Workshop")
- **Description:** Supporting detail (e.g. "Hands-on Claude Code. No coding experience needed. August 29th, Park Regis North Quay.")
- **CTA:** "Learn More"
- **Website highlights:** OFF (don't pull Eventbrite thumbnails)
- **Website summaries:** ON (selling points are useful)

### Advantage+ creative enhancements
Leave exactly ONE toggle ON: **Add overlays.** Turn OFF everything else:
- Video touch-ups → OFF
- Expand image → OFF
- Add music → OFF
- Text improvements → OFF
- Add details to ad layout → OFF
- Flex media → OFF

The campaign score will drop from 100 to ~98. Ignore it. Meta wants you to run everything. You want creative control.

### Essential enhancements
Leave all four ON: Relevant comments, Enhance CTA, Adjust brightness and contrast, and the fourth.

### Before publishing
- Verify the date in the description is correct
- Verify the Eventbrite URL resolves
- Check "All errors have been resolved" in ad preview

### After publishing
- Do not touch for 72 hours minimum
- Do not adjust budget, audience, or creative during the learning phase
- Check back at day 4 to assess CTR, CPC, and link clicks

## Key Hormozi principles for Meta Ads
1. Creative is the targeting. Don't over-layer interests.
2. One hook. One promise. One CTA. Complexity kills conversion.
3. $20/day is plenty to test. Don't scale until you have data.
4. Broad audiences win. Let the algorithm find the buyers.
5. UGC/talking-head beats motion graphics for cold audiences.
6. 72 hours of silence after publish. No fiddling.

## Reference files
- `references/performos-account-config.md` — Account IDs, pixel, Eventbrite URL, geo targeting, UTM template. Load this for every campaign setup session.
