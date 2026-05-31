---
name: notebooklm
description: Complete API for Google NotebookLM - full programmatic access including features not in the web UI. Create notebooks, add sources, generate all artifact types, download in multiple formats. Activates on explicit /notebooklm or intent like "create a podcast about X"
---
<!-- notebooklm-py v0.6.0, skill updated 31 May 2026: video rate limit + Telegram media upload pitfalls -->
# NotebookLM Automation

Complete programmatic access to Google NotebookLM—including capabilities not exposed in the web UI. Create notebooks, add sources (URLs, YouTube, PDFs, audio, video, images), chat with content, generate all artifact types, and download results in multiple formats.

> **Session notes:** See `references/session-notes.md` for login fix (Playwright/Chromium crash on macOS) and the audio+video generation pattern for course content delivery via Telegram.

## Installation

**Using uv (recommended on macOS):**
```bash
uv tool install "notebooklm-py[browser]"
```

**Upgrade existing install:**
```bash
cd /tmp && UV_TOOL_DIR=$HOME/.local/share/uv/tools uv tool install "notebooklm-py[browser]" --force
```

**From PyPI:**
```bash
pip install "notebooklm-py[browser]"
```

**Skill install methods:**

- `notebooklm skill install` installs this skill into the supported local agent directories managed by the CLI.
- `npx skills add teng-lin/notebooklm-py` installs this skill from the GitHub repository into compatible agent skill directories.
- If you are already reading this file inside an agent skill directory, the skill is already installed. You only need the Python package and authentication below.

**CLI-managed install:**
```bash
notebooklm skill install
```

## Prerequisites

**IMPORTANT:** Before using any command, you MUST authenticate:

```bash
notebooklm login          # Opens browser for Google OAuth
notebooklm list           # Verify authentication works
```

If commands fail with authentication errors, re-run `notebooklm login`.

### Jared stack sync rule

When Jared says NotebookLM was updated in Claude Code, do not assume Hermes or Nelly inherited that change.

Use this verification and alignment sequence:

1. Check the live CLI first:
   ```bash
   notebooklm --version
   notebooklm auth check
   notebooklm list
   ```
2. Compare the Hermes skill copy against the Claude-managed canonical copy when both exist:
   - `~/.claude/skills/notebooklm/SKILL.md`
   - `~/.hermes/skills/productivity/notebooklm/SKILL.md`
3. If Claude's copy is newer or version-matched to the live CLI, back up the Hermes copy and replace it from the Claude copy.
4. Restart the `nellynotebook` gateway after replacing the Hermes skill so new Nelly sessions pick up the updated instructions.
5. Verify Nelly end-to-end with a real NotebookLM command through the `nellynotebook` profile, not just the default shell.

Pitfall: updating the NotebookLM skill in Claude Code does not automatically update Hermes. Jared's stack can drift unless Hermes is re-synced deliberately.

### CI/CD, Multiple Accounts, and Parallel Agents

For automated environments, multiple accounts, or parallel agent workflows:

| Variable | Purpose |
|----------|---------|
| `NOTEBOOKLM_HOME` | Custom config directory (default: `~/.notebooklm`) |
| `NOTEBOOKLM_PROFILE` | Active profile name (default: `default`) |
| `NOTEBOOKLM_AUTH_JSON` | Inline auth JSON - no file writes needed |

**CI/CD setup:** Set `NOTEBOOKLM_AUTH_JSON` from a secret containing your `storage_state.json` contents.

**Multiple accounts:** Use named profiles (`notebooklm profile create work`, then `notebooklm -p work login`). Alternatively, use different `NOTEBOOKLM_HOME` directories per account.

**Parallel agents:** The CLI stores notebook context per profile (`~/.notebooklm/profiles/<profile>/context.json`, with a legacy fallback to `~/.notebooklm/context.json` for the implicit default profile). Multiple concurrent agents that share a profile and use `notebooklm use` can overwrite each other's context — use one of the isolation strategies below.

**Solutions for parallel workflows:**
1. **Always use explicit notebook ID** (recommended): Pass `-n <notebook_id>` (for `wait`/`download` commands) or `--notebook <notebook_id>` (for others) instead of relying on `use`
2. **Per-agent isolation via profiles:** `export NOTEBOOKLM_PROFILE=agent-$ID` (each profile gets its own context file)
3. **Per-agent isolation via home:** Set unique `NOTEBOOKLM_HOME` per agent: `export NOTEBOOKLM_HOME=/tmp/agent-$ID`
4. **Use full UUIDs:** Avoid partial IDs in automation (they can become ambiguous)

## Agent Setup Verification

Before starting workflows, verify the CLI is ready:

1. `notebooklm status` → Should show "Authenticated as: email@..."
2. `notebooklm list --json` → Should return valid JSON (even if empty notebooks list)
3. If either fails → Run `notebooklm login`

## When This Skill Activates

**Explicit:** User says "/notebooklm", "use notebooklm", or mentions the tool by name

**Intent detection:** Recognize requests like:
- "Create a podcast about [topic]"
- "Summarize these URLs/documents"
- "Generate a quiz from my research"
- "Turn this into an audio overview"
- "Create flashcards for studying"
- "Generate a video explainer"
- "Make an infographic"
- "Create a mind map of the concepts"
- "Download the quiz as markdown"
- "Add these sources to NotebookLM"

