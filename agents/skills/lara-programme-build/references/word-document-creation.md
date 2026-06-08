# Creating Word Documents on macOS — python-docx Pattern

## When to use this

Use this pattern whenever you need to create a Microsoft Word document on Jared's Mac — a source brief, a companion document, a content draft, or any `.docx` file that needs to land in his Documents folder or Desktop.

## Why not AppleScript / osascript

AppleScript launched via `osascript` in the terminal will fail if the document text contains `&` characters. The shell interprets `&` as a background operator and the script breaks with a syntax error. Escaping is fragile and unreliable for long documents.

```bash
# This WILL fail if content has &
osascript <<'APPLESCRIPT'
tell application "Microsoft Word"
  set content of text object to "Learning & Development"  # breaks here
end tell
APPLESCRIPT
```

## The reliable pattern: python-docx

`python-docx` is already installed on Jared's Mac. Build the document programmatically, save it, then open it.

### Minimal example

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

# Set default font
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

# Add content
p = doc.add_paragraph()
run = p.add_run("Document Title")
run.bold = True
run.font.size = Pt(18)

doc.add_paragraph("Body text goes here.")

# Save
doc.save("/Users/jc/Documents/Filename.docx")
```

### Opening the result

```bash
open -a "Microsoft Word" "/Users/jc/Documents/Filename.docx"
```

## Key formatting patterns

```python
# Centered title
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("TITLE TEXT")
run.font.size = Pt(18)
run.bold = True

# Colored subtitle
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)  # dark blue

# Gray date line
run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)

# Section header with spacing
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(18)
run = p.add_run("SECTION HEADER")
run.font.size = Pt(13)
run.bold = True

# Body paragraph
doc.add_paragraph("Your body text here.")
```

## Pitfalls

- **Don't use `osascript` for any document containing `&`.** The content WILL contain it in phrases like "Learning & Development", "Talent Acquisition & Retention", etc.
- **python-docx is already installed.** No `pip install` needed in most cases.
- **Always use `open -a` to show the result.** The user expects to see the document on screen.
- **Save to Documents or Desktop.** These are Jared's expected locations.
