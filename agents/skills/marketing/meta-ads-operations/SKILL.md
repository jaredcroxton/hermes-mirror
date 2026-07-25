---
name: meta-ads-operations
description: Use when Jared asks Brock to review video creative for Meta (Facebook/Instagram) ad suitability, launch campaigns in Ads Manager, or walk through campaign setup step by step. Covers creative review methodology, Hormozi-style ranking criteria, campaign structure (Advantage+ audience and placements OK; creative and budget stay manual), and Ads Manager navigation.
category: marketing
---

# Meta Ads Operations

## When to load

Load this skill when Jared asks to:
- "review these reels for ads"
- "which video should I run as a Facebook ad"
- "rank these videos for Meta"
- "take me through posting on Facebook Ads"
- "set up a Meta campaign"
- "walk me through Ads Manager"
- Review or launch Meta ad creative

## Creative review: the Hormozi framework

When reviewing video reels for Meta ad suitability, rank them ruthlessly. No hedging. Name the winners. Name the losers. Explain why in one sentence.

### The hierarchy (what actually stops the scroll)

1. **Hook strength** — Does the first two seconds create a pattern interrupt? Does it call out a lie, name a pain point, or make a bold claim? The hook IS the ad.
2. **Format** — Talking-head (face-to-camera) outperforms motion-graphics-only on Meta by 30-50% for cold audiences. Pure motion graphics is retargeting-only material.
3. **Point of view** — Does the creative take a stance, or is it neutral/educational? Neutral content doesn't convert. Debunking, calling out BS, and strong opinions stop thumbs.
4. **Promise** — What does the viewer get by watching to the end? A clear promise ("you're going to learn") keeps retention.
5. **Structure** — Does it have a clear arc? Hook → problem → solution → close. Talking-head bookends with graphics in the middle is a proven pattern.

### Output format

