---
name: html-slide-deck
description: Build premium, self-contained, branded HTML slide decks with smooth animations, navigation controls, responsive layouts, and zero overflow. Use whenever Jared asks for a deck, slides, presentation, HTML presentation, pitch deck, product demo, or branded multi-slide visual output.
version: 1.1.0
author: PerformOS / Jared Croxton
platforms: [macos]
metadata:
  hermes:
    tags: [html, slide-deck, presentation, animation, frontend, performos]
---

# HTML Slide Deck Builder

## Standard

Build a single production-ready `.html` file that works offline in any browser.

The **final deliverable** is one self-contained file. Everything ships inline:

- CSS
- JavaScript
- SVG icons
- Logo or generated wordmark
- Animations
- Content
- Images and video, embedded as base64 data URIs

No external JavaScript. No external CSS framework. No local asset dependency unless Jared explicitly provides one and asks to embed or reference it.

Decks must feel premium: clean formatting, generous spacing, strong colour discipline, smooth motion, and no clipping or overflow.

## Working process vs final artifact

The single-file rule describes the **deliverable**, not the build process. Media embedded as base64 makes the file very large (a deck with several photos and a video easily passes 5MB) and too large to read or edit normally.

Build in this order so editing stays fast:

1. Build and iterate with **no media embedded**. Use short placeholder `src` values while the file is small and fully readable.
2. Get structure, copy, layout, and motion right first.
3. **Embed media last**, as a separate scripted step (see Media Workflow).
4. After media is embedded, make further text or CSS edits with targeted tools (`grep`, `awk`, a small Python script). Keep edits surgical. Do not try to read the whole multi-megabyte file.

If a deck must be reopened later, prefer editing a media-light source and rerunning the embed step over hand-editing a huge file.

## Non-negotiables

- No text overflow, clipping, or cropped controls.
- No placeholder copy in the delivered deck.
- No broken navigation.
- No static, lifeless deck when the brief asks for a premium presentation.
- No generic SaaS look unless the brand explicitly calls for it.
- Single self-contained HTML file as the deliverable, unless Jared asks otherwise.
- Inspect the rendered file before delivery (see Render Verification Loop).

## When to use this skill

Use for:

- HTML slide deck, presentation, pitch deck, training deck
- Product demo deck, branded multi-slide file, executive deck, visual briefing deck
- Executive operating models, board-paper style visual narratives, and premium HTML briefing documents when Jared wants to "see the flow" before or alongside a PDF

If the request is only strategy or critique, do not build. If Jared asks to create the deck, build it.

## Source-of-truth rule for HTML + PDF requests

When Jared wants both **HTML and PDF**, build the HTML first and treat it as the source of truth. Then export the PDF from the finished HTML.

Preferred sequence:

1. Build the full HTML artifact.
2. Verify the HTML renders cleanly.
3. Export a PDF from the HTML.
4. Deliver both files.

For executive strategy artifacts, the HTML does not need to behave like a click-through slide deck if the brief is better served by a scrolling visual narrative. In those cases, prioritize clear section flow, executive readability, print cleanliness, and a strong story arc over slide navigation chrome.

## HTML + MP4 requests

When Jared wants a deck, dashboard walkthrough, product intro, or training explainer as video, keep the HTML artifact as the design source of truth and use HyperFrames only as the MP4 rendering layer.

Preferred sequence:

1. Build or adapt the HTML/deck first.
2. Confirm the story, timing, and motion plan.
3. Convert the motion version into a HyperFrames composition.
4. Run `npx hyperframes lint` where available.
5. Preview in HyperFrames Studio.
6. Render with `npx hyperframes render --output <name>.mp4`.
7. Deliver the HTML source and MP4 when both are useful.

Do not replace a usable dashboard or deck with a video. Video explains or promotes the artifact. It does not replace interactive workflow features such as filtering, notes, localStorage, CSV export, or navigation.

## Intake

Extract these details. Ask one question only if a missing item materially changes the build.

**Brand**

- Company or product name
- Primary, secondary, and accent colours
- Heading and body font preferences
- Logo, or generate a wordmark
- Logo position

