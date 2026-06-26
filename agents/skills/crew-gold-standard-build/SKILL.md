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

One skill at a time by default. Same Claude Code chat. The context carries pack conventions across builds. Splitting loses that.

**Ultracode for everything.** Jared (27 June 2026): "okay, don't change anything. Let's keep everything the same. It's only limited by tokens. It's no extra cost. It's just taking a little bit longer." Run every upgrade in ultracode. Every skill gets the 3-lens adversarial review. The token cost is worth the quality — the review catches real domain errors on every skill.

**Exception — batch related skills.** Three batching patterns are proven:
- **Pairs:** Two halves of the same workflow (context-save + context-restore). The adversarial review verifies they interoperate.
- **Triples:** Three skills sharing the same structural pattern (idea-pressure-tester + plan-reviewer + quality-checker). All review/gate skills, same family, same shape.
- **Do NOT batch unrelated skills.** The reviewer splits attention and errors slip through.

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

Deliver prompts as clean, copyable plain text. **Never wrap the prompt body in markdown code fences.** Jared pastes directly into Claude Code. Code fences force him to manually strip them.

**Correct delivery:**
Each prompt starts with a bold Task line, then sections with bold headers. Paths and commands inline. No ``` markers around the prompt itself.

**Incorrect:** Wrapping prompts in triple-backticks. Forces manual cleanup before pasting.

**Prompt length decreases as a pack fills up.** By skill 5-6 in a pack, the pattern is so established that the prompt can be compact — just the source, the closest same-pack gold sibling as benchmark, the promote candidates, and the standard sections. No need to re-explain the gold-standard structure on every skill.

**Iterate before encoding.** When defining a new pattern (discovery questions, brand-context onboarding, test protocols), get it right in conversation first. Jared: "don't add it to these prompts yet. Let's just get it right first." Push back on premature encoding.

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

## Discovery questions methodology

Every skill needs discovery — the user should never have to guess what to provide. Two patterns proven in this session:

**Build skills (7 questions):** What are we building? Existing brand or new? Show me the product. What style? What mood? Who's the audience? Images: generate or prompts?

**Brand context (11 questions):** What do you do and why does it matter? Who buys from you? Why would a customer leave? If your business was a person at a dinner party, how would they show up? What do you always get right? What are you trying to achieve? Website and online presence? What's unwritten? Where do you let customers down? Anything I must know? What haven't I asked?

**Key insight from this session (26 June 2026):** Questions that produce no actionable data must be cut. The "past agencies/tools" question was removed because it overlapped with "why customers leave" and "anything I must know." Jared's test: "What outcome do you want from this question?" If you can't name the skill action it feeds, drop it.

**Visual design questions do NOT belong in brand onboarding.** A florist or marketing person should never have to think about fonts, colours, or visual style registers. Those are gathered by the design skills at build time or scraped from the website. The brand-context file captures who the business is. The design skills capture what they look like.

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

**Test prompt discipline (critical):** NEVER fabricate company names, product names, or lead data in test prompts. The user has corrected this repeatedly. Three rules:

1. Give the skill RAW MATERIAL — support tickets, URLs, handoffs from upstream skills, real websites. Let the skill source its own questions, extract its own leads, and build its own output. Never pre-digest the data.

2. If testing a chain (lead-research → prospect-brief → outreach-draft), give the first skill real data and let the handoffs carry context forward. Don't skip to the third skill with pre-written briefs.

3. If no real data is available, use the skill's own fixture cases. The fixture IS the test data. Or explicitly state "fictional test data" and flag it as a test-only run.

**FAQ Builder specific:** Give raw support ticket dumps — exact customer phrasing, messy, ungrouped. Not pre-written questions. The skill's job is to extract, group, and write. Pre-written questions bypass the skill's core value.

**Lead Research specific:** Give a real website URL or company name. Let the skill scrape, research, and produce the brief. Don't pre-write the brief and test from there.

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

## Commodity pack upgrade cadence

When upgrading a pack of shallow (5-section) skills:

1. **Anchor first.** Upgrade the skill that siblings build on (lead-research in sales, campaign-plan in marketing, sop-builder in docs).
2. **Use same-pack gold siblings as benchmarks.** Once the anchor is gold, reference IT along with cross-pack benchmarks. This is faster than always referencing 07-support.
3. **One per round.** Paste one prompt, wait for build + adversarial review + QA, then next.
4. **The prompts get shorter** as the pack fills up. By skill 5-6, the pattern is so established that the prompt can be compact — source, closest same-pack gold sibling, promote candidates, standard sections. No re-explanation.
- **Test the chain before calling it done.** Run a real-world test: lead-research → prospect-brief → outreach-draft on a real business. Anti-fabrication, eligibility, and handoff continuity are chain-level concerns that single-skill QA won't catch. Full protocol: references/sales-pack-testing-protocol.md
6. **Throughput (from sales + marketing packs):** 7-skill packs take roughly one session each at ultracode depth. The adversarial review catches real domain errors on every skill (LinkedIn limits, CASL/Spam Act consent models, missing Terms blocks, alt-text-as-invention vectors). The token cost is worth the quality.

## Enrichment tools for sales pack

**ScrapeGraphAI** (https://github.com/ScrapeGraphAI/Scrapegraph-ai): Python library for LLM-powered structured data extraction from websites. For lead research, automates the "visit company website, extract products, pricing, news, growth signals" step. One prompt, one URL, structured JSON. Requires pip install + playwright install + LLM API key. Useful as an automated option in the lead-research `## Research sources` section.

