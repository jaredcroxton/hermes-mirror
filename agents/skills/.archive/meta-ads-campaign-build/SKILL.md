---
name: meta-ads-campaign-build
description: Use when Jared asks to build, launch, or walk through a Facebook/Instagram ad campaign live in Ads Manager. Covers campaign setup, creative selection, copy writing, audience targeting, and A/B testing with Hormozi-style directness.
category: marketing
---

# Meta Ads Campaign Build

## When to load

Load this skill when Jared asks to:
- "walk me through posting live on Facebook Ads"
- "build a campaign for [event/product]"
- "launch this ad"
- "set up an A/B test for..."
- "review these reels for Meta ads"
- "post these videos as ads"

## Persona

Assume the personality of an expert Meta ads buyer — direct, high-conviction, no fluff. Think Alex Hormozi style. Short punchy sentences. Call out bad creative immediately. Name risks clearly. The creative is the targeting.

## Creative Selection Principles

### For cold audiences (TOF)
- Talking-head / UGC video beats motion graphics every time. Face = trust = lower CPM.
- Motion-graphics-only reels are retargeting material, not cold-audience openers.
- The hook is the entire game. Rank reels by hook strength, not production value.
- Pattern-interrupt hooks ("It is actually noise") beat explainer hooks ("Here's how AI works").

### For retargeting / warm audiences
- Motion graphics and explainer content can work here.
- People already know who you are. Now you can educate.

## Campaign Setup Preferences

### Objective
- Traffic for Eventbrite/landing pages without pixel optimization.
- Sales if pixel is installed and purchase/registration events are firing.

### A/B Testing
- Test ONE variable at a time. Usually: different hooks (different videos) with identical copy.
- $20/day minimum budget split between A and B.
- Let run 4-7 days before touching anything. Do not adjust budgets, audiences, or copy during the test window.

### Audience Targeting
- Advantage+ audience: leave ON. Creative does the filtering.
- One interest stack max for cold audiences. Do not layer interests.
- Location: single city/metro + reasonable radius. Drop redundant suburbs already inside the radius.
- Age: tighten to likely buyer range (e.g., 25-55+). Don't waste budget on the tails.

### Placements
- Advantage+ placements ON when creative is 9:16 vertical.
- 16:9 horizontal creative requires manual placements: Feed only, no Reels/Stories.
- Threads placement warning: ignore. Ad still runs everywhere else.

### Advantage+ Creative Enhancements
- Add overlays: ON. Selling points tags add free signal on the reel.
- Everything else: OFF by default (Video touch-ups, Expand image, Text improvements, Add music, Flex media, Add details to ad layout).
- Advantage+ creative image generation: leave ON. Fills placements video can't reach (Right Column, Banners).
- Campaign score will drop when you turn these off. Ignore it. The score rewards enabling Meta AI features, not better performance.

## Copy Writing

### Primary text
- Three lines max.
- Line 1: hook / pattern interrupt.
- Line 2: what to do / value proposition.
- Line 3: scarcity or close.
- Example: "Most of what you hear about AI is noise. / Come build something real. One day. In person. Brisbane CBD. 25 seats only."

### Headline
- Short. Descriptive.
- Example: "One-Day AI Build Workshop"

### Description
- Supporting detail. Date, location, requirements. One line.
- Example: "Hands-on Claude Code. No coding experience needed. August 29th, Park Regis North Quay."

### Call to action
- "Learn More" for consideration-phase traffic.
- Not "Shop Now" or "Sign Up" unless direct purchase flow.

## Walkthrough Flow

1. **Orient** — Screenshot Ads Manager. Identify account, existing campaigns, what stage Jared is at.
2. **Campaign level** — Naming convention: `[Product]-[Audience]-[Funnel Stage]-[MonthYear]`. Objective: Traffic unless pixel ready for Sales. A/B test OFF unless explicitly testing.
3. **Ad set level** — Location (city + radius), age (tighten), gender (all), one interest max. Advantage+ audience ON. Daily budget $20.
4. **Ad level** — Upload video. Write primary text, headline, description. Set CTA to Learn More. Strip all Advantage+ creative enhancements except Add overlays. Add UTM parameters in Tracking: `utm_source=meta&utm_medium=paid&utm_campaign=[campaign-name]&utm_content=[ad-name]`.
5. **Creative setup** — Website summaries ON, Website highlights OFF. Let Meta AI generate static images but don't let them crowd out the video.
6. **Review** — Check date accuracy. Check Threads placement warning (ignore). Check campaign score drop (ignore). Hit Publish.
7. **A/B test** — Duplicate campaign. Swap ONE variable (almost always the video/creative). Identical audience, copy, budget. Let both run 4+ days. Winner declared by Meta or by cost per result.

## Pitfalls

- Do NOT stack multiple interests. Each layer narrows AND, choking delivery at low budgets.
- Do NOT touch the ad in the first 72 hours. Let the algorithm learn.
- Do NOT let Meta auto-generate primary text. Write it manually.
- Do NOT use 16:9 video with Advantage+ placements. It pillarboxes in Reels and Stories.
- Do NOT trust Meta's campaign score as a quality metric. It rewards enabling more Meta AI features.
- Do NOT forget UTM parameters. Without them, you can't attribute ticket sales to specific ads.
- Do NOT leave wrong dates in copy. Verify against the actual event date before publishing.
- Do NOT enable Add music, Flex media, or Text improvements. They dilute the ad.
