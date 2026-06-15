---
name: claude-code-builder
description: Use when the user asks to build, deploy, create a dashboard, create a deck, push to GitHub, ship a page/tool, or deploy to Vercel. Orchestrate the Express build protocol using Claude Code, GitHub, and Vercel.
version: 1.0.0
author: PerformOS / Jared Croxton
license: MIT
metadata:
  hermes:
    tags: [claude-code, github, vercel, build, deploy, express, frontend]
related_skills: [claude-code, github-repo-management]
---

# Claude Code Builder: Express Protocol

## Jared-specific quality gates

For any HTML dashboard, lead dashboard, landing page, deck, or client-facing interface, route the finished artifact through the `premium-dashboard-design-reviewer` gate before completion. See `references/premium-dashboard-design-qa-gate.md` for the required review stack, typography standard, and AgentOS reference lesson.

## Overview

Use this skill whenever the user asks Hermes to build, deploy, or ship a finished artifact such as an HTML dashboard, slide deck, tool, calculator, training page, briefing page, or static web page.

The responsibility split is fixed:

- **Hermes / Brock** reasons, plans, writes the build brief, verifies prerequisites, orchestrates the workflow, and reports the final links.
- **Bob Builder / Forge** (profile `bobbuilder`) executes builds via `delegate_task`.
- **Claude Code CLI** writes the finished file (when Bob is Claude-based).
- **GitHub** stores the source of truth.
- **Vercel** deploys the public production URL.

The user-facing result must be a live URL when deployment succeeds.

## Delegation Rules (Non-Negotiable)

**Brock does NOT execute build, research, or enhancement tasks himself.**

| Task type | Who does it | How |
|---|---|---|
| Greenfield build (new file, new page, new dashboard) | Bob Builder | `delegate_task` to bobbuilder |
| Research / competitor analysis | Research subagent | `delegate_task` with `toolsets: ["web"]` |
| Content generation (100+ workflows, copy, etc.) | Content subagent | `delegate_task` with `toolsets: ["file"]` |
| Large-file enhancement (500+ line existing file, targeted CSS/JS fixes) | Bob times out at 600s. **Brock does targeted `patch` edits directly.** | `patch` tool in parent session |
| Quick one-line edits to existing files | Brock | `patch` / `write_file` |
| Reading files, reviewing output | Brock | `read_file` |
| Strategic decisions before build | Brock clarifies with Jared first | `clarify` if needed |

**Why Bob times out on large-file tasks:** Reading a 500+ line file + understanding context + generating targeted edits exceeds the 600s `delegate_task` limit. Bob works best on greenfield builds with a clear brief.

**Research note:** The `web_search` tool does NOT exist in this Hermes setup. For research tasks, delegate to a subagent with `toolsets: ["web"]` which has access to web-independent search, or use `browser_navigate` + `browser_snapshot` directly for specific URLs. Do NOT call `web_search` — it fails with "Tool does not exist."

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
- express (and "Express Protocol" or "/express")
- blast / BLAST / B.L.A.S.T. — redirect user to "Express" (the framework was renamed; BLAST is dead)

**Cross-reference — do not confuse with similarly-named items:**
- `Taste` — not a standalone skill. Taste design thinking lives inside `claude-design` (process+taste for one-off artifacts) and `popular-web-designs` (top 50 brand design systems sourced from VoltAgent/awesome-design-md). Both live in Bob's profile under `creative/`.
- `Awesome Design` / "top 50 websites" — this IS `popular-web-designs`. Each brand (Stripe, Airbnb, Figma, NVIDIA, etc.) is a separate template file. Not a separate named skill.

See `references/express-taste-bundle-placement.md` for details on how the Taste bundle works (claude-design + popular-web-designs) and why it loads in Blueprint, not Stylize.

## Research Delegation

When research or competitive analysis is needed, do NOT use the browser tool directly. The headless browser is detected and blocked by Google, Bing, and DuckDuckGo.

Instead, use `delegate_task` with `toolsets: ["web"]` to spawn a subagent that has access to `web_fetch` and `web_search` which work differently and more reliably for research.

