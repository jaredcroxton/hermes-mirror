# PerformOS Crew Skill Template — G-Stack Depth Standard

Every PerformOS Crew skill must match this standard before it ships. A skill shorter than a few thousand words or 8 KB almost certainly does not pass. A skill with four bullet workflow steps and an output block is a placeholder, not a skill.

## Required sections

### 1. YAML frontmatter

```yaml
---
name: flow-[pack]-[name]
description: One sentence describing what the skill does in plain English.
triggers: [list of phrases that should trigger this skill]
language: white-label business language only
---
```

### 2. Preamble

Operational setup that runs before the skill body. Must include:

- session tracking (timestamp, branch, project slug)
- state directory init (`.claude/flow-state/`)
- context recovery (check for prior saved context on this topic)
- methodology link (reference the 8 standards)
- no telemetry, no gbrain, no external binaries, no auto-update

### 3. When to invoke this skill

- Trigger rules: what phrases, requests, or contexts should invoke this skill
- Anti-trigger rules: when NOT to invoke (wrong mode, wrong context, duplicate of another skill)
- Mode selection: fast (skip heavy gates), controlled (standard), governed (full gates)

### 4. Operating modes

Every skill must define three modes:

- **Fast mode:** skip cognitive framework, use light guardrails, output directly. For routine work with low risk.
- **Controlled mode:** full framework, standard guardrails, decision briefs for non-trivial choices. Default mode.
- **Governed mode:** full framework, strict guardrails, every decision briefed, context saved on exit, learnings captured. For client-facing work, financial decisions, or high-risk operations.

### 5. Cognitive framework

The thinking patterns the skill applies. Must include:

- Forcing questions: 3 to 6 diagnostic questions the agent must answer before acting. These expose assumptions and prevent rushing.
- Rubric: how quality is scored, what good looks like, what a 10 looks like
- Pattern language: reference taxonomy for the domain (e.g. severity levels, topic categories, mode labels)

### 6. Step-by-step workflow

Numbered phases with gates between them. Each phase must include:

- What the phase does
- What inputs it consumes
- What outputs it produces
- What must be true before proceeding to the next phase
- What to do if the gate fails

### 7. Guardrails

Safety constraints that run throughout the workflow:

- Escalation triggers: when to stop and ask the human
- Boundary enforcement: what this skill may and may not do
- Mandatory confirmations: what actions require explicit approval
- Soft vs hard: which are conventions and which are rules

### 8. Decision briefs

For any non-trivial decision, the skill must produce a structured decision brief:

- ELI10: plain English explanation of what is being decided
- Stakes: what happens if we pick wrong
- Recommendation with reason
- Completeness score per option (10 = all edge cases, 7 = happy path, 3 = shortcut)
- At least two pros and one con per option

### 9. Output format

A structured template showing exactly what the output looks like. Use fenced code blocks. Every field documented.

### 10. Context bridge

Cross-session continuity:

- On exit: save current state, decisions made, remaining work, files touched to `.claude/flow-state/contexts/`
- On entry: check for prior saved context, restore if found, warn if branch or state differs
- Compounding: reference any prior learnings relevant to this skill

### 11. Learning capture

After completing the workflow, capture durable discoveries:

- Pattern: reusable approach discovered
- Pitfall: what NOT to do, learned the hard way
- Preference: user-stated preference relevant to this skill
- Architecture: structural decision affecting future work

Save to `.claude/flow-state/learnings/`. Format: `{skill}-{date}-{type}.json`.

### 12. Completion protocol

Every skill invocation ends with a status:

- DONE: completed with evidence
- DONE_WITH_CONCERNS: completed but list concerns
- BLOCKED: cannot proceed, state blocker and what was tried
- NEEDS_CONTEXT: missing information, state exactly what is needed

### 13. Cross-skill integration

- What skills call this one
- What skills this one calls
- What skills this one hands off to
- What skills should NOT be invoked alongside this one

### 14. Plan mode behaviour

- What this skill can do without executing (analysis, planning, review)
- What it must never do in plan mode (write files, execute commands, call external APIs)
- How to signal that plan mode is complete and the skill is ready to execute

### 15. Verification checklist

Before the skill can claim DONE:

- Every phase completed
- Every gate passed
- Every guardrail respected
- Output matches the output format template
- Context saved if governed mode
- Learnings captured if non-trivial
- Completion status accurately reported

## Minimum size

A skill shorter than approximately 8 KB almost certainly does not include the full operational stack. A 15-line stub with four workflow bullets is not a skill. It is a product description.

## White-label rule

Zero business-specific references. A skill must be portable across any business. If a skill mentions "Accor Plus" or any client name, it is not a skill. It is a configuration that leaked. Use `[business name]`, `[contact email]`, `[brand voice]` as placeholders.
