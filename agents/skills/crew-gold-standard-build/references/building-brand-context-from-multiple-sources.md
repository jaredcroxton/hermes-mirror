# Building Brand Context from Multiple Sources

Proven 28 June 2026 for PerformOS. When a business doesn't have a single brand document, pull from scattered sources and consolidate into one `brand-context.md`.

## When to use this pattern

The business has brand identity spread across:
- A live website
- Obsidian vault MARKDOWN files
- Desktop brand style guides
- Agent soul files that carry product positioning
- Founder conversations and accumulated agent memory

No single document captures everything. You need to synthesise.

## Source priority

1. **Published website** — what customers actually see. The public face.
2. **Brand style guides** — canonical hex codes, typography, voice rules. Authoritative.
3. **Obsidian MARKDOWN** — IDENTITY.md, VISUAL.md, COPY.md. Internal source of truth.
4. **Agent souls** — product positioning, audience framing, sub-agent ecosystem.
5. **Memory and conversation** — accumulated understanding of the founder's intent.

Synthesise in that order. Later sources fill gaps, not override earlier ones.

## The consolidation process

### Step 1: Scrape the website

```bash
# Get the homepage, any /about or /products pages
curl -s https://example.com | # extract content
```

Capture: hero line, positioning statement, product names, audience framing, commercial model, contact details.

### Step 2: Read brand style files

Look for files like `01-brand-identity.md`, `brand.json`, `design-tokens.css`.
Extract: hex codes, font stack, logo specifications, retired identity notes, naming rules.

### Step 3: Read Obsidian MARKDOWN

```bash
ls ~/Desktop/Obsidian/PerformOS/MARKDOWN/
```

Read IDENTITY.md, VISUAL.md, COPY.md for the brand. Read per-product files if the brand has multiple product lines.

### Step 4: Read agent souls

Agent SOUL files often carry the most current product positioning:

```bash
ls ~/Desktop/Obsidian/Agents/
```

Read the orchestrator soul (e.g. Polly_PerformOS.md) for the product ecosystem map.

### Step 5: Pull from memory

Check what the agent already knows: brand colours, voice principles, commercial model, product statuses.

### Step 6: Write the consolidated file

Follow the 11-question structure from the CREW brand-context format:

1. What we do and why it matters
2. Products (table: name, description, status)
3. Commercial model
4. Who buys from us
5. Why they pick us
6. Why they leave
7. The voice (pillars, always say, never say, master lines)
8. What we always get right
9. Where we let customers down
10. What we are trying to achieve
11. Website and online presence
12. What is unwritten
13. Anything I must know
14. Colour system (reference only)
15. What I have not covered

### Step 7: Mark gaps honestly

For pre-launch businesses:
- Mark pricing as "not yet published — owner sign-off required"
- Mark customer data as "pre-launch — no churn data exists"
- Mark audience profiles as "based on product design, not purchase history"
- Never fabricate. Flag the gap explicitly.

## PerformOS example

Sources synthesised:
- performos.com.au (hero, positioning, product cards, commercial framing)
- `/Users/jc/Desktop/performos-brand-styles/01-brand-identity.md` (manifesto, naming rules, retired identity)
- `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/IDENTITY.md` (voice pillars, product principles)
- `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/VISUAL.md` (colour palette, typography, components)
- `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/COPY.md` (master lines, vocabulary, house style)
- `/Users/jc/Desktop/Obsidian/Agents/Polly_PerformOS.md` (product ecosystem, sub-agents)

Output: 9,501 bytes, 236 lines. All 11 fields filled. Pre-launch gaps marked honestly.
