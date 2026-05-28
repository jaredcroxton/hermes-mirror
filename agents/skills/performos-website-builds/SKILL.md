---
name: performos-website-builds
description: How Brock produces PerformOS website builds — research, legal, strategy, markdown deliverables. NEVER deploys. NEVER pushes Vercel or GitHub. Hands markdown files to Jared directly.
---

# PerformOS Website Builds — Brock Operating Pattern

## The rules that change everything

1. **Brock NEVER pushes to Vercel. Brock NEVER pushes to GitHub. Brock NEVER deploys.**
2. **Brock hands markdown files directly to Jared.** Not to Bob_Builder. Not to Claude. Not to anti-gravity.
3. **Brock's job ends when files are on Jared's desktop.**

These rules were locked in after Jared explicitly corrected the workflow multiple times (27 May 2026):
> "Yeah, you totally stuff the website up."
> "In future, with PerformOS markdown strategy code, you hand them to me, not Claude or Antogravity. You don't push it to Vercel or GitHub. You don't need to do any of that. You just hand the markdown files to me before you've done."

## Brock's lane

1. **Research** — Outlier methodology: scrape top competitors, extract section structure, identify frequency patterns, find blue-ocean positioning gaps
2. **Legal** — Route to Atticus_Counsel for analysis, Atticus_Governance for operational translation. Embed Option B compliance rules into the strategy.
3. **Strategy** — Define the beat structure. Name each section's job. Map every decision to a research finding or legal requirement.
4. **Structure** — Write the full page as a 15-beat layout with clear annotations.

## What Brock produces

A folder of markdown files:

```\nperformos-{project}/\n├── README.md                         ← Overview and quick start\n├── research/\n│   ├── 01-competitor-analysis.md     ← Sites analysed, frequency tables\n│   └── 02-key-findings.md            ← 3-5 findings that shaped the build\n├── legal/\n│   ├── 01-option-b-rules.md          ← Safe vs prohibited, legal anchor\n│   ├── 02-safe-claims.md             ← Exact approved wording\n│   └── 03-certificate-rules.md       ← Certificate design + wording\n├── build/\n│   ├── 01-page-structure.md          ← Beat-by-beat explained\n│   ├── 02-{page}-code.md             ← ★ THE DELIVERABLE: full HTML in ```html block\n│   └── 03-css-notes.md               ← CSS dependencies and inline style notes\n└── deploy/\n    └── 01-deploy-instructions.md     ← How to get it live (for Jared, not Brock)\n```

## The code delivery format

The HTML goes INSIDE a markdown file, inside a ` ```html ` code block. The markdown file has:
- Header with summary of what the build is
- 15-beat structure list
- Option B compliance checklist
- Deploy instructions (for Jared to run himself)
- The full HTML in a code block

**Never produce a standalone .html file as the primary deliverable.** The .html goes inside .md. Jared takes the .md file and handles deployment himself — Brock never deploys.

## Handoff to Jared

When the build is complete:
1. Confirm both copies exist (Desktop + Obsidian)
2. Tell Jared the path: `/Users/jc/Desktop/website-performOS/`
3. Point him to the key file: `build/02-course-code.md`
4. Stop. No deploy commands. No git push. No vercel.

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

Before telling Jared the build is done:
- [ ] Two copies saved (Desktop + Obsidian)
- [ ] `02-{page}-code.md` contains full HTML in ```html block
- [ ] Deploy instructions reference the .md file (Jared does the deploy, not Brock)
- [ ] README.md updated with project overview
- [ ] Legal folder includes Option B rules + safe claims + certificate rules
- [ ] Zero attempts made to push to Vercel or GitHub
- [ ] Zero attempts to hand files to Bob_Builder, Claude, or anti-gravity — handoff is to Jared only

## Pitfalls

- **Don't suggest when you can execute.** When Jared asks for a capability upgrade (e.g. "build Lara out more"), give the suggestion and then offer to execute. Don't just describe what could be done and wait. Jared's correction: "I'm talking about Lara. What, you just gave suggestions. Don't change subjects." The right response is a concise recommendation followed by "Want me to write it?" — not a long strategy memo followed by a subject change.
- **External CSS/JS dependencies.** The original page may reference external `styles.css` and `main.js`. When converting to a self-contained deliverable, inline ALL CSS and ALL JS. The final HTML must work as a single file with zero external dependencies beyond Google Fonts and GA4. This surfaced when the Vercel deploy included `course.html` but not `styles.css` — the page served but had no styling.
- **File overwrite on vercel deploy.** Running `vercel --prod --yes` uploads whatever is on disk at that moment. If the git remote has a different version of `course.html`, and the remote is ahead of local, a prior `vercel deploy` can pull the remote version and overwrite local changes. Always verify the file on disk is the correct version BEFORE running vercel deploy. Use `grep "personal AI tutor\\|hero-eyebrow" course.html` to verify.
- **Git push blocked in Hermes sandbox.** The sandbox cannot access macOS Keychain for HTTPS git credentials. SSH also fails (host key verification). The only deploy path that works is `vercel --prod --yes` from terminal. But Brock never runs vercel either — hand the files to Jared and let him handle deployment.
- **Recovering overwritten files.** If course.html gets overwritten (by git operations, vercel pulls, or accidental edits), recover from the local git commit: `git checkout <commit-hash> -- course.html`. Verify recovery with `grep` for a known-unique string from the correct version. Then redeploy.
- **cp -r captures .git repos.** When copying the website build package to Obsidian, `cp -r` will copy hidden `.git` directories and balloon the output with thousands of git object files. Always verify the destination after copy and remove any `.git` directories that were accidentally included. Use `find /path -name ".git" -type d` to check.

## Agent soul updates (Brock's lane)

Brock owns agent soul design. When Jared asks to build out an agent's capability:

1. Read the current soul file from `/Users/jc/Desktop/Obsidian/Agents/`
2. Identify the gaps against the capability Jared wants
3. Write the updated soul directly using `write_file` or `patch`
4. Confirm the file is saved and count lines

Brock writes souls. Bob's sub-agents handle build execution. If the soul update requires craft-specific depth that benefits from a longer generative pass (like Rex_Stack's React patterns or Dexter_Decks' slide architecture), Brock writes a one-page brief and Jared can hand it to Claude Code for the deep generation pass. But for structural additions (Archie's competitive analysis, Lara's thinkers and activity library), Brock writes them directly.

## Reference files

- `references/competitor-research-ai-courses.md` — Full competitor analysis from the 27 May 2026 session (8 AI course sites, frequency table, 3 key findings). Reference when building education/course pages.
- `references/agent-thinker-installation-pattern.md` — Reusable pattern for adding named thinkers to agent souls. Format, rules, placement. Used on Archie_Architect (v2.0) and Lara_LearningDesign (v3.0).
- `references/agent-operating-skeleton-pattern.md` — The seven structural sections every principal agent soul needs: output contract, scorecard, decision rights, escalation triggers, routing rules, cadence, hard lines. Applied to Lara_LearningDesign.
- `references/agent-sub-agent-structure-pattern.md` — Reusable pattern for adding sub-agents to a principal agent. Naming convention, delegation contract, soul structure, profile config, registry update. Applied to Lara_LearningDesign (Rory_Research, Ava_Activities, Eva_Evaluation).
