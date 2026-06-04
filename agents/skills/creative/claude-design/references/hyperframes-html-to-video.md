# HyperFrames HTML-to-Video Workflow

Use when Jared wants a designed HTML artifact turned into a deterministic MP4 video, or when a dashboard, deck, product mockup, or training explainer needs a short motion version.

## Core positioning

HyperFrames does not replace HTML dashboards, HTML decks, or Claude Design-style artifacts. It adds a video rendering layer on top of them.

- HTML dashboards win when the output must be used: search, filters, notes, localStorage, CSV export, CRM actions, decision workflow.
- HTML decks and design artifacts win for interactive review, executive browsing, and reusable source-of-truth files.
- HyperFrames wins when the output must be watched or shared as video: MP4, social clips, async briefings, animated explainers, product walkthroughs.

Best framing for Jared: design once, publish three ways.

1. Interactive HTML artifact.
2. HyperFrames MP4 walkthrough or explainer.
3. Share assets, for example thumbnail, still frames, GIF, and LinkedIn-ready clip.

## Prerequisites

HyperFrames requires:

- Node.js 22+
- npm / npx
- FFmpeg

Quick checks:

```bash
node -v
npm -v
npx hyperframes --version
ffmpeg -version
```

## Install and first project

```bash
mkdir -p ~/code/hyperframes-lab
cd ~/code/hyperframes-lab
npx hyperframes init first-test
cd first-test
npx skills add heygen-com/hyperframes
npx hyperframes preview
```

Render:

```bash
npx hyperframes render --output output.mp4
```

If rendering a specific composition, try:

```bash
npx hyperframes render compositions/stats.html --output stats.mp4
```

If that syntax fails, try:

```bash
npx hyperframes render --composition compositions/stats.html --output stats.mp4
```

## Claude Code prompt pattern

Open Claude Code from the project folder:

```bash
cd ~/code/hyperframes-lab/first-test
claude
```

Prompt pattern:

```text
Using the HyperFrames skills, create a 15-second 1920x1080 video for [product/topic].

Message:
[one clear message]

Tone:
[brand/tone]

Use clean HTML/CSS animation, lint it, then render to [filename].mp4.
```

For Accor Plus training, a strong first test:

```text
Using HyperFrames, create a 30-second 1920x1080 video explaining the six Accor Plus sales pillars.

Use one scene per pillar:
Connect Early, Clarify Needs, Confirm and Present, Close, Celebrate Belonging, Manage Concerns.

Use a clean executive training style. Run lint and render to accor-plus-sales-pillars.mp4.
```

For PerformOS:

```text
Using HyperFrames, create a 15-second product intro video for PerformOS AgentOS.

Message:
Private AI team for business leaders.

Tone:
Premium, sharp, executive, dark background, subtle motion, no hype.

Run lint and render to agentos-intro.mp4.
```

## Hermes/Bob handoff pattern

When Jared asks Brock how to use this in Hermes, route build work to Bob:

```text
Bob, create a HyperFrames video in ~/code/hyperframes-lab/[project].
Make a [duration] [topic] explainer.
Use HyperFrames.
Lint it.
Render the MP4.
Give me the file path.
```

Brock should stay at the decision layer: what story, audience, output, and quality bar. Bob owns build, lint, preview, render, and file delivery.

## Verification in Studio

A successful Studio preview usually shows:

- Project name loaded in the top bar.
- Composition list in the sidebar.
- Selected composition path, for example `compositions/stats.html`.
- Browser preview rendering the frame.
- Timeline visible.
- No JavaScript errors in console.

Telemetry info in console is not a blocker.

## Design guidance

Use HyperFrames for the motion version only after the message is clear.

Good first experiments:

1. Accor Plus Sales Pillars, 30 to 45 second explainer.
2. PerformOS AgentOS intro, 15 seconds.
3. HTML leads dashboard plus 30-second video walkthrough.
4. Weekly KPI story, with dials, talk time, connects, presentations, sales, and NSE units.

Avoid converting every artifact into video. Use video when it creates reach, clarity, or executive momentum.