---
name: crew-gold-standard-build
description: Use when Jared and Brock are upgrading Crew skills to gold-standard depth. Covers shallow upgrades, migration from .claude/skills, merged-source skills, and commodity pack upgrades. Includes prompt templates, Brock review checklist, and architectural conventions.
category: performos
---

# Crew Gold-Standard Build

## When to use

Jared wants to bring a Crew skill to gold-standard depth. Four scenarios:

1. **Shallow upgrade:** A canonical skill exists at 5 sections. Needs the full 15+ section treatment.
2. **Migration:** A skill in /Users/jc/.claude/skills/ needs porting into the crew pack tree.
3. **Merged-source:** Two .claude/skills/ files cover the same library. Merge into one crew skill.
4. **Commodity pack upgrade:** Shallow skills in packs 01-09, 11 need gold-standard treatment.

## Execution cadence

One skill at a time. Same Claude Code chat. The context carries pack conventions across builds. Splitting loses that.

For anchor skills and design packs: "Run in ultracode." After building, run the 3-lens adversarial review before the smoke QA.

Brock writes prompts. Jared pastes into Claude Code. Brock reviews output before writing the next prompt.

## Gold standard definition

A gold-standard Crew skill has:

- 15 ## sections minimum: Inputs, Modes and when to use them, cognitive framework, domain-specific reference sections, Workflow (Step 0 + 6+ numbered steps + Final Step), Output format, Decision briefs, Guardrails, Handoffs, Plan mode, Verification, Completion
- Context Loop: Step 0 reads from .claude/crew-state/<pack>/<skill>-handoff.md, Final Step writes back
- Brand context: Step 0 reads .claude/crew-state/brand-context.md BEFORE the per-skill handoff
- White-label: no Accor examples, no internal agent names, no Sarah
- No em dashes
- Fixture: Cases A, B, and C all required
- Discovery section: after role paragraph, before Inputs
- QA PASS on --smoke --pack <pack>

No arbitrary size ceiling. Skills go as deep as content demands.

## Prompt format

Clean, copyable plain text. No markdown code fences wrapping the prompt body. Bold headers. Paths and commands inline.

**Correct format:**

```
**Task:** Upgrade X to gold-standard depth. Run in ultracode.

**Source file:** /path/to/source
**Target file:** /path/to/target
**Reference benchmarks:**
- /path/to/benchmark-1
- /path/to/benchmark-2
**Current state:** size, sections, description.

**What to do:**
1. Read source completely. Preserve ALL existing depth.
2. Read benchmarks for structure.
3. Add Discovery section + 6 gold-standard sections.
4. Promote buried Workflow content into ## reference sections.
5. Context Loop, fixture A/B/C, adversarial review, QA.
6. Report.
```

## Shallow upgrade prompt template

```
**Task:** Upgrade crew-<pack>-<skill> from 5 sections to full gold-standard depth. Run in ultracode.

**Source file:** [path]
**Reference benchmarks:**
- [same-pack sibling at gold standard]
- [cross-pack benchmark for structure]
**Current state:** ~X bytes, 5 sections.

**What to do:**
1. Read source completely. Preserve ALL existing depth.
2. Read benchmarks.
3. Add Discovery section after role paragraph.
4. Add 6 gold-standard sections: Modes, How the [skill] thinks, Decision briefs, Plan mode, Verification, Completion.
5. Promote buried Workflow blocks to ## reference sections. Name candidates in the prompt.
6. Context Loop, fixture A/B/C, adversarial review (3 lenses), QA.
7. Report: old size, new size, sections added/promoted, QA result.
```

## Two extraction patterns

### Pattern A: Promote ### to ##

Skill has ### headings with real depth. Promote to ##.

### Pattern B: Extract from monolith Workflow (most common)

Skill has ZERO ### headings. Extract and consolidate buried detail into ## reference sections. Thin Workflow steps to one-line pointers. Net new content is structural only.

Proven across: escalation-review (5 extracted), faq-builder (4 extracted), lead-dashboard-builder (6 extracted), fly-through-builder (4 extracted), lead-research (5 extracted).

## Discovery sections

Every skill needs a Discovery section after the role paragraph, before Inputs. Build skills use the 7-question design discovery. Support skills use the 5-question pattern. Commodity pack skills use domain-specific discovery.

## Brand context architecture

Every Crew skill reads .claude/crew-state/brand-context.md in Step 0 before its own handoff. If the file exists: "Working with [brand]." If not: route to crew-core-brand-context for the 11-question onboarding. 93 skills have this wired.

The brand-context file captures who the business is. Design specifics are gathered by design skills at build time. A florist can onboard without thinking about fonts.

## Design review gates (pack 10)

Every build skill must have a ## Design review gate referencing packs 12-14 with pass/fail conditions.

## Dual failure mode (style skills)

Style skills must fail in two opposite directions with named verdict axes. The "right lens" off-ramp fires before dimensional scoring.

## Adversarial review

After every ultracode build, run 3 independent lenses: harness-compliance, leak/ban audit, senior-domain-engineer content critique. Apply sharp refinements before smoke QA.

## Live testing protocol

After structural QA, test against a real input designed to trigger one specific failure mode or boundary decision. For build skills: build and inspect on localhost. For style skills: review a deliberately-wrong design. For animation skills: route to siblings at correct boundaries.

## Asset manifest (pack 10)

Every build skill outputs a prompt manifest alongside the HTML. Series consistency lock enforces same product, same light, same temperature across all images.

## Design pack naming

After market research (24 June 2026): "taste" rejected. Enterprise buyers understand "standards."

| Pack | Name |
|------|------|
| 12 | design-standards |
| 13 | design-styles |
| 14 | animation |

## Brock review checklist

1. **Size:** wc -c on target. Confirm growth or legitimate decrease.
2. **Sections:** grep -c '^## ' — 15 minimum.
3. **Banned terms:** grep -in for Accor, Sarah, PerformOS, Brock, Bob, Lara, Hermes[^s], gstack, APOGEE, apogee, jaredcroxton, aether-genesis, Lila.
4. **Em dashes:** grep -c '—' — must be 0.
5. **Harness:** Step 0, Final Step, handoff path, output header, Guardrails contains "em dash", frontmatter exactly two keys.
6. **Fixture:** Cases A, B, C all present.
7. **Off-ramps:** register skills must have "when this is the WRONG lens" guards.
8. **Report:** table format.

## Never trust memory over disk

Always verify with wc -c and grep -c '^## ' directly on disk.

## Pitfalls

- **QA workflow step count failure.** Split longest combined step if below 6.
- **Substring traps.** "Bob" in "sine bob on y", "Lara" in "gallery". Verify standalone words.
- **Coincidental source names.** Read source completely. Frame around task intent.
- **Size decrease can be legitimate.** Framework code stripped + section count increased = clean extraction.
- **FAQ Builder testing trap.** Give raw ticket dumps, not pre-written questions.
- **Support skills missing discovery.** All skills need discovery questions.
- **crew-web-design-reviewer phantom.** Never existed. Route gates to real pack-12 skills.
- **Headless Claude Code fails.** Builds must run interactively.
- **Series consistency trap.** Asset manifest must enforce consistency lock.

## Canonical paths

- Pack tree: /Users/jc/Desktop/cluade/crew-skill-packs/packs/
- Migration source: /Users/jc/.claude/skills/
- QA harness: /Users/jc/Desktop/cluade/crew-skill-packs/shared/qa-check.sh
