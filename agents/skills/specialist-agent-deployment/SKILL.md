---
name: specialist-agent-deployment
category: hermes
description: Deploy and maintain profile-backed specialist agents by executing the full wiring directly, including SOUL setup, profile config, gateways, Telegram bot attachment, and live verification.
tags: [telegram, bots, agents, deployment, handler]
---

# Specialist Agent Deployment

When the user wants a new specialist agent made live, **execute the full wiring yourself** using tools. Do not give the user a list of manual steps.

This skill is the class-level umbrella for **profile-backed specialist-agent deployment**: creating or updating Hermes profiles, wiring canonical SOUL files, configuring platform credentials, starting or restarting the correct gateway or runtime, and verifying end-to-end behavior. Telegram is the most common transport, but the same deployment pattern applies to any specialist profile that needs to be brought live.

## Core Principle
User explicitly prefers the agent to "just make it work" rather than being asked to run commands, edit files, or configure things themselves.

## When to Use
- New specialist agent/profile needs to be created or cloned
- A canonical SOUL file exists in Obsidian and must be wired into the profile
- A Telegram bot created via BotFather needs to be attached to a profile
- A specialist profile's `.env`, gateway, or MCP setup needs to be fixed
- An existing specialist agent needs to be updated, restarted, or verified after configuration changes

## Default deployment pattern
1. Identify the exact Hermes profile name to use.
2. Create or clone the profile if needed.
3. Wire the specialist's canonical `SOUL.md`, preferably by linking the profile SOUL to the Obsidian source of truth.
4. Put platform-specific secrets in the **profile-local** `.env`, not the default profile.
5. Start or restart the **profile gateway** and verify the agent with a real end-to-end probe.
6. Only fall back to a custom handler script when the normal profile gateway path is unavailable or explicitly required.

## Execution standard
- Do the file edits, environment updates, restarts, and verification directly.
- Prefer profile-backed gateways over ad hoc polling scripts.
- When the user says a specialist SOUL was updated, verify the canonical source file first and confirm any stated backup path exists before treating the update as landed.
- Do not assume the Hermes profile is implemented as a symlink at a guessed path. Check the actual profile wiring before reporting profile-link state.
- Separate verification into **soul ready**, **profile brain works**, **gateway loaded**, and **live on Telegram/transport**. See `references/profile-brain-vs-live-transport-verification.md`.
- For fresh Telegram bots, verify the BotFather token with `getMe`, restart the profile gateway, then recognise `Bad Request: chat not found` as the normal sign that the user has not pressed **Start** in the new bot chat yet. See `references/profile-telegram-bot-verification.md`.
- Verify with a live identity or reply test before claiming the specialist is fully ready.
- Report the concrete profile, source-of-truth SOUL path, gateway state, and verification result.

## Handler fallback
Custom handler scripts are a fallback path, not the default. Use them only when a profile gateway cannot satisfy the requirement. If a handler is required, keep the handler-specific recipe in references instead of making the main skill narrowly about one session's implementation.

## Production routing patterns

### Kanban governance for specialist agents

For the default Jared ecosystem rule set, see `references/kanban-governance-for-specialist-agents.md`.

For the applied Brock-led Kanban governance pattern, specialist soul snippets, config pattern, readiness test, and Telegram workflow examples, see `references/kanban-governance-jared-agent-ecosystem.md`.

Default rule: **Brock is the Kanban orchestrator. Specialists are workers. Only Jared and Brock create cross-agent workflows by default.** Specialists should work their assigned lane and escalate to Brock with a comment or block if another specialist is needed.

Before enabling Kanban workflows across Bob, Nelly, Lara, Sam, Polly, or Harry, add a Kanban operating block to the relevant SOUL files. Include: task card is source of truth, read full context first, stay inside lane, do not create cross-agent child tasks unless Jared or Brock explicitly says so, and complete with a structured handoff covering work done, files changed, checks run, risks, and next action.

Use `references/kanban-governance-for-specialist-agents.md` for the exact Brock block, generic specialist block, specialist-specific additions, Telegram `/kanban` start patterns, and the recommended first Bob-only test workflow.

