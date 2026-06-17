# Crew skill pack review methodology

Use this when Jared asks Brock to review Claude Code's completed skill packs before sign-off. Applied and proven on the 58-skill Crew build (17 June 2026).

## Purpose

Review every pack against a fixed standard before it ships. Do not trust build logs. Read actual files. Run structural sweeps. Return a pass/amber/fail verdict per gate.

## The 7 gates

### Gate 1: Is it actually a skill, not a brochure?

Read one skill per pack. Minimum bar:
- Named expert role with cognitive instinct
- Decision forks (not just sequential steps)
- Forcing questions asked one at a time
- Verification step that re-reads inputs before emitting
- At least 6 numbered workflow phases
- Fenced output block with a filled example

If a skill reads like a product description with four bullet points, it fails.

### Gate 2: Is it white-label?

Search all SKILL.md files for banned names:
- Internal agent names (Brock, Bob, Lara, Neo)
- Runtime references (Hermes, NemoClaw, Claude Code)
- Source-tool names (gstack, gbrain)
- Product names in skill bodies (PerformOS)

Also check CREDITS.md — it must state all text is authored fresh, credit influences only, and name no internal files.

### Gate 3: Does it follow the promised methodology?

Every skill must visibly reference the 8 standards and 5 loops documented in crew-method.md. Check:
- Handoffs section names crew-core-quality-checker and crew-core-context-save
- Verification step exists before emitting
- Guardrails include "label inferences, name sources"
- Context Loop (Step 0 + Final Step) is present

### Gate 4: Does it have loops?

Check that the skill's workflow has decision forks, not a straight line:
- Missing input: "ask once, then proceed with gaps marked"
- Quality failure: "verify, revise, re-verify"
- Escalation: "mark and route, never fabricate"
- Context change: Step 0 recovery + Final Step save
- Learning capture: the "Learned" note in the handoff

### Gate 5: Is it testable?

Check:
- A tests/ directory exists per pack
- One fixture per skill (3 cases minimum: clean, messy, missing-input)
- Fixtures have EXPECT markers the smoke harness asserts against
- qa-check.sh has structural and functional smoke passes

### Gate 6: Does it integrate?

Check the Handoffs section in each skill:
- Names at least one sibling skill by name
- Names crew-core-quality-checker
- Names crew-core-context-save
- References crew-method.md as the methodological parent

### Gate 7: Is the install package real?

Check:
- install.sh exists and supports --dry-run, --pack, --target
- package.sh gates on QA pass
- Zips are self-contained (installer + method + credits per zip)
- Plugin wrapper works: /crew:install, /crew:list, /crew:uninstall
- No settings, hooks, or CLAUDE.md edits

## Sweep commands

Run these on every pack before sign-off:

```bash
# Em dashes
grep -rn '—' --include="*.md" packs/ | head -20

# Banned names
grep -rn 'Brock\|Bob\b\|\bLara\b\|\bNeo\b\|Hermes\|NemoClaw\|gstack\|gbrain\|PerformOS' --include="*.md" packs/

# Context Loop presence
for dir in */crew-*/SKILL.md; do
  if ! grep -q "Step 0: Context Recovery" "$dir"; then echo "MISSING Step 0: $dir"; fi
  if ! grep -q "Handoff Save" "$dir"; then echo "MISSING Handoff Save: $dir"; fi
done
```

## Inspection depth

At minimum, read one skill from every pack in full. For packs flagged as "limit boundary" or "first of a new phase," read two skills. Always read the gold standard skill first to calibrate the bar.

## Verdicts

- **Green:** Passes all 7 gates. Approve.
- **Amber:** Passes structure but has a gap (e.g. smoke not run, fixture too light). Approve with conditions.
- **Red:** Fails a gate. Reject. Name the exact skill and section that failed.

## Output format

Return a review with:
- Source agent, what it is, audience, decision needed
- Gate-by-gate table with Pass/Amber/Fail and evidence column
- Inspection register listing every skill read in full with line count and quality note
- Structural sweep results (em dashes, banned names, Context Loop)
- Honest gaps (things Claude flagged, things you found)
- Overall verdict
- Exact reply to give Claude Code