Brock writes the research brief. The subagent does the research. Brock reviews and synthesises.

When a request arrives that involves building, coding, deploying, or shipping a finished artifact, the FIRST action is to delegate to Bob Builder (Forge) via `delegate_task`. Brock writes the brief and sets the constraints. Bob executes.

Exceptions where Brock handles directly:
- Quick one-line patches or edits to existing files (use patch/write_file)
- Reading files or reviewing output
- Strategic decisions that need human input before a build begins

Everything else goes to Bob. This is not optional. Brock executing build tasks himself is a failure mode.

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
```
Deploy:

```bash
vercel --prod --yes
```

**Note:** The `--name` flag is deprecated as of Vercel CLI v53.1+. Do not use it. Vercel auto-generates the project name from the repo or directory name.

Extract the URL containing `vercel.app` from Vercel output. If no URL appears, run:

```bash
vercel ls
```

## Express Protocol

Every build follows these five phases in order. Do not skip phases. Use these exact phase names when reporting status: **Blueprint, Link, Architect, Stylize, Trigger**. Do not substitute alternate expansions like Login or Authorise.

### Phase 1: Blueprint

Before running any command, write a complete build brief. Internally answer:

1. What is the exact output file, including filename and file type?
2. What sections, data, and content go in it?
3. What colors, fonts, and layout apply?
4. Which GitHub repo does it land in?
5. What is the Vercel project name?

**Taste bundle auto-loads here.** Before answering the five questions, load both:
- `claude-design` — design process and taste framework. This gives the design-taste lens for every decision in this phase.
- `popular-web-designs` — top 50 brand reference. This gives real-world design benchmarks (Stripe, Airbnb, Figma, etc.).

Use both to shape the five answers into a proper design brief. By the end of Blueprint, the functional spec AND the design direction are locked. No design decisions happen later in the process.

See `references/express-taste-bundle-placement.md` for the rationale behind Taste-in-Blueprint and the before/after flow.

Default visual system (PerformOS master brand):

- Dark theme
- Background: `#0A0A0A`
- Cream text: `#F5EADB`
- Lime accent: `#D4FF3B`
- Display font: Archivo or Calibri Bold
- Body font: Inter
- Label font: JetBrains Mono

Alternative brand palettes:

**Performlytics** (blue-driven analytics instrument):
- Background: `#0A0A0A` (same ink)
- Text: `#F0F0F5` (cooler cream)
- Accent: `#3B82F6` (blue)
- Secondary: `#8B5CF6` (violet, gradients/highlights)
- Tertiary: `#22D3EE` (cyan, data viz)
- Cards/surface: `#111111`
- Buttons: pill shape, blue fill on dark
- Same font stack as PerformOS

**Pocket Customer** (warm cream + lime):
- Background: `#0A0A0A`
- Primary text: `#F5EADB`
- Accent: `#D4FF3B` (Electric Lime)
- See Obsidian `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/PocketCustomer/VISUAL.md`

**LearnOS** (light theme only):
- Never use dark background or lime on LearnOS
- See Obsidian `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/LearnOS/IDENTITY.md`

