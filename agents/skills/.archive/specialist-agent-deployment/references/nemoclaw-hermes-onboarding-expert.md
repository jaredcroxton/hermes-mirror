# NemoClaw Hermes — Expert Onboarding Reference

Prepared 14 June 2026 after extensive cloud-instance testing (Brev MASSEDCOMPUTE L40S, 128GB RAM, $1.06/hr).

## The golden rule

**Study the videos first, become an expert, THEN guide.** Do not discover alongside the user on expensive cloud instances. Three reference videos:

1. **Nemotron Labs Demo** (Johnny/Karan, Nous Research) — Custom onboarding scripts, token masking, multi-user sandboxes, PR workflow
2. **DGX Spark Setup** (Patrick Moorhead, NVIDIA) — Exact wizard install with Telegram, Ollama models, dashboard URL, pairing flow, Q&A
3. **NemoClaw Roadmap** (Chris Murphy, NVIDIA) — Alpha status, Hermes experimental, "delightful UX" June/July, multi-tenant Aug/Sep

## The correct quickstart

```bash
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Do NOT use `nemoclaw onboard` without the env var.

If the curl installer has already installed/updated `nemohermes` and then gets stuck in repeated gateway/port errors, **stop rerunning the full curl installer**. The installer starts or upgrades the OpenShell gateway during its own pre-upgrade step, which can make onboarding complain that the same gateway is already occupying the port. In that state, clean the stale process and run the installed CLI directly:

```bash
export PATH="/home/shadeform/.local/bin:$PATH"
export NEMOCLAW_AGENT=hermes
nemohermes onboard --fresh
```

If port 8080 keeps respawning, use an alternate gateway port and open the matching firewall rule:

```bash
export PATH="/home/shadeform/.local/bin:$PATH"
export NEMOCLAW_AGENT=hermes
export NEMOCLAW_GATEWAY_PORT=8081
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8081 proto tcp
nemohermes onboard --fresh
```

## Brev cloud instance quirks

- **L40S GPU:** 48GB VRAM, 70GB RAM, 614GB disk
- **Firewall rule required:** `sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp`. If using `NEMOCLAW_GATEWAY_PORT=8081`, open the same rule for port 8081.
- **Stale processes:** Every interrupted onboard can leave an `openshell` process on the gateway port. First try `sudo killall openshell openshell-gateway`; if it persists, use `sudo lsof -i :8080` or `sudo lsof -i :8081` to identify the PID and `sudo kill -9 <PID>`. If a user service keeps respawning it, run `systemctl --user stop openclaw-gateway.service 2>/dev/null` and `systemctl --user disable openclaw-gateway.service 2>/dev/null`.
- **`brev exec` is non-interactive.** Use `brev shell` for the wizard. `brev exec` cannot handle the onboarding prompts.
- **Port forwarding:** use `brev port-forward <instance-name> -p 8642:8642` for the reliable Hermes OpenAI-compatible API, then open `http://127.0.0.1:8642/v1/models` locally. Use `brev port-forward <instance-name> -p 18789:18789` only if you specifically need to test the dashboard path.
- **Dashboard port:** 18789 (not 9119). 9119 is local-only inside sandbox. Do not append an OpenClaw `#token=` fragment to Hermes URLs. Hermes API clients authenticate with the bearer token from the generated Hermes environment instead of an OpenClaw dashboard URL token.
- **Instance names:** do not reuse stale test instance names from past sessions; always get the current Brev instance name first.

## Wizard answers — correct sequence

| Step | Prompt | Correct answer |
|---|---|---|
| Resume/fresh | `Resume or start fresh?` | **f** |
| Provider | `Choose [1]:` | **1** (NVIDIA Endpoints) |
| API key | Paste key | Your NVIDIA API key |
| Model | `Choose model [1]:` | **1** (Nemotron 3 Super 120B) |
| Sandbox name | `[hermes]:` | Enter (accept default) or use lowercase/hyphen format such as `my-assistant`; no capitals or spaces |
| Apply config | `[Y/n]:` | **y** |
| Messaging | `Press 1-5 to toggle` | **Press 1** (toggles Telegram ON), then Enter |
| Bot token | Paste | Your BotFather token |
| Chat/User ID | Enter | Jared's Telegram user ID is `8647481186`. If the sandbox later shows a different `TELEGRAM_ALLOWED_USERS`, Telegram will not work for Jared. |
| Resource profile | `Choose [6]:` | **6** (no profile / OpenShell defaults) |
| Policy tier | Select | **Balanced** (NOT Restricted — Restricted blocks Telegram) |
| Presets | Toggle | github, nous-web, nous-code, npm, telegram, local-inference |
| Web search | Skip | Not yet supported by Hermes Agent |

## Critical model pitfall

**GPT-OSS 120B (model 6) throws ToolDescription validation errors with Hermes.**

```
Error: 1 validation error for ToolDescription
description Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
```

Use **Nemotron 3 Super 120B (model 1)** instead. Johnny and Patrick both used Nemotron in the demos.