### Lara (Learning Design): full-package vs single-sheet, sub-agent routing, model migration

Lara defaults to a single-sheet Excel output. When the user wants her complete learning design methodology (Bloom's outcomes, Tell-Show-Do-Check, activities, assessment, materials, facilitator brief), explicitly request "your full standard learning design package with all the tabs you normally include." Specify the exact tabs: Cover, Outcomes, Session Plan, Activities, Assessment, Materials, Facilitator Brief. Without this instruction, Lara produces a minimal single-sheet workbook. See `references/lara-full-package-pattern.md`.

**Lara's sub-agents (3):** Lara spawns Rory_Research (deep topic research, source validation, pre-design scan), Ava_Activities (creative activity design, pattern library, two-option constraint), and Eva_Evaluation (Kirkpatrick planning, assessment design, manager reinforcement). Soul files at `/Users/jc/Desktop/Obsidian/Agents/Rory_Research-Soul.md`, `Ava_Activities-Soul.md`, `Eva_Evaluation-Soul.md`. Sub-agents produce raw material; Lara owns the final design integration. See `references/agent-sub-agent-structure-pattern.md` in performos-website-builds for the full pattern.

**Model migration (27 May 2026):** Lara was migrated from gpt-5.4 / openai-codex to deepseek-v4-pro / deepseek. Symptoms: `Provider authentication failed` on gateway start. Root cause: openai-codex OAuth token expired or gpt-5.4 model unavailable. Fix: update model.default, model.provider, model.base_url in profile config.yaml. Copy DEEPSEEK_API_KEY from default profile if not present. Restart gateway.

### File delivery after specialist production
After any specialist agent produces a file, deliver it in-chat via MEDIA or send_message. Do not just tell the user the file path. The user expects files to appear in the conversation. Already captured in memory; reinforced here for routing agents.

### General agent routing
Prefer `hermes --profile <profile> chat -q "..." --quiet` over send_message for agent-to-agent routing. send_message only works when the agent has a registered Telegram bot and the chat is known. The terminal path works for all profiles.

## Pitfalls to Avoid
- Never output long step-by-step instructions for the user to follow.
- Never ask the user to run commands unless absolutely unavoidable.
- Do not put specialist bot tokens only in the default Hermes `.env`.
- Do not assume profile names match bot names or Obsidian note names.
- Do not claim the agent is live until an end-to-end reply or identity probe succeeds.
- Do not default to custom handlers when the standard profile gateway will work.
- **execute_code read_file corrupts files on writeback.** `read_file()` in execute_code returns content with line-number prefixes baked in (e.g. `     1|content`). Writing that content back via `write_file()` bakes the prefixes into the file. Every subsequent read compounds the corruption. Fix: strip with `re.sub(r'^ +\d+\|', '', content, flags=re.MULTILINE)` before any write_file. Prefer `patch()` for targeted edits over `write_file()` when the file already exists — it avoids this class of bug entirely. See `references/execute-code-file-corruption-pitfall.md`.

## References
- `references/atticus-handler-pattern.md` for the handler fallback template when a custom polling path is truly required.
- `references/kanban-governance-for-specialist-agents.md` for the Brock-as-Kanban-orchestrator model, specialist SOUL blocks, Telegram `/kanban` start patterns, and first test workflow.
- `references/brock-agent-to-agent-routing.md` for the Brock-as-router pattern when Jared needs multi-agent pipelines without copy-paste.
- `references/lara-full-package-pattern.md` for triggering Lara's complete multi-tab learning design output.
- `references/execute-code-file-corruption-pitfall.md` for the read_file/write_file line-number corruption bug and fix.
- `references/profile-brain-vs-live-transport-verification.md` for separating soul readiness, local profile brain, gateway state, and real Telegram/live transport verification.
- `references/profile-telegram-bot-verification.md` for BotFather token `getMe` validation, profile-local `.env` wiring, gateway log checks, and the Telegram **Start** / `chat not found` pitfall.
- `references/seo-content-pipeline.md` for the full Serge→Polly→Bob SEO content production pipeline (keyword brief to HTML delivery).

## Full deployment sequence (Telegram bot)

When deploying a new specialist agent with a BotFather-created Telegram bot, run this sequence directly:

1. **Create profile:**
```bash
hermes profile create <profile> --clone-from default
```

2. **Wire canonical SOUL** by removing the cloned default and symlinking to Obsidian:
```bash
rm ~/.hermes/profiles/<profile>/SOUL.md
ln -s /Users/jc/Desktop/Obsidian/Agents/<Agent>_<Role>-Soul.md ~/.hermes/profiles/<profile>/SOUL.md
```

3. **Strip inherited Telegram config** from the cloned .env (the new bot must not use the default bot token):
```bash
sed -i '' '/^TELEGRAM_BOT_TOKEN=/d' ~/.hermes/profiles/<profile>/.env
sed -i '' '/^TELEGRAM_ALLOWED_USERS=/d' ~/.hermes/profiles/<profile>/.env
```

4. **Add the agent's own bot token and allowlist Jared:**
```bash
echo 'TELEGRAM_BOT_TOKEN=<botfather_token>' >> ~/.hermes/profiles/<profile>/.env
echo 'TELEGRAM_ALLOWED_USERS=8647481186' >> ~/.hermes/profiles/<profile>/.env
```

5. **Copy API key** if using a key-based provider like DeepSeek (not needed for OAuth providers):
```bash
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/<profile>/.env || grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/<profile>/.env
```

6. **Verify the bot exists** via Telegram API:
```bash
curl -s "https://api.telegram.org/bot<token>/getMe" | python3 -m json.tool
```

7. **Identity probe** before starting the gateway:
```bash
hermes --profile <profile> chat -q "Who are you? Reply in two sentences." --quiet
```

8. **Install and start the gateway service:**
```bash
hermes --profile <profile> gateway install
hermes --profile <profile> gateway start
```

9. **Verify gateway is loaded and Telegram connected:**
```bash
hermes --profile <profile> gateway status
tail -n 80 ~/.hermes/profiles/<profile>/logs/gateway.log
```
Look for `Connected to Telegram (polling mode)` and `✓ telegram connected`. If a proactive Telegram `sendMessage` returns `Bad Request: chat not found`, tell the user to open the bot and press **Start**, then run the end-to-end test again. That is a Telegram first-contact rule, not a Hermes failure.

## Model migration: openai-codex timeout → DeepSeek

When a profile on gpt-5.4/openai-codex starts timing out silently (60s+ CLI probe with no response, curator-review thread stuck in error log), switch it to DeepSeek. This is distinct from the DeepSeek silent-stop issue (which affects heavy-context build workflows).

**Symptoms:** CLI probe times out after 60s. Error log shows `Non-streaming API call timed out after 1953s with no response`. Gateway may start cleanly and show as loaded, but the agent cannot respond to any message. The curator-review background thread is often the canary.

**Fix:**
```bash
hermes --profile <profile> config set model.default "deepseek-v4-pro"
hermes --profile <profile> config set model.provider "deepseek"
hermes --profile <profile> config set model.base_url "https://api.deepseek.com/v1"
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/<profile>/.env || grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/<profile>/.env
hermes --profile <profile> gateway restart
```

**Pitfall:** The API key lives in the default `.env`. Profiles do not inherit it. The 401 error (`Your api key: ****ired is invalid`) means the key was not copied. The fix is always the same: copy the key and restart the gateway.

**DeepSeek silent-stop (separate from openai-codex timeout):** On heavy-context build/orchestration workflows (Bob delegating to Dexter, multi-skill loads), DeepSeek may return empty after a series of tool calls. The agent stalls mid-workflow without an error. The fix is to simplify the prompt — fewer skills loaded, delegate first then stop researching. If the pattern repeats, the build chief (Bob) may be better on gpt-5.4 for reliability. DeepSeek is fine for shorter specialist queries (Polly reviews, Serge briefs).