## Autonomy Rules

**Run automatically (no confirmation):**
- `notebooklm status` - check context
- `notebooklm auth check` - diagnose auth issues
- `notebooklm list` - list notebooks
- `notebooklm source list` - list sources
- `notebooklm artifact list` - list artifacts
- `notebooklm language list` - list supported languages
- `notebooklm language get` - get current language
- `notebooklm language set` - set language (global setting)
- `notebooklm artifact wait` - wait for artifact completion (in subagent context)
- `notebooklm source wait` - wait for source processing (in subagent context)
- `notebooklm research status` - check research status
- `notebooklm research wait` - wait for research (in subagent context)
- `notebooklm use <id>` - set context (⚠️ SINGLE-AGENT ONLY - use `-n` flag in parallel workflows)
- `notebooklm create` - create notebook
- `notebooklm ask "..."` - chat queries (without `--save-as-note`)
- `notebooklm history` - display conversation history (read-only)
- `notebooklm source add` - add sources
- `notebooklm profile list` - list profiles
- `notebooklm profile create` - create profile
- `notebooklm profile switch` - switch active profile
- `notebooklm doctor` - check environment health

**Ask before running:**
- `notebooklm delete` - destructive
- `notebooklm generate *` - long-running, may fail
- `notebooklm download *` - writes to filesystem
- `notebooklm artifact wait` - long-running (when in main conversation)
- `notebooklm source wait` - long-running (when in main conversation)
- `notebooklm research wait` - long-running (when in main conversation)
- `notebooklm ask "..." --save-as-note` - writes a note
- `notebooklm history --save` - writes a note

## Quick Reference

| Task | Command |
|------|---------|
| Authenticate | `notebooklm login` |
| Diagnose auth issues | `notebooklm auth check` |
| Diagnose auth (full) | `notebooklm auth check --test` |
| One-shot cookie keepalive (for cron) | `notebooklm auth refresh --quiet` |
| List notebooks | `notebooklm list` |
| Create notebook | `notebooklm create "Title"` |
| Set context | `notebooklm use <notebook_id>` |
| Show context | `notebooklm status` |
| Add URL source | `notebooklm source add "https://..."` |
| Add file | `notebooklm source add ./file.pdf` |
| Add YouTube | `notebooklm source add "https://youtube.com/..."` |
| List sources | `notebooklm source list` |
| Delete source by ID | `notebooklm source delete <source_id>` |
| Delete source by exact title | `notebooklm source delete-by-title "Exact Title"` |
| Wait for source processing | `notebooklm source wait <source_id>` |
| Web research (fast) | `notebooklm source add-research "query"` |
| Web research (deep) | `notebooklm source add-research "query" --mode deep --no-wait` |
| Check research status | `notebooklm research status` |
| Wait for research | `notebooklm research wait --import-all` |
| Chat | `notebooklm ask "question"` |
| Chat (specific sources) | `notebooklm ask "question" -s src_id1 -s src_id2` |
| Chat (with references) | `notebooklm ask "question" --json` |
| Chat (save answer as note) | `notebooklm ask "question" --save-as-note` |
| Chat (save with title) | `notebooklm ask "question" --save-as-note --note-title "Title"` |
| Show conversation history | `notebooklm history` |
| Save all history as note | `notebooklm history --save` |
| Continue specific conversation | `notebooklm ask "question" -c <conversation_id>` |
| Save history with title | `notebooklm history --save --note-title "My Research"` |
| Get source fulltext | `notebooklm source fulltext <source_id>` |
| Get source guide | `notebooklm source guide <source_id>` |
| Generate podcast | `notebooklm generate audio "instructions"` |
| Generate podcast (JSON) | `notebooklm generate audio --json` |
| Generate podcast (specific sources) | `notebooklm generate audio -s src_id1 -s src_id2` |
| Generate video | `notebooklm generate video "instructions"` |
| Generate report | `notebooklm generate report --format briefing-doc` |
| Generate report (append instructions) | `notebooklm generate report --format study-guide --append "Target audience: beginners"` |
| Generate quiz | `notebooklm generate quiz` |
| Revise a slide | `notebooklm generate revise-slide "prompt" --artifact <id> --slide 0` |
| Check artifact status | `notebooklm artifact list` |
| Wait for completion | `notebooklm artifact wait <artifact_id>` |
| Download audio | `notebooklm download audio ./output.mp3` |
| Download video | `notebooklm download video ./output.mp4` |
| Download slide deck (PDF) | `notebooklm download slide-deck ./slides.pdf` |
| Download slide deck (PPTX) | `notebooklm download slide-deck ./slides.pptx --format pptx` |
| Download report | `notebooklm download report ./report.md` |
| Download mind map | `notebooklm download mind-map ./map.json` |
| Download data table | `notebooklm download data-table ./data.csv` |
| Download quiz | `notebooklm download quiz quiz.json` |
| Download quiz (markdown) | `notebooklm download quiz --format markdown quiz.md` |
| Download flashcards | `notebooklm download flashcards cards.json` |
| Download flashcards (markdown) | `notebooklm download flashcards --format markdown cards.md` |
| Delete notebook | `notebooklm notebook delete <id>` |
| List languages | `notebooklm language list` |
| Get language | `notebooklm language get` |
| Set language | `notebooklm language set zh_Hans` |
| List profiles | `notebooklm profile list` |
| Create profile | `notebooklm profile create work` |
| Switch profile | `notebooklm profile switch work` |
| Delete profile | `notebooklm profile delete old` |
| Rename profile | `notebooklm profile rename old new` |
| Use profile (one-off) | `notebooklm -p work list` |
| Health check | `notebooklm doctor` |
| Health check (auto-fix) | `notebooklm doctor --fix` |