Jared is actively moving away from the yellow-green lime look across his dashboards. When he asks for a brand update, consult the PerformOS brand docs at `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/` for the correct product palette.

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
```
Deploy:

```bash
vercel --prod --yes
```

**Note:** The `--name` flag is deprecated as of Vercel CLI v53.1+. Do not use it. Vercel auto-generates the project name from the repo or directory name.

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
- **Cinematic dashboard entry screen:** when Jared asks for a first page, scroll-text intro, date, Enter button, high visual, Taste, Awesome Design, or HyperFrames-style dashboard motion, preserve the existing dashboard/data and add a full-screen intro overlay. Verify visually with `browser_vision`, test Enter, then deploy live. See `references/cinematic-dashboard-entry-pattern.md`.
- **Data-driven dashboard with cron:** `.html`, research agent scrapes external data into JSON, build agent produces dashboard, cron handles weekly refresh. See `references/data-driven-cron-dashboard.md` for the full pattern.
- **Fresh GitHub repo dashboard refresh:** when Jared asks to refresh a deployed dashboard with new GitHub repos from the last five days and says nothing should be copied from before, use GitHub repository search via `gh api`, dedupe results, exclude spam/NSFW bait, update both the JSON source and embedded `RAW_DATA`, and verify old story terms are absent. See `references/fresh-github-repo-dashboard-refresh.md`.
- **Slide deck, presentation:** `.html`, also load and follow `html-slide-deck`. Premium decks require brand-correct colour, smooth animation, navigation controls, mobile layout at `375 x 812`, and zero overflow or clipping. For reusable animation code (particle canvas, spring easing, gradient borders, count-up stats, parallax orbs, typing effects, alternating slide-ins, pulse dots), see `references/html-animation-patterns.md`.
- **Training page, onboarding module:** `.html`, use scroll-journey style where relevant.
- **Tool, calculator, form:** `.html`, all logic inline.
- **Sports draft simulator app:** when Jared asks for an app plan or build brief based on roster-draft games like 82-0 or 38-0, study the gameplay loop first: setup, random spin constraint, player pick, position placement, fit modifier, scoring, season simulation, and shareable result. For AFL, use the 23-0 pattern and start with an 18-player on-field MVP before adding bench complexity. Explain the difference between the builder prompt and the gameplay loop if Jared looks confused. See `references/sports-draft-simulator-planning.md`.
- **Claude Code skill library hygiene:** when Jared complains that Claude Code skills are messy, overlapping, or hard to use, do not create more narrow skills. Map overlaps into class-level umbrellas, preserve unique content in `references/`, and consolidate before archiving. See `references/claude-code-skill-library-hygiene.md`.
- **PerformOS Crew workflow layer in Claude Code:** when Jared asks how Claude Code, named agents, Superpowers, and the project-local flow skills link together, explain the distinction plainly: agents are **who**, skills are **how**, and flow skills are checkpoints Claude Code can load before, during, or after a build. Use the term **PerformOS Crew** for the adapted workflow layer, not the old external repo framing. See `references/performos-crew-flow-layer.md`.
- **Workflow automation form:** build a local HTML form that POSTs to a Zapier catch webhook. Dropdown logic resolves downstream targets (e.g. role + market → manager). Summary panel with Send to Zapier / Copy payload / Close buttons. Loading, success, and error states on send. Always Local artifact mode — no GitHub or Vercel deploy. See `references/workflow-automation-form.md` for the full pattern.
- **Briefing document:** `.html`, clean layout, printable where useful.
- **Pasted HTML dashboard rescue:** when Jared pastes raw HTML from another agent, Brev sandbox, server output, or terminal and wants it opened/built, save it as a single-file dashboard, repair paste damage, upgrade the shell enough for executive review, verify locally, then deploy to Vercel if a click link is useful. See `references/pasted-html-dashboard-rescue.md`.
- **PerformOS website page:** `.html`, match the existing PerformOS design system. Always reference `/Users/jc/Desktop/Website - PerformOS/faq.html` as the visual source of truth. Ivory/ink palette, Instrument Serif + Inter + JetBrains Mono, shared nav/footer. See `references/performos-website-design-system.md` for full tokens, typography, components, and build rules. See `references/performos-website-management.md` for site inventory, deploy workflow, operational patterns, DNS troubleshooting, and competitive teardown methodology.
- **World-class quality upgrade:** when Jared says "make it world class" or "use the right people" about an existing artifact, use the world-class goal brief pattern: read the artifact, write 10 numbered quality goals, delegate to Bob with Taste bundle. See `references/world-class-goal-brief.md` for delegation pattern and trigger conditions.
- **AgentOS typography and design QA correction:** when Jared points to the AgentOS site or says the page is good but the text size, font, or legibility feels wrong, treat it as a typography-discipline correction, not a minor CSS tweak. Use AgentOS posture without cloning: controlled hero scale, clean sans typography, sparse body copy, mono labels only, generous spacing, and a balanced right-side visual. Re-run `premium-dashboard-design-reviewer` after revision. See `references/agentos-typography-and-design-qa.md`.

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

- **Confusing named agents with PerformOS Crew skills.** When Jared asks how Brock, Bob, Lara, or Neo link to Claude Code flows, explain it plainly: agents are **who**, skills are **how**. PerformOS Crew flow skills are not separate agents with souls. They are checkpoints or lenses Claude Code can load. Example: `Act as Bob. Use flow-plan-review-eng before building.` means Bob is the builder and the flow skill is the engineering checkpoint. See `references/performos-crew-flow-layer.md`.
- **Skipping the premium design gate.** For any HTML dashboard, landing page, lead dashboard, deck, or client-facing interface, Bob must run `premium-dashboard-design-reviewer` before final handoff. A verdict of `pass with minor fixes` means draft-ready only. If Jared wants production-ready, route fixes back to Bob and rerun the reviewer.
- **Treating typography feedback as a small CSS tweak.** When Jared says text size, font, or readability is wrong, especially against an AgentOS reference, revise the visual system: type scale, line length, font pairing, copy density, spacing, and hero balance. See `references/agentos-typography-and-design-qa.md`.
- **Skipping the Blueprint.** Always create a complete brief before touching the terminal.
2. **Proceeding without auth.** Stop if `claude`, `vercel`, or `gh` checks fail.
3. **Letting Claude ask questions.** The prompt must say not to ask questions and must include enough detail to build.
4. **Missing output path.** Always specify `~/Desktop/hermes_builds/<filename>` in the Claude prompt.
5. **Em dashes in generated copy.** Explicitly ban em dashes in every build brief. After every build, run the automatic strip command — do not rely on visual scanning. The build brief ban alone is regularly insufficient; generated labels, footers, and placeholder text frequently still carry them. **This is a hard gate, not a manual check.**

   ```bash
   python3 - <<'PY'
