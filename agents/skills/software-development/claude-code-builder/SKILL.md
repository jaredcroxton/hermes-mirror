---
name: claude-code-builder
description: Use when the user asks to build, deploy, create a dashboard, create a deck, push to GitHub, ship a page/tool, or deploy to Vercel. Orchestrate the BLAST build protocol using Claude Code, GitHub, and Vercel.
version: 1.0.0
author: PerformOS / Jared Croxton
license: MIT
metadata:
  hermes:
    tags: [claude-code, github, vercel, build, deploy, blast, frontend]
    related_skills: [claude-code, github-repo-management]
---

# Claude Code Builder: BLAST Protocol

## Overview

Use this skill whenever the user asks Hermes to build, deploy, or ship a finished artifact such as an HTML dashboard, slide deck, tool, calculator, training page, briefing page, or static web page.

The responsibility split is fixed:

- **Hermes / GPT-5.5** reasons, plans, writes the build brief, verifies prerequisites, orchestrates the workflow, and reports the final links.
- **Claude Code CLI** writes the finished file.
- **GitHub** stores the source of truth.
- **Vercel** deploys the public production URL.

The user-facing result must be a live URL when deployment succeeds.

## Trigger Phrases

Load and follow this skill for requests containing or implying:

- build
- deploy
- create a dashboard
- create a deck
- create a page
- create a tool
- create a calculator
- push to GitHub
- ship it
- Vercel deploy
- make this live
- send me the link

## Auth Context

Jared prefers ChatGPT/Codex where possible without separate API costs. Do not assume an Anthropic API key or Claude API access exists. Verify the active provider and model before changing the stack or giving build instructions.

Hermes reasoning commonly runs through OpenAI Codex OAuth. GitHub access uses `gh`. Vercel access uses the Vercel CLI. Claude Code may be available on the machine, but treat it as optional unless the current Bob profile is explicitly configured to use it.

## Build Stack

- **Reasoning:** Hermes on the currently verified provider/model
- **Build:** The configured coding engine for Bob's profile
- **Dedicated build profile:** Forge, local Hermes profile `bobbuilder`, alias command `bob_builder`
- **Storage:** GitHub account `jaredcroxton`
- **Deploy:** Vercel CLI for web artifacts unless the brief names another target

## Dedicated Forge Profile

A separate Hermes build agent named **Forge** exists for this workflow. It uses profile `bobbuilder` and alias `bob_builder`.

Use Forge when the user wants a focused build-and-ship worker, or when the main Hermes assistant is delegating a build rather than directly orchestrating it:

```bash
bob_builder chat
bob_builder chat -q "Build a dark theme KPI dashboard and deploy it"
```

Forge's identity and local profile details are captured in `references/forge-profile.md`. Do not rename the profile or alias unless the user explicitly asks. The public mirror spec lives at `agents/Bob_Builder.md` in `jaredcroxton/hermes-mirror`, even though the agent's display identity is Forge.

## Default Output Directory

All builds land in:

```bash
~/Desktop/hermes_builds/
```

Create it if needed:

```bash
mkdir -p ~/Desktop/hermes_builds
```

## BLAST Protocol

Every build follows these five phases in order. Do not skip phases. Use these exact phase names when reporting status: **Blueprint, Link, Architect, Stylize, Trigger**. Do not substitute alternate expansions like Login or Authorise.

### Phase 1: Blueprint

Before running any command, write a complete build brief. Internally answer:

1. What is the exact output file, including filename and file type?
2. What sections, data, and content go in it?
3. What colors, fonts, and layout apply?
4. Which GitHub repo does it land in?
5. What is the Vercel project name?

Default visual system:

- Dark theme
- Background: `#0A0A0A`
- Cream text: `#F5EADB`
- Lime accent: `#D4FF3B`
- Display font: Archivo or Calibri Bold
- Body font: Inter
- Label font: JetBrains Mono

The brief must be specific enough that Claude Code can build without asking questions.

### Phase 2: Link

Verify prerequisites before building:

```bash
vercel whoami
gh auth status
```

If the work is being done by Bob_Builder or any profile-backed build agent, also verify auth from the profile's isolated home, not just the host shell:

```bash
HOME=/Users/jc/.hermes/profiles/bobbuilder/home gh auth status
HOME=/Users/jc/.hermes/profiles/bobbuilder/home vercel whoami
```