For each reel:
- Rank (#1 through #N)
- Verdict: Cold-audience ready / Retargeting only / Skip
- One-line reason
- Suggested placement in campaign (which audience, which objective)

Then a summary table. Then the campaign launch plan for the winners.

## Campaign setup: Ads Manager walkthrough

### Account navigation

Start at `adsmanager.facebook.com`. The user must be logged into Facebook in their own browser — you cannot authenticate for them.

If the quick-create modal appears (name fields for campaign/ad set/ad without objective selection), close it or click through, then switch to **Guided creation** — this gives full control over objective, budget, and placements.

Ignore the naming convention template popup. Close it.

## Screenshot-driven walkthrough protocol

This is the primary technique for guiding Jared through Ads Manager live. He shares his screen at each step — you analyze and direct.

### The loop

1. **Jared shares a screenshot** — usually via system screenshot tool
2. **You call vision_analyze** on the image URL. Ask for every field, button, dropdown, toggle, and value visible
3. **Respond with exactly what to do** — name the field or button verbatim as it appears on screen. No generic instructions. \"Click the '+ Create' button top-left\" not \"create a new campaign\"
4. **Jared acts, screenshots again** — loop continues

### Response format for each step

- **What you're seeing:** One sentence naming the current page/section
- **What to do:** Bullet list of specific actions with exact button/field names
- **Why:** One sentence of rationale. No more.
- **Next:** What screen to expect after the action

### Frustration signals

Jared sends \"??\" or garbled text (\"sone\") when:
- Something isn't where you said it would be
- He's on a different screen than you assumed
- Meta's UI has changed since your last instruction

When this happens: re-analyze the new screenshot. Re-orient. Don't double down on a wrong instruction.

## Meta AI creative setup (Website summaries and highlights)

When creating a Traffic or Sales ad with a destination URL, Meta scrapes the landing page and offers AI-generated extensions. This screen appears as the "Creative setup" step before the media upload.

### Which toggles to flip

- **Website summaries** — leave ON. The auto-extracted description and selling points are harmless and show as overlays. You'll override the important copy in the Text step.
- **Website highlights (Images)** — turn OFF. You don't want Eventbrite/Landing Page thumbnails crowding out your reel. The reel is the hero asset.
- **Discovery links** — leave OFF unless you have a specific multi-link strategy.

### Selling points approval

When you reach the Text sub-step within Creative setup, Meta shows extracted selling points as checkboxes:

- **Check "Selling points"** — these show as tag overlays beneath the video (e.g. "Build apps," "No coding exp," "5.5 hours"). Free signal. Good for stopping scrollers.
- **Leave "Product descriptions" unchecked** — write your own primary text instead.

### Advantage+ creative enhancements location

Jared will often ask where a specific toggle is. The "Add overlays" toggle (which enables selling-point tags) lives under:

**Advantage+ creative enhancements (expand the dropdown) → Add overlays → toggle ON**

It is NOT in the Website summaries section. It's further down the Ad Creative panel, collapsed by default. Expand the dropdown to reveal it.

### Campaign structure

Manual campaign. Never use Advantage+ Creative (the AI that rewrites your copy). Advantage+ audience and Advantage+ placements are fine — creative and budget control should stay manual.

Three levels:

**1. Campaign level**
- Objective: **Traffic** if no pixel on landing page. **Sales** if Meta pixel installed and firing on purchase/registration confirmation. **Leads** if using Instant Forms.
- Buying type: Auction
- Budget: Campaign-level daily budget ($20-50 AUD). Simple. Clean. One budget to manage.
- A/B test: ON when launching two creatives. Same audience. Same budget. Let the market pick the winner. Turn OFF when running a single proven creative.
- Naming: `CREW-[Product]-[Funnel Stage]-[Month][Year]` — e.g. `CREW-Workshop-Cold-TOF-July2026`

**2. Ad set level**
- One audience per ad set. Do not stack audiences.
- Advantage+ audience: Leave ON. Creative is your targeting. Advantage+ takes signals and finds responders. One interest as a directional signal is enough — do not stack interests.
- Age: 25-55+ default. Tighten upper bound if product skews younger.
- Gender: All. Don't touch.
- Location: Target city + 40-50km radius. Remove redundant sub-locations inside the main radius. Exclude states/countries that can't attend. Cut locations beyond 90 minutes travel for in-person events.
- Detailed targeting: **ONE interest.** Not three. Each layer narrows with AND logic. One broad interest (e.g. "Artificial intelligence") is enough — the creative does the rest.
- Placements: Advantage+ placements ON if creative is 9:16. If creative is 16:9, see placement rules below.

**3. Ad level**
- Creative: Upload directly (not via Instagram post ID — native upload performs better)
- Primary text: Three lines max. The formula: **Hook → Action → Scarcity.** Line 1 stops the scroll. Line 2 tells them what to do. Line 3 creates urgency. No emoji spam. One clear CTA.
- Headline: Under 40 characters. Direct. Usually "[Product] [Format]" — e.g. "One-Day AI Build Workshop"
- Description: One line of practical detail — date, venue, key qualifier. e.g. "Hands-on Claude Code. No coding experience needed. August 21st, Park Regis North Quay."
- CTA button: "Learn More" or "Sign Up" depending on the destination
- Destination: Event page, landing page, or lead form URL
- UTM parameters: Always add. Structure: `utm_source=meta&utm_medium=paid&utm_campaign=[campaign-slug]&utm_content=[creative-name]`. Add these in the Tracking section under URL parameters.

## Placement rules by aspect ratio

This is the single most common mistake. Know the format rules cold.

### 16:9 horizontal video

Will NOT natively fill Reels or Stories. Meta pillarboxes it — black bars on both sides. Looks amateur.

**Can run in:** Facebook Feed, Instagram Feed, Facebook Video Feeds, Instagram Explore.

**Cannot run well in:** Reels (both platforms), Stories (both platforms), In-Stream.

**The fix:** Re-export at 9:16 (1080x1920) or minimum 4:5 (1080x1350).

**Quick path when stuck with 16:9:** Turn Advantage+ placements OFF → Manual placements → select only Feed + Video Feeds + Explore → turn OFF Stories, Reels, In-Stream. Launch today. Re-export 9:16 tonight. Launch a Reels ad set tomorrow.

### 9:16 vertical video

Runs everywhere. Advantage+ placements wide open. Meta pushes hard into Reels and Stories where cheap inventory lives.

## Post-launch rules

- Do NOT touch anything for **4 days minimum**. The algorithm needs a learning phase. Fiddling resets it.
- Day 5: Check CPM, CTR, CPC. Kill ad sets with CTR under 1% or CPM 2x above the others.
- Day 7: First budget adjustment. Scale winners by 20-30% per day max. Never double overnight.
- If an ad set has zero conversions after $50 spend, pause it. Not enough signal = move on.

## Pitfalls

- Do not use Advantage+ for creative or budget on a launch campaign. It removes control and makes optimization impossible.
- Do not stack interests in one ad set. One interest = one ad set. Split testing is the whole game.
- Do not touch the campaign in the first 4 days. Fiddling resets the learning phase.
- Motion-graphics-only creative (no human face) is retargeting material only. Never use it for cold audiences.
- Facebook Ad Library blocks browser automation after 2-3 page loads. Don't rely on it for live setup — use it only for competitive research.
- The Ads Manager interface changes frequently. When navigating, use browser_vision to verify what's on screen before clicking.

## Reference files

- `references/video-frame-extraction.md` — ffmpeg technique for extracting frames from MP4 reels for vision analysis
- `references/crew-workshop-july-2026.md` — Current active campaign: CREW Workshop, Brisbane CBD, 21 Aug 2026, $299, 25 seats. Reel inventory, audience, and campaign structure.