from pathlib import Path
p = Path('<output filepath>')
c = p.read_text()
c = c.replace('\u2014', '-').replace('&mdash;', '-')
p.write_text(c)
print('Em dashes remaining:', c.count('\u2014') + c.count('&mdash;'))
PY
6. **External dependencies.** The artifact must be a single file with inline CSS, JS, and content. Avoid imports from local files.
7. **Vercel URL missing.** Use `vercel ls` to find the most recent production deploy URL.
8. **Pushing secrets.** Never include `.env`, tokens, OAuth files, private emails, or sensitive PII in GitHub or Vercel deploys.
9. **Drifting Forge's identity.** The local profile name remains `bobbuilder` and alias remains `bob_builder`; the agent identity shown to the user is Forge. Keep public mirror paths stable unless Jared asks for a rename.
10. **Wrong framework expansion.** The phases are Blueprint, Link, Architect, Stylize, Trigger (Express Protocol). If verification output shows BLAST, patch the SOUL or skill text and re-test the profile.
11. **Forcing Claude when Bob is on Codex.** Always verify the active Bob provider/model before using Claude-specific commands. Jared prefers ChatGPT/Codex where possible without separate API costs.
12. **Bulk model rollouts without verification.** Before changing the whole agent stack, probe the intended provider/model first. `gpt-5.5` failed for Jared's account; `gpt-5.4` via `openai-codex` was verified working.
13. **Git push blocked in sandbox.** `git push origin main` times out in the Hermes sandbox because the osxkeychain credential helper cannot be reached from the isolated environment. For deployments, use `vercel --prod --yes` directly from the project directory instead. The git commit is still created locally; the user pushes from their terminal later.
14. **Editing existing website repos.** When editing files in an existing tracked repo (not `~/Desktop/hermes_builds/`), the working tree can be overwritten by external processes. After writing a file, verify it with `grep` for expected content before deploying. If the file regressed, restore from the last commit with `git checkout <commit> -- <filename>`, then redeploy with `vercel --prod --yes`.
15. **Bob timeout on large-file enhancement tasks.** When the task involves reading an existing large file (500+ lines) and making targeted visual/CSS/JS enhancements, `delegate_task` to bobbuilder often times out at the 600s limit. The workaround is: for targeted fixes to existing files, apply `patch` edits directly from the parent session instead of delegating. Use `delegate_task` for Bob only on greenfield builds or tasks with a clear small-file scope.
15b. **Full-featured dashboard builds time out on first attempt.** When a build includes data model + scoring logic + world-class UI + Taste bundle, the total time exceeds 600s even for Bob. The split-build pattern solves this: Phase A (data engine, 200-210s) then Phase B (dashboard UI, 280-340s). See `references/dashboard-split-build-pattern.md` for delegation pattern and trigger conditions.
16. **Bob timeout on complex first builds with full Express + Taste + data pipeline.** When a build includes multiple phases (data engine, UI, cron scripts), delegate it in two phases to stay under 600s. Phase A: data files only (JSON, weights, README). Phase B: UI and deployment. Each phase stays under 300s. Do not send the entire build in one goal — it will time out.