Then verify the configured coding engine for the current Bob profile before assuming Claude. If Bob is explicitly configured for Claude workflows, check Claude availability. If Bob is on ChatGPT/Codex, do not force Claude-specific commands.

If any check fails, stop and tell the user which tool or auth path needs attention. Do not proceed until fixed.

Reference: `references/bob-profile-auth-and-vercel.md`

### Phase 3: Architect

Pass the full build brief to the configured coding engine with an explicit output path under `~/Desktop/hermes_builds/`.

Rule:
- If the current Bob workflow is Claude-based, use the Claude print-mode path.
- If the current Bob workflow is Codex/ChatGPT-based, use the configured Bob coding path instead of forcing Claude.
- In both cases, the prompt must include the exact output path, structure rules, and a direct instruction to write the finished artifact immediately.

Claude template when Claude is the active build engine:

```bash
claude -p "
You are a senior frontend developer. Build exactly what is described below.
Write the complete, finished file to: ~/Desktop/hermes_builds/<filename>
Single monolithic file. No components. No imports from external files.
Do not ask questions. Do not explain. Build and write the file now.

BUILD RULES:
- Single monolithic HTML file. Everything inline, including CSS, JavaScript, and content.
- No em dashes anywhere, including comments.
- No componentisation. One file is the entire product.
- Dark theme default unless specified otherwise.
- PerformOS brand: Archivo or Calibri Bold for display, Inter for body, JetBrains Mono for labels.
- Soft delete only if any data logic is involved.
- Spell out one to nine. Numerals for 10 and above.

BUILD BRIEF:
<full brief here>
"
```

After the coding engine returns, verify the file exists:

```bash
test -f ~/Desktop/hermes_builds/<filename>
```

If the file is missing, rebuild with a more explicit output path and brief.

### Phase 4: Stylize

Push the result to GitHub.

For a new repo:

```bash
cd ~/Desktop/hermes_builds
gh repo create jaredcroxton/<repo-name> --public --source=. --push
```

For an existing repo or if you need precise control:

```bash
cd ~/Desktop/hermes_builds
git init
git remote add origin https://github.com/jaredcroxton/<repo-name>.git
git add <filename>
git commit -m "Hermes build: <filename> - <one line description>"
git push origin main
```

Tell the user the GitHub URL after pushing.

### Phase 5: Trigger

Deploy to Vercel.

```bash
cd ~/Desktop/hermes_builds
```

Create `vercel.json` if needed:

```json
{
  "version": 2,
  "builds": [{"src": "<filename>", "use": "@vercel/static"}],
  "routes": [{"src": "/", "dest": "/<filename>"}]
}
```

Deploy:

```bash
vercel --prod --yes --name <vercel-project-name>
```

Extract the URL containing `vercel.app` from Vercel output. If no URL appears, run:

```bash
vercel ls
```

Return the result in this format:

```text
Build complete.
File: <filename>
GitHub: https://github.com/jaredcroxton/<repo-name>/blob/main/<filename>
Live: https://<project>.vercel.app
```

## Build Types

- **Dashboard, KPI view, sales report:** `.html`, dark theme, lime accent.
- **Slide deck, presentation:** `.html`, also load and follow `html-slide-deck`. Premium decks require brand-correct colour, smooth animation, navigation controls, mobile layout at `375 x 812`, and zero overflow or clipping.
- **Training page, onboarding module:** `.html`, use scroll-journey style where relevant.
- **Tool, calculator, form:** `.html`, all logic inline.
- **Workflow automation form:** `.html`, self-contained form that POSTs to a Zapier catch webhook. Dropdown logic resolves downstream targets (e.g. role + market → manager). Summary panel with Send to Zapier / Copy payload / Close buttons. Loading, success, and error states on send. Always Local artifact mode — no GitHub or Vercel deploy. See `references/workflow-automation-form.md` for the full pattern.
- **Briefing document:** `.html`, clean layout, printable where useful.
- **PerformOS website page:** `.html`, match the existing PerformOS design system. Always reference `/Users/jc/Desktop/Website - PerformOS/faq.html` as the visual source of truth. Ivory/ink palette, Instrument Serif + Inter + JetBrains Mono, shared nav/footer. See `references/performos-website-design-system.md` for full tokens, typography, components, and build rules. See `references/performos-website-management.md` for site inventory, deploy workflow, operational patterns, DNS troubleshooting, and competitive teardown methodology.

## Local artifact mode

Not every build should go to GitHub and Vercel.

