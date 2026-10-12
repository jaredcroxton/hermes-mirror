# Orchestrator-delegate pattern for study agents (Sam v2)

**Captured:** 02 June 2026
**Context:** Restructuring Sam_StudyNerd from flat do-everything agent to orchestrator that delegates to specialist sub-agents via `delegate_task`.

## The pattern

An **orchestrator agent** (Sam) holds:
- Course registry (what Jared is studying, progress, what is due)
- Routing logic (which specialist handles what)
- Study preferences and voice rules

The orchestrator does NOT execute deep domain work itself. It:
1. Reads the relevant Obsidian vault files itself (never delegates blind)
2. Triages: can I answer directly, or does this need a specialist?
3. If specialist needed → fires `delegate_task` with full context
4. Reviews sub-agent output before delivering to Jared

## Sub-agent structure

| Sub-agent | Territory | When Sam delegates |
|---|---|---|
| ECU_MBP | ECU Master of Business Psychology — assignments, rubrics, academic writing | Any ECU subject work beyond quick concept lookup |
| MIT_AgenticAI | MIT Agentic AI — module content, frameworks, concepts | Any MIT module deep-dive or concept explanation |
| Study_Tools | Flashcards, spaced recall, concept breakdowns, summaries | Study sessions, revision, exam prep |

## How Sam triages

- Quick concept explanation from known vault content → Sam answers directly
- Progress check or course navigation → Sam answers directly
- Work problem needing brief framework → Sam reads vault, answers if brief
- Assignment drafting, rubric checking, deep content work → Sam delegates

## Routing logic at a glance

ECU subject content, assignments, rubrics → delegate_task → ECU_MBP
MIT course modules, frameworks, concepts → delegate_task → MIT_AgenticAI
Work problem → Sam reads vault first, decides: answer directly or delegate
Quick concept or progress → Sam answers directly

## Key principle

Sam stays lean. He holds the map and makes the routing call. He never crams every course into one context window. Each sub-agent loads only what it needs for its territory.

## Comparison: flat vs orchestrator

**Flat (Sam v1):** All course content in one soul file. All context in one window. Slower as more courses added. Cross-contamination between subjects.

**Orchestrator (Sam v2):** Sam holds the map. Sub-agents hold the depth. Each context window stays focused. Scales as Jared adds more courses.

## Related

- Lara uses the same pattern with Rory_Research, Ava_Activities, Eva_Evaluation (see `references/lara-full-package-pattern.md`)
- Brock oversees the whole agent ecosystem but does not execute specialist work