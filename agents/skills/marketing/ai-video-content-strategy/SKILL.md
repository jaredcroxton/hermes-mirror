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

## The 8-Second Standalone Clip Format

When Jared asks for short launch videos ("8sec 720P"), deliver standalone clips — not a single 60-second multi-shot. Each 8-second clip carries ONE message. They can be used individually on social or strung together as a reel.

**Structure per clip:**
- One clear message (e.g. "One call. One output.")
- A single Seedance prompt with timeline markers [0s] to [8s]
- A separate VO script line alongside the visual prompt for the editor to record and layer in post
- 6 clips make a 48-second reel when strung together

**Per clip:** 720p, 8 seconds, Fast mode. 17 credits each on Higgsfield. Budget 3 attempts per clip.

**The VO line is a deliverable, not an afterthought.** Write it alongside the visual prompt. The editor needs both. Seedance audio should be mixed low as texture only; the VO carries the message.

## Pivot to CapCut When Seedance Doesn't Land

When Seedance 2.0 generative prompts produce unusable results (paper planes, abstract metaphors, anything requiring precise physical motion), pivot Jared to CapCut's AI video maker. CapCut is not a generative model — it's a script-to-edit tool that assembles stock footage, kinetic typography, and music. Different strengths:

| Seedance 2.0 | CapCut AI Video |
|---|---|
| Generative visuals from scratch | Matches stock footage to script |
| Camera control, lighting, scene logic | Text overlays, transitions, music beds |
| Best: abstract worlds, product spectacle | Best: kinetic typography, clean edits |
| Weak: on-screen text, faces, complex motion | Weak: novel visuals, camera choreography |

**When to pivot:** Jared says "they're not quite turning out" or asks for "a prompt to go into CapCut." He has already tried Seedance and wants a different tool.

**CapCut prompt structure:**
- Describe scenes with stock-footage-matchable keywords
- Specify visual style, colours, aspect ratio
- Use kinetic typography as the hero, not generative visuals
- Include music direction and timing
- No timeline markers — CapCut uses scene descriptions, not [0s] notation

**Example CapCut prompt** (from the Crew launch, 24 June 2026):
```
A bold product launch video, 8 seconds, 9:16 vertical.
Visual style: clean minimalist tech. Dark charcoal and warm cream palette
with electric lime green accents. Negative space is the hero.

Scene 1 (0-2s): Solid cream background. "13 PACKS" in large serif type,
dark charcoal. The number 13 pulses lime.

Scene 2 (2-4s): "92 SKILLS" replaces it. 92 pulses lime.

Scene 3 (4-6s): Both collapse into "ONE CREW." in lime on dark charcoal.
Background fades to near-black. Music swells.

Scene 4 (6-8s): PERFORMOS CREW wordmark fades in below. A lime line
draws across beneath the logo. Music resolves. Hold.
```

## The Seedance → CapCut fork

When Seedance generations are not turning out (abstract metaphors, paper planes, complex object physics), do not keep iterating. Switch to CapCut. The two tools serve different jobs:

| Tool | What it actually does | Best for |
|---|---|---|
| Seedance 2.0 (Higgsfield) | Generative AI video from text + references | Physical scenes, camera moves, cinematic spectacle |
| CapCut Instant AI Video | Script-to-edit: matches stock footage, builds text overlays, scores music | Kinetic typography, clean product launches, social cuts |

**CapCut prompt structure:** describe scenes chronologically with visual style, text overlay content, music mood, and CTA. CapCut assembles from stock. It cannot generate novel imagery like paper planes in formation. Lean into what it does well: bold text on clean colour fields, tight cuts, strong music beds.

**CapCut prompt template:**
```
A [mood] [video type], [duration], [aspect ratio].

Visual style: [palette, aesthetic, keywords].

Scene 1 (0-Xs): [background]. [text overlay content]. [music cue].
Scene 2 (X-Ys): ...
Scene N: ...

Music: [genre, arc]. [Voiceover or text-only].

[Stock footage direction or "text overlays only"].
```

## The 8-second short-form format

For standalone social clips (8 seconds, 720p, 9:16), each prompt carries ONE message. No multi-shot timelines. No complex narratives. The structure:

