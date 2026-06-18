---
name: ai-video-content-strategy
description: Use when Jared asks to build a video content strategy using an AI video generation model (Seedance, Kling, Sora, Veo, etc.). Covers deep model research, brand-aligned prompt library construction, 30-day production calendars, Excel operational plans, and the integration of AI-generated video with real-content companion pieces.
tags: [video, content-strategy, seedance, marketing, prompts, production-calendar]
---

# AI Video Content Strategy

## Trigger
Use when Jared asks to build a video content strategy, generate marketing videos with an AI model, create a prompt library for video generation, or plan a content calendar around a video generation tool (Seedance 2.0, Kling, Sora, Veo, Runway, etc.).

## Operating Principle

**The prompts are the primary deliverable.** Everything else — the calendar, the strategy doc, the brand alignment — supports the prompt library. Never bury the prompts inside a strategy document. The prompts must be the first thing Jared can reach, in a single file, with clear copy-paste boundaries.

## Workflow

### Phase 1: Deep Model Research
1. Search the web for the specific model (e.g., "Seedance 2.0 capabilities features best practices")
2. Search for platform-specific details (e.g., "Higgsfield Seedance 2.0 pricing unlimited plan")
3. Search for prompt engineering guides (e.g., "Seedance 2.0 prompt structure camera direction cinematic")
4. Search for use-case examples (e.g., "Seedance 2.0 SaaS demo marketing video examples")
5. Extract key pages: official model page, platform page, prompt guides, SaaS playbooks, Reddit/community best practices
6. Synthesise into a concise capability map: inputs, outputs, resolution, duration, audio, camera control, text-in-video, pricing model, limitations

### Phase 2: Brand Alignment
1. Load the brand's visual and voice guidelines (PerformOS: Polly_PerformOS soul, VISUAL.md, COPY.md)
2. Map every prompt to brand colours, fonts, voice, master lines, and forbidden vocabulary
3. Identify which brand elements need to become Seedance Elements (@BrandMark, @Founder, product screenshots)

### Phase 3: Prompt Library Construction
1. Define content pillars (4 to 5 max) tied to business outcomes
2. Build 40+ video concepts across pillars with specific durations, formats, and jobs
3. Write every prompt using the model's best-practice structure (timeline markers, camera direction, physical detail)
4. Write ALL prompts as full standalone copy-paste blocks — no variant shortcuts
5. Every prompt block must have clear start/end boundaries so Jared can copy one at a time
6. Use the brand's exact vocabulary, colours, and master lines in every prompt

### Phase 4: Production Calendar
1. Map all videos to a day-by-day 30-day calendar
2. Phase the calendar: Foundation → Products → Authority → Campaigns → Iteration → Real Content → Polish → Ship
3. Include Elements setup, review days, and real-content filming days

### Phase 5: Delivery
1. **First deliverable:** A single `.txt` file with all prompts, separated by clear blocks. Name it `[brand]-[model]-all-prompts.txt`. This is the file Jared opens to generate.
2. **Second deliverable:** An Excel workbook with sheets for Video Catalogue, Production Calendar, Prompt Reference, Distribution Plan, Brand Specs, Elements Setup, Real Content Tracker.
3. **Supplemental:** A markdown strategy document with full context (only if Jared asks for the depth).

## Excel Building Pattern

When building the Excel workbook:
- Use openpyxl from **terminal** (not execute_code — the sandbox is missing the package)
- Write the full Python script to `/tmp/build_excel.py`
- Run with `python3 /tmp/build_excel.py`
- Apply PerformOS brand colours: Ivory `#f2efe8`, Ink `#0a0a0a`, Lime `#d4ff3b`
- Use Inter font, thin borders, data validation dropdowns for status columns
- Freeze panes on row 1, auto-filter on headers
- Mirror the Excel to Obsidian: `cp /Users/jc/Desktop/filename.xlsx /Users/jc/Desktop/Obsidian/PerformOS/`

## Deliverable Format Rules

1. **Prompts file first, always.** Before the Excel or strategy doc, the prompts must exist as a clean `.txt`.
2. **Clear copy-paste boundaries.** Use `───` or `▶` markers between prompts so Jared never has to guess where one ends and the next begins.
3. **No variant shortcuts.** Every video gets its own fully-written prompt. "Same as 3.1 but vertical" is not acceptable.
4. **Single file for prompts.** Not spread across markdown, Excel, and strategy doc. One file. Open. Copy. Paste. Generate.
5. **Label every prompt** with its number, name, and pillar so Jared can track what he has generated.

## Brand Integration

For PerformOS specifically:
- Colours: Ivory `#f2efe8`, Ink `#0a0a0a`, Electric Lime `#d4ff3b`
- Fonts: Instrument Serif (headings), Inter (body), JetBrains Mono (labels)
- Voice: Precise, editorial, confident, operator-first
- Master lines: "We don't build platforms. We build instruments." / "Compound. Execute. Decide. Dominate." / "The Future of High Performance"
- Forbidden: platform, suite, all-in-one, revolutionary, game-changer, enterprise-grade, seamless, unlock, leverage
- Products: Pocket Customer, LearnOS, PulseCheck 360, Performlytics, AgentOS
- Training: 10 modules at $449 AUD/module

## The AI + Real Pairing Rule

Every AI video campaign must have real-content companion pieces. Seedance carries the spectacle and builds the world. Jared's face, voice, and actual products on screen carry the trust. Never ship an AI-only campaign. Include real-content filming days in the production calendar.

## Pitfalls

- **Do not bury the prompts.** If Jared has to ask "where are the prompts?" you have failed the primary deliverable. Prompts must be the first, simplest, most accessible file.
- **Do not use variant shortcuts.** "Same as X but in 9:16" forces Jared to do the mental work of adapting the prompt. Write it out fully.
- **Do not put prompts in Excel as the primary location.** Excel is for tracking and planning. The `.txt` file is for generating.
- **execute_code sandbox does not have openpyxl.** Write the Excel script to `/tmp/` and run from terminal with `python3`.
- **Seedance Fast model has a quality ceiling.** For hero/keeper videos, recommend Standard mode even if it costs credits.
- **The 30-day unlimited window is promotional.** Front-load the most important videos in case of throttling or early termination.
- **Elements must be created first.** The @mention system requires uploaded reference images before any prompt using @ references will work.
- **Never use "Sarah" in any demo, product name, or prompt example.**

## References

- `references/seedance-2.0-capabilities.md` — Full capability map, prompt engineering rules, cinematography vocabulary bank, platform comparison
- `references/performos-brand-for-video.md` — PerformOS brand applied to video: colours, fonts, voice, master lines, what carries into every prompt
