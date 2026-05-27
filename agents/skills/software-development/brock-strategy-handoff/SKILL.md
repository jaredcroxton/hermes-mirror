---
name: brock-strategy-handoff
description: Brock's operating model for website and product builds — own strategy/research/legal, package as a Bob_Builder task with exact edit instructions and deploy commands, never deploy directly.
version: 1.0.0
author: PerformOS / Jared Croxton
---

# Brock Strategy Handoff

## Core rule

**Brock does not deploy. Brock packages for Bob_Builder.**

When Jared wants a website change, a product page, a course page, or any HTML/CSS build:
- Brock owns: research, strategy, legal gatekeeping, competitive analysis, page structure
- Brock produces: a complete build package with exact source files and a Bob_Builder task file
- Brock hands off: the task file to Bob_Builder, who does the actual editing and deployment
- Brock never: edits HTML directly, pushes to git, or runs Vercel deploy commands

## Trigger phrases

- "update the website"
- "add X to the course page"
- "apply Option B to the site"
- "put this on performos.com.au"
- "build the page"
- Any request to modify a live PerformOS web property

## Why this exists

Jared corrected the workflow after multiple failed deploy attempts:
> "every time you edit the performos.com.au never works"
> "stop trying to post it live, and I want you just to give it to me in a markdown file"
> "Don't worry about trying to make the editing. You just tell them about the logic, and call the builder with the editing."

The sandbox cannot push to GitHub (osxkeychain unavailable). `vercel --prod --yes` from the project directory works but requires the correct file to be in place first. Bob_Builder owns the terminal execution.

## The Build Package pattern

When Brock completes strategy work for a website change, produce this folder structure:

```
~/Desktop/website-performOS/
├── README.md                        # Overview, quick start
├── research/
│   ├── 01-competitor-analysis.md    # Outlier findings
│   └── 02-key-findings.md           # Top findings that shaped the build
├── legal/
│   ├── 01-option-b-rules.md         # What's safe, what's prohibited
│   ├── 02-safe-claims.md            # Exact approved wording
│   └── 03-certificate-rules.md      # Certificate design rules
├── build/
│   ├── 01-page-structure.md         # Beat-by-beat structure explained
│   ├── 02-course.html               # The full HTML file (source of truth)
│   ├── 03-css-notes.md              # CSS dependencies and inline style notes
│   └── bob-builder-task.md          # ← THE KEY FILE: handoff to Bob
└── deploy/
    └── 01-deploy-instructions.md    # How to get it live
```

Also save a copy to Obsidian: `~/Desktop/Obsidian/PerformOS/website-build/`

### The Bob_Builder task file

`build/bob-builder-task.md` is the executable handoff. It must contain:

1. **Task** — one-line description of what to do
2. **Source file path** — the exact HTML file to deploy (from the package)
3. **Copy command** — `cp source → destination` for the Website - PerformOS repo
4. **What changed** — old vs new table so Bob understands the scope
5. **Deploy command** — `cd /path && vercel --prod --yes`
6. **Post-deploy verification checklist** — 10-item checklist of things to check on the live page
7. **Strategy context** — brief note that full strategy docs are at the Obsidian path

The task file should be self-contained. Bob should be able to execute it without loading any other files.

## Brock's lane vs Bob's lane

| Brock owns | Bob owns |
|------------|----------|
| Competitor research (Outlier methodology) | Copying HTML files into the website repo |
| Legal analysis (Atticus_Counsel + Governance) | Running `vercel --prod --yes` |
| Page structure and beat design | Post-deploy verification |
| Safe claims wording | Git commits and pushes |
| Certificate design rules | Terminal execution |
| Writing the complete HTML file (as a source artifact) | Deploying the file Brock wrote |
| Packaging everything into the folder structure | Following the bob-builder-task.md checklist |

## Related skills

- `claude-code-builder` — Bob_Builder's BLAST protocol for builds and deploys
- `pdf-report-generation` — For PDF exports of legal analysis and governance packs
- `claude-design` — For HTML artifact design when Brock needs to produce a source file

## Pitfalls

1. **Never run vercel deploy from Brock's context.** Even though the command exists and is authenticated, Brock should not execute it. Package it in the Bob_Builder task file instead.
2. **The website repo file can get overwritten.** After writing to `/Users/jc/Desktop/Website - PerformOS/course.html`, always verify with `grep` that the new content is present. If the file regressed, restore from git: `git checkout <commit> -- course.html`.
3. **The Build Package must be complete before handoff.** Bob should not need to ask questions about strategy, legal, or wording. Every decision Brock made should be captured in the package.
4. **Don't hand Bob a strategy document and expect him to extract the build instructions.** The `bob-builder-task.md` file is the executable interface. It translates strategy into copy-paste commands.