A gap the real-world test exposed: owner names not on public websites. The skill correctly stops at "not found" but the chain needs a LinkedIn/ABN enrichment step the crew pack doesn't have yet. Worth a future crew-sales-lead-enrich skill or Apify LinkedIn integration.

## Prompt discipline

- **No explanatory preamble** when giving Jared a prompt. Deliver the prompt directly. One clean block of text. He'll paste it.
- **Never repeat yourself in a prompt.** Jared flagged this: "you said that paragraph, and how would they arrive? You've said it all twice."
- **Iterate before deploying.** Jared: "don't add it to these prompts yet. Let's just get it right first." Get the thing right in conversation first, THEN encode it into prompts. Don't push half-formed ideas into Claude Code builds.
Lock the prompt format. Never change it. Jared (26 June 2026, training pack): "don't change the prompts though that you're giving me for the next ones. Keep the prompts the same. Everything the same because it's working." And again (27 June 2026): same format, no changes. The upgrade prompt format is frozen. Same structure every skill. No experimentation. No format improvements mid-pack. No preamble, no code fences, no structure changes.

## Never trust memory over disk

Always verify with wc -c and grep -c '^## ' directly on disk.

## Sales pack compliance

The Sales pack must model APAC consent-based spam laws, not just CAN-SPAM (opt-out). The Australian Spam Act requires express or inferred consent before the first commercial send. CASL is similar. CAN-SPAM is opt-out only. These are different legal models — do not conflate them.

The outreach-draft skill correctly splits these. Lead-research and prospect-brief now carry eligibility/compliance screens (do-not-contact, existing-customer, open-opportunity, regulated sector checks) that block downstream skills. The continuity chain matters: lead-research must write its eligibility result into its handoff so prospect-brief's inherited check has something to read.

## Enrichment tools

