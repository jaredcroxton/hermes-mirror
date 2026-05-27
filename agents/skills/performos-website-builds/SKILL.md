---
name: performos-website-builds
description: How Brock produces PerformOS website builds — research, legal, strategy, and markdown deliverables. NEVER deploys. Hands off to Bob_Builder for code execution.
---

# PerformOS Website Builds — Brock Operating Pattern

## The rule that changes everything

**Brock NEVER pushes to Vercel. Brock NEVER pushes to GitHub. Brock NEVER deploys.**

Every failed deploy in this session came from Brock attempting git push or vercel deploy. The sandbox blocks git push. Vercel CLI works but is flaky. The user explicitly said: "What I want you to do is stop trying to post it live, and I want you just to give it to me in a markdown file that I can upload into Claude code."

## Brock's lane

1. **Research** — Outlier methodology: scrape top competitors, extract section structure, identify frequency patterns, find blue-ocean positioning gaps
2. **Legal** — Route to Atticus_Counsel for analysis, Atticus_Governance for operational translation. Embed Option B compliance rules into the strategy.
3. **Strategy** — Define the beat structure. Name each section's job. Map every decision to a research finding or legal requirement.
4. **Structure** — Write the full page as a 15-beat layout with clear annotations.

## What Brock produces

A folder of markdown files:

```
performos-{project}/
├── README.md                         ← Overview and quick start
├── research/
│   ├── 01-competitor-analysis.md     ← Sites analysed, frequency tables
│   └── 02-key-findings.md            ← 3-5 findings that shaped the build
├── legal/
│   ├── 01-option-b-rules.md          ← Safe vs prohibited, legal anchor
│   ├── 02-safe-claims.md             ← Exact approved wording
│   └── 03-certificate-rules.md       ← Certificate design + wording
├── build/
│   ├── 01-page-structure.md          ← Beat-by-beat explained
│   ├── 02-{page}-code.md             ← ★ THE DELIVERABLE: full HTML in ```html block
│   ├── 03-css-notes.md               ← CSS dependencies and inline style notes
│   └── bob-builder-task.md           ← Handoff instructions for Bob
└── deploy/
    └── 01-deploy-instructions.md     ← How to get it live
```

## The code delivery format

The HTML goes INSIDE a markdown file, inside a ` ```html ` code block. The markdown file has:
- Header with summary of what the build is
- 15-beat structure list
- Option B compliance checklist
- Deploy instructions
- The full HTML in a code block

**Never produce a standalone .html file as the primary deliverable.** The .html goes inside .md.

## Bob_Builder task format

Every build includes `build/bob-builder-task.md` with:
- Exact command to copy the HTML from the code block into place
- The `vercel --prod --yes` deploy command
- 10-point post-deploy verification checklist
- Strategy context so Bob knows WHY

## Save locations

Two copies of every build:
1. Desktop: `/Users/jc/Desktop/website-performOS/` — for quick access
2. Obsidian: `/Users/jc/Desktop/Obsidian/PerformOS/website-build/` — for Brock reference

## Research methodology (Outlier pattern)

When building a course/landing page:
1. Scrape 8-10 top competitor homepages
2. Extract section structure top-to-bottom
3. Build frequency table — what appears in 7+/10 sites is universal
4. Identify 3 surprising findings — what competitors DON'T do
5. Use the gaps to differentiate
6. Every beat in the structure traces to either a frequency finding or a differentiation finding

## Option B compliance (always embedded)

For any PerformOS page referencing Microsoft/Azure/OpenAI certifications:
- Instructor credentials in body text only (never hero H1)
- No third-party logos or icons
- No certification names on certificate
- Mandatory negative disclosure on page
- Trademark attribution in footer
- PerformOS brand more prominent than any third-party mark

## Post-build checklist

Before handing off:
- [ ] Two copies saved (Desktop + Obsidian)
- [ ] `02-{page}-code.md` contains full HTML in ```html block
- [ ] Bob_Builder task includes deploy command and verification
- [ ] README.md updated with project overview
- [ ] Legal folder includes Option B rules + safe claims + certificate rules
- [ ] Zero attempts made to push to Vercel or GitHub