15b. **Bob timeout on complex multi-component builds.** When a single build involves multiple distinct components (data engine + UI + cron scripts + deploy), the 600s `delegate_task` limit will likely be exceeded. The workaround is to split the build into sequential phases, each delegated separately: Phase A (data model + sample data), Phase B (UI build), Phase C (automation/cron). Each phase is a separate `delegate_task` call. See `references/split-build-pattern.md`.
16. **delegate_task requires `goal`, not `context`, as the task spec.** The `delegate_task` tool requires a `goal` parameter (string) describing what the subagent should accomplish. Do NOT pass the task description as `context` — it will fail with "Provide either 'goal' (single task) or 'tasks' (batch)." The `context` field is for background information only. Always use `goal` for the primary task instruction.
17. **Git commit shortcut error.** The `git add` command does not accept a `-m` flag. Use `git add -A` (or `git add <file>`) followed by `git commit -m "message"` as two separate commands. Never combine them as `git add -m`.
18. **web_search tool does not exist.** The `web_search` tool is not available in this Hermes setup. Use `browser_navigate` + `browser_snapshot` for web research instead. Note: the headless browser is detected and blocked by Google/Bing/DuckDuckGo. For research that requires search engines, use `delegate_task` with `toolsets: ["web"]` to spawn a subagent with `web_fetch`/`web_search` access.
19. **Jared expects Brock to route, not execute.** When the user asks for something to be built, coded, or deployed, the correct response is delegation — not doing the work in Brock's session. Jared has corrected this explicitly multiple times. The hierarchy is: Brock (strategy, briefs, decisions) → Bob Builder (builds, code, deploys) → Research subagents (research, analysis). Brock only touches files directly for quick patches, reviews, or when the user explicitly asks Brock to do it.
21. **Local artifacts go to the Obsidian vault by default.** When Jared asks for something to be saved, created, or built as a local artifact, the default output path is now `~/Desktop/Obsidian/` (the Obsidian vault directory), not `~/Desktop/hermes_builds/`. The hermes_builds directory is still used for web artifacts, dashboards, and deployable files. Everything else — notes, research, flows, strategy docs, agent context — goes to Obsidian unless the user explicitly asks for a different location.
22. **`localhost` in JavaScript resolves to client, not server.** When building a web UI (chat, dashboard) served from a remote host (EC2, VPS) that calls a backend API running on the same server, never use `fetch('http://localhost:<port>')` in the JavaScript. `localhost` in the browser always means the user's machine. Use a same-origin backend proxy (`/api/chat`) or the server's public IP/domain. See `local-dashboard-access` skill and `references/ec2-api-proxy-server.md` for the proxy pattern.
23. **Tabbed dashboard pattern for time-series comparisons.** When building dashboards that compare batches over time (e.g. weekly GitHub trending repos), use a tabbed layout with separate inline JSON data per batch rather than separate files. Each batch gets its own tab button. Data is embedded inline in the HTML (no fetch calls) to avoid CORS issues from file:// URLs. Extract GitHub Trending data via `browser_console` with `JSON.stringify(Array.from(document.querySelectorAll('article.Box-row')).map(...))` — this is faster and more structured than parsing browser_snapshot text.
24. **Cron mode limitations tightened.** In cron jobs: `execute_code` is blocked, piped interpreters are blocked, `patch` tool may not work reliably, and direct git push times out in the sandbox. For cron-triggered builds, use `write_file` + `read_file` + standalone `python3` scripts (not piped). For deployments, use `vercel --prod --yes` from the project directory rather than git push.
20. **Vercel `--name` flag deprecated.** As of Vercel CLI v53.1+, the `--name` flag is deprecated. Do not use `vercel --prod --yes --name <project>`. Use `vercel --prod --yes` without `--name`. Vercel auto-generates the project name from the repo or directory name.
21. **delegate_task returns summaries, not structured data.** Subagents return a text summary of what they did — not the actual JSON, CSV, or structured data they collected. If the task requires structured output (a JSON array of repos, a list of research findings), the subagent's summary will not contain it. **Workaround for web page data extraction:** use `browser_navigate` + `browser_console` with a JavaScript `JSON.stringify(...)` expression that queries the DOM directly (e.g. `document.querySelectorAll('article.Box-row')`). This returns structured data in one call. **Workaround for API data:** download to a temp file (`curl -o /tmp/data.json`), then read with `read_file` or process with a standalone `python3` script.
22. **Cron job mode: execute_code and piped interpreters blocked.** When running as a scheduled cron job, `execute_code` is blocked ("Cron jobs run without a user present to approve it"). Piped commands that feed interpreter input (`curl | python3`, `cat | python3`) are blocked by security scanning. **Workaround:** download API responses to temp files first (`curl -s -o /tmp/file.json`), then read with `read_file` or run a standalone `python3 -c "..."` that reads the local file. Never pipe directly to an interpreter in cron mode.
23. **browser_console is the fastest page-data extraction method.** When scraping structured data from a loaded page, use `browser_console` with a JavaScript expression instead of parsing `browser_snapshot` text. The snapshot output is verbose, truncated, and requires manual parsing. A single `browser_console` call with `JSON.stringify(Array.from(document.querySelectorAll(...)).map(...))` extracts all repo names, descriptions, star counts, and growth metrics in one structured response. This is the preferred pattern for any data extraction from GitHub Trending, search result pages, or any listing page with consistent DOM structure.
24. **Headless browser blocks JavaScript on `file://` URLs.** When verifying a local HTML dashboard, the headless browser will not execute inline JavaScript. `browser_snapshot` will show only the static HTML shell (header, tabs, timestamp) with no rendered cards. `typeof BATCHES` will return `undefined`. This is normal — the dashboard works fine in Chrome/Safari. Verify local dashboards with structural HTML checks instead: count GitHub URLs, check DOCTYPE/script/style tags, validate JSON data integrity. Do not report a non-rendering local file as a build failure.

