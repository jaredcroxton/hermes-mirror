---
name: meta-ads-hormozi-campaign
description: "Use when Jared asks Brock to set up or walk through a Meta (Facebook/Instagram) Ads campaign — creative review, campaign architecture, targeting, copywriting, A/B testing, and post-launch discipline. Hormozi-style: direct, punchy, no fluff."
category: marketing
---

# Meta Ads Campaign Setup (Hormozi Style)

## When to load

Load this skill when Jared:
- Asks to launch a Meta/Facebook/Instagram ad campaign
- Hands over creative assets (reels, images) for ad review and ranking
- Wants a step-by-step walkthrough of Ads Manager
- Wants an A/B test set up
- Asks "which reel should I use" for a Meta ad
- Needs copywriting guidance for ad creative

## Core principles

1. **Creative is targeting.** The reel does the filtering. Keep audience broad. Let Advantage+ find buyers.
2. **Talking head > motion graphics for cold audiences.** Face-to-camera builds trust. Motion graphics and abstract explainers are retargeting-only material.
3. **One variable per test.** A/B test changes ONE thing. Same copy, same audience, same budget. Different creative only.
4. **Don't touch it for 4 days minimum.** The algorithm needs data. Fiddling in the first 48 hours is the number one killer of Meta campaigns.
5. **Meta's AI suggestions are mostly upselling.** Campaign score doesn't matter. Ignore "Flex media," "Text improvements," and "Expand image." They dilute control in exchange for a higher score number.

## Creative review for cold audiences

When reviewing reels for Meta ads, rank by hook strength.

### Tier 1 — Use for cold audiences
- **Pattern-interrupt hooks:** "It is actually noise," "Stop doing X," "You're being lied to about Y"
- **Value-promise hooks:** "You're going to learn," "Then you never have to," "In 5.5 hours you'll"
- **Format:** Talking head, UGC style, face visible within the first second
- **Length:** 30-45 seconds

### Tier 2 — Retargeting only
- Motion graphics only (no human face)
- Abstract explainer concepts ("Your second brain," "Shared context")
- Pure kinetic typography
- People who already know the brand will watch; cold audiences won't

### What kills a cold-audience reel
- No face visible in the first 3 seconds
- Abstract concept as the hook instead of emotion or pain
- "Explainer" framing instead of "problem" framing
- Too polished — looks like a corporate ad, not a person sharing something

## Campaign architecture

### Campaign level
- **Objective:** Traffic (if no conversion pixel on destination) or Sales (if pixel installed)
- **Campaign budget:** $20/day starting point for tests
- **Bid strategy:** Highest volume
- **A/B test:** ON for creative testing. Let the market decide which hook wins.

### Ad set level
- **Advantage+ audience:** ON
- **Age:** 25-55+ (tighten from the default 18-65+)
- **Gender:** All
- **Location:** Primary city + 40-50mi radius. Remove redundant suburbs already inside the radius.
- **Detailed targeting:** ONE interest stack max. Do not layer interests — each layer narrows the pool.
- **Advantage+ placements:** ON (if creative is 9:16 vertical)

### Ad level — creative setup
- **Website summaries:** ON — let Meta pull selling points from the destination URL
- **Website highlights (images):** OFF — don't let third-party thumbnails compete with the reel
- **Selling points checkbox:** ON. These tags show as overlays on the ad.

### Ad level — Advantage+ creative enhancements
Only ONE toggle ON: **Add overlays.**

Turn OFF:
- Video touch-ups — lets Meta crop/stretch your content
- Expand image — irrelevant for video ads
- Text improvements — lets Meta shuffle your words around
- Add music — dilutes your audio
- Flex media — generates unapproved ad variations
- Add details to ad layout

### Ad level — copy structure

**Primary text:** Three lines max.
- Line 1: Hook / pattern interrupt
- Line 2: What to do
- Line 3: Scarcity / urgency

**Headline:** Short and descriptive.

**Description:** One line of practical details (date, location, requirements).

**CTA:** "Learn More" preferred over "See details" or "Sign Up."

### Tracking
- UTM parameters in Tracking → URL parameters:
  `utm_source=meta&utm_medium=paid&utm_campaign=campaign-name&utm_content=ad-variant`

## Common Ads Manager UI pitfalls

### "Review and publish" can refer to any draft
The blue "Review and publish (N)" button at the top right aggregates ALL pending drafts across the account. It may pull up an unrelated ad. If the modal shows the wrong ad, close it. The ad you're working on may already be submitted.

### "Processing" means already submitted
If an ad shows "Processing" in the Delivery column, it has already been published. Meta is encoding the media. It will flip to "Active" automatically. No further action needed.

### Aspect ratios and placements
- **9:16 (1080x1920):** Fills Reels and Stories natively. No pillarboxing.
- **16:9:** Will NOT fill Reels. Meta pillarboxes it with black bars. Use manual placements (Feed-only) or re-export as 9:16.
- **4:5 (1080x1350):** Compromise. Works in Feed and most placements but not full-screen Reels.

### Meta AI assistant popup
The Meta AI chat sidebar is noise. Close it immediately.

### Advantage+ image generation popup
When Meta generates static AI images from your reel and destination URL, let it finish. These fill placements where video won't run (Right Column, some Banner spots). They supplement your reel, not replace it.

## Post-launch rules

1. **No Ads Manager for 4 days.** No peeking, no budget fiddling, no pausing.
2. **Day 4 review:** Check CTR, CPM, CPC. Kill anything below 0.8% CTR on cold traffic.
3. **Day 7 review:** Check conversions. The winner should be clear.
4. **Scaling:** If CPA is within target, increase budget by 20-30% every 3 days. Don't double overnight.

## Naming conventions

- Campaign: `[Product]-[Stage]-[Temperature]-[Month][Year]` — e.g., `CREW-Workshop-Cold-TOF-July2026`
- Ad set: `[Targeting description]` — e.g., `Brisbane-Broad-AI-Interest`
- Ad: `[Creative-Name]-V[Number]` — e.g., `AI-Noise-Reel-V1`

## User preferences for this workflow

- Guide step by step. Don't dump the whole plan at once.
- Give exact button locations when the user is stuck ("top right," "blue button next to Discard drafts").
- Hormozi persona: direct, punchy, no hedging. Call bad creative out. Name the winners clearly.
- When the user says "??" — they're lost. Be more specific about what's on their screen and what to click.
- Don't navigate for them unless explicitly asked. Walk them through their screen.
- One instruction per message when they're inside Ads Manager. Don't queue up three steps at once.

## Reference files

- `references/performos-meta-account.md` — Ad account ID, pixel ID, pages, Eventbrite URL, and other account-specific details.
