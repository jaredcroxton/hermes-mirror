# CREW Gap Analysis — 27 June 2026

## State at analysis
82 of 93 gold skills. 11 complete packs. 11 remaining.

## Structural Gaps

### Discovery sections missing (30 skills)
Packs 07, 12, 13, 14 were built before the Discovery pattern. None have `## Discovery` sections.
- 07-support: 6 skills
- 12-design-standards: 7 skills
- 13-design-styles: 5 skills
- 14-animation: 12 skills

### Brand-context at 13 sections
2 short of the 15-section gold floor. Anchor skill every other skill depends on.

### Em dash in FAQ builder
Line 43: "Same rules apply — capture exact phrasing." One character fix.

### AU-law hardcoding
4 training skills (facilitator-guide, learner-workbook, onboarding, skill-gap-mapper) mention specific Australian acts. Not fatal for AU users. Wrong for everyone else.

## Integration Gaps

### Cross-pack references without guarantees
FAQ-builder hands to help-document-generator. CRM-cleanup references pipeline-review handoff. If a business bought one pack but not the other, those references break. No graceful fallback.

### No full-chain test
Never tested: brand-context → discovery → build → design review gate → output in one session.

### Design packs (12-14) are reference-only
Can't be invoked for output. Their Workflows say "produce a spec." A business might try to "run" crew-animation-gsap and get nothing deployable. Anti-triggers in Modes cover this but it's still confusing.

## Quality Gaps

### No smoke tests have passed
CLI 401 has blocked functional QA since day one. Every skill is structurally green. Zero skills confirmed to produce correct output under automated testing.

### Image generation gap
Build skills produce prompt manifests. Can't auto-generate. Higgsfield/KIE MCP not connected. Cinematic builds ship with placeholder voids.

### Design review gates only in pack 10
Support, sales, marketing skills have Verification checklists but no automated gate that blocks ship. Quality is manual.

## Runtime Gaps

### No error recovery
If step 4 of 7 fails, nothing captures state. User starts over. No handoff from failure. No route to fix.

### No fresh-install test
Never wiped .claude/skills/ and installed CREW from zero. Brand-context flow, Step 0 reads, handoff paths all assume files already exist. **Highest-risk gap.**

### Plugins not built
No zips. No installers. No distribution. Skills exist on disk. A business can't install them.

## Fix Sequence

| Priority | Gap | Effort |
|----------|-----|--------|
| 1 | Fresh-install test | 1 session |
| 2 | 30-skill Discovery sweep | 1 prompt |
| 3 | Brand-context to 15 sections | 1 prompt |
| 4 | FAQ em dash | 30 seconds |
| 5 | Image MCP integration | 1 prompt per build skill |
| 6 | Smoke test actual output | Ongoing |
| 7 | Error recovery hooks | 1 session (post-gold) |
| 8 | AU-law generalization | 1 prompt |
| 9 | Cross-pack reference hardening | 1 prompt |
| 10 | Distribution (plugins, zips) | 1 session |
