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
- Jared wants to move the live Hermes or Claude Code agent ecosystem from one Mac to another, usually to make a Mac mini the always-on host
- Jared wants to switch multiple or all specialist profiles to a local Ollama model for API-cost testing

Reference: for cross-machine MacBook → Mac mini moves, use `references/cross-machine-agent-host-migration.md`.

## Default deployment pattern
1. Identify the exact Hermes profile name to use.
2. Create or clone the profile if needed.
3. Wire the specialist's canonical `SOUL.md`, preferably by linking the profile SOUL to the Obsidian source of truth.
4. Run the post-clone hygiene pass before starting the gateway: strip inherited platform credentials the specialist should not own, disable cloned platforms such as Email or Google Chat unless explicitly wanted, and clear cloned cron jobs unless the user asked for them. See `references/profile-clone-hygiene-and-duplicate-souls.md`.
5. Put platform-specific secrets in the **profile-local** `.env`, not the default profile.
6. Start or restart the **profile gateway** and verify the agent with a real end-to-end probe.
7. Only fall back to a custom handler script when the normal profile gateway path is unavailable or explicitly required.

## Execution standard
- Do the file edits, environment updates, restarts, and verification directly.
- Prefer profile-backed gateways over ad hoc polling scripts.
- When the user says a specialist SOUL was updated, verify the canonical source file first and confirm any stated backup path exists before treating the update as landed.
- Do not assume the Hermes profile is implemented as a symlink at a guessed path. Check the actual profile wiring before reporting profile-link state.
- Separate verification into **soul ready**, **profile brain works**, **gateway loaded**, and **live on Telegram/transport**. See `references/profile-brain-vs-live-transport-verification.md`.
- Treat `Gateway: running` as necessary but not sufficient. A stale gateway process can receive Telegram messages and still fail at agent import/runtime. Check profile brain, token `getMe`, gateway logs, and live transport before declaring the agent online.
- When a specialist gateway is running but Telegram replies fail with an import/runtime error after a Hermes update, restart that profile's gateway process. If `hermes --profile <profile> gateway restart` is blocked because the command is being invoked from inside a gateway session, stop only the target profile's process by matching `hermes_cli.main --profile <profile> gateway run`, then start it again with `hermes --profile <profile> gateway start`. Verify the new log shows `Connected to Telegram (polling mode)` and send or request a live reply test.
- When changing a profile's model/provider and Jared reports Telegram still shows the old provider, verify the Telegram runtime path, not just the CLI brain. A CLI probe can pass while the live Telegram gateway/session footer is stale. See `references/telegram-runtime-model-verification.md`.
- When wiring a specialist profile to OpenAI Codex, remember Codex uses OAuth in profile-local `auth.json`, not an API key in `.env`. Set `model.provider=openai-codex`, `model.default=gpt-5.5`, copy verified Codex auth into the profile if needed, restart the live Telegram gateway, then run both CLI and live transport probes. See `references/codex-wiring-for-specialist-profiles.md`.
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

### Capability install + proof demo for specialist profiles
When Jared says to make sure a specialist agent "has this skill" or asks for "a demo from Bob", treat it as a profile capability deployment. Installing or testing a tool in the current shell is not enough. Verify the target profile can respond, install or copy the capability into the profile skill library where appropriate, then have the specialist produce a small real artifact and independently verify it before reporting success. For HyperFrames specifically, Bob should prove the chain by rendering an MP4, not by describing the workflow. See `references/hyperframes-profile-capability-demo.md`.

### General agent routing
Prefer `hermes --profile <profile> chat -q "..." --quiet` over send_message for agent-to-agent routing. send_message only works when the agent has a registered Telegram bot and the chat is known. The terminal path works for all profiles.

## Gateway stopped — triage before provider debugging

When a specialist agent stops responding on Telegram, the most common failure mode is a **stopped gateway**, not a dead provider or config error. Always check this first.

When **multiple** specialist Telegram bots are silent, use the bulk recovery flow in `references/multi-profile-telegram-outage-recovery.md`: profile list first, gateway status/log scan, token `getMe` mapping, restart stale launchd gateway services, probe each profile brain, then fix any profile-local provider credential drift.

