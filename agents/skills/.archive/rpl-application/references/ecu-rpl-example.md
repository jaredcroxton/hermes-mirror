# ECU RPL Statement Structure — Worked Example

This reference captures the structure used for Jared Croxton's successful RPL application to ECU's Master of Business Psychology, mapping three units simultaneously.

## Document trio

```
Final Copies/
  Jared Croxton RPL Cover Letter.docx    (~1 page, formal letter)
  Jared Croxton RPL Statement.docx       (~6 pages, the main document)
  Jared Croxton CV.docx                  (~2 pages, supporting)
```

## RPL Statement anatomy

### Header block
```
Title: "Recognition of Prior Learning Statement"
Subtitle: "Master of Business Psychology, Edith Cowan University"
Meta line: "Applicant: [Name]  |  Date: [DD Month YYYY]  |  Verified by: [Name, Title, Organisation]"
```

### Introduction section
Three paragraphs + grades paragraph (if applicable):

1. **What you are applying for.** State the units with codes. State that the statement maps experience to published LOs.
2. **Who you are and what you do.** Current role, scope (markets, team size), progression, core accountability.
3. **The headline transformation.** The major piece of work being relied on. Size, scale, countries, team members, outcome.
4. **Academic alignment (optional but powerful).** Completed units with grades, showing immediate applicability of course to practice.

### Unit sections (repeat for each unit)

```
## Unit N: [Unit Name] ([Unit Code])
Handbook: [URL]
[Narrative paragraph — 2-3 sentences describing the relevant work in the language of this unit]

### Mapping to ECU Learning Outcomes

**Learning Outcome 1: [exact wording].** [Evidence paragraph]
**Learning Outcome 2: [exact wording].** [Evidence paragraph]
... (one per LO)
```

### Evidence of Leadership Scope
Bullet list of 20+ specific, verifiable facts. Each bullet is one concrete achievement or accountability.

### Verification
```
Verified by:
[Name]
[Title]
[Organisation]
```

## Quality cross-check script pattern

```python
checks = {
    'Market count consistent': 'eight markets' in text,
    'No old count': 'seven markets' not in text.lower(),
    'Singapore included': 'Singapore' in text,
    'Date correct': '10 July 2026' in text,
    'All unit codes': all(code in text for code in ['MBA6066', 'HRM6011', 'HRM6005']),
    'All LOs present': all(f'Learning Outcome {i}' in text for i in range(1,6)),
    'Verifier named': 'Leanne Edwards' in text,
    'Grades referenced': 'Distinction' in text and 'High Distinction' in text,
}
```

## Key evidence types that strengthen an RPL

| Evidence type | Example |
|---|---|
| Quantitative outcome | "Delivered a 40 percent performance lift in India" |
| Scale | "Across eight markets, nine countries, 350+ team members, 460,000 members" |
| Named frameworks | "Kotter's eight-step model, ADKAR, Bridges, GROW" |
| Named programs | "Manage and Change program, four-hat leadership model, six-pillar sales methodology" |
| Cross-functional scope | "Marketing, sales, finance, IT, people and culture, hotel operations" |
| Regulatory depth | "Fair Work Australia, local employment law across markets, do-not-call registries" |
| Cultural adaptation | "Training adapted for Bahasa-speaking teams in Indonesia, indirect feedback in Thailand" |
| Verification | "Verified by Leanne Edwards, Vice President, People and Culture, Accor Plus" |

## Common university handbook URL patterns

ECU handbook URLs follow this structure:
```
https://www.ecu.edu.au/handbook/unit?id=[UNIT_CODE]&year=[YEAR]
```
Example: `https://www.ecu.edu.au/handbook/unit?id=MBA6066&year=2026`

Extract using `web_extract` — the handbook pages render clean markdown with Learning Outcomes clearly listed.