## Restricted vs Balanced policy

- **Restricted** blocks Telegram outbound by default. The `telegram` preset toggling may not override the base tier restriction in practice.
- **Balanced** allows Telegram. Patrick used Balanced.
- Enterprise demo recommended: Balanced with github, nous-web, nous-code, npm, telegram toggled.

## The Real Architecture

The `NEMOCLAW_AGENT=hermes` env var builds an OpenClaw sandbox base with Hermes loaded as an experimental agent type inside. Status shows "Agent: OpenClaw v2026.5.16" — this is correct, not a bug.

- `hermes` command inside sandbox = Hermes TUI (with all tools and skills)
- `openclaw tui` inside sandbox = OpenClaw TUI (for dashboard + pairing flow)
## Telegram configuration traps

Inside the sandbox, a masked `TELEGRAM_BOT_TOKEN` value is expected. That is OpenShell token masking. Do not replace it with the real BotFather token inside `/sandbox/.hermes/.env`. The agent should not see the raw token. OpenShell resolves it at egress.

Check the allowlist instead. Jared's expected value is `TELEGRAM_ALLOWED_USERS=8647481186`.

If the value is not Jared's Telegram user ID (`8647481186`), Telegram direct messages will be ignored or fail. Fix at the NemoHermes/OpenShell host layer, or rebuild the sandbox and enter the correct Telegram user ID during onboarding.

If onboarding warns that another sandbox uses the same Telegram credential, stop and destroy the old sandbox first. One Telegram bot token can only be polled by one sandbox/gateway at a time.

## Enterprise path vs wizardnstead. Jared's expected value is `TELEGRAM_ALLOWED_USERS=8647481186`.

If the value is not Jared's Telegram user ID (`8647481186`), Telegram direct messages will be ignored or fail. Fix at the NemoHermes/OpenShell host layer, or rebuild the sandbox and enter the correct Telegram user ID during onboarding.

If onboarding warns that another sandbox uses the same Telegram credential, stop and destroy the old sandbox first. One Telegram bot token can only be polled by one sandbox/gateway at a time.

## Enterprise path vs wizard

The wizard is a starter tool for single-user setups. The enterprise path uses:

1. Custom onboarding scripts that create sandboxes with env vars pre-loaded
2. OpenShell token masking — agent sees placeholders, real tokens substituted at egress
3. Policy files defined upfront (not chosen from preset list)
4. Multi-user sandbox creation in parallel

## Quick chat verification

```bash
# Connect to sandbox
nemoclaw hermes connect
hermes

# Test inference
curl http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"nvidia/nemotron-3-super-120b-a12b","messages":[{"role":"user","content":"reply ok"}]}'

# Status
nemoclaw hermes status
nemoclaw hermes list
nemoclaw hermes logs --follow
```

## Audit architecture (three layers)

1. **Gateway logs** — every egress attempt, ALLOW/DENY, token substitution, policy changes (`nemoclaw hermes logs --follow`)
2. **Session history** — every prompt, response, tool call, skill load, memory write (`hermes session search`)
3. **Policy audit trail** — versioned, hashed, every change logged (`nemoclaw hermes status`)

## NemoClaw specialist agent pattern (Neo)

For ongoing NemoClaw expertise, create a dedicated specialist agent (like `Neo_NemoClaw`) rather than loading Brock with every detail. The specialist:

- Owns the NemoClaw knowledge domain end-to-end
- Has a canonical soul at `/Users/jc/Desktop/Obsidian/Agents/[name]-soul.md`
- Runs a cron job that monitors NVIDIA's developer channels daily for Hermes/NemoClaw/OpenShell updates
- Can be invoked via `hermes --profile <profile> chat -q "..." --quiet` for cross-agent routing
- Has its own Telegram bot, allowlisted to Jared only, for direct interaction during cloud builds
- Should not delegate to Bob or other specialists unless Jared explicitly changes the role. For narrow domain experts, set delegation depth/concurrency to zero.

**Cron monitoring sources:**
- `docs.nvidia.com/nemoclaw/` — user guide, API docs, release notes
- `github.com/NVIDIA/NemoClaw` — commits, releases, issues
- `youtube.com/@NVIDIADeveloper` — live streams, demos, roadmap updates

**Cron setup:** `0 8 * * *` (daily 8am AEST). The specialist reviews changes, updates its reference knowledge, and reports significant updates to Brock.

**Why this exists:** NemoClaw moves fast (alpha, weekly releases). A dedicated specialist with automated monitoring prevents knowledge drift between sessions.
\n## Cleanup

```bash
# Destroy sandbox
nemoclaw hermes destroy hermes

# Delete instance
brev delete <instance-name>

# Full cleanup on instance
sudo killall openshell openshell-gateway 2>/dev/null
docker rm -f $(docker ps -aq) 2>/dev/null
docker system prune -a -f --volumes 2>/dev/null
rm -rf ~/.local/state/nemoclaw ~/.nemoclaw ~/.local/share/openshell
```
