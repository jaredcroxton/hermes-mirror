---
name: word-document-generation
description: Create formatted .docx files via Python (python-docx). Use when the user asks you to create, write, or generate a Word document, especially for training materials, briefs, reports, or formatted documents with sections.
version: 1.0.0
author: PerformOS / Jared Croxton
metadata:
  hermes:
    tags: [word, docx, document-generation, python-docx, productivity]
    category: productivity
---

# Word Document Generation

## When to use this skill

Load this skill when:
- User asks to create a Word document (.docx)
- User asks to "write a document" or "generate a report" in Word
- User mentions Microsoft Word output
- User asks for a formatted document with sections, headers, titles

## Approach: python-docx (preferred)

Use the `python-docx` library. It is installed on Jared's machine and produces clean, formatted .docx files without the character-escaping headaches of AppleScript.

### Why not AppleScript

AppleScript passed to the shell breaks on special characters:
- `&` is interpreted as shell background operator
- Quotes require careful escaping
- Multi-paragraph content is fragile

python-docx avoids all of this. Content is plain Python strings.

### Document structure template

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

# Default style
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)
```

### Formatting helpers

Use these function patterns for consistent formatting:

- **Title**: Center-aligned, 18pt, bold
- **Subtitle**: Center-aligned, 14pt, bold, dark blue (`RGBColor(0x1F, 0x4E, 0x79)`)
- **Date/attribution line**: Center-aligned, 11pt, grey (`RGBColor(0x80, 0x80, 0x80)`), 18pt space after
- **Section headers**: Left-aligned, 13pt, bold, 18pt space before, 6pt space after
- **Body text**: Left-aligned, 11pt, 6pt space after
- **Final/closing line**: Center-aligned, 12pt, bold, dark blue, 18pt space before

### Pattern

```python
def add_title(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.size = Pt(18)
    run.bold = True

def add_section_header(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.bold = True

def add_body(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
```

### Save location

Default save path: `~/Documents/<document-name>.docx`

User may specify a different location. When they say "save to my documents", use `~/Documents/`.

### Opening the file

After saving, open the file so the user can see it immediately:

```bash
open -a "Microsoft Word" "/Users/jc/Documents/<document-name>.docx"
```

## Page estimation

For Calibri 11pt with 2.54cm margins and the spacing above:
- ~350 words per page
- Section headers add ~2-3 lines each
- A two-page document is roughly 1,000-1,300 words with 5-7 sections

## Pitfalls

1. **Do not use AppleScript for document content.** Shell interpretation of `&`, quotes, and special characters causes fragile scripts. Use python-docx instead.
2. **pip install if missing.** If `python-docx` is not installed: `pip3 install python-docx`
3. **Verify Word is installed** before writing: `ls /Applications/Microsoft\ Word.app`
4. **Launch Word first** if it's not already running: `open -a "Microsoft Word"`

## Reference files

- `templates/word-document-template.py` — Full working template with all formatting helpers. Copy and modify for new documents.
