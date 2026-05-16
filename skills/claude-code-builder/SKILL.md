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

This is the public, sanitized mirror copy of the local Hermes skill `claude-code-builder`.

## Purpose

Use this skill whenever the user asks Hermes to build, deploy, or ship a finished artifact such as an HTML dashboard, slide deck, tool, calculator, training page, briefing page, or static web page.

The responsibility split is fixed:

- **Hermes / GPT-5.5:** reason, plan, write the build brief, verify prerequisites, orchestrate, and report final links.
- **Claude Code CLI:** write the finished file.
- **GitHub:** store the source of truth.
- **Vercel:** deploy the production URL.

## Trigger Phrases

Load this skill for requests containing or implying:

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

## Default Build Stack

- Reasoning: Hermes, GPT-5.5
- Build: Claude Code CLI
- Storage: GitHub account `jaredcroxton`
- Deploy: Vercel CLI
- Output directory: `~/Desktop/hermes_builds/`

## Visual Defaults

- Dark theme
- Background: `#0A0A0A`
- Cream text: `#F5EADB`
- Lime accent: `#D4FF3B`
- Display font: Archivo or Calibri Bold
- Body font: Inter
- Label font: JetBrains Mono

## BLAST Protocol

Every build follows these five phases in order.

### Phase 1: Blueprint

Before running any command, write a complete build brief that specifies:

1. Exact output filename and file type.
2. Sections, data, and content.
3. Colors, fonts, and layout.
4. GitHub repo.
5. Vercel project name.

The brief must be specific enough that Claude Code can build without asking questions.

### Phase 2: Link

Verify prerequisites before building:

```bash
claude --version
vercel whoami
gh auth status
```

If any check fails, stop and tell the user which tool needs authentication.

### Phase 3: Architect

Use Claude Code print mode to write the complete file:

```bash
mkdir -p ~/Desktop/hermes_builds
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

Verify the file exists:

```bash
test -f ~/Desktop/hermes_builds/<filename>
```

### Phase 4: Stylize

Push the result to GitHub.

For a new repo:

```bash
cd ~/Desktop/hermes_builds
gh repo create jaredcroxton/<repo-name> --public --source=. --push
```

For an existing repo:

```bash
cd ~/Desktop/hermes_builds
git init
git remote add origin https://github.com/jaredcroxton/<repo-name>.git
git add <filename>
git commit -m "Hermes build: <filename> - <one line description>"
git push origin main
```

### Phase 5: Trigger

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

Return:

```text
Build complete.
File: <filename>
GitHub: https://github.com/jaredcroxton/<repo-name>/blob/main/<filename>
Live: https://<project>.vercel.app
```

## Build Rules

- Single monolithic HTML file.
- Everything inline.
- No em dashes.
- No componentisation.
- Dark theme by default.
- PerformOS brand fonts.
- Soft delete only if data logic exists.
- Spell out one to nine. Use numerals for 10 and above.

## Security Rules

Never commit or deploy:

- `.env` files
- API keys
- OAuth tokens
- cookies
- SSH private keys
- GitHub tokens
- raw private email or calendar contents
- sensitive PII

Use sanitized templates and documentation instead.