If Jared asks for a simple local artifact such as:
- "just a PDF"
- "HTML to view the org chart"
- a draft operating model
- an internal executive visual
- a companion PDF with no request to publish or deploy

then use **Local artifact mode**.

In Local artifact mode:
- still follow Blueprint, Link, Architect, Stylize, Trigger as thinking phases
- but **Stylize** means final file polish, not GitHub push
- and **Trigger** means PDF export and file verification, not Vercel deploy
- deliver local file paths, not GitHub or live URLs

Preferred Local artifact sequence:
1. Write the HTML artifact to `~/Desktop/hermes_builds/<project>/<name>.html`
2. Inspect the HTML render locally
3. Export PDF from the final HTML
4. Verify both files exist
5. Return the local file paths

## Common Pitfalls

1. **Skipping the Blueprint.** Always create a complete brief before touching the terminal.
2. **Proceeding without auth.** Stop if `claude`, `vercel`, or `gh` checks fail.
3. **Letting Claude ask questions.** The prompt must say not to ask questions and must include enough detail to build.
4. **Missing output path.** Always specify `~/Desktop/hermes_builds/<filename>` in the Claude prompt.
5. **Em dashes in generated copy.** Explicitly ban em dashes in every build brief. After the build, scan the output file for `&mdash;` and Unicode `—` (U+2014) and replace with `-` if any slipped through. The build brief ban is not always enough — generated labels, footers, and placeholder text can still carry them.
6. **External dependencies.** The artifact must be a single file with inline CSS, JS, and content. Avoid imports from local files.
7. **Vercel URL missing.** Use `vercel ls` to find the most recent production deploy URL.
8. **Pushing secrets.** Never include `.env`, tokens, OAuth files, private emails, or sensitive PII in GitHub or Vercel deploys.
9. **Drifting Forge's identity.** The local profile name remains `bobbuilder` and alias remains `bob_builder`; the agent identity shown to the user is Forge. Keep public mirror paths stable unless Jared asks for a rename.
10. **Wrong BLAST expansion.** The phases are Blueprint, Link, Architect, Stylize, Trigger. If verification output shows other names, patch the SOUL or skill text and re-test the profile.
11. **Forcing Claude when Bob is on Codex.** Always verify the active Bob provider/model before using Claude-specific commands. Jared prefers ChatGPT/Codex where possible without separate API costs.
12. **Bulk model rollouts without verification.** Before changing the whole agent stack, probe the intended provider/model first. `gpt-5.5` failed for Jared's account; `gpt-5.4` via `openai-codex` was verified working.
13. **Git push blocked in sandbox.** `git push origin main` times out in the Hermes sandbox because the osxkeychain credential helper cannot be reached from the isolated environment. For deployments, use `vercel --prod --yes` directly from the project directory instead. The git commit is still created locally; the user pushes from their terminal later.
14. **Editing existing website repos.** When editing files in an existing tracked repo (not `~/Desktop/hermes_builds/`), the working tree can be overwritten by external processes. After writing a file, verify it with `grep` for expected content before deploying. If the file regressed, restore from the last commit with `git checkout <commit> -- <filename>`, then redeploy with `vercel --prod --yes`.

## Verification Checklist

- [ ] Blueprint brief written with filename, content, visual system, repo, and Vercel project name.
- [ ] `claude --version` succeeded (if Claude is the active build engine).
- [ ] `vercel whoami` succeeded.
- [ ] `gh auth status` succeeded.
- [ ] Output directory exists.
- [ ] Build engine wrote the requested file.
- [ ] File exists at `~/Desktop/hermes_builds/<filename>` (or repo path for existing site edits).
- [ ] For existing website repos: file content verified with `grep` for expected text before deploying.
- [ ] For HTML decks, `html-slide-deck` has been followed and mobile was checked at `375 x 812` before delivery.
- [ ] For HTML decks, navigation arrows, dots, counter, keyboard, and swipe controls work.
- [ ] For HTML decks, no text overflow, clipping, logo overlap, or mobile nav crowding remains.
- [ ] If using Local artifact mode, export the PDF from the final HTML and verify both local files exist.
- [ ] If deploying via Vercel CLI, `vercel --prod --yes` succeeded and aliased correctly.
- [ ] If deploying via git push (from user's terminal, not sandbox), push succeeded and Vercel auto-deployed.
- [ ] Final response includes the correct artifact paths or URLs for the mode used.
