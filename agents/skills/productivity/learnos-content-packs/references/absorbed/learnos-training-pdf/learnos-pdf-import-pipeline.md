# LearnOS PDF Import Pipeline Reference

## Three Depth Levels

### Quick (level=quick)
- 2-3 modules, ~5 min total read
- Each module: 2-3 sections

### Standard (level=standard) -- DEFAULT
- 4-5 modules, ~15 min total read
- Each module: 3-5 sections
- Each section: 2-3 short paragraphs, 3-5 keyPoints, APPLICATION-level quiz

### Deep (level=deep)
- 6-8 modules, 30+ min total read
- Each module: 4-6 sections

## Per-Module Required Fields
- title (string, verb+topic format)
- summary (string)
- learningObjective ("By the end of this module, you will be able to...")
- sections (array)

## Per-Section Required Fields
- title (string, max 8 words)
- content (string, 2-3 short paragraphs Tell+Show)
- keyPoints (string[], 3-5 bullets, NO bullet prefix chars)
- reflection (string or null -- the DO prompt)
- quiz ({question, difficulty, options[{id,text}]x4, correctOptionId, explanation})
- roleplay ({scenario, persona, goal} or null)

## Block Kinds in LearnOS
text, heading, quiz, reflection, roleplay, image, video, divider, split

## Key Constraints
- NEVER invent facts from source material
- Short scannable paragraphs, not walls of text
- Quiz should test APPLICATION not recall
- Module titles: verb + topic
- Section titles: max 8 words
- Max 80,000 chars input

## What pypdf Extraction Preserves vs Loses
- Blockquote > marker is STRIPPED -- must render "Quote:" as visible text
- "### Show" heading extracts as bare "Show" without colon -- must render "SHOW:" in PDF
- ListFlowable with bulletType="bullet" extracts as literal "bullet" word -- use inline unicode bullet
- Key Takeaways heading without callout renders as bare H3 -- must wrap heading + bullets in callout
- Quiz blocks without header label have no importer anchor -- must render "QUIZ" label at top
