---
name: academic-award-nomination
description: Build competitive university award and scholarship self-nominations by mapping completed coursework to professional outcomes. Use when the user asks about applying for a university award, scholarship, Vice-Chancellor's award, or any competitive academic recognition that requires evidence of impact.
version: 1.0.0
author: Brock / Jared Croxton
metadata:
  hermes:
    tags: [academic, university, award, scholarship, nomination, ecu]
    category: productivity
---

# Academic Award Nomination Builder

## When to use this skill

Load this skill when:
- User wants to self-nominate for a university award, scholarship, or prize
- User asks whether they have a viable case for a competitive academic award
- User needs to draft nomination sections (summary, evidence, sustainable impact)
- User asks about endorsement requirements or submission logistics

This is NOT for RPL (Recognition of Prior Learning) applications. RPL says "I already know this, give me credit." An award nomination says "Look what I did with the learning, give me recognition." For RPL, use the `rpl-application` skill.

## Core methodology

An award nomination is an evidence-based argument that the nominee's academic work translated into real-world impact beyond what is reasonably expected of a student. The panel evaluates on four lenses:

1. **Depth of Impact** — degree of change or influence achieved
2. **Breadth of Impact** — reach of the change or influence
3. **Sustainability of Impact** — expected longevity of the change
4. **Relevance of Impact** — alignment with award purpose and university values

### The golden rule

**Every claim must be traceable to a specific subject, a specific professional action, and a specific measurable outcome.** "I applied my studies at work" is weak. "HRM6008 People Analytics directly informed the KPI framework I redesigned across seven APAC markets, improving performance visibility for 100+ sales agents" is strong.

## The subject-to-career mapping technique

For each completed subject, map three things:

| Element | Example |
|---|---|
| What was learned | Workforce data methodologies, KPI frameworks |
| How it was applied | Redesigned performance dashboards across seven markets |
| Measurable outcome | Improved KPI visibility for 100+ agents; promotion to Director |

Build a table internally before writing. Every subject with a grade of Distinction or above should have a clear application story. If a subject cannot be mapped to a professional outcome, leave it out. An unmapped subject weakens the narrative.

## The three-section nomination structure

Most university awards use a variant of this structure. Load the `references/` file for award-specific word counts and section names.

### Section 1: Summary (typically 500 words)

This is the narrative arc. Structure it as:

1. **Opening hook** — the most impressive single fact (promotion, grade, scale)
2. **Subject-by-subject evidence** — each completed subject mapped to a professional outcome, with named frameworks, metrics, and regions
3. **Beyond-the-degree evidence** — what the nominee did that no coursework required (side ventures, additional study, workshops delivered, products built)
4. **Closing frame** — why this adds up to something exceptional, tied to university values

### Section 2: Evidence of Impact (typically 200 words)

Three paragraphs maximum:
1. The most direct evidence (promotion, measurable KPI improvement, scale numbers)
2. Evidence beyond the primary organisation (community workshops, products, knowledge sharing)
3. A single sentence that closes the loop: "The impact is not theoretical. It is live, applied, and growing."

### Section 3: Sustainable Change (typically 200 words)

Focus on systems, not one-off wins:
1. Internal systems: frameworks, tools, processes that outlast the nominee's direct involvement
2. External systems: workshops, products, documented knowledge that scales beyond the nominee
3. A closing sentence that names the pattern: "The nominee does not just achieve outcomes. They build the scaffolding so the outcomes outlast them."

## The personal disclosure decision framework

When a user asks whether to include a personal disclosure (disability, hardship, disadvantage) in a nomination:

**If the user asks once and accepts the recommendation:** The question was tactical. Answer it and move on.

**If the user asks twice or hesitates after an initial recommendation:** The hesitation is itself the answer. Recommend removal. A disclosure the nominee is not fully comfortable with will leak uncertainty into the application. Panels can sense instrumental disclosure. Let the body of work stand on its own.

**If the disclosure is integral to the story and the user is confident:** Include it once, early, as context — never as a plea. Two sentences maximum. Frame it as a strength, not a liability.

## The endorsement barrier

Most university awards require endorsement from a Dean of School or Director. This is often the hardest logistical step. Identify the barrier early:

- Does the nominee have a relationship with any academic staff who can endorse?
- If not, the month before the deadline should include deliberate outreach to unit coordinators
- The endorsement is not a formality — it is a gate. Plan for it.

## Quality gates

Before finalising:
1. Every subject claim has a specific professional action and outcome attached
2. Numbers are consistent across all sections (market count, team size, dates)
3. University values (Integrity, Respect, Rational Inquiry, Personal Excellence, Courage) are reflected in the narrative
4. No empty claims ("I applied this at work" without specifics)
5. The endorsement pathway is identified
6. Award-specific word counts are respected
7. No personal disclosures the nominee is uncertain about

## Reference files

- `references/ecu-vc-awards.md` — ECU Vice-Chancellor's Student Awards: six categories, word counts, submission process, and nomination form structure.
