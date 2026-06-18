# Excel Operational Plan Delivery Pattern

## When to use

When Jared asks for a plan, strategy, or operational roadmap and the output needs to be something he can track, update, and work from — not just read. Deliver BOTH:

1. **Markdown strategy document** — the thinking, the architecture, the prompts, the principles. For reading once.
2. **Excel workbook** — the operational plan. For working daily. Colour-coded. Dropdowns. Filterable. Trackable.

## Signal

Jared: "post the plan in here in an Excel."

Translation: the markdown strategy is correct, now make it operational.

## Excel Workbook Architecture

### Brand Rules (non-negotiable)
- Use PerformOS brand colours: Ivory (`#f2efe8`) for backgrounds, Ink (`#0a0a0a`) for headers, Electric Lime (`#d4ff3b`) for ship/completion phases
- Header font: Inter 11pt bold, white on Ink background
- Body font: Inter 10pt, Ink
- Thin borders in `#d9d9d9` (Ink 12%)
- Alternate-row shading in Ivory Soft (`#e8e4da`) for readability

### Sheet Structure (for a full operational plan)

| Sheet | Purpose | Key Features |
|---|---|---|
| **Catalogue / Master List** | All items (videos, tasks, deliverables) | Auto-filter, status dropdown, pillar/phase colour coding, freeze top row |
| **Production Calendar** | Day-by-day execution plan | Date column calculated from start date, phase colour fills, lime colour for ship/milestone days |
| **Reference / Rules** | Quick-reference rules or prompts | Alternate-row shading, concise |
| **Distribution / Execution** | Where things go, how they execute | Platform, format, frequency, notes |
| **Specs / Brand** | Brand tokens, specs, do/don't | Token + value + use pattern |
| **Setup Checklist** | Things to create/configure before starting | Status dropdown, what's needed |
| **Tracker** | Companion/related items to track | Status dropdown, pairing references |

### Technical Patterns (openpyxl)

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# Brand constants
INK = "0a0a0a"
IVORY = "f2efe8"
IVORY_SOFT = "e8e4da"
LIME = "d4ff3b"

# Reusable style helpers
header_fill = PatternFill(start_color=INK, end_color=INK, fill_type="solid")
header_font = Font(name="Inter", size=11, bold=True, color=IVORY)
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

body_font = Font(name="Inter", size=10, color=INK)
thin_border = Border(
    left=Side(style='thin', color="d9d9d9"),
    right=Side(style='thin', color="d9d9d9"),
    top=Side(style='thin', color="d9d9d9"),
    bottom=Side(style='thin', color="d9d9d9")
)

# Freeze top row on every sheet
ws.freeze_panes = "A2"

# Auto-filter on catalogue sheets
ws.auto_filter.ref = f"A1:Z{len(data)+1}"

# Data validation dropdowns
dv = DataValidation(type="list", formula1='"To do,In progress,Done"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"F2:F{len(data)+1}")

# Column width helper
for c, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(c)].width = w
```

### Phase Colour Coding
Use distinct light fills for each phase/type so the calendar is scannable:

| Phase | Hex | Use |
|---|---|---|
| Foundation / Brand | `#f2efe8` (Ivory) | Brand work, setup |
| Products | `#e8f0fe` (light blue) | Product-specific work |
| Authority / Social | `#e8f4e8` (light green) | Social proof, content |
| Campaigns / Launch | `#fef3e8` (light orange) | Campaign assets |
| Real Content | `#fce4ec` (light pink) | Real-person filming |
| Hybrid Edit | `#ede7f6` (light purple) | Post-production |
| Ship / Complete | `#d4ff3b` (Lime) | Milestone days only |

### Pitfalls

- **Do not deliver only the markdown strategy.** If the output has a sequence, deadlines, or trackable items, the Excel is the primary deliverable. The markdown is the companion.
- **Use openpyxl, not pandas to_excel().** pandas strips formatting. The brand aesthetic matters.
- **Always freeze the top row.** Jared will scroll.
- **Always add data validation dropdowns for status columns.** The Excel is meant to be worked in, not just read.
- **Calculate dates programmatically from a start date.** Don't hardcode dates — the calendar shifts.
- **Save to Desktop, not a temp path.** Jared opens these files directly.

## Version

Captured 18 June 2026 from the Seedance 2.0 PerformOS content strategy build.
