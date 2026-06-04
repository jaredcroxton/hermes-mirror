---
name: lara-programme-build
description: Use when Jared asks Brock to build a training programme via Lara_LearningDesign. Standard 2-pass delegation pattern to prevent Lara timeout on large builds.
tags: [lara, learning-design, training, programme, spreadsheet]
---

# Lara Programme Build

## Trigger
Use when Jared asks Brock to build a training programme via Lara_LearningDesign. This is the standard delegation pattern that prevents Lara from timing out on large single-pass builds. Before any build fires, Brock must ask Jared the 10 discovery questions.

### Lara has NO sub-agents
Lara is a single specialist agent. She does not delegate internally. Brock's delegation to her is 2-pass sequential (Pass 1: source MDs, Pass 2: Excel). Do not ask Lara about sub-agents — she has none. Only Sam_StudyNerd uses the orchestrator-with-sub-agents pattern.

## The pattern

### Small academic workshop review mode

When Jared asks for a smaller academic learning-design cross-check, do **not** launch the full two-pass programme build or ask the 10 commercial programme discovery questions. Use this lighter sequence:

1. Read Sam's current assessment context and the relevant study vault file.
2. Read Lara's soul or use Lara's learning-design lens for activity structure, engagement, Tell-Show-Do-Check, and evaluation.
3. Cross-check against peer-reviewed sources where neuroscience accuracy matters.
4. Give concise adjustment notes first. Wait for Jared to say **lock it** or **go** before building the Word document or Part 2 resource.
5. Keep the output as assessment support, not ghostwriting. Focus on structure, mechanisms, activity quality, rubric alignment, and source choices.

Reference for a worked example: `references/neuroscience-loneliness-remote-workshop-review.md`.

### Step 0: Discovery (Brock only)
Before any delegate_task fires, Brock asks Jared the 10 discovery questions from the Programme Build Baseline at `/Users/jc/Desktop/Obsidian/PerformOS/Programme-Build-Baseline.md`. No build starts without these answered.

Lara cannot do everything in one delegate_task pass. After discovery is complete, split into two sequential calls:

### Pass 1: Build the source files
```
delegate_task(
  goal="Build the learner and manager source markdown files for [programme name].",
  context="[full programme brief, product context, audience, scope, design standards]",
  toolsets=["file", "web"]
)
```
Output: `*-learner-source.md` and `*-manager-source.md` on Desktop.

### Pass 2: Build the spreadsheet
```
delegate_task(
  goal="Build the Lara-standard learning-design spreadsheet for [programme name] using the source files.",
  context="[same programme context]. Source files at /Users/jc/Desktop/[name]-learner-source.md and /Users/jc/Desktop/[name]-manager-source.md. Read both before building. Build TWO sheets — Sheet 1: Programme Overview (title, details table, module summary, key evidence sources) and Sheet 2: Lara Design (16 columns — Section, Module Title, Learning Outcomes, Content to be Taught, Content Sources, Tell (Explain), Show (Demonstrate), Do - Baseline, Do - Creative Alternative, Check (Assess), Practical Application, Facilitator / Manager Action, Duration, Kirkpatrick, Evaluation Method, Notes). One row per module section (not per module). Every column filled for every row. Navy header row, Helvetica, thin grey borders, freeze panes. Full spec in Programme Build Baseline.",
  toolsets=["file", "terminal"]
)
```
Output: `[name]-session.xlsx` on Desktop.

## Output hierarchy — three tiers (always)

Every programme produces three deliverables, in this exact hierarchy:

### Tier 1: Excel spreadsheet (business-facing source of truth)
- **TWO sheets**, not a single-sheet workbook. Full spec in Programme Build Baseline at `/Users/jc/Desktop/Obsidian/PerformOS/Programme-Build-Baseline.md`.
- **Sheet 1: Programme Overview** — title in navy header, programme details table, module summary table, key evidence sources table
- **Sheet 2: Lara Design** — 16 columns:
  1. Section
  2. Module Title
  3. Learning Outcomes
  4. Content to be Taught
  5. Content Sources
  6. Tell (Explain)
  7. Show (Demonstrate)
  8. Do - Baseline
  9. Do - Creative Alternative
  10. Check (Assess)
  11. Practical Application
  12. Facilitator / Manager Action
  13. Duration
  14. Kirkpatrick
  15. Evaluation Method
  16. Notes
