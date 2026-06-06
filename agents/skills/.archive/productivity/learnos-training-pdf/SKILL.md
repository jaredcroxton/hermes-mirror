---
name: learnos-training-pdf
description: Build LearnOS-ready training module PDFs and Manager Pack companions from a markdown-source pipeline. Handles variable module counts, coloured callout boxes (SHOW, REFLECT, QUIZ, ROLEPLAY, KEY TAKEAWAYS), and exports two PDFs per programme.
---

# LearnOS Training PDF Builder

Build the two PDFs required for every LearnOS training programme: a Learner Pack (uploaded to LearnOS) and a Manager Pack (facilitator companion).

## Trigger

- Jared mentions LearnOS, online module, course upload, or training PDF
- Jared provides content that needs to become a structured online learning module
- Jared says "turn this into an online module" or "make this LearnOS-ready"

## Architecture

### Source files (per programme, all in one folder)

```
<topic>-learner-source.md    # PRIMARY content source
<topic>-manager-source.md    # Facilitator companion source
<topic>-session.xlsx         # Business-facing source of truth (REQUIRED)
config.yaml                  # Optional: colours, page layout, role-to-colour mapping
```

### Build workflow — complete sequence

Every training programme produces **four** deliverables in this order:

1. **Programme design document** (`<topic>-programme.md`) — Learning outcomes (Bloom's taxonomy), module structure, Tell-Show-Do-Check flows per section, Kirkpatrick evaluation plan, facilitation guide
2. **Learner source MD** (`<topic>-learner-source.md`) — Formatted for the build script with all importer optimisations
3. **Manager source MD** (`<topic>-manager-source.md`) — Facilitator companion with coaching notes, evaluation criteria, Kirkpatrick mapping
4. **Excel spreadsheet** (`<topic>-session.xlsx`) — Business-facing source of truth with 5 sheets: Programme Overview, Module 1 Detail, Module 2 Detail, Assessment and Kirkpatrick, Manager Coaching Guide

### Build command

```bash
python3 build_learnos_packs.py /path/to/folder
```

### Output

```
<slug>-Learner.pdf    # Upload to LearnOS
<slug>-Manager.pdf    # Distribute to facilitators
```

### Excel spreadsheet (required, not optional)

The Excel file is the business-facing source of truth that sits behind the programme. It must be included with every programme build. Jared will ask for it specifically ("where is the spreadsheet").

Required sheets:
1. **Programme Overview** — Programme name, product, audience, delivery method, duration, module summary table
2. **Module N Detail** — Section-level breakdown: section number, title, type, duration, key content summary, assessment approach
3. **Assessment and Kirkpatrick** — L1-L4 evaluation plan: what to measure, how, when, and target
4. **Manager Coaching Guide** — 4-week reinforcement cycle with weekly activities, durations, and success indicators. Include common failure modes and coaching cues.

Use `openpyxl` to generate. Save with the naming convention `<topic>-session.xlsx`.

**Sheet title restriction:** Excel sheet titles cannot contain colons (`:`). Use hyphens or en-dashes instead (e.g. "Module 1 - Prime Yourself" not "Module 1: Prime Yourself").

### Configurable elements (config.yaml)

YAML file with three top-level keys:

```yaml
colours:
  navy:   "#0B1E3D"
  gold:   "#D4A437"
  teal:   "#1F8A70"
  blue:   "#2C4A7C"
  ink:    "#1F2937"
  mute:   "#6B7280"
  rule:   "#E5E7EB"
  show_bg:    "#EAF2FB"
  reflect_bg: "#FEF6E2"
  role_bg:    "#F0E8FB"
  check_bg:   "#E8F5EC"
  key_bg:     "#F5F6F8"
  quote_bg:   "#FAF6EC"

accents_per_module: ["#2C4A7C", "#D4A437", "#1F8A70", "#D4A437", "#2C4A7C"]

page:
  left_margin_mm: 22
  right_margin_mm: 22
  top_margin_mm: 28
  bottom_margin_mm: 22
  header_height_mm: 16
  bar_height_mm: 20
  tile_width_mm: 24
```

## Learner Pack MD format

```
# [Programme Title]
[Audience, format, duration, source]
[Description paragraph]

---

## Importer instructions
Do not summarise. Preserve narrative paragraphs in full. Direct quotes in blockquote
form must land verbatim. Do not use em dashes. Each section has a Duration: line —
honour the value. Show: blocks must render as distinct blocks.

---

# Module 1: [Verb + Topic]
Summary: [One sentence]
Learning objective: [By the end of this module you can...]

## Section 1.1: [Title ≤8 words]
Duration: N minutes (concept N, reflect N, quiz N)
[Concept paragraphs]
> "[Canonical quote]" (Attribution)

### Show
[Self-contained worked example]

### Key Takeaways
- [Bullet 1 — full sentence]
- [Bullet 2]
- [Bullet 3]

**Reflect:** [Open-ended application prompt]

**Check question:**
[Question stem]

- A) [Distractor]
- B) [Distractor]
- C) [Correct answer]
- D) [Distractor]

**Correct answer:** C
Explanation: [1-2 sentences, teaches not just states]

## Section 1.2: [Title]
[Same pattern, no roleplay]

## Section 1.3: [Title]
Duration: 10 minutes (concept 3, reflect 1, quiz 1, roleplay 5)
[Same pattern, plus:]

**Roleplay scenario:** [3-4 sentences, solo learner can enter]
**Persona:** [Who the learner plays, who the AI plays]
**Goal:** [Observable outcome — "by the end the learner has..."]

---
# Module 2: [Verb + Topic]
[Same structure]

[Repeat for all modules — module count varies per programme]

# Closing
[2-3 sentence call to action]
```

**Module count is variable**: set by the number of `# Module N:` headings in the MD file.

## Manager Pack MD format

```
# [Programme]: Manager and Facilitator Pack
Companion to: [Learner Pack title]
Audience: Managers, facilitators, L&D leads

## How to use this pack
[3-5 bullets]

# Module 1 Companion: [Title]
## Manager actions
[Coaching questions, modelling tips]
## Facilitator notes for live delivery
- [Pre-reads, backup scenarios]
## Live activity option
[Activity description]
## Evaluation
- Level 2: [Observation/assessment, target]
- Level 3: [Behaviour follow-up, target]

[Repeat per module]

# Sources
[Bibliography in groups: primary texts, modern interpreters, neuroscience etc.]
```

## Rendering requirements (what the build script must produce)

All of these were reverse-engineered from the LearnOS importer pipeline (`src/app/api/import-content/route.ts`) and verified with pypdf text extraction:

1. **SHOW: heading** — Render `### Show` as a callout box with bold `"SHOW:"` label (with colon, uppercase). The colon is critical: pypdf extracts the bare word without format cues.

2. **QUIZ header** — Every quiz callout box must start with a `"QUIZ"` label inside the box. Without this, the importer has no anchor for quiz blocks.

3. **Quote: prefix** — Every blockquote callout must have `"Quote:"` rendered as a visible prefix inside the box. The `>` character alone is stripped during extraction.

4. **Inline bullets** — Use unicode `•` in Paragraph text, NEVER reportlab's `ListFlowable` with `bulletType="bullet"`. ListFlowable extracts as the literal string `"bullet"` in pypdf output.

5. **KEY TAKEAWAYS in callout** — `### Key Takeaways` headings must be wrapped in the grey callout box along with their bullets. Not a bare H3 followed by a separate bullet list.

6. **Zero em dashes** — The U+2014 character must not appear anywhere in the MD source.

7. **Two separate PDFs** — Never merge learner and manager content into one document.

## Importer instructions preamble (include verbatim in every learner MD file)

```
## Importer instructions

Do not summarise. Preserve narrative paragraphs in full. Direct quotes appearing in
blockquote form (`> "..." (Attribution)`) must land verbatim in the output: do not
paraphrase, do not shorten, do not strip the attribution.

Do not use em dashes in any rendered learner-facing text. Use periods, commas,
parentheses, or rewrite.

Each section has a `Duration:` line giving target estimated minutes. Honour the value.

`### Show:` blocks must render as a distinct scenario block separated from the
preceding concept paragraphs.
```

## LearnOS JSON schema the importer enforces

```json
{
  "modules": [{
    "title": "string (verb + topic, e.g. Filter What You Can Control)",
    "summary": "string",
    "learningObjective": "By the end of this module, you will be able to...",
    "sections": [{
      "title": "string (≤8 words)",
      "content": "string (2-3 short paragraphs Tell+Show)",
      "keyPoints": ["string x3-5 (standalone takeaway bullets)"],
      "reflection": "string (DO prompt) or null",
      "quiz": {
        "question": "string",
        "difficulty": "recall | application | scenario",
        "options": [{"id": "opt-0", "text": "..."}, ...4],
        "correctOptionId": "opt-N",
        "explanation": "string (teaches)"
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

## Content rules for training modules

1. **Plain English only** — Rewrite ALL expert/academic content into everyday language. Strip citations, neuroscience jargon, academic framing. Short sentences. Active voice.
2. **Solo learner voice** — Every prompt, scenario, and instruction must work without another human present. No "discuss with a partner" or "volunteer to the room."
3. **Self-check before output** — Run the 12-point checklist against the MD before rendering:
   - [ ] Every module title starts with a verb
   - [ ] Every section title ≤ 8 words
   - [ ] Every section has a Duration line
   - [ ] Every canonical quote is in blockquote form `> "..." (Attribution)`
   - [ ] Zero em dash characters (U+2014)
   - [ ] Every quiz has exactly 4 options + Correct answer + Explanation
   - [ ] Each module has exactly 1 roleplay on its final section
   - [ ] Zero facilitator or live-session references in learner content
   - [ ] All content works for a solo learner
   - [ ] SHOW: heading has colon
   - [ ] QUIZ label at top of every quiz block
   - [ ] Quote: prefix at top of every blockquote callout

## Pitfalls

- **delegate_task timeout on large programme builds** — When delegating a full programme build to a sub-agent (e.g. Lara_LearningDesign via delegate_task), the sub-agent may time out after 10 minutes on large programmes. The fix: build the MD source files and design doc directly in the orchestration layer, then run the build script yourself. Delegate only specific sub-tasks (e.g. "write Module 2 content for this programme") rather than the full programme build.

- **Multi-programme glob ordering** — When multiple `*-source.md` exist in the build folder, `_find()` returns the first glob match (filesystem order, non-deterministic). Move unwanted source files to an archive subfolder before running the build script.
- **`<bullet>` tag in reportlab Paragraph** causes `ValueError: Parse error`. Always use unicode `•` character, never `<bullet>` XML tag.
- **Functions must be defined BEFORE use** in Python scripts. Put helpers at the top.
- **ListFlowable with bulletType="bullet"** extracts as literal "bullet" string in pypdf. Use inline `•` in Paragraph text instead.
- **Em dashes in source** → the importer sometimes introduces them from source. Search-and-replace U+2014 to period or comma before rendering.
- **`<para>` and `<bullet>` are not valid reportlab XML tags** in Paragraph HTML. Only `<b>`, `<i>`, `<font>`, `<br/>`, `<bullet/>` (the self-closing tag for bullet indent, NOT `<bullet>`) are supported.
- **Spaced data tuples in TableStyle** — `('BACKGROUND', (0,0), (-1,-1), bg_color)` requires a Color object, not a tuple of Colors. A tuple of two Colors (from a function returning `(bg, accent)`) will cause `AssertionError: Can only convert 3 and 4 sequences to color`.
- **Never merge learner and manager packs** into one PDF. They are always two separate files.
- **Module count comes from the MD source** — the build script detects `# Module N:` headings dynamically. Do not hardcode module counts.

### Quiz option rendering — ReportLab auto-bullet + pypdf Table flattening

**The problem:** When quiz options (`A) text`, `B) text`, etc.) are rendered inside a Table cell (even as separate Paragraphs in separate rows), pypdf/pdfplumber flattens all cell content into one line joined by `\x7f` (ReportLab's internal bullet character, ASCII 127). ReportLab's Paragraph parser auto-detects `A)`, `B)`, `C)`, `D)` at line starts as bullet markers and replaces them with `\x7f`.

**Verified in testing:** A simple `Paragraph("A) option", style)` outside a Table extracts cleanly as `A) option`. Inside a Table cell, it extracts as `\x7f A) option`. This is a ReportLab + pypdf interaction, not a pypdf-only issue.

**The fix — QuizCallout Flowable:** For quiz blocks, use a custom `Flowable` subclass that draws the background rect and left border directly on the canvas (`draw()` method), then renders each child (label, question, options, correct answer, explanation) via `drawOn()`. This completely avoids Table nesting, so pypdf extracts each element on its own line.

```python
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

    def wrap(self, availWidth, availHeight):
        # Measure label + question + each option + correct + explanation
        # Return (width, height)

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.rect(0, 0, self._w, self._h, stroke=0, fill=1)  # background
        c.setStrokeColor(self.accent)
        c.setLineWidth(3)
        c.line(0, 0, 0, self._h)                           # left stripe
        # Render each child via drawOn() at calculated y positions
```

**Key rules:**
1. Each option must be a separate `Paragraph(opt_text, body_style)` rendered via `drawOn()` — never joined with `\n` in one Paragraph, never inside a Table cell.
2. Strip `\x7f` from option text as a safety measure: `opt.replace("\x7f", "")`
3. Import `Flowable` from `reportlab.platypus`

### Check question multi-line parsing

**The problem:** The MD source format has `**Check question:**` on one line and the actual question text on the NEXT line. The `_LABEL_RE` regex `r"\*\*Check question:\*\*\s*(.*)"` only captures text on the same line, so `rest` is empty.

**The fix:** After matching `**Check question:**`, look ahead past blank lines for the next `p` event. If `rest` is empty, use that next paragraph's text as the question:

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

### pypdf/pdfplumber Table text extraction

Both pypdf and pdfplumber flatten Table cell content. Multi-line text within a single cell gets joined with spaces or `\x7f`. Separate Paragraphs in separate Table rows also get joined. The only reliable way to get per-line extraction is to render content outside any Table structure — either as direct story items or via a custom `Flowable` that uses `drawOn()`.

## Reference files

- **`references/HERMES-LEARNOS-PROMPT.md`** — Paste-ready system prompt encoding all importer rules. Feed this to the LLM when generating or editing learner MD content.
- **`references/learnos-pdf-import-pipeline.md`** — Full documentation of the LearnOS import pipeline, block kinds, depth levels, and schema.
- **`references/excel-spreadsheet-template.md`** — Structure, styling, and openpyxl gotchas for the required Excel spreadsheet output.
- **`references/build_learnos_packs.py`** — The current build script. Copy to the programme folder and run.

## Related skills

- `learnos-pdf-builder` — Class-level umbrella for this build pipeline. These two skills overlap significantly. Consider consolidating into one skill focused on the build pipeline, with a separate skill for learning design (module/rubric/content architecture) if the scope warrants it.
- `pdf-report-generation` — PDF rendering patterns, design conventions, reportlab gotchas (also covers governance/legal PDFs)
- `learning-design` — Lara's domain; for programme architecture and learning outcomes