```
VISUAL:
[0s] [opening frame]. [Static or movement].
[2s] [development].
[4s] [peak moment].
[6s] [resolution].
[8s] Hold. Fade.

VO SCRIPT:
"[one line]"
```

Six of these string together as a 48-second reel. Each is independently usable. Include VO line alongside the visual prompt — Jared records VO separately and lays it over in CapCut.

## Seedance text-on-screen limitation

Seedance 2.0 garbles on-screen text — 90% unreadable. One large centered word is the safe ceiling. For any text beyond that (brand names, taglines, CTAs), add it as a text overlay in CapCut after generation. Never bake "Join the Crew" or similar multi-word phrases into a Seedance prompt expecting them to render cleanly.

## Pitfalls

- **Do not bury the prompts.** If Jared has to ask "where are the prompts?" you have failed the primary deliverable. Prompts must be the first, simplest, most accessible file.
- **Do not use variant shortcuts.** "Same as X but in 9:16" forces Jared to do the mental work of adapting the prompt. Write it out fully.
- **Do not put prompts in Excel as the primary location.** Excel is for tracking and planning. The `.txt` file is for generating.
- **execute_code sandbox does not have openpyxl.** Write the Excel script to `/tmp/` and run from terminal with `python3`.
- **Seedance Fast model has a quality ceiling.** For hero/keeper videos, recommend Standard mode even if it costs credits.
- **The 30-day unlimited window is promotional.** Front-load the most important videos in case of throttling or early termination.
- **Elements must be created first.** The @mention system requires uploaded reference images before any prompt using @ references will work.
- **Never use "Sarah" in any demo, product name, or prompt example.**
- **Seedance cannot do abstract metaphors reliably.** Paper planes in formation, ink drops resolving into logos, light emerging from darkness — these produce weird unusable outputs. Use physical scenes with real objects and clear action. If Jared's concept keeps failing, propose the CapCut fork instead of iterating.
- **Seedance cannot render readable on-screen text beyond one word.** For multi-word brand names, taglines, or CTAs, add text as a CapCut overlay in post. Never bake them into the Seedance prompt.
- **Seedance 2.0 blocks realistic human faces.** (Confirmed June 2026.) Identifiable faces are blocked at the content-safety level. Do NOT design launch videos around human characters in Seedance 2.0. Use the product-only spectacle pattern instead: Seedance carries the world (cubes, typography, architecture, abstract visuals), and real Jared footage + voiceover carry the trust. Layer them in post. If the video genuinely needs AI-generated human faces, use Seedance 1.5 Pro, Kling, or Veo 3.1.
- **When Jared is actively generating, deliver single prompts inline.** If he says "send me the prompt for that one" or "I just used X, send me Y", he is inside Higgsfield generating. Do not point him back to a file. Paste the one prompt he needs directly into the chat. Clean. No commentary. Just the prompt block.
- **Images dropped without commentary are reference signals.** If Jared drops an image link mid-conversation, he expects you to read the visual, interpret the intent, and weave it into the strategy. Do not ask "what should I do with this?" — read it, name what you see, and update the deliverable.

## The Product-Only Launch Video Pattern

When faces are off the table (Seedance 2.0 limitation), here is the proven structure for a 60-second product launch video:

1. **Open on the brand's visual metaphor** — not the product, but the world. For PerformOS Crew: the cube grid. For a SaaS app: the dashboard glowing on a dark desk. Establish the aesthetic register first.
2. **Reveal the scale** — numbers with motion. "13 Packs. 92 Skills." Let the count build visually.
3. **Show the architecture** — how it fits together. Diagrams that animate. Hierarchies that reveal themselves.
4. **Make the contrast** — old way vs new way. Split screen. The chaos recedes, the order owns the frame.
5. **Close on the lockup** — logo, tagline, constellation of everything that came before.

**6 to 8 Seedance generations** for a 60-second video. Each generation is 10 to 12 seconds with multi-shot timeline markers inside. Fast mode for first pass, Standard for keepers. Budget 3 attempts per shot. Expected keeper rate: 40%.

