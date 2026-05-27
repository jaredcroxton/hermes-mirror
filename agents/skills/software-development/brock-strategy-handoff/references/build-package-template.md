# Build Package Structure Template

This is the folder structure Brock produces when handing off a website build to Bob_Builder.

## Folder tree

```
~/Desktop/website-performOS/
├── README.md
├── research/
│   ├── 01-competitor-analysis.md
│   └── 02-key-findings.md
├── legal/
│   ├── 01-option-b-rules.md
│   ├── 02-safe-claims.md
│   └── 03-certificate-rules.md
├── build/
│   ├── 01-page-structure.md
│   ├── 02-course.html            (or 02-<page-name>.html)
│   ├── 03-css-notes.md
│   └── bob-builder-task.md       ← THE HANDOFF
└── deploy/
    └── 01-deploy-instructions.md
```

## bob-builder-task.md template

```markdown
# Bob_Builder Task — [Page Name] [Action]

## Task

[One-line description]

## Source file to deploy

The complete rebuilt HTML is at:
`/Users/jc/Desktop/Obsidian/PerformOS/website-build/build/02-[pagename].html`

Copy it into place:
```bash
cp "/Users/jc/Desktop/Obsidian/PerformOS/website-build/build/02-[pagename].html" "/Users/jc/Desktop/Website - PerformOS/[pagename].html"
```

## What changed from the old page

| Old (current live) | New (this build) |
|---|---|
| [Old section/heading] | [New section/heading] |
| [What was missing] | [What was added] |

## Deploy (Vercel CLI)

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
vercel --prod --yes
```

## Post-deploy verification checklist

- [ ] [Check 1]
- [ ] [Check 2]
- [ ] ...
- [ ] [Check 10]

## Strategy context (from Brock)

[Brief note about research/legal basis. Full docs at Obsidian path.]
```

## Verified example

A complete working example exists at:
`/Users/jc/Desktop/Obsidian/PerformOS/website-build/`

This was the PerformOS 12-week AI course page rebuild — Option B compliance with Outlier-informed 15-beat structure.
