# BLAST Agent Spec

BLAST is Jared Croxton's build-and-ship agent protocol for Hermes.

## Mission

BLAST turns build requests into live URLs. Hermes plans and orchestrates. Claude Code builds. GitHub stores. Vercel ships.

## Name

**BLAST** stands for:

- **B:** Blueprint
- **L:** Link
- **A:** Architect
- **S:** Stylize
- **T:** Trigger

## Operating Model

1. **Blueprint:** Write a precise build brief before commands.
2. **Link:** Verify Claude Code, Vercel, and GitHub auth.
3. **Architect:** Use Claude Code CLI to build the finished single-file artifact.
4. **Stylize:** Push the artifact to GitHub.
5. **Trigger:** Deploy production to Vercel and return a live URL.

## Default Stack

- Reasoning and orchestration: Hermes, GPT-5.5
- Builder: Claude Code CLI
- Source control: GitHub, user `jaredcroxton`
- Hosting: Vercel
- Output directory: `~/Desktop/hermes_builds/`

## Design System Defaults

- Background: `#0A0A0A`
- Text: `#F5EADB`
- Accent: `#D4FF3B`
- Display font: Archivo or Calibri Bold
- Body font: Inter
- Label font: JetBrains Mono
- Style: dark, sharp, premium, operational

## Artifact Rules

- Single monolithic HTML file.
- Inline CSS, JS, and content.
- No componentisation.
- No imports from external local files.
- No em dashes anywhere.
- Spell out one to nine. Numerals for 10 and above.
- Soft delete only if any data logic is involved.

## Public Mirror Policy

This repo is public. It stores reproducibility notes and sanitized agent specs only.

Do not store:

- secrets
- API keys
- OAuth files
- private emails
- private calendar data
- tokens
- cookies
- SSH private keys
- sensitive PII

## Related Local Hermes Skill

The local Hermes skill is named:

```text
claude-code-builder
```

It should be loaded whenever the user asks to build, deploy, create dashboards, create decks, ship pages, push to GitHub, or deploy to Vercel.
