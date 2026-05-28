# Excel Spreadsheet Template for Training Programmes

Every programme build requires an Excel file (`<topic>-session.xlsx`) as the business-facing source of truth.

## Required Sheets (in order)

### Sheet 1: Programme Overview
Columns: Field | Value (merge B-E for each row)
Rows: Programme Name, Product, Audience, Delivery, Total Duration, Modules, Manager Facilitation, Kirkpatrick Target
Then: Module Summary table with columns: Module | Title | Duration | Sections | Focus

### Sheet 2: Module N Detail (one sheet per module)
Columns: Section | Title | Type | Duration | Key Content | Assessment
One row per section. Type values: "Concept", "Concept + Roleplay", "Concept + Reflect"

### Sheet 3: Assessment and Kirkpatrick
Columns: Level | What we measure | How we measure it | When | Target
Rows for each Kirkpatrick level (L1 Reaction, L2 Learning, L3 Behaviour, L4 Results)

### Sheet 4: Manager Coaching Guide
Columns: Week | Activity | Duration | Success Indicator
Rows for each week of the 4-week reinforcement cycle.
Then: Common Failure Modes section with columns: Failure Mode | What it sounds like | Coaching cue

## Styling conventions
- Header row: Helvetica-Bold 14pt, white text, navy fill (#0B1E3D)
- Sub-headers: Helvetica-Bold 11pt, navy text, light blue fill (#D6EAF8)
- Body: Helvetica 10pt, left-aligned, top-aligned, wrap text
- Borders: thin grey (#CCCCCC) on all cells

## openpyxl gotchas
- Sheet titles cannot contain colons. Use hyphens: "Module 1 - Prime Yourself"
- Run openpyxl scripts via terminal(), not execute_code (sandbox may lack the package)
- PatternFill requires both start_color and end_color set to the same hex value

## Naming convention
Save as: `<topic>-session.xlsx` in the same folder as the MD source files.