**Slides**

- Number of slides
- Slide title and message for each slide
- Slide type: title, content, feature cards, comparison, process, code, visual, CTA
- Any required speaker flow

**Delivery context** (this drives responsive and file-size decisions)

- Where it will be shown: projector, desktop screen, web page, email attachment, live URL
- Target viewport, for example 1920x1080, 1440x900, or 16:9 projector
- Does it need to work on phones, yes or no
- File-size budget. An emailed deck must stay small. A hosted deck has more room.

**Media inventory**

- Number of photos, and their source
- Video, yes or no, and length
- Logo source format (PNG, SVG, or a vector file such as .ai or .pdf that must be converted)
- Whether the media can be compressed

**Timing**

- Total duration, auto-advance yes or no, seconds per slide if auto-advance is required

**Style**

- Animation intensity: minimal, standard, dramatic
- Background style: gradient, solid, glassmorphism, dark, light, photographic
- Layout: centered, left-aligned, split-screen, editorial, dashboard-like

## Build plan before code

Before coding, write a concise slide plan:

```text
Slide 1 [Title] - Hero headline, subtitle, animated gradient field
Slide 2 [Problem] - Three tension cards with staggered reveal
Slide 3 [Model] - Process timeline with draw-in connector
Slide 4 [Evidence] - KPI cards with count-up animation
Slide 5 [CTA] - Decision ask and next step
```

Do not ask Jared to approve the plan unless the brief is ambiguous or the deck affects a sensitive executive decision.

## Media workflow before embedding

Compress every asset before turning it into base64. Base64 adds about 33 percent on top of the binary size, so compress hard.

**Images**

- Resize to the largest size actually shown. Full-bleed backgrounds rarely need more than 1600px wide. Use macOS `sips`:
  ```bash
  sips -Z 1600 --setProperty formatOptions 70 input.jpg --out out.jpg
  ```
- Target roughly 150KB to 350KB per full-bleed photo.

**Video**

- Compress with `ffmpeg`. Drop audio if it is a silent background. Cap resolution:
  ```bash
  ffmpeg -i input.mp4 -an -vf "scale=1920:-2" -c:v libx264 -crf 30 -preset slow -movflags +faststart out.mp4
  ```
- Target roughly 1.5MB to 3MB for a short background clip.

**Vector logos**

- A `.ai` or `.pdf` logo can be rendered to PNG with `qlmanage -t -s 2000 -o outdir logo.pdf`, then trimmed and recoloured as needed.

**Embedding**

- Embed media last, as a separate scripted step, after the layout is final.
- A small Python script that base64-encodes each file and substitutes it into the HTML keeps this repeatable.
- State the final file size when delivering. If it exceeds the brief's budget, compress further.

## Required HTML architecture

Use this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Presentation Title]</title>
  <style>
    /* reset and base */
    /* brand variables */
    /* deck shell */
    /* slide layouts */
    /* components */
    /* animations */
    /* navigation */
    /* responsive rules */
  </style>
</head>
<body>
  <main class="deck" aria-label="Presentation">
    <!-- slides -->
  </main>
  <!-- navigation, dots, counter, logo -->
  <script>
    /* state, navigation, keyboard, swipe, auto advance, animation hooks */
  </script>