ScrapeGraphAI (https://github.com/ScrapeGraphAI/Scrapegraph-ai) is a Python library that uses LLMs to extract structured data from websites. For lead research, it can automate the "visit company website, extract products, pricing, news, growth signals" step. One prompt, one URL, structured JSON back. Requires pip install + playwright install + LLM API key. Useful addition to the lead-research `## Research sources` section as an automated extraction option.

## Output format delivery (28 June 2026)

Build skills produce beautiful HTML. But businesses need PowerPoint, Word, and PDF. Three things surfaced from the fresh-install Mac Mini test:

1. **PDF output breaks.** HTML is stunning on screen but "Save as PDF" strips backgrounds, breaks page layouts, and leaves animation artefacts. Fix: add `@media print` block to every build skill output template: page breaks at section boundaries, `print-color-adjust: exact`, animations disabled, margins 0.5in, no navigation UI.

2. **No delivery format choice.** The skill assumes HTML. Add Question 8 to every build skill Discovery: "How should this be delivered? HTML (screen, animations), PDF (clean print), or Both (HTML with print stylesheet)."

3. **No PowerPoint or Word export.** Businesses share .pptx and .docx. The PowerPoint and Word document generation skills handle formatting — build skills should route output to them when those formats are chosen.

4. **Navigation arrows invisible on dark backgrounds.** The slide-deck-builder output has left/right navigation arrows that vanish against dark backgrounds. Contrast check needed in the design review gate for interactive elements.

5. **Animation never fires in output.** The design review gate references `crew-animation-gsap` and `crew-animation-motion` as reviewers, but no actual `<script>` block with animation code gets injected into the HTML. The gate confirms quality but the skill doesn't produce the motion. Fix: add an `## Animation injection` step after HTML generation, before the gate.

## Brand-context hard rule (27 June 2026)

Crew-core-brand-context Discovery section now has a hard rule: "Do not scan the repo, README, or any other file for business clues. Do not guess. The only source of brand truth is brand-context.md or the answers the user gives you. The repo you are installed in is not evidence of who the business is."

This was added because Claude Code auto-loads the repo README into every session. On a fresh install, the brand-context skill saw "Built by PerformOS" in the README and offered it as the business. Two fixes applied:

- **README stripped of brand identification.** "Built by PerformOS" section removed. Brand story lives nowhere in the repo — not README, not ABOUT.md. Repo is technically clean.
- **Skill hard rule added.** Even if Claude reads something, the skill refuses to use it. Only brand-context.md or user answers establish the business.

## Fresh-install directory gap (27 June 2026)

The `.claude/crew-state/` directory does not exist on a brand new machine. Skills' Step 0 tries to read from it and fails with a path error. The skill then tries to route to `crew-core-brand-context` which isn't installed as a plugin. Two issues:

1. **No directory scaffolding.** Nothing creates `.claude/crew-state/` before skills try to read from it. Fix: Step 0 should `mkdir -p` the directory, or the install script should scaffold it.

2. **Cross-skill routing on fresh install.** Step 0 says "run crew-core-brand-context" but that skill isn't registered yet. The FAQ-builder failed on the Mac Mini because it couldn't route. The test bypass was: "Do not route to brand-context. Ask me the 11 onboarding questions yourself."

## Pitfalls

- **README brand leak trap.** Claude Code auto-loads repo README into session context before any skill runs. If the README names a brand or founder, Claude offers it as context to the user. Fix: strip all brand identification from README. Keep it technical.
- **Em dashes in README.** Public-facing repo docs must have zero em dashes. 22 were found and fixed (27 June 2026). Standard is now total.
- **QA workflow step count failure.** Harness requires 6+ numbered Workflow steps between ## Workflow and the next ## heading. If a combined step puts you at 5, split the longest step into two. Proven fix on webcam-website.
- **Substring traps.** "Bob" in "sine bob on y", "Lara" in "gallery". Verify standalone words, not substrings.
- **Coincidental source names.** Read source completely. power-design was an HTML-deck generator, not an authority skill. composition-patterns was React component architecture, not visual composition. Frame around task intent, not source filename.
- **Size decrease can be legitimate.** Framework code stripped (GSAP, Framer, R3F) + section count increased from 5 to 20 = clean extraction. Confirm what was stripped.
- **FAQ Builder testing trap.** Give raw ticket dumps, not pre-written questions. The skill's job is to extract, group, and write. Pre-written questions bypass the core value.
- **Support skills missing discovery.** All skills need discovery questions. Not just build skills. FAQ Builder, Ticket Triage, and every support skill must ask the user what they need before executing.
- **crew-web-design-reviewer phantom.** Never existed. Route gates to real pack-12 skills (quality, composition, patterns).
- **Headless Claude Code fails.** Builds must run interactively. Terminal pipes time out on complex file operations.
- **Series consistency trap.** Asset manifest must enforce consistency lock: same product, same light, same temperature across all images. Without it, each image drifts.
- **Brand-context count lock-in.** Hardcoded "twelve questions" or "61 skills" in 92+ skill Step 0 boilerplate breaks on every change. Use count-agnostic language: "a few quick questions" and "every skill." Fixed once, never breaks again.
- **Compliance model conflation.** CAN-SPAM (US, opt-out) and CASL/Australian Spam Act (consent-based, express or inferred) are different legal models. Sales outreach skills must split these correctly. The Australian Spam Act's 3-to-5-unanswered-message rule is the highest-stakes compliance note for APAC sellers.
- **Proposal Terms gap.** A skill that defines a Terms section but never produces one in the emit-ready artifact is shipping incomplete contracts. Legal exposure. Verify the output template has every section the skill claims.

## Session continuity protocol

When a long build session hits Claude Code token limits (ultracode chews through them), do a clean handover:

1. **Save a Brock handoff** to `.claude/crew-state/brock-handoff.md`. Include: pack in progress, skills done, skill currently building, remaining skills, source paths, benchmark references, the standard upgrade pattern, and standing rules.

2. **Open a fresh Claude Code chat** from the crew-skill-packs directory.

3. **First message:** "Read .claude/crew-state/brock-handoff.md and pick up where I left off."

Brock stays in the original chat. Claude Code resumes in the fresh chat. No context lost. No re-teaching.

**Fresh chat handover trap (critical pitfall).** When continuing work in a new chat, always verify every skill claimed as gold is actually upgraded on disk. coaching-conversation-guide (27 June 2026) was claimed gold by the fresh chat but was still at 5 sections/10KB — only Step 0 brand-context was added, not the full upgrade. Always verify with wc -c and grep -c '^## ' before marking done. Never trust a fresh chat claim without disk verification.

## Throughput and stats

**Complete packs (27 June 2026):** All 14 packs — 01-core (8), 02-sales (7), 03-marketing (7), 04-ops (5), 05-hr (5), 06-finance (6), 07-support (6), 08-docs (7), 09-training (8), 10-web-design (9), 11-infrastructure (1), 12-design-standards (7), 13-design-styles (5), 14-animation (12). **93 of 93 gold. 100%.** ~3.5MB of skill content. **All sweeps complete:** count-agnostic boilerplate, AU-law generalisation (24 replacements, 8 files), 30-skill Discovery sweep, FAQ builder em dash. **Distribution complete:** 15 zips, 16 plugins, GitHub repo live. **Remaining:** fresh-install test, hooks architecture.

Pack throughput: 7-skill packs (sales, marketing, docs, training) take roughly one session each at ultracode depth. 5-skill packs (ops, hr) take half a session. Core utility skills can be batched in pairs (context-save + context-restore) or triples (idea-pressure-tester + plan-reviewer + quality-checker) because they share the same structural pattern and domain.

## Gap analysis methodology

After every build wave, run a systematic 4-layer sweep across all skills:

1. **Structural gaps** — Discovery sections, Modes, Verification, Completion, handoff paths, brand-context in Step 0, em dashes, banned terms. Automated via grep sweeps.
2. **Integration gaps** — cross-pack references without guarantees. What happens when skills reference each other but aren't installed? Chain-level concerns QA won't catch.
3. **Quality gaps** — design review gates only in pack 10. Other packs have Verification checklists but no automated gate. Smoke tests blocked by CLI auth — structural QA is the gate but functional output unconfirmed.
4. **Runtime gaps** — no error recovery, no fresh-install test, plugins not built, image MCP not connected, AU-law hardcoding in 4 training skills.

The highest-risk gap is always the fresh-install test. We've never wiped the skill registry and installed from zero. Everything else is fixable. That one could reveal fundamental architecture problems.

## Hooks architecture (post-gold, from Ruflo review)

After all packs are gold, add three hook skills: pre-flight (validates inputs, checks brand context on load), post-flight (runs quality gate before handoff save), error-recovery (captures failure state, writes recovery handoff). Wire into all skills' Step 0 and Final Step. One session to build + one batch sweep. Identified from Ruflo review as the one missing architectural piece. CREW has everything else Ruflo promised but didn't deliver.

## Post-build plan

After all commodity packs are gold, four sweeps and distribution:

### Sweep 1: Count-agnostic boilerplate
Replace hardcoded "twelve questions" → "a few quick questions" across all shipped SKILL.md files. One prompt, idempotent script, verified with grep. Never breaks on a count change again.

### Sweep 2: AU-law generalisation (27 June 2026)
Replace every hardcoded AU statute (Disability Discrimination Act, Privacy Act, ACL ss 18/29, Fair Work Act, WHS) → "local law (jurisdiction from brand-context.md)." 24 replacements across 8 files. Leave dialect defaults (Australian English) untouched — those are language, not statute. One prompt. Verified with grep for zero statute residuals. All 14 packs QA PASS.

### Sweep 3: Discovery sweep (27 June 2026)
Add Discovery sections to 30 gold skills across 4 packs (07, 12, 13, 14) that were upgraded before the Discovery pattern existed. Identical ## Discovery block after role paragraph, before ## Inputs. +9 lines per file, nothing else touched. One prompt. Verified with placement check + QA all 4 packs.

### Sweep 4: Em dash fix
FAQ builder line 43. One character. 30 seconds.

### Distribution (DONE — 27 June 2026)
package.sh and build-plugins.sh updated for all 14 packs. 15 zips built (14 per-pack + 1 full bundle at 2.0MB). 16 plugins built (14 pack plugins + crew-full + crew-installer). Marketplace manifest regenerated.

### GitHub repo (DONE — 27 June 2026)
Private repo at github.com/jaredcroxton/crew-skill-packs. 216 files, 34,622 lines. Professional README with header image, badges, architecture, pack table, quality standards, brand story. MIT LICENSE. .gitignore. Pushed on main. Full presentation standards: references/github-repo-presentation.md

### Fresh install test (NOT YET DONE)
Wipe Claude skill registry. Install CREW packs clean. Run full onboarding flow as a brand new company. Test every layer.

### Hooks architecture (NOT YET DONE, post-gold)
Three hook skills: pre-flight, post-flight, error-recovery. Wire into all skills' Step 0 and Final Step.

## QA crew-state scope fix

the white-label guard for shipped content stays fully intact.

- **Fresh chat handover trap.** When continuing work in a new Claude Code chat to save tokens, verify every skill claimed as gold is actually upgraded on disk. coaching-conversation-guide (27 June 2026) was claimed gold but was still at 5 sections/10KB — the fresh chat only added Step 0 brand-context. Always verify with wc -c and grep -c '^## ' before marking done.
- **Silent default trap.** Numerical floors/thresholds used at output time that were never gathered in discovery silently default to zero and defeat the floor discipline. The finance cashflow-brief minimum-cash-buffer was used in output but never solicited. If a number gates a decision (minimum cash, maximum budget, target threshold), it MUST be gathered in Discovery or Inputs, never defaulted.
- **AU-law dialect trap.** When generalising hardcoded AU statutes, leave dialect defaults (Australian English, AU workplace) untouched. Those are language preferences, not legal references. Every gold skill can default to its local dialect. The statute replacement targets only legal acts and regulations.

## Canonical paths

- Pack tree: /Users/jc/Desktop/cluade/crew-skill-packs/packs/
- Migration source: /Users/jc/.claude/skills/
- QA harness: /Users/jc/Desktop/cluade/crew-skill-packs/shared/qa-check.sh