When Jared asks to move a group of profiles from one provider/model to another while leaving selected profiles on a different model, use `references/profile-model-provider-split-refresh.md`: probe the target model first, copy key-based provider credentials into profile-local `.env` files, clear stale base URLs, restart every gateway to drop cached model state, and verify with direct reply probes.

When Jared asks to switch everyone to a local Ollama model for cost testing, run the backup gate first. Back up the sanitized durable profile layer to GitHub before changing providers, then switch profiles, restart gateways, and verify each profile. See `references/global-profile-local-model-trial.md`.

**Quick triage:**

```bash
hermes profile list | grep <profile>
```

If the gateway column shows `stopped` while others show `running`:

```bash
hermes gateway start --profile <profile>
```

Then verify:

```bash
hermes profile list | grep <profile>
```

If the gateway shows `running` and the agent still does not respond, only then move to the provider probe:

```bash
hermes --profile <profile> chat -q "ok" --quiet
```

**Why this order matters:** The CLI probe spins up an ad-hoc session and will succeed even when the gateway is down. This creates a false positive — the profile brain works fine, but Telegram messages never reach it because no gateway is listening. Checking `hermes profile list` first reveals the real problem in one command.

See `references/gateway-stopped-triage.md` for the full diagnostic flow, false-positive pitfall, and common causes.

## Pitfalls to Avoid
- Never output long step-by-step instructions for the user to follow.
- Never ask the user to run commands unless absolutely unavoidable.
- Do not put specialist bot tokens only in the default Hermes `.env`.
- Do not assume profile names match bot names or Obsidian note names.
- Do not claim the agent is live until an end-to-end reply or identity probe succeeds.
- Do not default to custom handlers when the standard profile gateway will work.
- **Do not trust cloned profile state.** A `--clone-all` specialist profile can inherit Email, Google Chat, Telegram home channel, cron jobs, and stale session/runtime history. Strip anything the specialist should not own, clear copied cron jobs, and verify the gateway runs with only the intended platform before calling it ready. See `references/profile-clone-hygiene-and-duplicate-souls.md`.
- **Do not blindly replace duplicate SOUL files.** First check which SOUL the live profile points to. Larger or older files may contain richer logic but stale delivery rules. Merge deliberately into the active canonical SOUL, then restart and probe the profile.
- **Do not start with the provider probe when an agent goes silent on Telegram.** Check `hermes profile list` first. A stopped gateway is the most common cause and the CLI probe will give a false positive. See Gateway stopped triage above.
- **Do not trust `grep -q` for API key presence during model migrations.** A profile `.env` can have a `DEEPSEEK_API_KEY=*** entry with a different, stale, or expired value from a prior experiment. The key EXISTS but is WRONG. Always compare the actual key VALUE against the working default key before declaring it present. See `references/bulk-profile-model-migration.md` for the audit pattern.
- **execute_code read_file corrupts files on writeback.** `read_file()` in execute_code returns content with line-number prefixes baked in (e.g. `     1|content`). Writing that content back via `write_file()` bakes the prefixes into the file. Every subsequent read compounds the corruption. Fix: strip with `re.sub(r'^ +\\d+\\|', '', content, flags=re.MULTILINE)` before any write_file. Prefer `patch()` for targeted edits over `write_file()` when the file already exists — it avoids this class of bug entirely. See `references/execute-code-file-corruption-pitfall.md`.

## NemoClaw Hermes sandbox deployment

When deploying Hermes agents inside NVIDIA NemoClaw/OpenShell sandboxes for client or test use, see `references/nemoclaw-hermes-onboarding-expert.md`. That reference covers:

- The correct quickstart command and wizard sequence (model 1 Nemotron, NOT model 6 GPT-OSS)
- Brev cloud instance quirks (firewall rules, stale process cleanup, port forwarding)
- Restricted vs Balanced policy for Telegram
- Dashboard URL limitations (Hermes alpha gap)
- Three-layer audit architecture
- Enterprise path vs interactive wizard

Do NOT attempt local macOS NemoClaw install — Docker Desktop arm64 cannot pull the sandbox base image. Use a Brev GPU cloud instance or wait for the DGX/MacBook Pro local path.

When the user says "build an agent" in the context of NemoClaw sandboxes, the deploy sequence is different from standard Telegram bot deployment. Use the quickstart command and wizard answers from the reference, not the default profile creation + gateway install flow.

**Repeated port conflict pitfall:** Once the curl installer has installed `nemohermes`, do not keep rerunning the full `curl | bash` installer to recover onboarding. The installer may start or recreate the gateway during its upgrade step, then onboarding reports that the same gateway is blocking 8080/8081. After install, recover with the installed CLI directly: clear stale processes, export `NEMOCLAW_AGENT=hermes` and any `NEMOCLAW_GATEWAY_PORT`, then run `nemohermes onboard --fresh`. If using a non-default gateway port such as 8081, also add the matching UFW rule: `sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8081 proto tcp`.

**Telegram credential collision pitfall:** If onboarding warns that another sandbox uses the same Telegram credential, stop and destroy the old sandbox first. One bot token can only be polled by one sandbox/gateway at a time. Do not continue through that warning for a clean team bot setup.

**Telegram masking and allowlist pitfall:** Inside a NemoClaw Hermes sandbox, `TELEGRAM_BOT_TOKEN=openshell:resolve:env:TELEGRAM_BOT_TOKEN` is correct. It means OpenShell is masking the real token and resolving it at egress. Do not try to paste the real bot token into `/sandbox/.hermes/.env`. If Telegram does not reply, check `TELEGRAM_ALLOWED_USERS`. Jared's current Telegram user ID is `8647481186`; if the sandbox shows a different user ID, rebuild or fix the host-layer onboarding config. The token and allowlist are host/NemoHermes configuration, not something to solve from inside the agent TUI.

**Localhost access pitfall:** For NemoHermes, the reliable browser-access path is the OpenAI-compatible API on port 8642. From the local Mac, forward `8642:8642` with Brev, then open `http://127.0.0.1:8642/v1/models`. Do not append an OpenClaw `#token=` fragment to Hermes URLs. The 18789 dashboard path is unreliable for the Hermes alpha path and should not be the primary success criterion.

