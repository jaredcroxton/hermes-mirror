# LearnOS PDF Builder - Verified Technical Notes

## ReportLab + pypdf/pdfplumber Interactions

### Auto-bullet detection in Paragraph

ReportLab's Paragraph parser auto-detects these patterns at line starts as bullet markers:
- `A)`, `B)`, `C)`, `D)` - letter + paren
- `1)`, `2)`, `3)` - digit + paren
- `a)`, `b)`, `c)` - lowercase + paren

When detected, ReportLab replaces the marker with `\x7f` (ASCII 127, DELETE character). In extracted text this appears as `(cid:127)` in pdfplumber or `\x7f` in pypdf.

**This happens ONLY inside Table cells.** A standalone `Paragraph("A) text", style)` outside a Table extracts cleanly. Inside a Table cell, it becomes `\x7f A) text`.

**Workarounds tested and FAILED:**
- Separate Paragraph per option in separate Table rows - still flattened
- `Preformatted` instead of `Paragraph` - still flattened (Table-level issue)
- `\n`-joined single Paragraph in one cell - `\x7f` separators
- Zero-width space before letter - changes visible text

**Workaround that WORKS:**
Custom `Flowable` subclass that draws directly on canvas via `drawOn()`, avoiding Table nesting entirely. See QuizCallout implementation in the build script.

### Table text extraction flattening

Both pypdf and pdfplumber extract text from Tables by flattening all cell content:
- Multi-line text in one cell - joined with spaces
- Multiple Paragraphs in multiple rows - joined with `\x7f` or spaces
- `\n` characters within cell content - stripped, replaced with space separators

**Only reliable approach for clean extraction:** Render content as direct story items or via custom Flowable using `drawOn()`.

## Quiz MD Format

The `**Check question:**` label and question text are on SEPARATE lines. The regex only captures inline text. The parsing code must look ahead past blank lines for the next `p` event to get the actual question text.

### Parsing fix pattern

```python
question = inline(rest) if rest else ""
j = i + 1
while j < len(events) and events[j][0] == "blank":
    j += 1
if not question and j < len(events) and events[j][0] == "p":
    question = inline(events[j][1])
    j += 1
# Continue looking for bullets at position j, NOT i+1
```

## Extraction Verification

After every build change, verify quiz output with pypdf. Each option (A, B, C, D) must be on its own line. No `\x7f` characters anywhere. "Correct answer:" and "Explanation:" on their own lines.

Verified clean output (05 Jun 2026):
```
QUIZ
A customer cancels a deal. Which is inside your control?
A) The customer budget decision
B) The market conditions
C) Your next five outbound calls
D) Your manager reaction
Correct answer: C
Explanation. Effort and your next action are always inside the circle.
```