**Brand references as Elements.** Screenshot the brand's own assets (catalogue cover, logo, colour swatches) and upload as @references. Brand-accurate is better than AI-generated approximations.

**Real footage layers in post.** Screen-record the product. Record VO separately. Seedance is the spectacle layer, not the trust layer.

## References

- `references/seedance-2.0-capabilities.md` — Full capability map, prompt engineering rules, cinematography vocabulary bank, platform comparison
- `references/performos-brand-for-video.md` — PerformOS brand applied to video: colours, fonts, voice, master lines, what carries into every prompt
- `references/seedance-research-sources.md` — Full research bibliography from the 18 June 2026 deep dive
- `references/crew-launch-video-case-study.md` — Proven Elements-first workflow, 8-second clip format, and prompt libraries from the 24 June 2026 Crew catalogue launch

## Seedance 2.0 Prompt Engineering Rules (absorbed from seedance-video-generation)

When writing prompts for Seedance 2.0 (ByteDance), follow these hard rules:

### Non-Negotiable Rules
| Rule | Why |
|---|---|
| **Under 80 words** | Beyond ~80 words the model cherry-picks random details |
| **Subject → Action → Scene → Camera → Style** | Fixed order. Early tokens weighted heavier |
| **One camera move per shot** | Multiple moves = jittery garbage |
| **Max 2 characters** | 3+ = faces drift, bodies warp |
| **No on-screen text** | 90% garbled. One large centered word max |
| **No fast hand gestures** | Slow movements only |
| **Start at 5 seconds** | Lock the look first. Scale up once it holds |
| **Fast for drafts, Standard for keepers** | Never generate first attempts in Standard |

### Universal Prompt Template
```
[Specific subject with age, clothing, expression] + [One concrete physical action] +
[Environment with objects, textures, time of day] + [One camera movement with framing] +
[Lighting source, direction, quality] + [Style anchor and finish]
```

### Camera Language
Pick ONE: wide shot, medium shot, medium close-up, close-up, over-the-shoulder, top-down.
Pick ONE movement: slow dolly in/out, locked tripod with micro push-in, tracking shot, slow pan.

### Lighting Language
Name source, direction, quality. Never say "cinematic lighting."
Example: "Soft key light from the left, warm rim light, shallow depth of field."

### Style Anchors
Pick one primary + one reinforcement. Examples: `cinematic, soft contrast, warm grade, 50mm` or `iPhone handheld, slightly overexposed, harsh midday sun`.

### Reference Image System
- Tag every reference explicitly: `@image1 as the main character, preserve face and outfit exactly`
- Without explicit role assignment, the model guesses — often using a character reference as background texture.

### Hybrid Workflow (Critical for product demos)
1. Generate the human element in Seedance (person at desk, screen glow visible, content NOT)
2. Record the real product via QuickTime screen recording
3. Edit together in CapCut/DaVinci Resolve with text overlays and voiceover
4. Export at 1080p minimum

### What Seedance Cannot Do
| Limitation | Workaround |
|---|---|
| **Realistic identifiable human faces blocked** | Content moderation rejection, not just a quality issue. Use Seedance 1.5 Pro, Kling, or Veo 3.1 for people. For Seedance 2.0: product-only spectacle, abstract visuals, architecture, environments. Layer real human footage in post. |
| Cannot render realistic software UI | Use real screen recordings, edit together |
| Cannot produce readable on-screen text | One large centered word max. Text overlays in post |
| Cannot hold 3+ consistent characters | Max 2. Crowds stay blurry background |
| Cannot handle prompts over ~100 words | Stay under 80. Multi-shot timeline format ([0s]...[3s]...) is the exception — longer prompts work when structured as timeline markers. |

### Worked Example: Product Catalogue Launch Video
See `references/crew-launch-video-example.md` for a complete worked example: a 6-generation launch video for a product catalogue, including Elements-first setup, multi-shot timeline prompting, 8-second short-form variants, and the AI + Real pairing rule in practice.

**Pitfall:** Abstract brand metaphors fail. "Ink drops resolving into a logo" and "light emerging from darkness" produce weird unusable outputs. Use physical scenes with real objects and clear action.
