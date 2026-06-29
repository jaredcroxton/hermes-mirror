---
name: crew-training-session-design
description: Use when Jared is designing a face-to-face CREW training session, planning the day structure, sequencing demos, or building the training Google Doc. Covers I Do/We Do/You Do architecture, explore windows, agent chaining narratives, demo moments for each pack, and the pre-flight/pre-onboarding/post-training flow.
---

# CREW Training Session Design

## What this skill covers

Designing a face-to-face CREW training day. 25 people. $299 per person. Brisbane CBD (then Sydney, Melbourne). The session is a practical build day, not a lecture. Participants leave with 94 agents installed, brand-context.md completed, and live output deployed.

## Brock's lane: plan and pressure-test, do not build

When Jared says "let's build this out" or "let's start building this," he is often in planning mode — developing the thinking, mapping the architecture, pressure-testing the concept. Do not jump to writing code, creating metadata files, or executing builds. Stay in discussion, ask the right questions, map the terrain. Jared will redirect to execution when he is ready.

If he says "just go in there and make the change" or "build the actual Google Doc now," that is the execution signal. Until then, plan.

**Pitfall:** Interpreting "build out" as "start coding." Jared uses it to mean "develop and flesh out the idea." Confirm the mode if ambiguous.

## Session architecture

### Pre-session

- **Pre-flight check script.** One command. Validates Docker, Node.js 18+, Claude Code subscription, GitHub account, Git. Green or red with fix link. Run the night before.
- **Google Doc.** View-only. They make a copy. Every command, prompt, URL is one Ctrl+C away.
- **Portal sign-in.** Google OAuth via Supabase Auth. Brand-context onboarding completes here before training day.

### Recommended stack (attendees bring or buy)

- Claude Max subscription ($167/month) — throughput for the day plus runway for weeks after
- $5 API credit (KIE or equivalent) — for external calls
- Firecrawl account (created during session)
- Supabase account (created during session)
- Vercel account (created during session)

### I Do / We Do / You Do

The three-phase teaching model:

1. **I Do (Jared demos, 30-45 min).** No one touches a machine. Three builds with no filler. Page Builder, Stitch, Lead Dashboard. The hook lands here.
2. **We Do (together, 45-90 min).** Everyone moves together through the Google Doc. Same prompt, same output, everyone lands at a live URL. Facilitator floats for anyone stuck.
3. **You Do (their idea, 35-60 min).** They name a business problem. Use the portal matcher. Run discovery, build, deploy. Show neighbour. Volunteers show room.

### Explore windows

Free play periods between guided sections. 5-30 minutes each. Structured prompts in the Google Doc so they are not staring at a blank screen. Purpose: let them try what matters to them, not just follow along.

### The money-shot chain

Demo agents in sequence so they produce one compound output. Example:

```
Training Needs Analyser → Module Outline Builder → Facilitator Guide Creator
→ Learner Workbook Builder → Assessment Designer → Page Builder → Vercel deploy
```

A live learning site. Built in 90 minutes. From nothing. That is the sell.

## Terminology

- **"Agents," not "skills."** Public-facing. An agent is a team member with methodology and expertise. A skill is a feature.
- **"Packs," not "categories."** The 14-pack architecture.
- **Pack names for public:** Core, Sales, Marketing, Ops, HR, Finance, Support, Docs, Training, Web Design, Infrastructure, Design Standards, Design Styles, Animation.

## Portal as ongoing asset

The PerformOS portal behind login serves three jobs:

1. **Pre-training.** Brand-context onboarding. Browse agents before arriving.
2. **During training.** Matcher — "I am trying to build X" → right agent + suggested prompts.
3. **Post-training.** Reference catalogue. 94 agents browseable by function, pack, or problem.

## Google Doc structure

Preferred over HTML slide deck for training workbooks. Reasons:
- Copy-paste is one keystroke. No browser rendering quirks.
- Works on every machine. Zero dependencies.
- View-only. They make a copy. Annotated reference after the day.

Structure sections: Pre-Flight Check, Setup, Brand Context, Connect Your Stack, First Build, Data Build, Your Build, Agent Reference, Post-Training, Troubleshooting.

## Key demo moments by pack

### Web Design (pack 10)
- **Page Builder:** "Build me a 5-page website." 90 seconds. Live URL.
- **Stitch:** Before/after brand lock-in.
- **Immersive Narrative:** Scroll-driven story. Frame-scrubbed video.
- **Fly-Through Builder:** Scroll as camera descent.
- **Spotlight Hero:** Dark hero. Cursor spotlight reveal.
- **Slide Deck Builder:** Branded HTML deck.
- **Lead Dashboard Builder:** Scored leads. "Call this one first."
- **Cinematic Build:** 3D objects, fog, bloom.
- **Website Architect:** Reverse-engineer a competitor's design system.

### Training (pack 09)
- **Training Needs Analyser:** "My team needs training. What do I spend on first?"
- **Module Outline Builder:** Topic → structured module. TSDC flow.
- **Facilitator Guide Creator:** Outline → runnable script.
- **Learner Workbook Builder:** Guide → participant workbook.
- **Assessment Designer:** Outcomes → valid test.
- **Coaching Conversation Guide:** GROW model questions.
- **Onboarding Programme Builder:** Role → 90-day programme.

## Session timing

Full day: 10:30am to 4:00pm. Buffer built into every section. Breakout desk for anyone who falls behind.

| Block | Time | What |
|---|---|---|
| Settle + verify | 15 min | Pre-flight. Portal sign-in. |
| I Do (hook) | 30 min | Three demos. No machines. |
| We Do (setup) | 45 min | Clone, install, connect. |
| We Do (first build) | 45 min | Page Builder + Stitch + deploy. |
| Explore (Core + Design) | 30 min | Free play. Stitch deep dive. |
| Lunch | 30 min | |
| Pack tour (Sales + Marketing) | 30 min | Walk through + explore window. |
| Pack tour (HR + Ops + Finance) | 20 min | Quick hits + explore. |
| Pack tour (Support + Docs + Training) | 20 min | Quick hits + explore. |
| Pack tour (Web + Animation) | 20 min | Cinematic stuff. Room lean-in. |
| You Do (their build) | 35 min | Their idea. Build. Deploy. Share. |
| Close | 10 min | WhatsApp group. Portal. Next steps. |

## What makes a session work

- Build, don't watch. Three guided builds. One free build.
- Explore, don't rush. Four explore windows.
- Chain, don't isolate. Show agents working together.
- Social, don't solo. Show neighbour. WhatsApp group. Shared URLs.
- Portal, not PDF. Live asset that outlasts the day.

## Pitfalls

- **Jumping to execution during planning.** Jared says "build it out" and means "develop the plan." Do not start writing code. Stay in discussion until he gives the execution signal.
- **Machine variance kills the day.** One person with wrong Docker version loses 10 minutes. Five people fractures the room. Pre-flight check is non-negotiable.
- **Google Doc over HTML slide deck for commands.** Copy-paste from HTML introduces artefacts. Google Doc is boring technology that breaks for nobody.
- **Do not call them skills publicly.** They are agents.
- **Do not demo all 94 agents.** Pick the money-shot chain and the cinematic moments. The rest are self-discovery via explore windows.