**Parallel safety:** Use explicit notebook IDs in parallel workflows. Commands supporting `-n` shorthand: `artifact wait`, `source wait`, `research wait/status`, `download *`. Download commands also support `-a/--artifact`. Other commands use `--notebook`. For chat, use `-c <conversation_id>` to target a specific conversation.

**Partial IDs:** Use first 6+ characters of UUIDs. Must be unique prefix (fails if ambiguous). Works for ID-based commands such as `use`, `source delete`, and `wait`. For exact source-title deletion, use `source delete-by-title "Title"`. For automation, prefer full UUIDs to avoid ambiguity.

## Command Output Formats

Commands with `--json` return structured data for parsing:

**Create notebook:**
```bash
$ notebooklm create "Research" --json
{"notebook": {"id": "abc123de-...", "title": "Research", "created_at": null}}
# parse with: jq -r .notebook.id
```

**Add source:**
```bash
$ notebooklm source add "https://example.com" --json
{"source": {"id": "def456...", "title": "Example", "type": "SourceType.WEB_PAGE", "url": "https://example.com"}}
# parse with: jq -r .source.id
# Note: no `status` field on add — use `source list --json` or `source wait` to check processing state.
```

**Generate artifact:**
```bash
$ notebooklm generate audio "Focus on key points" --json
{"task_id": "xyz789...", "status": "pending"}
# When run with --wait, completed status also includes a `url` field.
```

**Chat with references:**
```bash
$ notebooklm ask "What is X?" --json
{"answer": "X is... [1] [2]", "conversation_id": "...", "turn_number": 1, "is_follow_up": false, "references": [{"source_id": "abc123...", "citation_number": 1, "cited_text": "Relevant passage from source..."}, {"source_id": "def456...", "citation_number": 2, "cited_text": "Another passage..."}]}
```

**Source fulltext (get indexed content):**
```bash
$ notebooklm source fulltext <source_id> --json
{"source_id": "...", "title": "...", "content": "Full indexed text...", "_type_code": null, "url": null, "char_count": 12345}
```

**Understanding citations:** The `cited_text` in references is often a snippet or section header, not the full quoted passage. The `start_char`/`end_char` positions reference NotebookLM's internal chunked index, not the raw fulltext. Use `SourceFulltext.find_citation_context()` to locate citations:
```python
fulltext = await client.sources.get_fulltext(notebook_id, ref.source_id)
matches = fulltext.find_citation_context(ref.cited_text)  # Returns list[(context, position)]
if matches:
    context, pos = matches[0]  # First match; check len(matches) > 1 for duplicates
```

**Extract IDs:** Singular endpoints wrap their result in an envelope —
parse `.notebook.id` (from `create`), `.source.id` (from `source add`),
or `.task_id` (from `generate *`). The chat `--json` references list uses
`.references[].source_id`.

## Generation Types

All generate commands support:
- `-s, --source` to use specific source(s) instead of all sources
- `--language` to set output language (defaults to configured language or 'en')
- `--json` for machine-readable output (returns `task_id` and `status`)
- `--retry N` to automatically retry on rate limits with exponential backoff

| Type | Command | Options | Download |
|------|---------|---------|----------|
| Podcast | `generate audio` | `--format [deep-dive\|brief\|critique\|debate]`, `--length [short\|default\|long]` | .mp3 |
| Video | `generate video` | `--format [explainer\|brief]`, `--style [auto\|classic\|whiteboard\|kawaii\|anime\|watercolor\|retro-print\|heritage\|paper-craft]` | .mp4 |
| Slide Deck | `generate slide-deck` | `--format [detailed\|presenter]`, `--length [default\|short]` | .pdf / .pptx |
| Slide Revision | `generate revise-slide "prompt" --artifact <id> --slide N` | `--wait`, `--notebook` | *(re-downloads parent deck)* |
| Infographic | `generate infographic` | `--orientation [landscape\|portrait\|square]`, `--detail [concise\|standard\|detailed]`, `--style [auto\|sketch-note\|professional\|bento-grid\|editorial\|instructional\|bricks\|clay\|anime\|kawaii\|scientific]` | .png |
| Report | `generate report` | `--format [briefing-doc\|study-guide\|blog-post\|custom]`, `--append "extra instructions"` (¹) | .md |
| Mind Map | `generate mind-map` | *(sync, instant)* | .json |
| Data Table | `generate data-table` | description required | .csv |
| Quiz | `generate quiz` | `--difficulty [easy\|medium\|hard]`, `--quantity [fewer\|standard\|more]` | .json/.md/.html |
| Flashcards | `generate flashcards` | `--difficulty [easy\|medium\|hard]`, `--quantity [fewer\|standard\|more]` | .json/.md/.html |

