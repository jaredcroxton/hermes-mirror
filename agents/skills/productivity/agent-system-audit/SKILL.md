---
name: agent-system-audit
description: Audit an agent ecosystem against a framework (12-Factor Agents, Anthropic best practices, etc.), produce per-agent scoring, gap analysis, architectural design, and a phased implementation plan. Use when Jared asks to audit, assess, score, upgrade, or optimise his agent ecosystem against a published standard.
---

# Agent System Audit

## When to use

Jared asks to audit, assess, benchmark, or upgrade his agent ecosystem against a framework. Triggers include:
- "Audit my agents against the 12 factors"
- "How do my agents score against [framework]?"
- "What is missing from my agent ecosystem?"
- "Upgrade Brock/every agent to meet [standard]"

## What this skill covers

A full audit has five phases. Do not skip phases. Do not rush.

### Phase 1 — Research

Load the framework. If it is a public repo (like 12-factor-agents), clone it and read every factor document. If it is a published article (like Anthropic's Building Effective Agents), navigate to it and extract all principles.

Also search for related implementation patterns, critiques, and community extensions. Browser search for "framework-name implementation patterns" and "framework-name production examples."

Save key excerpts into the audit folder as reference material.

### Phase 2 — Design the fix

Before assessing individual agents, design the architectural fix that addresses the framework's core demands. For 12-Factor Agents, this was the Thread/Event model. For another framework, it might be a different architectural primitive.

The design document should include:
- Data structures (classes, types, schemas)
- Core algorithms (context building, error handling, pause/resume)
- Migration path (how existing agents adopt the new primitive)
- Code sketches in Python (not full implementations — enough to communicate the design)

### Phase 3 — Per-agent assessment

Score every active agent against every factor. Use a consistent scale:

- **Strong:** Factor is fully implemented and intentional.
- **Moderate:** Factor is partially present but not systematic.
- **Weak:** Factor is absent or accidental.
- **N/A:** Factor does not apply to this agent type.

Produce a summary matrix. Identify patterns: which factors are strong across all agents? Which are weak across all? Which vary by agent class?

For each agent, reference its SOUL.md. The assessment must be grounded in the agent's actual prompt, not assumptions.

### Phase 4 — Beyond-framework optimizations

Every framework has gaps. Identify what the framework does NOT cover but the ecosystem needs. Common gaps:

- Cross-agent communication protocols
- Shared knowledge/memory
- Agent discovery and routing
- Performance monitoring
- Testing and evaluation
- Version management
- Security boundaries
- Cost optimization
- Onboarding for new agents

Score each optimization by impact and effort. Prioritize.

### Phase 5 — Implementation plan

Produce a phased plan with:
- Week-by-week sequencing
- Dependency map (what blocks what)
- Risk register (likelihood × impact × mitigation)
- Success metrics (measurable outcomes by phase end)
- Owner assignments (which agent handles which work)

The plan must be realistic. One agent migration per week maximum. Build the foundation first, then migrate agents, then add ecosystem features.

## Output structure

Save everything to a clean Obsidian folder:

```
/AgentOS/<audit-name>/
├── 00-index.md                  # TOC, summary, decisions needed
├── 01-<architectural-design>.md # The core fix design
├── 02-per-agent-assessment.md   # Scoring matrix + per-agent notes
├── 03-beyond-<framework>.md     # Ecosystem optimizations
└── 04-implementation-plan.md    # Phased rollout
```

Use the `00-index.md` as the handoff to Jared. It should stand alone — someone who reads only the index should understand the audit's conclusions and next steps.

## Pitfalls

- **Do not assess agents you have not read.** Every agent score must reference its actual SOUL.md. No assumptions.
- **Do not rush to recommendations.** The architectural design (Phase 2) must precede the per-agent assessment. The fix design informs how you score each agent.
- **Do not produce a plan without a dependency map.** Week 5 might depend on Week 2. Show it.
- **Do not propose migrating all agents simultaneously.** One agent per week. Start with the simplest specialist, then the most complex orchestrator, then the rest in parallel.
- **Do not skip the "decisions needed from Jared" section.** The audit is advice. Jared decides.
- **When updating a self-contained HTML dashboard's data array, verify JS utility functions survive the replacement.** If you use string replacement to swap a `var REPOS = [...]` block in an HTML file, the end-marker `];` can be ambiguous if it also appears inside utility functions like `groups[cat] = [];` or `delete map[name];`. After replacement, verify that `buildCard`, `loadRelevant`, `saveRelevant`, and `CATEGORY_ORDER` are still defined. If they are missing, inject them after `'use strict';` as a single utility block. The missing functions symptom is 0 cards rendered with no console errors because the script fails silently before `render()` is called.

## References

- `references/au-site-blocking-patterns.md` — Australian retail/travel bot detection patterns and Firecrawl workaround