## References
- `references/codex-wiring-for-specialist-profiles.md` for switching a profile-backed specialist to OpenAI Codex, handling profile-local OAuth auth, restarting stale Telegram gateways, and separating the specialist brain model from the target sandbox model.
- `references/nemoclaw-hermes-onboarding-expert.md` for NemoClaw Hermes onboarding, cloud instance quirks, model compatibility, audit architecture, enterprise path, and the Neo specialist agent pattern.
- `references/agentos-skill-injection-pattern.md` for injecting PerformOS agent profiles, skills, and memory into client NemoClaw sandboxes — the AgentOS product architecture.
- `references/atticus-handler-pattern.md` for the handler fallback template when a custom polling path is truly required.
- `references/kanban-governance-for-specialist-agents.md` for the Brock-as-Kanban-orchestrator model, specialist SOUL blocks, Telegram `/kanban` start patterns, and first test workflow.
- `references/brock-agent-to-agent-routing.md` for the Brock-as-router pattern when Jared needs multi-agent pipelines without copy-paste.
- `references/agentos-ec2-governance.md` for the Obsidian↔EC2 governance model (source-of-truth vs runtime, sync pipeline, client deliverables, session export).
- `references/lara-full-package-pattern.md` for triggering Lara's complete multi-tab learning design output.
- `references/ollama-ec2-storage.md` for EC2 Ollama model storage management — moving models to data volume, double-nesting fix, ollama user permissions, OLLAMA_MODELS env var, port conflict recovery.
- `references/self-hosted-chat-ui-pitfall.md` for the browser-localhost-vs-server-localhost pitfall, backend proxy pattern, and model pre-warming when serving chat UIs from EC2.
- `references/gateway-stopped-triage.md` for the stopped-gateway diagnostic flow: false-positive CLI probe trap, correct triage order, and common causes.
- `references/multi-profile-telegram-outage-recovery.md` for ecosystem-wide Telegram outages: bulk gateway restart, stale launchd refresh, token `getMe` mapping, profile brain probes, and profile-local provider credential drift fixes.
- `references/profile-model-provider-split-refresh.md` for model/provider split migrations across profiles: target model probes, profile-local provider keys, stale base URL clearing, gateway cache refresh, and direct reply verification.
- `references/bulk-profile-model-migration.md` for the full all-profiles migration pattern: probe, key audit, bulk config update, key mismatch fix, gateway restart, and per-profile verification.
- `references/global-profile-local-model-trial.md` for ecosystem-wide local Ollama model trials: GitHub backup gate, sanitized mirror boundary, local model config, gateway restart, verification, and restore path.
- `references/execute-code-file-corruption-pitfall.md` for the read_file/write_file line-number corruption bug and fix.
- `references/profile-brain-vs-live-transport-verification.md` for separating soul readiness, local profile brain, gateway state, and real Telegram/live transport verification.
- `references/running-gateway-silent-bot.md` for the case where `Gateway: running` is a false positive: profile brain works, token is valid, but inbound Telegram fails due to stale import/runtime errors and needs a target-profile process restart.
- `references/telegram-runtime-model-verification.md` for model/provider changes where CLI probes pass but Telegram still shows the old provider or stale session metadata.
- `references/profile-telegram-bot-verification.md` for BotFather token `getMe` validation, profile-local `.env` wiring, gateway log checks, and the Telegram **Start** / `chat not found` pitfall.
- `references/hyperframes-profile-capability-demo.md` for proving a specialist profile, especially Bob, has a newly installed capability by producing and verifying a real HyperFrames MP4 artifact.
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

