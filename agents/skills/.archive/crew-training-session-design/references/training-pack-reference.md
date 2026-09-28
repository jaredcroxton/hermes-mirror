# CREW Pack Reference — Training Day Demo Moments

Quick-reference catalogue of the two core demo packs. Use when designing session sequencing.

---

## Web Design Pack (10-web-design) — 14 agents

### Build agents (produce a site)

| Agent | What it does | Demo prompt | Runtime |
|---|---|---|---|
| **Page Builder** | Clean multi-page business site. Single HTML. Zero framework. Under 2s load. | "Build me a 5-page website for my business" | 90s |
| **Cinematic Build** | Epic scroll-driven site. 3D objects, fog, bloom, museum-drift. Fashion-film energy. | "Build me a site that feels like a luxury campaign" | 3-5 min |
| **Immersive Narrative** | Scroll-driven story. Frame-scrubbed video advances as you scroll. Multi-stage journey through a metaphor. | "Build an induction course as a mountain climb" | 3-5 min |
| **Fly-Through Builder** | Scroll as camera descent. Frame-for-frame. One arrival moment. | "Build me a product reveal that falls through space" | 3-5 min |
| **Spotlight Hero** | Dark full-screen hero. Cursor reveals second image through glowing circle. Before/after transformation. | "Build me a hero where the mouse reveals the transformation" | 3-5 min |
| **Slide Deck Builder** | Single-file HTML deck. Keyboard, swipe, dot navigation. Branded. | "Build me a pitch deck in my brand" | 2 min |
| **Webcam Website** | Hand-tracking. Open palm = state A. Fist = state B. Reversible scrub. | "Build me a gesture-driven experience" | 4-6 min |
| **Real Estate Immersive** | Scroll-scrubbed property tour from real listing. One chapter per room. | "Turn this listing into a digital open home" | 3-5 min |
| **App Builder** | Backend automations. Scrapers, webhooks, cron jobs. Deterministic. | "Build me an automation that pulls data daily" | 2-3 min |

### Analyse agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Website Architect** | Scrape site. Reverse-engineer design system. Type scale, palette, spacing, motion. Token kit output. | "Study this competitor site and tell me why it feels expensive" |

### Design authority agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Stitch** | DESIGN.md taste contract for Google Stitch. Anti-generic. Strict typography, calibrated colour. | "Generate a taste contract so Stitch output reads as curated design" |

### Dashboard agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Lead Dashboard Builder** | Scrape target market. Score leads 0-100. Find decision-makers. Draft cold email + LinkedIn DM. | "Score these 10 leads and tell me who to call first" |

---

## Training Pack (09-training) — 8 agents

### Analyse agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Training Needs Analyser** | Identify real capability gap. Role → current → goal. Separates skill gap from motivation gap. Ranked priority report. | "My team needs training. Tell me what to spend on first." |
| **Skill Gap Mapper** | Person-by-person capability map against new initiative. Who needs what before go-live. | "Map who needs training before this system rolls out." |

### Design agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Module Outline Builder** | Topic → structured module outline. Bloom objectives. TSDC flow. Timings. Activities. | "Design a growth mindset module. 90 minutes." |
| **Assessment Designer** | Learning outcomes → valid assessment. Recall, application, scenario questions. Every item maps to an outcome. | "Write a test that checks whether they understood the module." |

### Build agents

| Agent | What it does | Demo prompt |
|---|---|---|
| **Facilitator Guide Creator** | Approved outline → runnable facilitator script. Stage directions. Activity setup/debrief. Minute-by-minute. | "Turn this outline into a guide a team lead can deliver." |
| **Learner Workbook Builder** | Facilitator guide → learner-facing workbook. Guided notes. Activity worksheets. Check questions. Printable. | "Build the participant workbook for this session." |

### Coach agent

| Agent | What it does | Demo prompt |
|---|---|---|
| **Coaching Conversation Guide** | GROW model. Goal, Reality, Options, Will. Open questions the coachee owns. | "Help me coach someone on their confidence in meetings." |

### Onboard agent

| Agent | What it does | Demo prompt |
|---|---|---|
| **Onboarding Programme Builder** | Role profile → phased 90-day programme. Pre-start, day one, week one, month one, quarter one. | "Build onboarding for a new sales hire." |

---

## The money-shot chain

Eight agents across two packs. One compound output.

```
Training Needs Analyser
    → "The gap is mindset. Not skill. Not process. Mindset."
Module Outline Builder
    → "Growth Mindset module. 90 minutes. 4 objectives. TSDC flow."
Facilitator Guide Creator
    → "Here is the script. Anyone can deliver the same session."
Learner Workbook Builder
    → "Here is the participant workbook. Printable. Activity-ready."
Assessment Designer
    → "Here is the quiz. Every question maps to an objective."
    ↓
Page Builder (or Immersive Narrative)
    → "Now build the module into a live learning site."
    ↓
Deploy to Vercel
    → "A live learning journey. Built in 90 minutes. From nothing."
```

## Design Standards (pack 12) — system-facing

These agents are called by build agents for quality gates. Not user-facing. Do not demo directly.

| Agent | What it does |
|---|---|
| Design Quality | Design review gate. Pass/fail. |
| Design Kit | Generates complete design system from brand-context. |
| Design Language | Extracts premium design language from reference sites. |
| Design Composition | Layout, proportions, visual weight. |
| Design Patterns | UI patterns and component behaviour. |
| Design Reference | Reference library for all design decisions. |
| Design Authority | Final design sign-off authority. |
