# Test Prompt Discipline

Reinforced 27 June 2026 after repeated corrections from Jared.

## The golden rule

If the prompt includes the output you expect the skill to produce, the prompt is wrong. The skill should extract, build, or source that output itself.

## Three rules

1. Give the skill RAW MATERIAL — support tickets, URLs, handoffs from upstream skills, real websites. Let the skill source its own questions, extract its own leads, and build its own output. Never pre-digest the data.

2. If testing a chain (lead-research → prospect-brief → outreach-draft), give the first skill real data and let the handoffs carry context forward. Don't skip to the third skill with pre-written briefs.

3. If no real data is available, use the skill's own fixture cases. The fixture IS the test data. Or use real public data. Last resort: explicitly state "fictional test data."

## Per-skill wrong/right examples

### FAQ Builder
- WRONG: "Build an FAQ. Five questions: Can I skip a week? What if I don't like a meal?..."
- RIGHT: "Build an FAQ from these 12 support tickets: [raw ticket dump in customer's exact words]"
- Jared's correction: "why are you giving the 5??"

### Lead Research
- WRONG: "Build a prospect brief. Company: Northwind Traders, a mid-market food distributor..."
- RIGHT: "Research this company for a sales call: [real website URL]"
- The real Sunshine Coast test with 5 wellness businesses proved the pattern.

### Build Skills (slide-deck, fly-through, etc.)
- WRONG: "Build a slide deck for Tempo, a quiet-luxury audio brand. Ink background, ivory type, amber accent..."
- RIGHT: "I need a slide deck for my business." (Let the discovery questions fire)

### Chain Tests
- WRONG: "Read the lead research we just did on Northwind and build a prospect brief."
- RIGHT: Run lead-research first with real data. Let the handoff carry context forward.