5. **Copy API key** if using a key-based provider like DeepSeek or NVIDIA (not needed for OAuth providers):
```bash
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/<profile>/.env || grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/<profile>/.env
```

6. **Change the model** if the specialist should not use the default profile's model:
```bash
hermes --profile <profile> config set model.default "nvidia/nemotron-3-super-120b-a12b"
hermes --profile <profile> config set model.provider "nvidia"
hermes --profile <profile> config set model.base_url "https://integrate.api.nvidia.com/v1"
```

7. **Lock delegation** if the specialist must never spawn sub-agents or route to Bob/Lara/etc.:
```bash
sed -i '' 's/max_spawn_depth: 1/max_spawn_depth: 0/' ~/.hermes/profiles/<profile>/config.yaml
sed -i '' 's/max_concurrent_children: 3/max_concurrent_children: 0/' ~/.hermes/profiles/<profile>/config.yaml
```
This prevents `delegate_task` entirely. Apply for knowledge-only specialists, thinking partners, and domain experts with no build/execution responsibilities.

8. **Verify the bot exists** via Telegram API:
```bash
curl -s "https://api.telegram.org/bot<token>/getMe" | python3 -m json.tool
```

9. **Identity probe** before starting the gateway:
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

**Pitfall:** The API key lives in the default `.env`. Profiles do not inherit it. The 401 error (`Your api key: ****ired is invalid`) means the key was not copied.

**Pitfall — stale key vs missing key:** `grep -q 'DEEPSEEK_API_KEY' || grep ... >>` only checks whether the variable EXISTS in the profile `.env`. It does NOT check whether the value matches the working default key. Six profiles in the 17 June 2026 bulk migration already had `DEEPSEEK_API_KEY=...` entries from prior provider experiments — but the keys were different, stale, or expired. The profiles passed the `grep -q` existence check, then failed with 401 at runtime. **Always audit key VALUES across all profiles, not just key presence.** See `references/bulk-profile-model-migration.md` for the full audit pattern.

## Provider switch: dead key → new provider via config.yaml edit

When a provider key is invalid or dead (401 authentication_error), switch the profile to a working provider by editing the profile `config.yaml` directly. Do not rely on `.env` key alone — the `model.provider` and `model.base_url` in config.yaml control which API is called.

**Symptoms:** `hermes --profile <profile> chat -q "test" --quiet` returns 401 or "invalid api key". Gateway status shows connected but all chat attempts fail.

**Fix pattern (example: DeepSeek dead → OpenRouter owl-alpha):**