¹ `--append` only customizes the built-in templates. With `--format custom`, pass the prompt as the positional `DESCRIPTION` argument (`notebooklm generate report "PROMPT" --format custom`); `--append` is silently ignored in that mode (the CLI prints a warning).

## Features Beyond the Web UI

These capabilities are available via CLI but not in NotebookLM's web interface:

| Feature | Command | Description |
|---------|---------|-------------|
| **Batch downloads** | `download <type> --all` | Download all artifacts of a type at once |
| **Quiz/Flashcard export** | `download quiz --format json` | Export as JSON, Markdown, or HTML (web UI only shows interactive view) |
| **Mind map extraction** | `download mind-map` | Export hierarchical JSON for visualization tools |
| **Data table export** | `download data-table` | Download structured tables as CSV |
| **Slide deck as PPTX** | `download slide-deck --format pptx` | Download slide deck as editable .pptx (web UI only offers PDF) |
| **Slide revision** | `generate revise-slide "prompt" --artifact <id> --slide N` | Modify individual slides with a natural-language prompt |
| **Report template append** | `generate report --format study-guide --append "..."` | Append custom instructions to built-in format templates without losing the format type |
| **Source fulltext** | `source fulltext <id>` | Retrieve the indexed text content of any source |
| **Save chat to note** | `ask "..." --save-as-note` / `history --save` | Save Q&A answers or conversation history as notebook notes |
| **Programmatic sharing** | `share` commands | Manage sharing permissions without the UI |

## Common Workflows

### Research to Podcast (Interactive)
**Time:** 5-10 minutes total

1. `notebooklm create "Research: [topic]"` — *if fails: check auth with `notebooklm login`*
2. `notebooklm source add` for each URL/document — *if one fails: log warning, continue with others*
3. Wait for sources: `notebooklm source list --json` until all status=READY — *required before generation*
4. `notebooklm generate audio "Focus on [specific angle]"` (confirm when asked) — *if rate limited: wait 5 min, retry once*
5. Note the artifact ID returned
6. Check `notebooklm artifact list` later for status
7. `notebooklm download audio ./podcast.mp3` when complete (confirm when asked)

### Research to Podcast (Automated with Subagent)
**Time:** 5-10 minutes, but continues in background

When user wants full automation (generate and download when ready):

1. Create notebook and add sources as usual
2. Wait for sources to be ready (use `source wait` or check `source list --json`)
3. Run `notebooklm generate audio "..." --json` → parse `artifact_id` from output
4. **Spawn a background agent** using Task tool:
   ```
   Task(
     prompt="Wait for artifact {artifact_id} in notebook {notebook_id} to complete, then download.
             Use: notebooklm artifact wait {artifact_id} -n {notebook_id} --timeout 600
             Then: notebooklm download audio ./podcast.mp3 -a {artifact_id} -n {notebook_id}",
     subagent_type="general-purpose"
   )
   ```
5. Main conversation continues while agent waits

**Error handling in subagent:**
- If `artifact wait` returns exit code 2 (timeout): Report timeout, suggest checking `artifact list`
- If download fails: Check if artifact status is COMPLETED first

**Benefits:** Non-blocking, user can do other work, automatic download on completion

### Document Analysis
**Time:** 1-2 minutes

1. `notebooklm create "Analysis: [project]"`
2. `notebooklm source add ./doc.pdf` (or URLs)
3. `notebooklm ask "Summarize the key points"`
4. `notebooklm ask "What are the main arguments?"`
5. Continue chatting as needed

### Bulk Import
**Time:** Varies by source count

1. `notebooklm create "Collection: [name]"`
2. Add multiple sources:
   ```bash
   notebooklm source add "https://url1.com"
   notebooklm source add "https://url2.com"
   notebooklm source add ./local-file.pdf
   ```
3. `notebooklm source list` to verify

