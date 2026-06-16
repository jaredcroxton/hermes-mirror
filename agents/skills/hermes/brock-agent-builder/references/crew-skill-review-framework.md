# Crew Skill Pack — 7-Gate Review Framework

Use this when Claude Code returns a build plan for a new Crew skill pack. Apply before approving any construction.

## The 7 gates

### Gate 1: Is it actually a skill, not a brochure?

A real skill must include:
- when to use it (trigger conditions)
- when not to use it (anti-trigger conditions)
- intake questions
- step-by-step deterministic workflow with decision forks
- decision rules and taxonomies
- quality checks
- escalation rules
- output format with a filled example
- context save (handoff)
- handoff to other skills
- test cases

If the output only says "What it does, workflow, example output" with bullet points, it fails. It is a product description, not an executable skill.

### Gate 2: Is it white-label?

No client-specific names. No Accor Plus. No PerformOS internal context. No Brock, Bob, Lara, Neo. No runtime names (Hermes, NemoClaw, Claude Code). No local machine paths unless they are installation instructions.

The skill must work for a gym, a law firm, a real estate agency, an education provider, a finance team, a customer support team. Same skill, different business context.

### Gate 3: Does it follow the promised methodology?

Every skill should visibly follow the 8 standards:
1. Brainstorm before building
2. Plan in bite-sized steps
3. Build with testing built in
4. Debug from root cause
5. Verify before claiming done
6. Review before shipping
7. Finish cleanly
8. Save and restore context

If these are in the PDF but not wired into the skill's workflow steps, the skill fails.

### Gate 4: Does it have loops?

A world-class skill is not a straight line. It needs:
- **Missing input loop** — if information is missing, ask for it. Never fabricate.
- **Quality failure loop** — if output fails verification, revise and re-verify.
- **Escalation loop** — if risk is high (legal, safety, financial, media), escalate to human.
- **Context change loop** — Step 0 reads prior handoff; Final Step writes new handoff.
- **Learning capture loop** — patterns and corrections saved for compounding across sessions.

No loops means no real intelligence.

### Gate 5: Is it testable?

Minimum per skill:
- One clean scenario
- One messy real-world scenario
- One missing-input scenario
- One edge case
- Expected output markers the smoke test can assert against

If it cannot be tested, it is not ready to sell.

### Gate 6: Does it integrate with the rest of the Crew?

Each skill needs to state:
- which skill comes before it
- which skill comes after it
- what context it needs from the prior handoff
- what context it saves for the next skill
- what handoff it produces

Integration means handoffs, not just a folder of standalone prompts.

### Gate 7: Is the install package real?

For client installs:
- Folder structure with one SKILL.md per skill
- No global install, no hooks, no hidden dependencies
- Test fixtures
- Smoke-test script or checklist
- README for installation
- CREDITS.md for methodology lineage
- Acceptance criteria

If it cannot be copied into a new `.claude/skills/` folder and used, it is not sellable.

## Verdict language

- **Green:** approve and build. All 7 gates pass.
- **Amber:** fix specific items before build. Name exactly what is missing.
- **Red:** reject. Too shallow. Do not build until the plan is rewritten.

## Applying the framework

When Claude Code sends a build plan:
1. Run each gate against the plan.
2. Return the gate-by-gate assessment.
3. Give the exact reply to send back to Claude Code.
4. Do not approve anything that looks like 15-line stubs.

Captured 16 June 2026 from the Phase 1 Crew Skill Packs build review.
