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

## PerformOS-branded PDFs via HTML + headless Chrome

When the deliverable needs PerformOS brand typography (Instrument Serif / Inter / JetBrains Mono) or embedded screenshots, skip reportlab and render an HTML file to PDF with headless Chrome:

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="out.pdf" "file:///path/to/guide.html"
```

- Brand fonts are installed locally at `~/Library/Fonts/` (InstrumentSerif-Regular.ttf, InstrumentSerif-Italic.ttf, Inter.ttf variable, JetBrainsMono.ttf). Reference with `@font-face src: url('file:///Users/jc/Library/Fonts/<name>.ttf')`. Inter is a variable font, so `font-weight: 100 900` works.
- Brand tokens: Ivory `#f2efe8`, Ivory Soft `#e8e4da`, Ink `#0a0a0a`, Electric Lime `#d4ff3b`. Ink opacity scale (60/40/12/6%), never hard-coded greys. Headings Instrument Serif, body Inter, labels JetBrains Mono uppercase with 1.5-2px letter-spacing. Wordmark "Perform" roman + "OS" italic.
- Use `@page { size: A4; margin: 0; }` then each page as `<section class="page">` with `width:210mm; min-height:297mm; padding:20mm 18mm 22mm; page-break-after:always; overflow:hidden` and a per-page absolute footer. Add `print-color-adjust: exact` so backgrounds print.
- **Pitfall (spillover to blank pages):** `min-height:297mm` + `page-break-after:always` silently creates a near-empty page whenever a section's content exceeds one A4 (the last element spills onto the next page). Detect with `pdfinfo` (page count vs designed page count), then render `pdftoppm -png -r 80 out.pdf page` and vision-check the suspiciously small `.png` files (near-empty pages are ~7-15KB vs ~30-50KB for full pages). Fix by tightening vertical rhythm (lede/callout/code font sizes and paddings) or capping images (`.shot { max-height:60mm }`).
- Capture real screenshots with headless Chrome: `"$CHROME" --headless=new --disable-gpu --hide-scrollbars --screenshot=img/x.png --window-size=1280,900 "https://url"`. Never fake terminal output; render accurate command/output as styled dark mono blocks and caption them as examples.
- Verify before shipping: `pdfinfo` for page count, `pdftoppm` + vision for layout, and `grep -n "—" guide.html` plus a forbidden-word grep (platform, suite, all-in-one, revolutionary, game-changer, enterprise-grade, seamless, unlock, leverage) and "sarah" must all return empty.

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

### PerformOS Crew / white-label playbook PDFs

When Jared asks for a playbook PDF about PerformOS Crew, Claude Code workflow, or white-label AI work teams:

1. Update the source markdown first if the conversation corrected the operating model.
2. Use the white-label framing: Superpowers = standards layer, PerformOS Crew = role/workflow layer, Business Context Layer = the client-specific brand, workflows, risks, systems, access rules, approval rules, and commercial outcomes.
3. Do not describe Layer 3 as "PerformOS is the business layer" when the goal is white-label client installs. PerformOS Crew supplies the AI work team structure; the client business supplies the context and constraints.
4. Remove internal shorthand and identity leakage from client-facing playbooks. Do not include "Caveman mode", Jared-specific wording, internal agent names (Brock/Bob/Lara/Neo/etc.), PerformOS business-specific examples, or internal runtime details unless explicitly requested.
5. Use professional operating-mode names: Fast mode, Controlled mode, and Governed mode.
6. Use generic specialist-role examples: strategy lead, build lead, learning lead, compliance lead, operations lead, QA lead, release lead.
7. Render a polished PDF with a cover page, meta table, section headings, callout cards, and readable code blocks.
8. Deliver with `MEDIA:<absolute path>` and keep the markdown source as the source of truth in Obsidian.
9. Verify zero em dashes and zero client-facing internal leakage in the source before final response.

See `references/performos-crew-white-label-playbook.md` for the detailed white-label wording rules and verification checklist.

### Crew Skill Pack Catalogue PDF

When Jared asks to break the Crew system down one level further into individual skills:

1. Write the markdown source first. Structure it as a catalogue: one skill per section, each with a plain-English description of what it does, a simple workflow, an example use, and an example output.
2. Write for a business owner who has never used AI before. No technical language. No Claude Code or Hermes references. No internal agent names. Every skill should answer: "What does this actually do for my business?"
3. Use the same white-label rules as the playbook: zero em dashes, zero Jared references, zero caveman, zero internal runtime mentions. The name "PerformOS Crew" may appear but no other PerformOS business context.
4. Render as a reportlab PDF using `layer_box()` for the four-layer architecture diagram, `two_cards()` for skill pack overview cards, and dark-header tables for the skill catalogue rows.
5. The PDF should include a skill selection guide section so a business can identify which packs apply to them.

See `references/performos-crew-white-label-playbook.md` for the detailed white-label wording rules and verification checklist.

See `references/crew-catalogue-white-label-rules.md` for the critical distinction between installed flow skills and catalogue skills, the white-label language checklist, and the catalogue build pattern (build.py → index.html → headless Chrome PDF).

### RPL Statement PDF (academic submission)

When Jared asks for an ECU Recognition of Prior Learning statement:

1. Read the uploaded documents first: certificate, CV, cover letter, and original RPL form. Extract the unit codes, student details, and professional experience narrative.
2. Source the current unit outlines from ECU's handbook for the correct codes (note: codes change across years — the form may reference old codes; use the current codes in the statement and add a note explaining the code change).
3. Build the markdown source first. Address every learning outcome individually under its own numbered heading. Each outcome needs a substantial paragraph (200+ words) that maps specific professional experience to the outcome — describe HOW the experience demonstrates the outcome, not just WHAT was done.
4. Link professional experience to named frameworks (Kotter, ADKAR, GROW, etc.) where relevant, but keep the focus on applied practice, not theory recitation.
5. Include a verification section naming the verifier (employer who reviewed the statement), a note on unit code changes if applicable, and student details (name, number, course).
6. Render as a reportlab PDF with a clean academic cover page, dark header bars, callout boxes for verification notes, and clear learning outcome headings.
7. Verify: 0 em dashes, student number present, verifier named, all learning outcomes individually addressed, unit codes correct.

**Critical RPL pitfall:** Never use the course being applied for as evidence. If Jared is applying through his Master's programme, do not reference ECU study, MIT certificates taken during the programme, or grades from the current course as evidence. Ground every learning outcome in professional experience (Director of Operations and L&D, Accor Plus regional transformation, seven-market rollout, etc.). Academic evidence from the same degree path being assessed is circular — the assessor needs to see professional capability, not study already completed within the programme.

See `references/performos-crew-white-label-playbook.md` for the detailed white-label wording rules and verification checklist.

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
- **`references/performos-crew-white-label-playbook.md`** — White-label rules, verification checklist, catalogue update pattern, methodology slide template, canonical Crew architecture, and the "PDF first, website second" rule.
- **`references/ecu-rpl-statement-pattern.md`** — RPL statement formatting rules, document structure, critical "no current study as evidence" rule, and evidence sources for ECU Master's applications.

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
- **Callout icon column width must exceed padding sum. When building callout_box() or big_callout() tables with an icon column, the column width must be greater than leftPadding + rightPadding. Example: colWidths=[22, 442] with leftPadding=12, rightPadding=12 = 22 minus 24 = minus 2, causing ValueError: flowable given negative availWidth. Fix: ensure icon column width exceeds padding sum (use 30px minimum for 12px padding).
- **Blockquotes need a "Quote:" prefix** rendered as visible text inside the callout. The `>` character alone is stripped during text extraction.