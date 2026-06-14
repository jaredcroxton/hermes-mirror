---
name: pdf-report-generation
description: Generate beautiful, visual, color-coded PDF reports with reportlab — callout boxes, risk registers, option tables, section cards, and branded headers/footers.
---

# PDF Report Generation

Generate professional, visually rich PDF reports using reportlab. Use when the user asks for a PDF that is "easy to read," "visual," "beautiful," or for any structured analysis output (legal, risk, strategy, options evaluation) that deserves a polished document.

## Trigger

- User asks for a PDF, especially with visual/design expectations
- User asks to turn an analysis, strategy memo, or risk register into a document
- User says "make it visual," "easy to read," "colour-coded," "professional"

## Architecture

### Step 1: Install reportlab if needed

```bash
pip3 install reportlab
```

### Step 2: Build the PDF script

Use the template at `references/reportlab-template.py` as your starting point — load it with `skill_view(name='pdf-report-generation', file_path='references/reportlab-template.py')`. Copy to `/tmp/build_pdf.py` and insert your content. The template includes all reusable components:

- **callout_box(text, bg, icon)** — coloured alert/callout boxes with icon and background
- **risk_card(num, risk, materiality, color)** — risk register rows with colour-coded materiality dots
- **section_card(title, lines, color)** — white content cards with accent-colour top border
- **option_row(letter, label, signal, risk, bg)** — decision-option comparison rows
- **simple_table(headers, rows, col_widths)** — dark-header tables for controls, evidence, and ownership registers
- **on_page(canvas, doc)** — branded header bar (dark #1a1a2e rect) and footer with page numbers
- **spacer(h)**, **hr()** — spacing and horizontal rules
- **style_quote** — indented, italic, light-grey-background block for quoted approved wording
- **style_bullet** — indented bullet style for lists inside reports

### Step 3: Run via terminal, NOT execute_code

```bash
python3 /tmp/build_pdf.py
```

**Critical pitfall:** The `execute_code` sandbox does NOT have reportlab or other pip-installed libraries. Always write the script to a file and run it with `terminal`, not `execute_code`. The first run will fail silently with `ModuleNotFoundError` if you use execute_code.

### Step 4: Deliver

Use `MEDIA:<path>` to deliver the PDF file directly to the user.

## Design conventions

- **Header bar:** Dark background (#1a1a2e), white text, full-width rect at top of page
- **Footer:** Muted grey, centred page number, date, preparer
- **Colour palette:** Dark #1a1a2e, Accent #0f3460, Gold #e2b04a, Red #c0392b, Orange #e67e22, Yellow #f1c40f, Green #27ae60, Muted #6c757d
- **Callout backgrounds by purpose:**
  - Warning/Disclaimer: bg #fff3cd, border #ffc107, icon ⚠
  - Recommendation/Approval: bg #d4edda, border #28a745, icon ✓
  - Info/Context: bg #e8f4fd, border #b8daff, icon ℹ or 📊
  - Danger/Prohibition: bg #f8d7da, border #dc3545, icon ⚠ or 🚫
- **Quote blocks:** Use `style_quote` (indented, italic, #495057 text on #f8f9fa background) for approved wording, scripted responses, or legal text that must appear verbatim.
- **Dark-header tables:** Use `simple_table()` for controls registers, evidence checklists, ownership matrices. Dark background header (#1a1a2e), white text, alternating white rows.
- **Risk criticality:** Critical=Red, High=Orange, Medium=Yellow, Low-Medium=Green, Low=Muted
- **Font:** Helvetica throughout. Bold for headings and key terms.

## Output structures

### Analysis PDF (legal, strategy, options evaluation)

Standard eight-section flow:
1. Summary (2-3 key lines)
2. Recommendation (the core position)
3. Options/Decision Required (if multiple paths — use option_row())
4. Legal Reasoning / Why (the depth)
5. Risk Register (ordered critical to minor, colour-coded — use risk_card())
6. Quick Reference (safe vs prohibited, dos vs don'ts — use section_card())
7. Confidence Assessment
8. Next Steps (actionable, numbered)

### Platform architecture + training pathway PDFs

When Jared is still working through a product architecture concept, prioritise clarity over pricing. If he asks for both a separate training/pathway document and a combined proposal, produce two PDFs plus editable markdown sources:

1. **Pathway-only PDF** — focused on modules, outcomes, practical activities, deliverables, and training website structure.
2. **Combined platform proposal PDF** — includes platform distinction, one-soul/two-runtime model, agent flow, reporting line, audit model, training pathway summary, roadmap, risks, and recommendation.

Keep pricing out unless Jared explicitly asks for commercial terms. This is especially important for Crew vs AgentOS concept documents where he is still shaping the product rather than selling it.

### Training Module PDF (LearnOS upload) — UPDATED WORKFLOW

**Current workflow (post-28 May 2026): Markdown-source pipeline.**

1. **Source**: Markdown file (e.g. `stoic-learner-source.md`) is the single source of truth for content
2. **Build script**: `build_stoic_packs.py` reads MD, renders both PDFs via reportlab
3. **Output**: `LearnOS-Stoic-Learner.pdf` (upload to LearnOS) + `LearnOS-Stoic-Manager.pdf` (facilitator companion)
4. **Validation**: 12-point checklist run against MD before rendering

The old xlsx-based pipeline (`build_learner_pack.py` / `build_manager_manager_pack.py` reading from spreadsheet) is deprecated. New work should use the MD-source pipeline.

**MD file structure** (per module):
```
# Module N: [Verb + Topic]
Summary: ...
Learning objective: ...
## Section N.N: [Title ≤8 words]
Duration: N minutes
[Concept paragraphs]
> "[Canonical quote]" (Attribution)
### Show
[Worked example]
### Key Takeaways
- [Bullet]
**Reflect:** [Prompt]
**Check question:**
[Question]
- A) ... B) ... C) ... D) ...
**Correct answer:** C
Explanation: ...
**Roleplay scenario:** ...  (final section only)
**Persona:** ...
**Goal:** ...
```

See `stoic-mindset-pdf-builder` skill for full details, validation checklist, and the Hermes LearnOS prompt.

**Trigger signals:**
- Jared mentions LearnOS, online module, course upload, or training PDF
- Jared provides expert/academic content that needs simplifying for a sales team
- Jared says "turn this into an online module" or "make this LearnOS-ready"

**Two-pack output (always produce both):**

1. **Learner Pack** (`<Topic>-Learner-Pack.pdf`): Uploaded to LearnOS. Tell-Show-Do-Check format with learning objectives, SHOW examples, KEY POINTS, REFLECT prompts, QUIZ blocks (question + 4 options + correct marker + explanation), ROLEPLAY blocks (scenario/persona/goal), and a gold closing banner.

2. **Manager Pack** (`<Topic>-Manager-Pack.pdf`): NOT uploaded to LearnOS. Used by managers/facilitators. Contains coaching questions, modelling tips, facilitator notes, live activity options, and evaluation L1-L4 per module, plus an aggregated sources page.

3. **Simplified Excel** (`<topic>-session-simple.xlsx`): The editable source document. Jared presents this to the business. All content changes happen here, then both PDFs are regenerated.

**Regeneration workflow:** Edit Excel → run both build scripts → deliver both PDFs + updated Excel.

**Source of truth hierarchy:** The markdown source files (e.g. `stoic-learner-source.md`) are the PRIMARY source of truth for PDF content. The Excel spreadsheet is a secondary document Jared presents to the business. The build script (`build_stoic_packs.py`) reads from the markdown, NOT the Excel. Keeping the Excel simplified in parallel is a reporting concern, not a content-authoring concern.

**Standard Learner Pack structure (per the reference pack at performos):**

The reference Learner Pack format (extracted from the performos codebase) uses this exact structure:
- Cover page with title, audience, duration, format, importer instructions
- Per module: `# Module N: Verb + Topic` → Summary → Learning Objective → Sections with `## Section N.X: Short Title (≤8 words)` → Duration line → Narrative paragraphs (Tell) → Blockquote for canonical quotes → `### Show` → **Key points:** bullets → **Reflect:** prompt → **Check question:** MCQ → **Correct answer:** → Explanation: → **Roleplay scenario:** / **Persona:** / **Goal:** → Closing quote

**Importer instructions header (critical — include at top of every Learner Pack MD file):**
```
## Importer instructions

Do not summarise. Preserve narrative paragraphs in full. Direct quotes appearing in blockquote form
must land verbatim in the output: do not paraphrase, do not shorten, do not strip the attribution.

Do not use em dashes in any rendered learner-facing text. Use periods, commas, parentheses, or rewrite.

Each section has a `Duration:` line giving target estimated minutes. Honour the value, do not multiply or guess.

`### Show:` blocks must render as a distinct scenario block separated from the preceding concept paragraphs.
```

**Why this format matters:** The LearnOS importer (`src/app/api/import-content/route.ts`) uses `pdf-parse` to extract text, then sends it to OpenAI gpt-4.1 with a structured JSON schema. The LLM does ALL the structuring — it decides sections, quiz questions, roleplays. The importer instructions and structural cues in the MD file directly control what the LLM produces. Verbatim quotes, correct durations, and distinct SHOW blocks all survive the import.

**JSON schema the importer enforces:**
```json
{
  "modules": [{
    "title": "string (verb + topic)",
    "summary": "string",
    "learningObjective": "By the end of this module, you will be able to...",
    "sections": [{
      "title": "string (≤8 words)",
      "content": "string (2-3 short paragraphs)",
      "keyPoints": ["string", "string", "string"],
      "reflection": "string or null",
      "quiz": {
        "question": "string",
        "difficulty": "recall | application | scenario",
        "options": [{"id": "opt-0", "text": "..."}, ...],
        "correctOptionId": "opt-N",
        "explanation": "string"
      },
      "roleplay": {
        "scenario": "string",
        "persona": "string",
        "goal": "string"
      }
    }]
  }]
}
```

**Reusable build scripts:**
- `scripts/build_stoic_packs.py` — Reads markdown source files and renders both PDFs. Copy to `/tmp/` and run via terminal.
- The build script uses a `StoicDoc` class (navy header bar, footer with page number), `parse_markdown()` for MD→events, and coloured callout boxes for Show/Reflect/Roleplay/Check/Key Points.
- Module banners use a two-column table: left = coloured accent tile with "M1"/"M2" etc, right = dark background with white title text.
- Functions MUST be defined BEFORE they are called in the script (Python ordering matters).

**Standard module-per-page flow (Manager Pack):**
1. Cover page (title, audience, purpose, how-to-use)
2. Module divider (same visual style as Learner Pack)
3. Manager Actions: intro + numbered coaching questions (hard-coded per module)
4. Modeling tip (green callout, hard-coded per module)
5. Facilitator Notes (italic grey blocks, hard-coded per module)
6. Live Activity Option (blue callout, hard-coded per module)
7. Evaluation L1-L4 (hard-coded per module)
8. Sources page at end (aggregated from column E of all 4 module rows)

**Plain English rule (critical):** Rewrite ALL expert/academic content into everyday language a day-three sales rep can use on a live call. Strip citations, neuroscience jargon, and academic framing. Replace with direct, conversational, actionable language. Use short sentences. Active voice. No references to "amygdala" or "prefrontal cortex" — explain the *effect* ("your brain goes into threat mode") not the *mechanism*.

### Governance Pack PDF (operational controls from legal anchor)

Standard governance pack flow:
1. Cover (title, subtitle, meta table, disclaimer callout)
2. Summary + Recommendation
3. Part 1: Safe Claims Sheet (approved wording in style_quote blocks)
4. Part 2: Prohibited Claims (section_card with RED for prohibitions)
5. Part 3: Deliverable Wording (certificate, email templates, social posts)
6. Part 4: Marketing Guardrails (visual hierarchy, disclaimer placement, pre-pub checklist)
7. Part 5: Buyer/Objection Guidance (scripted responses in style_quote)
8. Part 6: Evidence Checklist (numbered E1-E8 items)
9. Controls Register (simple_table with ID, Description, Trigger, Owner columns)
10. Risk Register (risk_card rows)
11. Escalations (callout_box with ↑ icon)
12. Next Step + Quick Reference Card (section_card: ✅ CAN / 🚫 CANNOT / 📋 CHECK)
13. Scorecard + File Manifest

## Reference files

- **`references/training-module-pdf-notes.md`** — Design decisions, colour scheme, layout specs, and the dual-output rule for LearnOS-ready training module PDFs. Read this when building a Training Module PDF.

## Pitfalls

- **Training modules need dual output.** When Jared asks for a training PDF for LearnOS, always ALSO deliver the Manager Pack. He needs both files.
- **Expert content must be rewritten, not just reformatted.** Do not keep academic citations, neuroscience terminology, or expert framing in the training content. Rewrite into plain English a new sales rep can follow.
- **execute_code sandbox lacks pip packages.** Always terminal-run the Python script. Write to a file first.
- **reportlab needs Helvetica.** macOS has it. If fonts are missing, fall back to 'Times-Roman'.
- **`<bullet>` tag in reportlab Paragraph** causes `ValueError: Parse error`. Always use unicode `•` character, never `<bullet>` XML tag. Additionally, `ListFlowable` with `bulletType="bullet"` extracts as the literal string `"bullet"` in pypdf/text extraction. Use inline `•` in Paragraph text instead.
- **Functions must be defined BEFORE use in Python scripts.** A `NameError` at runtime means a function is called before its `def` statement. Always put helper functions at the top of the script.
- **Spaced data tuples in TableStyle** — `('BACKGROUND', (0,0), (-1,-1), bg_color)` requires a single Color object. A tuple of two Colors (from a function returning `(bg, accent)`) will cause `AssertionError: Can only convert 3 and 4 sequences to color`. Fix: unpack the tuple first: `bg_c, ac = bg(mapped)`.
- **Show headings must include colon** — render as `"SHOW:"` or `"Show:"` not bare `"Show"`. The importer extracts the word without format cues; the colon is the signal.
- **Quiz callouts need a header label** — render `"QUIZ"` at the top of every quiz callout box. Without this the importer has no anchor.
- **Key Takeaways must be wrapped in a callout** heading + bullets together in a single callout box, not a bare H3 followed by a separate bullet list.
- **Blockquotes need a "Quote:" prefix** rendered as visible text inside the callout. The `>` character alone is stripped during text extraction.