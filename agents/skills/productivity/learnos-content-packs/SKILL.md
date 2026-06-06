---
name: learnos-content-packs
description: Use when building LearnOS-ready learner packs, manager packs, training-module PDFs, and importable training content from Markdown or spreadsheet sources.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [learnos, training, pdf, learner-pack, manager-pack, markdown]
    related_skills: [pdf-report-generation, training-content-simplification]
---

# LearnOS Content Packs

## Overview

This umbrella covers LearnOS-ready training deliverables: learner packs, manager packs, module PDFs, and importable Markdown/source structures. It absorbs the narrower PDF-builder skills into one class-level workflow.

## When to Use

- Build a Learner Pack and Manager Pack for any programme.
- Convert Markdown, XLSX, or course notes into LearnOS-importable PDFs.
- Produce module-based training content with coloured callout boxes such as SHOW, REFLECT, QUIZ, ROLEPLAY, and KEY TAKEAWAYS.

## Source structure

Use a programme-level Markdown source with a predictable hierarchy:

```markdown
# Programme Title
## Importer instructions
# Module 1: Verb + Topic
## Section 1.1: Short title
## Section 1.2: Short title
## Section 1.3: Roleplay / practice / close
# Closing
```

Keep module counts variable; do not hard-code a fixed number of modules unless the user supplies one.

## Build workflow

1. Normalize source content into the Markdown structure.
2. Generate learner and manager variants from the same source of truth.
3. Render PDFs with consistent callout styling and page-safe spacing.
4. Validate that both PDFs open and contain the expected module/section count.
5. Return the PDF artifacts, not just the source files.

## Common Pitfalls

1. **One-off programme assumptions.** The builder must work for any programme, not only the session that created it.
2. **ReportLab layout overflow.** Long tables/callouts need page-break handling and conservative spacing.
3. **Manager pack drift.** Manager content should derive from the learner pack plus facilitation notes, not become a separate untracked source.

## Verification Checklist

- [ ] Source Markdown has the expected programme/module/section hierarchy.
- [ ] Learner and manager PDFs were generated.
- [ ] PDFs open successfully and page counts look plausible.
- [ ] Any spreadsheet/import notes were saved under references when relevant.