## Verification Checklist

- [ ] **Taste bundle loaded** — `claude-design` and `popular-web-designs` loaded in Phase 1 before any design decisions.
- [ ] Blueprint brief written with filename, content, visual system, repo, and Vercel project name. Design direction is locked here.
- [ ] `claude --version` succeeded (if Claude is the active build engine).
- [ ] `vercel whoami` succeeded.
- [ ] `gh auth status` succeeded.
- [ ] Output directory exists.
- [ ] Build engine wrote the requested file.
- [ ] File exists at `~/Desktop/hermes_builds/<filename>` (or repo path for existing site edits).
- [ ] **Em dash gate:** auto-strip `\u2014` and `&mdash;` from the output file. Confirm count is zero before continuing.
- [ ] For existing website repos: file content verified with `grep` for expected text before deploying.
- [ ] For HTML decks, `html-slide-deck` has been followed and mobile was checked at `375 x 812` before delivery.
- [ ] For HTML decks, navigation arrows, dots, counter, keyboard, and swipe controls work.
- [ ] For HTML decks, no text overflow, clipping, logo overlap, or mobile nav crowding remains.
- [ ] If using Local artifact mode, export the PDF from the final HTML and verify both local files exist.
- [ ] If deploying via Vercel CLI, `vercel --prod --yes` succeeded and aliased correctly.
- [ ] If deploying via git push (from user's terminal, not sandbox), push succeeded and Vercel auto-deployed.
- [ ] Final response includes the correct artifact paths or URLs for the mode used.
