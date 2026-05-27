---
name: pdf-report-generation
description: Generate beautiful, visual, color-coded PDF reports with reportlab — callout boxes, risk registers, option tables, section cards, and branded headers/footers.
---

# PDF Report Generation

Generate professional, visually rich PDF reports using reportlab. Use this when the user asks for a PDF that is "easy to read," "visual," "beautiful," or for any structured analysis output (legal, risk, strategy, options evaluation) that deserves a polished document.

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

Use the template at `references/reportlab-template.py` as your starting point — load it with `skill_view(name='pdf-report-generation', file_path='references/reportlab-template.py')`. Copy it to `/tmp/build_pdf.py` and insert your content. The template includes all reusable components:

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

```
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

## Pitfalls

- **execute_code sandbox lacks pip packages.** Always terminal-run the Python script. Write to a file first.
- **reportlab needs Helvetica.** macOS has it. If fonts are missing, fall back to 'Times-Roman'.
- **ROUNDEDCORNERS** in TableStyle works inconsistently across reportlab versions. It's a visual nicety, not structural — if it causes errors, remove it.
- **Long paragraphs in narrow table cells** can overflow. Keep risk descriptions to 2-3 lines max in card layouts.