**Source limits:** Varies by plan—Standard: 50, Plus: 100, Pro: 300, Ultra: 600 sources per notebook. See [NotebookLM plans](https://support.google.com/notebooklm/answer/16213268) for details. The CLI does not enforce these limits; they are applied by your NotebookLM account.
**Supported types:** PDFs, YouTube URLs, web URLs, Google Docs, text files, Markdown, Word docs, EPUB, audio files, video files, images

### Bulk Import with Source Waiting (Subagent Pattern)
**Time:** Varies by source count

When adding multiple sources and needing to wait for processing before chat/generation:

1. Add sources with `--json` to capture IDs (parse with `jq -r .source.id`):
   ```bash
   notebooklm source add "https://url1.com" --json  # → {"source": {"id": "abc...", ...}}
   notebooklm source add "https://url2.com" --json  # → {"source": {"id": "def...", ...}}
   ```
2. **Spawn a background agent** to wait for all sources:
   ```
   Task(
     prompt="Wait for sources {source_ids} in notebook {notebook_id} to be ready.
             For each: notebooklm source wait {id} -n {notebook_id} --timeout 120
             Report when all ready or if any fail.",
     subagent_type="general-purpose"
   )
   ```
3. Main conversation continues while agent waits
4. Once sources are ready, proceed with chat or generation

**Why wait for sources?** Sources must be indexed before chat or generation. Takes 10-60 seconds per source.

### Deep Web Research (Subagent Pattern)
**Time:** 2-5 minutes, runs in background

Deep research finds and analyzes web sources on a topic:

1. Create notebook: `notebooklm create "Research: [topic]"`
2. Start deep research (non-blocking):
   ```bash
   notebooklm source add-research "topic query" --mode deep --no-wait
   ```
3. **Spawn a background agent** to wait and import:
   ```
   Task(
     prompt="Wait for research in notebook {notebook_id} to complete and import sources.
             Use: notebooklm research wait -n {notebook_id} --import-all --timeout 300
             Report how many sources were imported.",
     subagent_type="general-purpose"
   )
   ```
4. Main conversation continues while agent waits
5. When agent completes, sources are imported automatically

**Alternative (blocking):** For simple cases, omit `--no-wait`:
```bash
notebooklm source add-research "topic" --mode deep --import-all
# Blocks for up to 5 minutes
```

**When to use each mode:**
- `--mode fast`: Specific topic, quick overview needed (5-10 sources, seconds)
- `--mode deep`: Broad topic, comprehensive analysis needed (20+ sources, 2-5 min)

**Research sources:**
- `--from web`: Search the web (default)
- `--from drive`: Search Google Drive

## Output Style

**Progress updates:** Brief status for each step
- "Creating notebook 'Research: AI'..."
- "Adding source: https://example.com..."
- "Starting audio generation... (task ID: abc123)"

**Fire-and-forget for long operations:**
- Start generation, return artifact ID immediately
- Do NOT poll or wait in main conversation - generation takes 5-45 minutes (see timing table)
- User checks status manually, OR use subagent with `artifact wait`

**JSON output:** Use `--json` flag for machine-readable output:
```bash
notebooklm list --json
notebooklm auth check --json
notebooklm source list --json
notebooklm artifact list --json
```

**JSON schemas (key fields):**

`notebooklm list --json`:
```json
{"notebooks": [{"index": 1, "id": "...", "title": "...", "is_owner": true, "created_at": "..."}], "count": 1}
```

`notebooklm auth check --json`:
```json
{"status": "ok", "checks": {"storage_exists": true, "json_valid": true, "cookies_present": true, "sid_cookie": true, "token_fetch": true}, "details": {"storage_path": "...", "auth_source": "file", "cookies_found": ["SID", "HSID", "..."], "cookie_domains": [".google.com"]}}
```

`notebooklm source list --json`:
```json
{"notebook_id": "...", "notebook_title": "...", "sources": [{"index": 1, "id": "...", "title": "...", "type": "SourceType.WEB_PAGE", "url": "...", "status": "ready|processing|error", "status_id": 1, "created_at": "..."}], "count": 1}
```

`notebooklm artifact list --json`:
```json
{"notebook_id": "...", "notebook_title": "...", "artifacts": [{"index": 1, "id": "...", "title": "...", "type": "Audio", "type_id": 1, "status": "in_progress|pending|completed|unknown", "status_id": 1, "created_at": "..."}], "count": 1}
```

**Status values:**
- Sources: `processing` → `ready` (or `error`)
- Artifacts: `pending` or `in_progress` → `completed` (or `unknown`)

## Pitfalls

- **Video generation rate limits are aggressive.** NotebookLM allows very few video generations per day per account (estimated 2-4). Videos can also fail mid-generation with "artifact was removed from the server" which means the daily quota was hit. When this happens, do NOT retry immediately — the quota will not reset for hours or until the next day. Tell the user and offer the NotebookLM web UI as an alternative (separate quota pool).

- **Audio generation is more reliable** than video but can still hit rate limits in bulk sessions. Generate audio first if both are needed.

- **Source processing takes time.** After adding a source, wait for `source status=ready` before generating artifacts. Use `source wait` to block until ready.

- **Artifacts can disappear.** If an artifact vanishes from `artifact list` during a `artifact wait`, the server removed it — usually a rate limit or quota issue. Do not assume the generation is still happening.

**On failure, offer the user a choice:**
1. Retry the operation
2. Skip and continue with something else
3. Investigate the error

**Error decision tree:**

| Error | Cause | Action |
|-------|-------|--------|
| Auth/cookie error | Session expired | Run `notebooklm auth check` then `notebooklm login --fresh` |
| Playwright/Chromium crash on login | Playwright `[browser]` extra not installed or stale Chromium | Reinstall with `uv tool install "notebooklm-py[browser]" --force`, then `$HOME/.local/share/uv/tools/notebooklm-py/bin/python -m playwright install chromium`, then `notebooklm login --fresh` |
| "No notebook context" | Context not set | Use `-n <id>` or `--notebook <id>` flag (parallel), or `notebooklm use <id>` (single-agent) |
| "No result found for RPC ID" | Rate limiting | Wait 5-10 min, retry |
| `GENERATION_FAILED` | Google rate limit | Wait and retry later |
| "Artifact was removed from the list" | Google daily quota exceeded | Wait 30-60 min. Generate videos one at a time, not in parallel. Fallback: NotebookLM web UI. |
| Download fails | Generation incomplete | Check `artifact list` for status |
| Invalid notebook/source ID | Wrong ID | Run `notebooklm list` to verify |
| RPC protocol error | Google changed APIs | May need CLI update |

## Exit Codes

All commands use consistent exit codes:

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | Continue |
| 1 | Error (not found, processing failed) | Check stderr, see Error Handling |
| 2 | Timeout (wait commands only) | Extend timeout or check status manually |

**Examples:**
- `source wait` returns 1 if source not found or processing failed
- `artifact wait` returns 2 if timeout reached before completion
- `generate` returns 1 if rate limited (check stderr for details)

## Known Limitations

**Rate limiting:** Audio, video, quiz, flashcards, infographic, and slide deck generation may fail due to Google's rate limits. This is an API limitation, not a bug.

**Reliable operations:** These always work:
- Notebooks (list, create, delete, rename)
- Sources (add, list, delete)
- Chat/queries
- Mind-map, study-guide, report, data-table generation
- Audio (podcast) generation — occasional rate limits but generally reliable

**Unreliable operations:** These may fail with rate limiting:
- Video generation — daily account-level quota; audio and video share the same quota pool. Generating multiple videos from the same account in one session frequently hits the limit.
- Quiz and flashcard generation
- Infographic and slide deck generation

**Video generation pitfall (30 May 2026):** Generating videos for multiple notebooks in one session can exhaust the daily quota. When the quota is hit, the artifact is removed from the server list before completion. The CLI reports "artifact was removed from the list by the server." This is not a transient error — it will not resolve by retrying in the same session.
- **Workaround:** Generate one video per session, or spread across multiple sessions separated by several hours, or use the NotebookLM web UI (separate quota from API).
- **Do not:** Attempt to generate more than 2 videos from the same account in a single session. The second one will likely fail.

**Workaround for unreliable operations:**
1. Check status: `notebooklm artifact list`
2. Retry after 5-10 minutes for audio; hours or next day for video
3. Use the NotebookLM web UI as fallback for video
4. Use the NotebookLM web UI as fallback (separate quota)
5. See `references/session-notes.md` for video rate limit and Telegram delivery pitfalls

**Processing times vary significantly.** Use the subagent pattern for long operations:

| Operation | Typical time | Suggested timeout |
|-----------|--------------|-------------------|
| Source processing | 30s - 10 min | 600s |
| Research (fast) | 30s - 2 min | 180s |
| Research (deep) | 15 - 30+ min | 1800s |
| Notes | instant | n/a |
| Mind-map | instant (sync) | n/a |
| Quiz, flashcards | 5 - 15 min | 900s |
| Report, data-table | 5 - 15 min | 900s |
| Audio generation | 10 - 20 min | 1200s |
| Video generation | 15 - 45 min | 2700s |

**Polling intervals:** When checking status manually, poll every 15-30 seconds to avoid excessive API calls.

## Language Configuration

Language setting controls the output language for generated artifacts (audio, video, etc.).

**Important:** Language is a **GLOBAL** setting that affects all notebooks in your account.

```bash
# List all 80+ supported languages with native names
notebooklm language list

# Show current language setting
notebooklm language get

# Set language for artifact generation
notebooklm language set zh_Hans  # Simplified Chinese
notebooklm language set ja       # Japanese
notebooklm language set en       # English (default)
```

**Common language codes:**
| Code | Language |
|------|----------|
| `en` | English |
| `zh_Hans` | 中文（简体） - Simplified Chinese |
| `zh_Hant` | 中文（繁體） - Traditional Chinese |
| `ja` | 日本語 - Japanese |
| `ko` | 한국어 - Korean |
| `es` | Español - Spanish |
| `fr` | Français - French |
| `de` | Deutsch - German |
| `pt_BR` | Português (Brasil) |

**Override per command:** Use `--language` flag on generate commands:
```bash
notebooklm generate audio --language ja   # Japanese podcast
notebooklm generate video --language zh_Hans  # Chinese video
```

**Offline mode:** Use `--local` flag to skip server sync:
```bash
notebooklm language set zh_Hans --local  # Save locally only
notebooklm language get --local  # Read local config only
```

## Troubleshooting

```bash
notebooklm --help              # Main commands
notebooklm auth check          # Diagnose auth issues
notebooklm auth check --test   # Full auth validation with network test
notebooklm notebook --help     # Notebook management
notebooklm source --help       # Source management
notebooklm research --help     # Research status/wait
notebooklm generate --help     # Content generation
notebooklm artifact --help     # Artifact management
notebooklm download --help     # Download content
notebooklm language --help     # Language settings
```

**Login browser crash fix:** If `notebooklm login` fails with `TargetClosedError` (Chromium crashes before you can interact), the persistent browser profile is corrupted. Fix:
```bash
notebooklm login --fresh
```
This clears the cached browser profile and starts a clean session. Always try `--fresh` before reinstalling.

**Chromium version mismatch fix:** If `notebooklm` was upgraded but Playwright browsers are missing or from an old version:
```bash
/Users/jc/.local/share/uv/tools/notebooklm-py/bin/python -m playwright install chromium
```
Then retry `notebooklm login --fresh`. (use `--fresh` flag if browser closes immediately)
**Check version:** `notebooklm --version`
**Refresh a CLI-managed install:** `notebooklm skill install`

## Login Troubleshooting (Playwright / Chromium Crash on macOS)

**Symptom:** `notebooklm login` fails with `TargetClosedError` or browser window opens then immediately closes.
**Cause:** Playwright not installed or stale Chromium binary incompatible with current macOS.

**Fix:**
```bash
# Reinstall with browser extra
cd /tmp && UV_TOOL_DIR=$HOME/.local/share/uv/tools uv tool install "notebooklm-py[browser]" --force

# Install Chromium browser binary
$HOME/.local/share/uv/tools/notebooklm-py/bin/python -m playwright install chromium

# Login with clean profile
notebooklm login --fresh
```

**If `notebooklm doctor` says auth passes but `notebooklm list` returns auth error:** Cookies are stale. Run `notebooklm login --fresh` — do not just retry `notebooklm login`.
**If `notebooklm login --browser chrome` fails with "Playwright not installed":** The `[browser]` extra is missing. Reinstall with it as shown above.
**Note:** `notebooklm login --browser chrome` uses your system Chrome but also requires Playwright. Always install the full `[browser]` extra.

---

## Adding NotebookLM to Cowork (MCP Server + Cloudflare Tunnel)

> **Note:** This section is preserved from a user-supplied skill version. It is not part of the CLI-packaged skill, so re-running `notebooklm skill install` regenerates this file and drops this section. Re-append it if you ever refresh the skill that way.

> **Credit:** This approach was contributed by Daniel at [skool.com/navaigate](https://www.skool.com/navaigate). It supersedes the older cookie-inlining method, which broke whenever Google rotated tokens.

When the user asks to "add this to Cowork", "use this in Cowork", or "make this work in Cowork":

### Why the MCP Approach

Cowork runs on Anthropic's servers. It can't see your local files. It can't run your CLI tools. The old approach of inlining auth cookies into a skill file failed repeatedly because:
- Tokens expire and force a full regeneration cycle
- Google's auth flow can change without warning
- You have to re-upload the skill every time

The MCP pattern solves this cleanly: the CLI stays on your Mac (full filesystem access, full auth), you wrap it in an MCP server, Cloudflare Tunnel gives it a public HTTPS URL, and Cowork connects to that URL like any other MCP server. The agent doesn't know or care where the tool runs, it just works.

### Architecture

```
Claude Code / Cowork
        |  MCP Protocol (SSE)
Cloudflare Tunnel (HTTPS)
        |
Your Mac (localhost:8484)
        |
MCP Server (Python + FastMCP)
        |
NotebookLM CLI -> Google NotebookLM
```

### Prerequisite Check

```bash
# Make sure the local CLI is installed and authenticated first
notebooklm doctor
```

If this fails, complete the Installation and authentication steps above before continuing.

You'll also need a domain on Cloudflare (for the tunnel hostname). If the user doesn't have one yet, they'll need to set that up first at cloudflare.com.

### Step 1: Build the MCP Server

Create the project and set up a Python 3.12 virtual environment:

```bash
mkdir -p ~/notebooklm-mcp && cd ~/notebooklm-mcp
/opt/homebrew/bin/python3.12 -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]" uvicorn
```

Create `~/notebooklm-mcp/server.py`. Every CLI command becomes a decorated Python function. Here's the pattern (extend with as many tools as you want exposed):

```python
import sys, subprocess
from mcp.server.fastmcp import FastMCP

NOTEBOOKLM = "/Users/jc/bin/notebooklm"  # your symlink path
mcp = FastMCP("notebooklm", host="0.0.0.0", port=8484)

def run_cli(*args, timeout=120):
    result = subprocess.run(
        [NOTEBOOKLM, *args],
        capture_output=True, text=True, timeout=timeout
    )
    return result.stdout.strip() or "(no output)"

@mcp.tool()
def notebooklm_list() -> str:
    """List all NotebookLM notebooks."""
    return run_cli("list")

@mcp.tool()
def notebooklm_use(notebook_id: str) -> str:
    """Set the active notebook context."""
    return run_cli("use", notebook_id)

@mcp.tool()
def notebooklm_ask(question: str) -> str:
    """Ask the current notebook a question (RAG query)."""
    return run_cli("ask", question, timeout=120)

@mcp.tool()
def notebooklm_source_add(url_or_path: str) -> str:
    """Add a URL, YouTube link, or local file as a source to the current notebook."""
    return run_cli("source", "add", url_or_path, timeout=180)

@mcp.tool()
def notebooklm_generate_audio(instructions: str = "") -> str:
    """Generate a podcast-style audio overview."""
    args = ["generate", "audio"]
    if instructions:
        args.append(instructions)
    return run_cli(*args, timeout=600)

# Follow this pattern for every command you want to expose,
# create, source list, generate video/report/quiz/flashcards, download, etc.
# See the Quick Reference table above for the full command surface.

if __name__ == "__main__":
    if "--sse" in sys.argv:
        import uvicorn
        app = mcp.sse_app()
        uvicorn.run(app, host="0.0.0.0", port=8484)
    else:
        mcp.run(transport="stdio")
```

The entry point supports two transport modes:
- **SSE mode** (`--sse`): for Cowork via the tunnel. Runs an HTTP server on port 8484.
- **Stdio mode** (default): for local Claude Code. Direct pipe, no network overhead.

Smoke test it:
```bash
source ~/notebooklm-mcp/.venv/bin/activate
python -c "from server import run_cli; print(run_cli('auth', 'check'))"
```

### Step 2: Set Up the Cloudflare Tunnel

Cowork runs on Anthropic's servers. `localhost` means nothing to it. You need a public HTTPS URL pointing at your Mac. Cloudflare Tunnel does this without opening any ports on your router.

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create notebooklm-mcp
cloudflared tunnel route dns notebooklm-mcp mcp-notebooklm.yourdomain.com
```

Create `~/.cloudflared/config-notebooklm-mcp.yml`:

```yaml
tunnel: YOUR_TUNNEL_ID
credentials-file: ~/.cloudflared/YOUR_TUNNEL_ID.json

ingress:
  - hostname: mcp-notebooklm.yourdomain.com
    service: http://localhost:8484
  - service: http_status:404
```

Test it end-to-end:
```bash
# Terminal 1: start the server
cd ~/notebooklm-mcp && source .venv/bin/activate
python server.py --sse

# Terminal 2: start the tunnel
cloudflared tunnel --config ~/.cloudflared/config-notebooklm-mcp.yml run notebooklm-mcp

# Terminal 3: verify
curl -s https://mcp-notebooklm.yourdomain.com/sse | head -3
```

You should see `event: endpoint` with a session ID. That means it's working.

### Step 3: Auto-Start on Boot (macOS Launch Agents)

You don't want to manually start two processes every time you turn on your Mac. Create two Launch Agents:

**MCP Server**: `~/Library/LaunchAgents/dev.navaigate.notebooklm-mcp.plist`
Points to `.venv/bin/python server.py --sse`. Set `RunAtLoad` and `KeepAlive` to `true`.

**Tunnel**: `~/Library/LaunchAgents/dev.navaigate.notebooklm-tunnel.plist`
Points to `cloudflared tunnel run` with the config file. Same flags.

Load them once. They persist across reboots, and macOS restarts either process automatically if it crashes:

```bash
launchctl load ~/Library/LaunchAgents/dev.navaigate.notebooklm-mcp.plist
launchctl load ~/Library/LaunchAgents/dev.navaigate.notebooklm-tunnel.plist
```

### Step 4: Connect to Cowork

1. Open Cowork and click the **+** icon
2. Go to **Connectors -> Add connection -> Add custom connector**
3. Enter: `https://mcp-notebooklm.yourdomain.com/sse`
4. Click **Add**

The NotebookLM tools appear immediately. Prompt naturally:

> "List my NotebookLM notebooks"
> "Switch to my AI Brain notebook and tell me the last 3 entries"
> "Ask my AI Brain: what were the key decisions from last week?"
> "Generate a podcast from my current notebook"

### Step 5: Local Claude Code Setup (Stdio Transport)

For terminal sessions you don't need the tunnel. Add the MCP server to `~/.claude/settings.json` using stdio transport:

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "/Users/jc/notebooklm-mcp/.venv/bin/python",
      "args": ["/Users/jc/notebooklm-mcp/server.py"]
    }
  }
}
```

Same server, different transport. The tools work identically, local sessions just skip the network hop.

### MCP Troubleshooting

| Symptom | Fix |
|---|---|
| Auth expired | Run `notebooklm login` locally. The MCP server picks up new tokens automatically, no restart needed. |
| Server not responding | `lsof -i :8484` to check the port, `tail ~/notebooklm-mcp/mcp-server.log` for errors, then `launchctl kickstart -k gui/$(id -u)/dev.navaigate.notebooklm-mcp`. |
| Tunnel down | `cloudflared tunnel info notebooklm-mcp`. `KeepAlive` usually restarts it automatically. |
| Cowork says "can't reach server" | Verify with `curl -s https://mcp-notebooklm.yourdomain.com/sse \| head -3`. If that works, remove and re-add the connector in Cowork. |

### Why This Pattern Generalizes

Local MCP server + Cloudflare Tunnel isn't just for NotebookLM. Any CLI tool, any local service, any API that needs local credentials can be wrapped as an MCP server and made available to Cowork the same way. Once you've done it once, you can do it for anything.

### Resources

- NotebookLM CLI Skill for Claude Code: [github.com/skyremote/claude-code-notebooklm-skills](https://github.com/skyremote/claude-code-notebooklm-skills)
- notebooklm-py (CLI tool): [github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
- MCP Python SDK: [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
- Cloudflare Tunnel docs: [developers.cloudflare.com/cloudflare-one/connections/connect-networks](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks)
