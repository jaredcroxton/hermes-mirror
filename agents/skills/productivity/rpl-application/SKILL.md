---
name: rpl-application
description: Build airtight Recognition of Prior Learning (RPL) applications that map professional experience to university learning outcomes. Use when the user asks for RPL, prior learning recognition, credit transfer based on work experience, or mapping their job to academic unit learning outcomes.
version: 1.0.0
author: PerformOS / Jared Croxton
metadata:
  hermes:
    tags: [rpl, academic, university, recognition, credit-transfer]
    category: productivity
---

# RPL Application Builder

## When to use this skill

Load this skill when:
- User asks for RPL, Recognition of Prior Learning, or credit transfer based on work experience
- User wants to map their professional experience to university learning outcomes
- User needs to build a formal submission for university assessment panels
- User asks to "make the case" or "build an airtight submission" for course credit

## Core methodology

An RPL application is an evidence-based argument. The assessment panel is not looking for a CV. They are looking for proof that the applicant has already achieved the learning outcomes through professional practice.

### The golden rule

**Every learning outcome must be addressed explicitly.** An empty mapping section is a guaranteed rejection. The panel will not infer evidence. You must connect each outcome to specific, named, verifiable experience.

## Document structure

An RPL application package typically has three documents:

### 1. Cover letter (1-2 pages)
- Formal letter format addressed to the Assessment Panel
- States which units are being applied for with codes
- Summarises the key evidence at a high level
- References the enclosed CV and RPL Statement
- Signed and dated

### 2. RPL Statement (the main document, 4-6 pages)
- Introduction: role context, scope, and the transformation/experience being relied on
- For each unit:
  - Narrative paragraph describing the relevant work
  - Explicit "Mapping to ECU Learning Outcomes" section
  - Each learning outcome addressed with a bold header and evidence paragraph
- Evidence of Leadership Scope: bullet-point summary
- Verification: signed by a senior leader who can confirm the claims

### 3. CV (supporting document)
- Professional summary aligned to the RPL claim
- Role progression showing increasing accountability
- Areas of expertise that map to the units
- Education and professional development

## Learning outcome mapping pattern

For each learning outcome, use this structure:

```
**Learning Outcome X: [exact wording from handbook].** [Evidence paragraph that:
  1. Opens with a direct claim matching the outcome verb
  2. Provides specific, named examples (programs, frameworks, metrics, regions)
  3. Includes quantitative evidence where available (percentages, team sizes, market counts)
  4. Closes by linking back to how this demonstrates the outcome]
```

### Key verbs and how to match them

| If the LO says... | Your evidence must show... |
|---|---|
| Examine | You have studied and applied global/disciplinary knowledge |
| Analyse | You have broken down a system or problem and drawn conclusions |
| Critique | You have identified issues, tensions, or limitations in practice |
| Justify | You have made and defended strategic decisions with rationale |
| Integrate | You have combined theory with practice in applied settings |
| Assess | You have evaluated a context or structure and acted on findings |
| Communicate | You have delivered knowledge to different audiences effectively |
| Collaborate | You have worked cross-functionally to produce solutions |

## Quality gates

Before finalising, verify:

1. **Market/region count consistency.** Every reference to how many markets/countries must match across all three documents.
2. **Date alignment.** Cover letter date matches submission date. CV and statement dates match.
3. **Every LO addressed.** Count them. If a unit has 5 LOs, there must be 5 explicit mapping entries.
4. **No empty sections.** "Mapping to ECU Learning Outcomes:" with nothing under it is a fail.
5. **Named evidence only.** "I led a transformation" is weak. "I led the first product transformation in 30 years across nine countries using Kotter and ADKAR" is strong.
6. **Verification present.** The statement must name the verifying executive with title and organisation.
7. **Unit codes correct.** Cross-check against the handbook URLs provided.

## Cross-checking consistency

After building all documents, run a verification script that checks:
- All market/country counts match
- All unit codes appear in all documents
- Key named evidence (programs, frameworks, metrics) appears consistently
- No "seven" where there should be "eight" (or vice versa)
- Date is correct and consistent

## Formatting standards

Use `word-document-generation` skill for .docx output. For RPL documents specifically:
- Calibri 11pt body, single line spacing, 2.54cm margins
- Section headers: 14pt bold
- Sub-headers (Learning Outcomes): 12pt bold
- Learning outcome labels in bold, evidence text in regular weight
- Bullet points for evidence of leadership scope
- Separator lines between units

## Pitfalls

1. **Empty mapping sections.** The most common RPL rejection reason. If the user's existing document has "Mapping to ECU Learning Outcomes:" with nothing underneath, that is the critical gap. Fill it completely.
2. **Generic evidence.** "I lead teams" fails. "I lead operations across eight APAC markets with 350+ team members" passes.
3. **Inconsistent numbers.** The cover letter says 7 markets, the CV says 7, the statement says 8. Panel will notice. Cross-check every number.
4. **Missing the verb.** If the LO says "critique" and your evidence only describes what you built, you have not met the outcome. Match the verb.
5. **No verification.** An unverified RPL statement carries less weight. Include a named verifier with title.
6. **Outdated dates.** Cover letters dated months before submission signal a rushed or recycled application.

## Reference files

- `references/ecu-rpl-example.md` — Full worked example of an ECU RPL statement structure with three-unit mapping pattern.
