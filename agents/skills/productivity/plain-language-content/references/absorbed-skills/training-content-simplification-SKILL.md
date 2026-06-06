---
name: training-content-simplification
description: Simplify expert-level or academic content into plain, direct language suitable for sales teams and frontline staff. Use when Jared forwards training material, workshop content, spreadsheet modules, academic references, or facilitator guides that are too technical, too jargon-heavy, or too theoretical for a day-three rep to use on a live call.
---

# Training Content Simplification

## When to use

Jared operates in L&D for a high-volume telesales environment. Subject matter experts, learning designers, or academic sources regularly produce content that is too dense for the end audience. This skill applies when:

- Jared forwards a training document, spreadsheet column, slide, or workbook and says it is too technical, too academic, or too wordy
- Expert citations and neuroscience terminology need to be translated into everyday language
- Facilitator talking points need to sound like a real person, not a textbook
- Content is for sales reps, team leaders, or frontline staff, not academics

## Core principle

The end reader is a sales rep who needs to use this on a call today. If they would not say it out loud to a colleague, it is too complex.

## The simplification process

1. **Read the source material.** Understand what each expert point is actually saying. Strip the citations, jargon, and qualifying language. Find the core insight.

2. **Rewrite in plain English.** Rules:
   - Conversational tone. Talk like a peer, not a professor.
   - Lead with the practical takeaway, then briefly explain why it works.
   - Replace technical terms with everyday ones: "amygdala activation" becomes "your brain goes into panic mode."
   - Short sentences. One idea per sentence.
   - Include concrete examples the audience recognises (angry customer, tough email, deal that fell over).
   - Keep action steps specific and physical: "take three slow breaths" not "activate the parasympathetic nervous system."
   - Never remove the meaning. Simplify the language, keep the substance.

3. **Preserve structure.** If the source has four bullet points, deliver four. Do not reorganise unless Jared asks.

4. **Save to spreadsheet.** When working with xlsx:
   - Create a new file (append `-simple` to filename) to preserve the original
   - Use `openpyxl` via Python to read/write `.xlsx` files
   - Verify the file opens correctly after saving

## LearnOS PDF generation

When Jared needs training content uploaded into LearnOS as an online module, the full workflow is documented in the `learnos-pdf-builder` skill. Key points:

1. **Simplify content** into plain English (see above)
2. **Write markdown source** (`[programme]-learner-source.md`) following the structure the LLM importer expects. See `learnos-pdf-builder` skill for the full template, checklist, and importer rules.
3. **Run the build script**: `python3 ~/Desktop/build_learnos_packs.py`
4. **Upload** `Learner.pdf` to LearnOS
5. **Distribute** `Manager.pdf` to facilitators

The MD file is the build source. The xlsx is Jared's business-facing reference document.

### Key rules (from learnos-pdf-builder)
- **Never merge the two packs.** Separate documents for separate audiences.
- **Module titles:** verb + topic format ("Filter What You Can Control")
- **Section titles:** ≤ 8 words
- **Canonical quotes:** always in `> "..." (Attribution)` blockquote form
- **Quiz format:** exactly 4 options (A/B/C/D), `**Correct answer:** X` line, NO inline markers
- **Roleplay:** only on final section of each module; scenario/persona/goal on consecutive lines
- **Zero em dashes** (U+2014) anywhere
- **Zero facilitator/partner/room/manager/evaluation/source references** in learner content
- **12-point validation checklist** before outputting MD

## What NOT to do

- Do not add new concepts. Simplify what is there.
- Do not over-simplify to the point of being wrong.
- Do not change the target audience.
- Do not hardcode content into the PDF build script. Always read from the source.

## Output benchmarks

A good simplification passes the "say it back" test: if a rep read it once and could explain it to a new starter in their own words, it is at the right level.

## Jared's format preferences (non-negotiable)

- Short, punchy sentences. Active voice.
- No em dashes. Ever.
- Spell out one to nine. Numerals for 10 and above.
- Dates in DD Month YYYY format.
- No warnings, disclaimers, or unnecessary extras.
- Include GROW coaching language where appropriate.
- Accor Plus context: dials, talk time, connects, presentations, sales. UAE, Philippines, Thailand, Vietnam markets. Chris Douglas and Jayne Brown are key stakeholders.
