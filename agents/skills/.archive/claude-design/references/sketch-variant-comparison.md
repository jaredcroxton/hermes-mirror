# Sketch: Throwaway Variant Comparison

> This is a reference file under `claude-design`. It captures the sketch skill's lightweight variant-comparison methodology for early-stage design exploration. Use when the user says "show me what X could look like" or "compare layout A vs B" — before committing to a polished artifact.

## When to use this pattern vs full claude-design

| Situation | Use |
|-----------|-----|
| "Show me 2-3 takes on this UI" | This sketch pattern |
| "Build me a landing page" | Full claude-design |
| "Compare layout A vs B" | This sketch pattern |
| "Polish this deck" | Full claude-design |
| Early exploration, disposable | This sketch pattern |
| Production-facing artifact | Full claude-design |

## Intake (3 questions, one at a time)

1. **Feel.** "What should this feel like? Adjectives, emotions, a vibe." — *"calm, editorial, like Linear"* beats *"minimal"*.
2. **References.** "What apps, sites, or products capture the feel you're imagining?"
3. **Core action.** "What's the single most important thing a user does on this screen?"

Reflect each answer briefly. Skip if already given.

## Variant axes

Pick ONE axis and pull apart from it. Never just tweak pixels — change the design stance:

- **Density:** compact / airy / ultra-dense
- **Emphasis:** content-first / action-first / tool-first
- **Aesthetic:** editorial / utilitarian / playful
- **Layout:** single-column / sidebar / split-pane
- **Grounding:** card-based / bare-content / document-style

## Variant delivery

Each variant is a single self-contained HTML file:

```
sketches/
├── 001-calm-editorial/
│   ├── index.html
│   └── README.md
├── 001-utilitarian-dense/
│   ├── index.html
│   └── README.md
└── 001-playful-split/
    ├── index.html
    └── README.md
```

Each variant README answers: design stance, key choices, trade-offs, best for.

## Head-to-head comparison

After all variants built, present as an opinionated comparison table:

```markdown
| Dimension | Calm editorial | Utilitarian dense | Playful split |
|-----------|----------------|-------------------|---------------|
| Density   | Low            | High              | Medium        |
| Primary action visibility | Low | High | Medium |
| Scan-ability | High | Medium | Low |
| Feel | Calm, trusted | Sharp, tool-like | Inviting, energetic |

**My take:** Utilitarian dense for power users, calm editorial for content-forward audiences.
```

## Verification

Use browser tools to visually check each variant — don't just write HTML and hope:

```bash
browser_navigate(url="file:///absolute/path/to/sketches/001-calm-editorial/index.html")
browser_vision(question="Does this layout look clean and readable? Any visible bugs?")
```

## Frontier mode (what to sketch next)

When sketches exist and user asks "what next?":
- **Consistency gaps** — winning variants from different sketches made independent choices
- **Unsketched screens** — referenced but never explored
- **State coverage** — happy path only; empty/loading/error/edge cases missing
- **Responsive gaps** — validated at one viewport only
