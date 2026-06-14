# NemoClaw specialist and onboarding lessons

Use this reference when Jared asks to create or deploy a NemoClaw/Hermes specialist agent, or when a specialist will guide NVIDIA NemoClaw sandbox setup.

## Specialist design pattern

For NemoClaw setup, do not overload Brock with all technical detail. Build or use a dedicated specialist such as `Neo_NemoClaw`.

Required specialist traits:
- Dedicated domain: NVIDIA NemoClaw, OpenShell, Hermes sandbox setup, Brev/GPU cloud instances, Telegram setup, policy presets, audit logs.
- Reports to Brock, but does not route sideways to Bob, Lara, Harry, or other specialists.
- Jared-only access by default if exposed via Telegram.
- Use allowlist-based Telegram access.
- Lock delegation in `config.yaml` for this profile:

```yaml
delegation:
  max_spawn_depth: 0
  max_concurrent_children: 0
  orchestrator_enabled: false
```

## Telegram deployment hygiene

When wiring the specialist to Telegram:
- Store the bot token only in that specialist profile's `.env`.
- Do not put bot tokens in memory, soul files, comments, or source-of-truth docs.
- Set `TELEGRAM_ALLOWED_USERS` to Jared's chat ID unless he explicitly wants a group/team bot.
- Verify `getMe` before starting the gateway.
- Restart the gateway and verify Telegram connects in the profile log.
- If a token appears in plain text during chat, treat it as burned after testing and recommend rotation.

## Correct NemoClaw Hermes wizard path

For a fresh cloud test, use the official quickstart:

```bash
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Prompt path Jared expects:
1. License: type the full word `yes`, not `y`.
2. Resume/fresh: `f` for fresh.
3. Provider: `1` for NVIDIA Endpoints.
4. Model: `1` for Nemotron 3 Super 120B.
5. Sandbox name: press Enter for `hermes` unless there is a specific client/user name.
6. Apply config: `y`.
7. Messaging: press `1` to toggle Telegram on, then Enter. Pressing Enter alone skips messaging.
8. Telegram bot token: paste the bot token.
9. Telegram chat ID: use Jared's chat ID or the target team/group ID.
10. Reply only when @mentioned: `Y` for any group/team use.
11. Resource profile: usually `6` for no profile/OpenShell defaults unless a specific resource cap is needed.
12. Policy tier: `Balanced` for a functional demo. Restricted is useful for enterprise stress testing, but it can block needed egress.
13. Presets: ensure Telegram, NVIDIA, nous-code, nous-web, GitHub, and npm are enabled when needed.

## Known setup pitfalls and fixes

### Port 8080 blocked

If onboarding says OpenShell gateway needs port 8080 and lists a PID:

```bash
sudo kill <PID>
sudo killall openshell openshell-gateway 2>/dev/null
sudo lsof -i :8080
```

Rerun onboarding only after `lsof` prints nothing.

### Firewall for Docker bridge callbacks

On Brev/MassCompute style hosts, if sandbox containers cannot reach the gateway:

```bash
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
```

### Running commands in the wrong shell

- `brev shell <instance>` runs on Jared's Mac, not inside the cloud instance.
- `nemoclaw hermes connect` runs on the cloud host.
- `hermes` runs inside the sandbox after connecting.

If Jared sees `shadeform@shadecloud`, he is on the cloud host.
If Jared sees `sandbox@...`, he is inside the sandbox.
If Jared sees `jc@Jareds-MacBook-Air`, he is on his Mac.

### Wrong model

Avoid GPT-OSS 120B for this workflow. It produced `ToolDescription description must be a valid string` errors with Hermes tools. Use NVIDIA Nemotron 3 Super 120B option 1 for the sandbox.

### License prompt

The NemoClaw installer requires `yes`. Typing `y` cancels installation.

## Audit model to include in souls or client materials

Explain auditing in three layers:
1. OpenShell gateway logs: egress attempts, allow/deny decisions, token substitution, policy reloads.
2. Hermes session history: prompts, responses, tool calls, skill loads, memory writes, durations.
3. Policy audit trail: versioned policies, hashes, active presets, filesystem/network gates.

AgentOS should turn these raw logs into readable manager-facing dashboards.

## Product distinction

Keep platform naming clear:
- Crew: Claude Code based, fast, pipeline-first.
- AgentOS: Hermes + NemoClaw/OpenShell, secure, audited, sandbox-first.
- Same canonical souls can run in both; do not duplicate specialist identities just because runtime changes.