- One row per module section (not per module). A 2-module programme with 7 sections + closing = 8 data rows + 1 header row.
- Navy (#0B1E3D) header row with white Helvetica Bold 11pt, filter arrows enabled, freeze panes at A2.
- Data cells: Helvetica 10pt, wrap text, top-aligned, thin grey borders.
- Every column is filled for every row with content pulled from the learner and manager source files.
- Tell, Show, Do, Check columns map the full instructional design flow per section.
- Facilitator/Manager Action column includes coaching scripts, session plans, and 4-week cycle actions.
- Kirkpatrick and Evaluation Method columns map L1-L4 per section with specific indicators and targets.
- Built by Lara in Pass 2 via openpyxl. This is what the business sees. It is the anchor file.

### Tier 2: Learner PDF (LearnOS upload)
- Self-paced module content only. No manager notes, no Kirkpatrick.
- Structured for the LearnOS import pipeline: verb+topic module titles, ≤8 word section titles, structured quizzes (4-option MCQ + correct answer + explanation), structured roleplays (scenario/persona/goal)
- Built by Brock running `build_learnos_packs.py` from the learner source MD file

### Tier 3: Manager PDF (full facilitation working document)
- NOT a summary. This is a working document a team leader runs from.
- Mandatory sections:
  - Programme overview table
  - Sources and evidence base (every framework and claim is sourced — HBR, Sales Executive Council, Journal of Consumer Research, etc.)
  - Manager preparation checklist (steps to complete before programme launch)
  - Live coaching session plan with timings for every part (e.g. 45 min session: 0-2 min opening, 2-5 min demo, 5-12 min practice, etc.)
  - Call review scorecard (printable table with yes/no columns for each behavioural indicator)
  - Common failure modes with full coaching scripts (not one-liner cues — full conversation scripts the manager can adapt)
  - 4-week reinforcement cycle with weekly manager actions
  - Kirkpatrick evaluation plan (L1 through L4 with what/how/when/target columns)
  - Kirkpatrick summary table (one-page reference)
  - Facilitator pre/post checklist
  - Revenue math (what the behaviour change means in dollars for the business)
- Template reference: `/Users/jc/Desktop/primer-question-manager-source.md`

## Crash recovery (Lara provider failure)

Lara may crash mid-build with a provider error (broken pipe, API failure). Her design content is preserved in the chat transcript but no files are saved to disk. Recovery pattern:

1. Save Lara's architecture/design output from the transcript to a reference file on Desktop (e.g. `[programme]-architecture.md`)
2. Re-delegate Pass 1 and Pass 2 as normal — Lara in a fresh delegate_task session will pick up from the saved architecture
3. Do NOT skip to the build script. The source files must exist on disk first

This worked in practice for the Leadership Programme build (28 May 2026).

## Build script staging (Step 4)

`build_learnos_packs.py` expects files named `learner-source.md` and `manager-source.md` in a dedicated folder — NOT programme-prefixed filenames on Desktop. Stage before running:

```
mkdir -p /path/to/[programme]-build
cp [programme]-learner-source.md /path/to/[programme]-build/learner-source.md
cp [programme]-manager-source.md /path/to/[programme]-build/manager-source.md
python3 /Users/jc/Desktop/build_learnos_packs.py /path/to/[programme]-build
```

Then copy the output PDFs back to Desktop with programme-prefixed names.

## Full redesign replacement
When Jared provides a completely new architecture that supersedes a previous build, archive old files before running the new pipeline. Create an archive folder (`~/Desktop/<programme-slug>-archive/`) and move all old deliverables there (Excel, source MDs, PDFs, build folder, old architecture). Then run the pipeline fresh with the new slug. This prevents glob conflicts in the build script and keeps Desktop clean.

## Timeout handling
If Pass 1 times out, retry with the same context. If it times out twice, split further: learner source file first, then manager source file. If Pass 2 times out, build individual sheets separately.

## Accor Plus context (standard)
Accor Plus outbound sales teams across 7 APAC markets: Australia, New Zealand, India, Indonesia, Philippines, Thailand, Vietnam. Product: ALL Accor+ Explorer membership ($349/year). High-volume outbound telesales. 6 sales pillars: Connect Early, Clarify Needs, Confirm and Present, Close, Celebrate Belonging, Manage Concerns.

## Design standards (standard)
- Module titles: verb + topic
- Section titles: 8 words or fewer
- No em dashes in learner-facing text
- Short punchy sentences, active voice
- Spell out one to nine
- Duration lines under each heading
- Show/Reflect/Key Takeaways/Quiz/Roleplay as distinct blocks
- Structured quizzes: 4-option MCQ + correct answer + explanation
- Structured roleplays: scenario/persona/goal
- Kirkpatrick L1 through L4 in the manager source
- **SOURCES ARE MANDATORY in the manager pack.** Every framework, claim, and statistic must cite its origin. Reps ask "why should I change" and the manager needs the source to point to. Examples: HBR study on pre-call emotional state, Sales Executive Council on discovery question ratios, Journal of Consumer Research on silence after questions. Sources go in a dedicated "Sources and evidence base" section near the top of the manager source file.
- **Coach the manager, not just inform them.** Coaching scripts for failure modes are FULL conversations the manager adapts, not one-line cues. Session plans include timings for every part. Checklists include pre, during, and post items. Scorecards are printable tables.

## Bob is not needed
The PDF build script is already on Desktop and works generically. Brock runs it directly. Bob_Builder is for deployment and custom builds, not for this pipeline.
