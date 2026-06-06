---
name: learnos-pdf-builder
description: Build LearnOS-ready Learner Pack and Manager Pack PDFs from Markdown source files. Works for ANY programme. Triggered when building training content for LearnOS upload, generating learner/manager packs, or converting xlsx/course content into LearnOS-importable PDFs.
category: productivity
---

# LearnOS PDF Builder

Generate two separate PDFs from Markdown source files for LearnOS course upload. Works for **any programme**.

## Source Files (per programme)

Place in the working directory:

- `[programme]-learner-source.md` — learner-facing content (uploaded to LearnOS)
- `[programme]-manager-source.md` — manager/facilitator companion (NOT uploaded)
- `config.yaml` — optional: colours, page layout, role-to-colour mapping

## Build Script

Generic, reusable build script: `~/Desktop/build_learnos_packs.py`

Run:
```bash
python3 ~/Desktop/build_learnos_packs.py /path/to/folder
```

Or with no args, uses `~/Desktop`.

Outputs:
- `Learner.pdf` — upload to LearnOS
- `Manager.pdf` — distribute to facilitators

## Critical Rules

- **Never merge the two packs.** Separate documents for separate audiences.
- **Learner Pack** = self-paced online content (upload to LearnOS)
- **Manager Pack** = facilitator/manager coaching companion (distributed separately)
- **Reportlab `Table([[flowable_list]])` bug.** Never pass a Python list as a single Table cell. Each cell must contain a single flowable, or use a nested `Table(rows)` with one flowable per row.
- **The `bg()` function returns a tuple `(bg_color, accent_color)`.** When unpacking, use `bg_c, ac = bg("Show")`, NOT `bg_c, ac = bg(...) if ... else ..., color` (operator precedence trap).
- **Run scripts via terminal(), not execute_code.** The sandbox lacks reportlab.

## Markdown Structure (Learner Pack)

```
# Programme Title
[Audience, Format, Duration, Source]
[Description paragraph]
---
## Importer instructions
[Verbatim importer instructions block]
---
# Module N: [Verb + Topic]
Summary: [One sentence]
Learning objective: [By the end of this module you can ...]
## Section N.1: [Title, <=8 words]
Duration: N minutes (concept 3, reflect 1, quiz 1)
[Concept paragraphs — 2-3 short paragraphs]
> "[Canonical quote, verbatim.]" (Attribution)
### Show
[Worked example scenario — self-contained]
**Show:** [Alternative: inline label if not using ### heading]
### Key Takeaways
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]
**Reflect:** [One question]
**Check question:**
[Question stem on NEXT line, not inline]
- A) [Distractor]
- B) [Distractor]
- C) [Correct answer]
- D) [Distractor]
**Correct answer:** X
Explanation: [1-2 sentences]
## Section N.3: [Final section — add roleplay]
[Same pattern as above, plus:]
**Roleplay scenario:** [Situation for solo learner]
**Persona:** [Who the learner plays]
**Goal:** [Observable success criteria]
# Closing
[Optional 2-3 sentences]
```

**Note:** `**Check question:**` has the question stem on the following line, not on the same line. The parser looks ahead past blank lines for the next `p` event.

## Reportlab Gotchas

### QuizCallout Flowable (REQUIRED for quiz blocks)

Quiz options (`A)`, `B)`, `C)`, `D)`) inside a Table cell trigger ReportLab's auto-bullet detector, which replaces `A)`, `B)`, `C)`, `D)` with `\x7f` (ASCII 127). Both pypdf and pdfplumber flatten Table cell content, so all four options appear on one line separated by `\x7f`.

**Fix: Use a custom `QuizCallout(Flowable)` that draws directly on the canvas, not inside any Table.**

Required import:
```python
from reportlab.platypus import Flowable
```

