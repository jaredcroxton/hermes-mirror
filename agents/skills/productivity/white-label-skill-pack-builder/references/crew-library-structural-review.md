# Crew Library Structural Review — 23 June 2026

This document captures findings from the Brock-level review of the Crew skill library. It is the structural companion to the current-state count reference.

## Current Architecture

11 packs, 63 skills. Every skill has a test fixture (clean, messy, missing-input). Build pipeline works. Plugin system works. Shared method and template are consistently applied.

## Pack-by-Pack Assessment

### Pack 01 — Core (7 skills)
**Status:** Solid. Dispatcher (crew-core-using-crew) plus 6 foundation skills (context save/restore, guard boundary, idea pressure tester, plan reviewer, quality checker). This is the bedrock. Do not change.

### Pack 02 — Sales (7 skills)
**Status:** Good but has a gap. Skills cover lead research, prospect brief, outreach draft, follow-up sequence, CRM cleanup, pipeline review, proposal builder. All are B2B enterprise sales oriented. **Missing:** high-volume outbound telesales skills (call scripting, objection handling for outbound, daily huddle prep, dial/talk-time/connects tracking). If Crew is used for Accor Plus work, this gap matters.

### Pack 03 — Marketing (7 skills)
Status: Solid. Brand voice check, campaign plan, content repurpose, email campaign builder, landing page review, SEO page builder, social post pack. Covers the full content pipeline.

### Pack 04 — Operations (5 skills)
Status: Solid. Automation opportunity review, operations dashboard plan, process map, recurring task automation, workflow improvement.

### Pack 05 — HR and People (5 skills)
Status: Solid. Employee communication draft, interview guide, performance conversation prep, policy summary, role profile builder. All follow structured evidence-based patterns.

### Pack 06 — Finance and Admin (6 skills)
Status: Solid. Admin automation, cashflow brief, expense review, finance dashboard plan, invoice workflow, monthly summary.

### Pack 07 — Customer Support (6 skills)
Status: Solid. Escalation review, FAQ builder, feedback summary, help document generator, reply builder, ticket triage.

### Pack 08 — Documentation (7 skills)
Status: Solid. Client playbook builder, compliance review check, handover document writer, meeting notes to actions, policy document generator, SOP builder, training guide creator.

### Pack 09 — Training and L&D (8 skills)
**Status:** Strongest pack for Jared's day job. Assessment designer, coaching conversation guide, facilitator guide creator, learner workbook builder, module outline builder, needs analyser, onboarding programme builder, skill gap mapper. Covers the full L&D pipeline from needs analysis through assessment. **Opportunity:** None of the skills reference Accor Plus, telesales, or APAC market context. They are generic by design (white-label), but adding domain-specific variants would increase value for Jared's core work.

### Pack 10 — Web Design (3 skills)
**Status:** Too narrow. Fly-through builder (heavily tailored to APOGEE build), slide deck builder, lead dashboard builder. The fly-through builder is essentially a production manual for one specific site. If Crew is a reusable product, this pack needs more general-purpose web design skills (landing page builder, portfolio site builder, blog/template site builder).

### Pack 11 — Infrastructure (1 skill)
**Status:** Minimal but functional. Project builder covers the full 5-phase build protocol (blueprint, link, architect, stylize, trigger). Could benefit from additional infrastructure skills (API integration builder, webhook configurator, monitoring setup).

## Structural Observations

1. **The training pack is the highest-value pack for Jared's day job** but is not connected to his Accor Plus context. Eight skills covering the full L&D pipeline, none referencing telesales, APAC markets, or the six Accor Plus sales pillars.

2. **The sales pack has a telesales gap.** All 7 skills are B2B enterprise. High-volume outbound telesales (Jared's actual environment) is a different motion. A telesales-specific skill or two would make this pack directly useful.

3. **Pack 10 is project-specific, not general-purpose.** The fly-through builder is tied to APOGEE. For Crew to be a product, this pack needs skills that work for any client.

4. **Quality is consistently high across all 63 skills.** The locked template is working. Every skill has the Context Loop, guardrails, handoffs, and test fixtures. No AI slop detected.

5. **The shared method (crew-method.md) and template (SKILL-TEMPLATE.md) are the backbone.** They are referenced by every skill and keep the library coherent. Do not change these without reviewing all 63 skills.

## Recommended Next Steps (Priority Order)

1. Add a telesales-specific skill to the sales pack (call scripting, objection handling for outbound)
2. Add Accor Plus context variants to the training pack (telesales learner profiles, APAC considerations)
3. Generalise pack 10 with additional web design skills not tied to a single project
4. Consider adding infrastructure skills to pack 11 (API integration, webhook config)
