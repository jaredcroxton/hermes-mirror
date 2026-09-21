---
name: academic-reference-verification
description: "Use when sourcing and verifying peer-reviewed academic references for postgraduate assignments. Covers search strategy, DOI verification, APA 7 element-by-element checking, claims verification against source text, and rubric cross-checking of assignment submissions. Triggered by requests for 'find me a reference', 'verify this citation', 'does this paper support my claim', 'check my reference list', or any assignment submission review."
---

# Academic Reference Verification

## When to Use

Load this skill whenever the user asks you to:
- Find peer-reviewed references for an assignment claim
- Verify that a specific reference's citation details are correct
- Confirm whether a paper genuinely supports a stated claim
- Cross-check an assignment slide deck or document against a rubric
- Review a reference list for APA 7 compliance

## Core Principles

1. **Accuracy is non-negotiable.** Every citation detail must come from the actual article, not from memory or a citation generator. If you cannot verify a detail, say so explicitly.
2. **Verify from the source, not aggregators.** DOI landing pages and PubMed indexed records are your primary verification surfaces. Google Scholar, Semantic Scholar, and ResearchGate are discovery aids only.
3. **Quote, do not paraphrase, when verifying claims.** Extract the exact sentence from the abstract or results section that supports or contradicts the user's claim.
4. **Flag errors transparently.** If any element does not match the source, state the mismatch and the correct value. Never silently fix a user's error.

---

## Phase 1: Reference Sourcing

### Search Strategy

Search across multiple databases. Try combinations of:

- PubMed: `"blue light" melatonin suppression`, `light-emitting screen melatonin`, `evening light exposure sleep onset`
- Google Scholar: broader discovery, check citation counts as a quality signal
- PsycINFO / Scopus: via ECU library if accessible

**Priority order for results:**
1. Primary empirical studies on human participants (not reviews, not animal studies)
2. High-quality systematic reviews or meta-analyses (acceptable as secondary option)
3. Published 2010 or later in reputable journals (Journal of Sleep Research, Sleep, Chronobiology International, PNAS, JCEM, Journal of Applied Physiology, etc.)

**Avoid:** predatory journals, non-indexed journals, popular science, blogs, conference abstracts without full text.

### Candidate Shortlisting

Before presenting candidates, verify each one by extracting from at least two independent sources:
- The DOI landing page (primary)
- PubMed indexed record (secondary cross-check)

Extract: authors, year, title, journal, volume, issue, pages, DOI.

---

## Phase 2: Element-by-Element Verification

When the user provides a reference to verify, open BOTH the DOI and PubMed record. Check each element separately:

| Element | Check |
|---|---|
| Author names and order | Match against DOI landing page author list |
| Publication year | Match against journal metadata |
| Article title | Word-for-word match, including capitalisation |
| Journal name | Full title (not abbreviated form) for APA 7 |
| Volume, issue | Match journal metadata |
| Page range | Match journal metadata |
| DOI resolution | Confirm DOI resolves to the exact article |

**Output format:** A single table with each element marked CONFIRMED or MISMATCH, with the correct value if mismatched. End with: "All elements verified, safe to cite" or "Discrepancies found, see flags above."

---

## Phase 3: Claims Verification

The user will state what they plan to cite the paper for. Extract the exact sentences from the abstract and/or results section that support or contradict each claim.

**If the paper supports the claim:** Quote the relevant passage and mark CONFIRMED.

**If the paper only partially supports the claim:** State exactly what is and is not supported.

**If the paper does not support the claim:** Quote what the paper actually found and mark MISMATCH.

---

## Phase 4: APA 7 Formatting Check

Check the reference against APA 7th edition rules:

- Ampersand (&) before the final author
- Year in parentheses, followed by a period
- Article title in sentence case (only first word, proper nouns, and first word after colon capitalised)
- Journal name in title case and italicised
- Volume italicised, issue number in parentheses NOT italicised
- Page range with en dash
- DOI as a full `https://doi.org/...` link, no trailing period

---

## Phase 5: Assignment Rubric Cross-Check

When the user provides an assignment submission (slide deck, document) and a rubric:

### Extract Content

For PowerPoint (.pptx):
```bash
python3 -m pip install python-pptx  # if not installed
python3 << 'PYEOF'
from pptx import Presentation
prs = Presentation("/path/to/deck.pptx")
for i, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(shape.text_frame.text.strip())
        if shape.has_table:
            # extract table rows
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text.strip())
PYEOF
```

**Note:** Use `terminal` with `python3 << 'PYEOF'` heredoc, not `execute_code`. The execute_code sandbox runs in a separate Python environment that lacks user-installed packages.

For Word documents (.docx): `read_file` handles these natively.

For PDF documents: `read_file` handles text extraction. For image-heavy PDFs (like sleep trackers), use `pymupdf` via terminal.

### Map to Rubric

For each rubric criterion:
1. Identify which slide(s) and narration address it
2. Compare content against HD descriptor
3. Flag any gaps between current content and HD requirements
4. Identify missing elements (e.g., empty citation slots, missing references, missing data)

### Output Format

A table with: Criterion, Weight, Current Score Estimate, Status, and specific gap descriptions.

End with a ranked list of concrete actions to close gaps, ordered by impact on overall grade.

---

## Pitfalls

- **Do not trust Google Scholar citation data.** Author names, page numbers, and even journal names are frequently wrong in Scholar metadata. Always verify against the DOI landing page.
- **Do not use `execute_code` for PPTX extraction.** The sandbox lacks `python-pptx`. Use `terminal` with a Python heredoc instead.
- **Do not fabricate page numbers.** If the DOI landing page does not show page numbers, search PubMed or the journal's own citation export. Never guess.
- **Do not assume a paper supports a claim because its title sounds relevant.** Always verify against the abstract and results text from the source.
- **Narrative citations in scripts.** When the user's narration script uses `[cite]` markers, those are spoken in-text citations — they need real author/year values, and the corresponding full reference must appear on the reference slide.

---

## References

- `references/chang-2015-verification.md` — Worked example: full verification of Chang et al. (2015) including element-by-element check, claims verification, and APA 7 formatting confirmation.