Full working implementation:
```python
_QUIZ_LBL_STYLE = ParagraphStyle("_ql", fontName="Helvetica-Bold",
    fontSize=9, leading=12, textColor=colors.HexColor("#0B1E3D"))

class QuizCallout(Flowable):
    def __init__(self, label, question, options, correct, explanation,
                 accent, bg, body_style, padding=10):
        Flowable.__init__(self)
        self.label = label
        self.question = question
        self.options = options       # list of strings: ["A) ...", "B) ...", ...]
        self.correct = correct
        self.explanation = explanation
        self.accent = accent
        self.bg = bg
        self.body_style = body_style
        self.padding = padding
        self._w = 0
        self._h = 0

    def wrap(self, availWidth, availHeight):
        pad = self.padding
        inner_w = availWidth - pad * 2
        h = pad
        lp = Paragraph(self.label.upper(), _QUIZ_LBL_STYLE)
        _, lh = lp.wrap(inner_w, availHeight)
        h += lh + 3
        qp = Paragraph(self.question, self.body_style)
        _, qh = qp.wrap(inner_w, availHeight)
        h += qh + 4
        for opt in self.options:
            op = Paragraph(opt.replace("\x7f", "").strip(), self.body_style)
            _, oh = op.wrap(inner_w, availHeight)
            h += oh + 2
        if self.correct:
            cp = Paragraph(
                f'<font color="#1F8A70"><b>Correct answer: {self.correct}</b></font>',
                self.body_style)
            _, ch = cp.wrap(inner_w, availHeight)
            h += ch + 2
        if self.explanation:
            ep = Paragraph(f"<b>Explanation.</b> {self.explanation}", self.body_style)
            _, eh = ep.wrap(inner_w, availHeight)
            h += eh
        h += pad
        self._w = availWidth
        self._h = h
        return self._w, self._h

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.rect(0, 0, self._w, self._h, stroke=0, fill=1)
        c.setStrokeColor(self.accent)
        c.setLineWidth(3)
        c.line(0, 0, 0, self._h)
        pad = self.padding
        y = self._h - pad
        inner_w = self._w - pad * 2
        lp = Paragraph(self.label.upper(), _QUIZ_LBL_STYLE)
        _, lh = lp.wrap(inner_w, y)
        y -= lh
        lp.drawOn(c, pad, y)
        y -= 3
        qp = Paragraph(self.question, self.body_style)
        _, qh = qp.wrap(inner_w, y)
        y -= qh
        qp.drawOn(c, pad, y)
        y -= 4
        for opt in self.options:
            op = Paragraph(opt.replace("\x7f", "").strip(), self.body_style)
            _, oh = op.wrap(inner_w, y)
            y -= oh
            op.drawOn(c, pad, y)
            y -= 2
        if self.correct:
            cp = Paragraph(
                f'<font color="#1F8A70"><b>Correct answer: {self.correct}</b></font>',
                self.body_style)
            _, ch = cp.wrap(inner_w, y)
            y -= ch
            cp.drawOn(c, pad, y)
            y -= 2
        if self.explanation:
            ep = Paragraph(f"<b>Explanation.</b> {self.explanation}", self.body_style)
            _, eh = ep.wrap(inner_w, y)
            y -= eh
            ep.drawOn(c, pad, y)
```

### Check question multi-line parsing

`**Check question:**` in the MD source has the question text on the NEXT line, not inline. The `_LABEL_RE` regex only captures same-line text. The parser must look ahead:

```python
question = inline(rest) if rest else ""
j = i + 1
while j < len(events) and events[j][0] == "blank":
    j += 1
if not question and j < len(events) and events[j][0] == "p":
    question = inline(events[j][1])
    j += 1
# Then continue looking for bullets at position j
```

### Nested Table Cell Content
```python
# WRONG — passing a list as cell content
inner = [Paragraph("label"), Paragraph("body")]
tbl = Table([[inner]])  # CRASH

# RIGHT — nested Table with one flowable per row
nested = Table([[label_p], [body_p]], colWidths=[None])
outer = Table([[nested]], colWidths=[None])
```

### bg() Tuple Unpacking
```python
# WRONG — operator precedence trap
bg_c, ac = bg(mapped) if mapped in ["Show", "Reflect"] else hex_(cfg, "key_bg"), C("mute")

# RIGHT — explicit if/else
if mapped in ["Show", "Reflect"]:
    bg_c, ac = bg(mapped)
else:
    bg_c, ac = hex_(cfg, "key_bg"), C("mute")
```

### <bullet> Tag
Reportlab's Paragraph parser does NOT support `<bullet>` inside `<para>`. Use unicode `•` character instead.

### ListFlowable
`ListFlowable` with `bulletType="bullet"` extracts as literal `"bullet"` string in pypdf. Use inline `•` in Paragraph text instead.

## Extraction Verification

After every build change, verify quiz output with pypdf:
```python
from pypdf import PdfReader
reader = PdfReader("Learner.pdf")
for page in reader.pages:
    text = page.extract_text()
    if text and "QUIZ" in text:
        print(text)
```