```bash
# 1. Edit config.yaml — change model provider
sed -i '' 's/^  default: deepseek-v4-pro/  default: openrouter/owl-alpha/' ~/.hermes/profiles/<profile>/config.yaml
sed -i '' 's/^  provider: deepseek/  provider: openrouter/' ~/.hermes/profiles/<profile>/config.yaml
sed -i '' '/^  base_url: https:\/\/api.deepseek.com\/v1/d' ~/.hermes/profiles/<profile>/config.yaml

# 2. Verify the target provider key exists (unmasked) in the profile .env or default .env
grep "OPENROUTER_API_KEY" ~/.hermes/profiles/<profile>/.env
# If masked (***), copy the real key from the default profile or have the user provide it.

# 3. Quick probe
hermes --profile <profile> chat -q "reply with ok" --quiet
```

**Bob-specific:** Bob's profile is `bobbuilder`. His config.yaml had `model.provider: deepseek` and `model.base_url: https://api.deepseek.com/v1`. After switching to OpenRouter, all three lines (default, provider, base_url) must be updated. The base_url line should be removed entirely — OpenRouter's URL is configured at the system level, not per-profile.

**If OpenRouter key is also masked/placeholder in `.env`:** The user must provide the real key. Do not proceed with a masked key. A masked key (`***`) means the real value is not available to the agent.

**If switching to openai-codex (OAuth):** openai-codex uses OAuth via `hermes auth`, not API keys. The provider value is `openai-codex`. No API key or base_url is needed — remove them from the provider block. The model must be one supported by Codex with a ChatGPT account. **Critical pitfall:** `gpt-4o` returns `"The 'gpt-4o' model is not supported when using Codex with a ChatGPT account"`. Use `gpt-5.5` or another supported model. Always probe with `hermes --profile <profile> chat -q "reply with ok" --quiet` after switching. If the model name is wrong, try the next supported model up.

**Example: Bob switched from DeepSeek to openai-codex (03 June 2026):**
- provider: `openai-codex`
- model: `gpt-5.5`
- base_url: removed (OAuth path, not needed)
- API key: not needed (OAuth)
- Verified: `hermes --profile bobbuilder chat -q "reply with one word: working" -m gpt-5.5 --quiet` returned `working`

**DeepSeek silent-stop (separate from openai-codex timeout):** On heavy-context build/orchestration workflows (Bob delegating to Dexter, multi-skill loads), DeepSeek may return empty after a series of tool calls. The agent stalls mid-workflow without an error. The fix is to simplify the prompt — fewer skills loaded, delegate first then stop researching. If the pattern repeats, the build chief (Bob) may be better on gpt-5.4 for reliability. DeepSeek is fine for shorter specialist queries (Polly reviews, Serge briefs).

## Bulk model migration: all profiles to one provider/model

When Jared asks to update every profile to the same model (e.g. \"all models to DeepSeek Pro\"), use the bulk pattern. Do not migrate one profile at a time.

**Sequence:**

1. Probe the target model first: `hermes --profile default chat -q \"Reply exactly PROBE_OK\" -m <model> --provider <provider> --quiet 2>&1`
2. Verify the provider API key is live in the default `.env` and note its exact last-4 characters.
3. **Audit every profile `.env` for the key.** Do not just check `grep -q` for key presence — compare the key VALUE against the working default. Six profiles in the 17 June 2026 migration had `DEEPSEEK_API_KEY=*** entries with different/stale values from prior experiments. They passed a presence check but failed at runtime with 401.
4. Update `model.default`, `model.provider`, and `model.base_url` in every profile `config.yaml`. Skip local-model profiles (e.g. `localgemma` on `gemma4:e4b`).
5. Fix any key mismatches by copying the working key into the profile `.env`.
6. Restart all running gateways. `hermes gateway restart` can fail on launchd-managed services — fall back to `hermes gateway stop` then `hermes gateway start`.
7. Verify every profile with an identity probe: `hermes --profile <name> chat -q \"Reply exactly <name>_OK\" --quiet 2>&1`. A 401 response means the key copy didn't take or the gateway didn't restart cleanly.
8. Report: profiles updated, skipped, key mismatches fixed, verification results.

Full recipe with audit script: `references/bulk-profile-model-migration.md`.