</body>
</html>
```

## Brand tokens

Declare brand variables near the top:

```css
:root {
  --color-primary: #000000;
  --color-secondary: #111111;
  --color-accent: #D4FF3B;
  --color-text: #F5EADB;
  --color-muted: rgba(245, 234, 219, 0.72);
  --color-surface: rgba(255, 255, 255, 0.08);
  --color-border: rgba(255, 255, 255, 0.14);
  --font-heading: Archivo, Calibri, Arial, sans-serif;
  --font-body: Calibri, Inter, Arial, sans-serif;
  --font-mono: "JetBrains Mono", "Courier New", monospace;
  --ease-premium: cubic-bezier(0.4, 0, 0.2, 1);
}
```

If external fonts are unavailable, use system fallbacks. Do not rely on external font loading for the deck to look good.

## Layout patterns

Reusable, proven patterns. Treat them as options chosen to support the story, not mandatory decoration.

- **Full-bleed photo with text panel** - the photo covers the slide, a darkened gradient panel on one side carries the text.
- **Split layout** - a solid text panel on one side, a photo column on the other. Good when the text should lead and the image should support.
- **Process timeline** - a horizontal connector line that draws in, with numbered nodes that drop or pop in sequence.
- **Particle field** - small drifting dots behind the content for subtle ambient motion.
- **Count-up metrics** - large numbers that animate from zero when the slide becomes active.
- **Staggered reveal** - slide content rises and fades in, one element after another.
- **Crossfade transition** - the outgoing slide holds underneath while the incoming slide fades in on top, so there is no flash of background.

## Photo backgrounds

When a slide uses a photograph:

- Use `object-fit: cover` for a full-bleed look. The photo will crop. Use `object-position` to keep the focal point (a face, a product, a key object) in frame.
- Expose the focal point as CSS variables so it is easy to tune per photo:
  ```css
  .slide-photo {
    object-fit: cover;
    object-position: var(--fp-x, 50%) var(--fp-y, 50%);
  }
  ```
- Photos and the slide frame rarely share an aspect ratio. Decide deliberately: `cover` (fills, crops) is usually right for backgrounds. `contain` (shows the whole image, leaves bands) only when the whole image must be seen.
- Always put a gradient overlay between the photo and the text so copy stays legible:
  ```css
  .photo-overlay {
    background: linear-gradient(90deg,
      rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.5) 46%, rgba(0,0,0,0.08) 100%);
  }
  ```
- Weight the overlay toward the text side only, so the rest of the photo stays clear.
- Check text contrast against the actual photo, not a flat colour.
- If a slide uses a background video, restart it (`currentTime = 0`) when the slide becomes active, so it always plays from the start of the clip.

## Navigation requirements

Always include all five:

1. Left and right arrow buttons.
2. Dot indicators, one per slide.
3. Slide counter, for example `3 / 8`.
4. Keyboard support: left arrow, right arrow, spacebar.
5. Touch support: swipe left and swipe right.

Navigation must not cover content.

## Motion and animation

Default to standard animation unless Jared asks otherwise.

Use:

- Slide transition with opacity and transform.
- Staggered content reveal per active slide.
- Subtle background motion where it adds polish.
- Hover effects for cards and buttons.
- Count-up animation for key metrics when relevant.
- Progress bar if auto-advance is enabled.

Do not over-animate paragraphs. Motion should support hierarchy, not distract.

Use easing:

```css
cubic-bezier(0.4, 0, 0.2, 1)
```

## Responsive targets

Match responsive effort to the delivery context captured at intake.

- **Projector or desktop presentation** - optimise for the stated target viewport (commonly 1920x1080 or 16:9). Do not spend effort on phone layout unless asked.
- **Web page or shared link** - also verify at 375x812 phone width.
- **Always**, regardless of context: no overflow, no clipping, no cropped controls at the agreed target viewport.

If the deck is mobile-relevant, see `references/mobile-html-deck-qa.md` for the concrete mobile QA pattern and selector pitfalls.

## Render verification loop

Inspect the rendered deck before telling Jared it is done. Use a local preview server and screenshots.

For each slide:

1. Navigate directly to the slide.
2. Wait until the slide transition and reveal animations have finished. Screenshotting during a crossfade captures the previous slide and gives a false read.
3. Capture a screenshot.
4. Check text fit, cropping, focal point, contrast, navigation state, and console errors.

Build in a verify mode so screenshots are reliable. It disables transitions and animation delays:

```js
if (new URLSearchParams(location.search).has('verify')) {
  document.documentElement.classList.add('verify-mode');
}
```

```css
.verify-mode *, .verify-mode *::before, .verify-mode *::after {
  transition-duration: 0ms !important;
  animation-duration: 0ms !important;
  animation-delay: 0ms !important;
}
```

Open the deck with `?verify` to capture clean, settled screenshots of every slide.

## Quality gate before delivery\n\nOne final checklist. Fix any failure before delivery.\n\n**Layout and render**\n\n- Every slide or section fits the target viewport with no overflow or clipping.\n- If mobile-relevant, layout is readable at 375x812.\n- Navigation, keyboard, and swipe all work when the artifact is a slide deck.\n- Active-slide animations trigger when the artifact uses slide states.\n- No console errors.\n- **After removing visual effects (like 3D perspective, transforms, or animations), verify all intended content remains visible and properly positioned.**\n- If Jared asked for a companion PDF, export it from the final HTML and verify both local files exist before delivery.\n\n**Copy QA**\n\n- No placeholder text remains.\n- No em dashes anywhere. Use commas, periods, or parentheses.\n- Spelling and brand names correct.\n\n**Craft**\n\n- Consistent spacing and alignment across slides or sections.\n- Strong text contrast on every background.\n- No default-looking fonts unless intentional.\n- No stretched, squashed, or low-resolution media.\n- No cramped text blocks and no orphaned headings.\n- Colours match the product brand.\n- Final file size is within the brief's budget.\n\nIf the deck fails the quality gate, fix it before delivery.

## Brand configs

### PerformOS suite default

- Display: Archivo, fallback Calibri Bold
- Body: Calibri, fallback Inter
- Mono: JetBrains Mono, fallback Courier New
- Display style: uppercase, bold, tight letter spacing
- Body: 14 to 16px, 1.55 line height
- Labels: mono, 10 to 11px, uppercase, 1.5px letter spacing

### LearnOS

- Theme: light only
- Background: `#F8FAFC`
- Card surfaces: `#FFFFFF`
- Primary text: `#0F172A`
- Accent: `#0891B2`
- Secondary: `#22D3EE`
- Hover/deep accent: `#0E7490`
- Borders: `#CBD5E1`
- Secondary text: `#64748B`
- Buttons: 12px radius, rounded
- Voice: straightforward, anti-SaaS, corporate-adjacent
- Do not use dark backgrounds, lime/green, terminal aesthetics, or warm cream
- Used for: LearnOS product pages, academy module pages (light theme contexts only)