Each option (A, B, C, D) must be on its own line. No `\x7f` characters. "Correct answer:" and "Explanation:" on their own lines.

## LearnOS Import Pipeline

The LearnOS academy extracts PDF text via `pdf-parse`, then sends it to OpenAI gpt-4.1 with a structured JSON schema. The LLM creates all modules, sections, quizzes, and roleplays.

Key implication: write RICH NARRATIVE TEXT with clear structural cues. Page breaks do not matter to the LLM.

Full pipeline details: see `learnos-training-pdf` skill references.

## 12-Point Validation Checklist

Before outputting the MD file, verify:
1. Every module title starts with a verb
2. Every section title <= 8 words
3. Duration line under every section heading
4. Every section has: concept, Show, Key Takeaways, Reflect, Check question, Correct answer, Explanation
5. Canonical quotes in `> "..." (Attribution)` blockquote form (never inline)
6. Zero em dashes (U+2014) anywhere
7. Exactly 4 quiz options (A/B/C/D), one `**Correct answer:** X` line, NO inline (correct) markers
8. One roleplay block per module (on final section), with scenario/persona/goal on consecutive lines
9. Zero facilitator/partner/room/manager/evaluation/source references in learner content
10. Every reflection prompt and scenario works for a solo learner on a screen
11. Importer Instructions block present between first `---` separators
12. Total length under 80,000 characters

## config.yaml Reference

```yaml
colours:
  navy:   "#0B1E3D"
  gold:   "#D4A437"
  teal:   "#1F8A70"
  blue:   "#2C4A7C"
  ink:    "#1F2937"
  mute:   "#6B7280"
  show_bg:    "#EAF2FB"
  reflect_bg: "#FEF6E2"
  role_bg:    "#F0E8FB"
  check_bg:   "#E8F5EC"
  key_bg:     "#F5F6F8"
  quote_bg:   "#FAF6EC"

accents_per_module:
  - "#2C4A7C"
  - "#D4A437"
  - "#1F8A70"
  - "#D4A437"
  - "#2C4A7C"

page:
  left_margin_mm: 22
  right_margin_mm: 22
  top_margin_mm: 28
  bottom_margin_mm: 22
  header_height_mm: 16
  bar_height_mm: 20
  tile_width_mm: 24

role_map:
  Show:          {bg_key: show_bg,    accent_key: blue}
  Reflect:       {bg_key: reflect_bg, accent_key: gold}
  Roleplay:      {bg_key: role_bg,    accent_key: "#6B46C1"}
  Check:         {bg_key: check_bg,   accent_key: teal}
  Key Takeaways: {bg_key: key_bg,     accent_key: mute}
```

## Multi-Programme Build Gotcha

When multiple `*-learner-source.md` and `*-manager-source.md` files exist in the same folder, the `_find()` function returns the first glob match — which may not be the one you want. Glob order is filesystem-dependent and non-deterministic across OS versions.

**Fix:** Before building, move other programme source files out of the folder temporarily:
```bash
mkdir -p ~/Desktop/stoic-archive
mv ~/Desktop/stoic-*-source.md ~/Desktop/stoic-archive/
python3 ~/Desktop/build_learnos_packs.py ~/Desktop
```

Or build from a dedicated subfolder:
```bash
mkdir -p ~/Desktop/primer-question-build
cp ~/Desktop/primer-question-*-source.md ~/Desktop/primer-question-build/
python3 ~/Desktop/build_learnos_packs.py ~/Desktop/primer-question-build
```

## Related Skills

- `learnos-training-pdf` — Sister skill with deeper technical notes, import pipeline docs, and the full programme build workflow including Excel spreadsheet output. These two skills overlap significantly; consider consolidating into one skill.
- `pdf-report-generation` — General reportlab PDF patterns (callout boxes, headers, tables).

## Excel Spreadsheet (Required Deliverable)

Every programme build requires an Excel file (`<topic>-session.xlsx`) as the business-facing source of truth. This is NOT optional. Jared will ask for it specifically.

Required sheets: Programme Overview, Module Detail (one per module), Assessment and Kirkpatrick, Manager Coaching Guide.

See `learnos-training-pdf` skill reference `references/excel-spreadsheet-template.md` for full structure and styling conventions.

**openpyxl gotcha:** Sheet titles cannot contain colons. Use hyphens instead.