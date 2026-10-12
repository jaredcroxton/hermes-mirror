Training Module PDF — Reference Notes
=====================================
Last updated: 28 May 2026
Source: Stoic Mindset session (4 modules, Learner Pack 9p + Manager Pack 6p)

## Two-Pack Output Structure

Every LearnOS training build produces TWO PDFs from one Excel source:

### Learner Pack (uploaded to LearnOS)
- Cover page with metadata table and usage callout
- Per-module pages (2-3 pages per module):
  - Module divider (number badge + title + duration)
  - Learning objective
  - Content summary (from Tell column)
  - SHOW box (grey background example)
  - KEY POINTS (yellow-tinted card with 3-5 bullets)
  - REFLECT prompt (grey italic box)
  - DO / Practice activity
  - QUIZ block: question, 4 options A-D with (correct) marker, explanation
  - ROLEPLAY block (blue box): Scenario, Persona, Goal
- Closing: gold banner quote
- Quiz bank and roleplay bank are defined in the build script, keyed by module number
- Quiz questions test application, not recall. Options are specific, not abstract.

### Manager Pack (NOT uploaded to LearnOS)
- Cover page with audience, purpose, how-to-use
- Per-module pages:
  - Module divider (same visual style as Learner Pack)
  - Manager Actions (coaching questions with numbered list)
  - Modeling tip (green callout)
  - Facilitator Notes (italic grey note blocks)
  - Live Activity Option (blue callout)
  - Evaluation (Level 1-4 criteria with targets)
- Sources page at end (aggregated from all modules, column E)

## Reportlab Component Reference

### Components used in both packs
- module_header(idx, title, duration): full-width two-column divider
- section_card(title, lines, color): white card with accent top border
- callout_box(text, bg, icon): coloured background box with icon
- show_box(text): grey background with SHOW label and dark top border
- key_points_box(points): yellow card with KEY POINTS header
- reflect_box(text): grey italic reflect prompt
- quiz_block(question, options, correct_idx, explanation): full quiz with options + explanation
- roleplay_block(scenario, persona, goal): blue box with ROLEPLAY header
- simple_table(headers, rows, col_widths): dark header table
- hr(): horizontal rule
- sp(h): vertical spacer

### Quiz bank format
QUIZ_BANK = {
    1: [  # Module number (1-indexed)
        {
            "q": "Question text?",
            "opts": ["A", "B", "C", "D"],
            "correct": 2,  # 0-based
            "exp": "Explanation."
        },
    ],
}

### Roleplay bank format
ROLEPLAY_BANK = {
    1: {
        "scenario": "Situation.",
        "persona": "Who the learner is.",
        "goal": "What to achieve."
    },
}

### Manager actions format
MANAGER_ACTIONS = {
    1: {
        "intro": "Context.",
        "questions": ["Q1?", "Q2?"],
        "modeling": "How manager models this.",
        "notes": ["Note 1", "Note 2"],
        "live_activity": "Live exercise.",
        "evaluation": ["Level 2: method. Target: X."]
    },
}

## Critical Pitfall: <bullet> Tag

NEVER use <bullet> as an XML tag in reportlab Paragraph strings.
Paragraph('<bullet> text') raises ValueError: Parse error.

ALWAYS use unicode bullet character: Paragraph('• text', style)

If spreadsheet content has <bullet> tags, strip in get_cell():
    str(v).replace('<bullet>', '•').replace('</bullet>', '').strip()

## Critical Pitfall: Function Definition Order

In reportlab build scripts, helper functions (show_box, reflect_box, quiz_block,
roleplay_box) MUST be defined BEFORE the loop that calls them. Python executes
top-to-bottom; a function called before definition raises NameError.

Put all helper function definitions right after the style definitions and before
the `on_page` callback and story-building loop.

## Page Layout
- A4, 20mm margins
- Header: dark bar (28pt), title left, "LEARNOS UPLOAD READY" / "COACHING COMPANION" right
- Footer: muted grey, "Source: *.xlsx · Generated DD MMM YYYY · Page N"
- Font: Helvetica throughout

## Colour Scheme Per Module
- Module 1: ACCENT blue #0f3460
- Module 2: GOLD #e2b04a
- Module 3: GREEN #27ae60
- Module 4: ORANGE #e67e22
- Closing banner: GOLD

## Spreadsheet Column Mapping (1-based)
A: Module number    B: Module title     C: Learning outcomes
D: Content to be Taught                E: Content Sources
F: Tell (Explain)  G: Show (Demonstrate)
H: Do - Baseline  I: Do - Creative    J: Check (Assess)
K: Practical Application               L: Manager Action
M: Duration        N: Kirkpatrick     O: Evaluation Method
P: Notes

## File Naming
- Excel: <topic>-session-simple.xlsx
- Learner Pack: <Topic>-Learner-Pack.pdf
- Manager Pack: <Topic>-Manager-Pack.pdf
- Build scripts: build_learner_pack.py and build_manager_pack.py

## Script Architecture
- All content read from Excel at runtime (openpyxl data_only=True)
- Quiz/roleplay/manager dicts defined in script (hard-coded, not from spreadsheet)
- Output to same directory as Excel
- Run via terminal, NEVER execute_code (sandbox lacks reportlab)
- Verify with pymupdf page count before delivering

## LearnOS LLM Import Pipeline (28 May 2026)

The LearnOS academy does NOT parse PDF structure directly. It:
1. Extracts raw text via `pdf-parse` library
2. Sends text to OpenAI gpt-4.1 with structured JSON schema
3. The LLM creates ALL modules, sections, quizzes, roleplays from the text
4. Backend maps LLM output → slides/blocks in the course

### What this means for PDF content
- Write RICH NARRATIVE TEXT with clear structural cues
- The LLM reads headings, bullets, examples, scenarios
- Page breaks do NOT matter — LLM reads full extracted text
- Labels like "SHOW", "REFLECT", "Quick Check", "Practice Scenario" help the LLM
- Keep total text under 80,000 characters (truncated above that)

### LLM JSON Schema (what the AI outputs per section)
- title (≤ 8 words), content (2-3 short paragraphs), keyPoints (3-5 bullets, NO prefix chars)
- reflection (practice prompt or null)
- quiz (1 MCQ, 4 options with ids opt-0..opt-3, correctOptionId, explanation, difficulty)
- roleplay (scenario/persona/goal or null)

### Three import depths
- quick: 2-3 modules, ~5 min, recall/application quiz
- standard: 4-5 modules, ~15 min, application quiz preferred
- deep: 6-8 modules, 30+ min, application/scenario quiz

### System prompt rules the LLM follows
- NEVER invent facts from source
- Short scannable paragraphs, not walls of text
- Quiz tests APPLICATION not recall
- keyPoints are standalone insights, not sentence fragments
- Module titles use verb + topic format
- Section titles ≤ 8 words

### Block kinds in LearnOS
heading (H2/H3), text, divider, quiz, reflection, roleplay, image, video

### Slide types in LearnOS
text (Tell+Show), reflection (Do), quiz (Check), interactive (Practice)