### Pocket Customer

- Theme: dark
- Background: `#0A0A0A`
- Card surfaces: `#141414`
- Primary text: `#F5EADB`
- Accent: `#D4FF3B`
- Hover: `#B8E81C`
- Alerts: `#FF5F57`
- Warnings: `#FF8A85`
- Subtle fills: `#E9FF8F`
- Buttons: pill, lime fill on dark
- Voice: urgent, uncompromising, frontline-focused
- Do not use light backgrounds, blue as primary accent, passive language, or warm earthy tones

### PulseCheck 360

- Theme: dark, terminal/grid aesthetic
- Background: `#000000`
- Card surfaces: `#0A0A0A`
- Primary text: `#FFFFFF`
- Accent: `#14B8A6`
- Secondary: `#3B82F6`
- Status green: `#00FF66`
- Alert warn: `#FFCC00`
- Alert critical: `#FF3333`
- Buttons: 6px radius, rectangular, not pill
- Voice: technical, precise, operations dashboard feel, `[SYS]` notation
- Do not use warm colours, serif fonts, rounded pill buttons, or soft gradients

### Performlytics

- Theme: dark
- Background: `#0A0A0A`
- Card surfaces: `#111111`
- Primary text: `#F0F0F5`
- Accent: `#3B82F6`
- Secondary: `#8B5CF6`
- Data viz: `#22D3EE`
- Hover: `#60A5FA`
- Secondary text: `#E0E0EA`
- Buttons: pill
- Voice: direct, data-first, no fluff
- Do not use light backgrounds, serif fonts, pastel colours, or generic SaaS language
- Used for: PerformOS AI Team sales deck (performos-ai-team-deck, rebuilt 30 May 2026)

## Delivery format

If building through Bob or Claude Code, return:

```
Done.
File: [path]
GitHub: [url]
Live: [url]
```

If only generating code in chat, output the complete HTML in one code block and one sentence: `Save as deck.html and open in any browser.`