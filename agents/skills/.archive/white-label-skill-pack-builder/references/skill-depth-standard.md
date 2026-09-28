# PerformOS Crew Skill Depth Standard

Captured: 15 June 2026

## Source

This standard was created after the user rejected 47 lightweight 15-line skill stubs as "pathetic" and "terrible" compared to G-Stack's 844-line skills. The user demanded every skill be rebuilt to match G-Stack depth.

## The 14 required sections

1. **Preamble** — bash script recording session start, project root, branch, prior context, state directories
2. **When to invoke** — trigger rules, anti-trigger rules, mode selection (Fast/Careful/Governed)
3. **Cognitive framework** — 3-5 named principles, structured rubric/taxonomy, 5 forcing questions
4. **Step-by-step workflow** — numbered phases with input, action, and output gate (minimum 4, typical 5-7)
5. **Guardrails** — minimum 6 safety constraints, escalation triggers, boundary enforcement
6. **Decision briefs** — ELI10, stakes, recommendation, completeness scoring, pros/cons, net line
7. **Output format** — fenced code block with exact output template
8. **Context bridge** — on-exit save to `.claude/flow-state/contexts/`, on-entry recovery
9. **Learnings capture** — bash logging to `.claude/flow-state/learnings/learnings.jsonl`
10. **Completion protocol** — DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT
11. **Cross-skill integration** — called by, calls, handoff protocol
12. **Plan mode behaviour** — what the skill can/cannot do in plan mode
13. **Verification checklist** — minimum 10 checkboxes before claiming DONE
14. **Brand/domain context** (optional) — voice spec, banned phrases, complaint handling rules

## Reference implementations

The Customer Support Pack was the first pack rebuilt to this standard. The three skills:

- `flow-support-triage` (15.7 KB, 7 phases)
- `flow-support-reply` (16.0 KB, 5 phases, full brand voice embedded)
- `flow-support-feedback` (14.1 KB, 5 phases, root cause taxonomy)

These are the reference implementations. Every future skill must match or exceed this depth.

## Rejection rule

A skill under 5 KB with role statement, four bullet workflow steps, and an output format is REJECTED. It is product marketing, not an executable skill.

## Verification

- Zero em dashes in every SKILL.md
- Zero internal agent names (Brock, Bob, Lara, Neo, etc.)
- Zero runtime references (Hermes, NemoClaw, Claude Code, OpenShell)
- White-label business language only
- Frontmatter: name + description only
