# Gateway Stopped — Diagnostic Flow

## The false-positive trap

When a specialist agent goes silent on Telegram, the intuitive first move is to probe the profile brain directly:

```bash
hermes --profile bobbuilder chat -q "ok" --quiet
```

This will often **succeed** even when the gateway is completely down. Why: the CLI probe spawns an ad-hoc session that talks to the model provider directly. It bypasses the gateway entirely. So you get `"Ready when you are."` and conclude the agent is fine — while Telegram messages pile up unanswered.

## Correct triage order

### Step 1: Check gateway status

```bash
hermes profile list | grep <profile>
```

Look at the Gateway column. Compare to other profiles:

```
Profile          Model                        Gateway      Alias
 ───────────────    ───────────────────────────    ───────────    ───────────
 ◆default         deepseek-v4-pro              running      —
  bobbuilder      gpt-5.5                      stopped      —            ← HERE
  harryhr         deepseek-v4-pro              running      —
```

A single `stopped` among many `running` profiles is the smoking gun.

### Step 2: Start it

```bash
hermes gateway start --profile <profile>
```

Expected output:

```
↻ Updated gateway launchd service definition to match the current Hermes install
✓ Service started
```

### Step 3: Confirm

```bash
hermes profile list | grep <profile>
```

Should now show `running`.

### Step 4: Only now — if still not responding — probe the provider

```bash
hermes --profile <profile> chat -q "reply with ok" --quiet
```

## Why gateways stop

- Profile created but `gateway install` / `gateway start` was never run
- System restart killed the launchd service and it did not auto-restart
- Gateway was manually stopped and never restarted
- launchd plist corrupted or removed (rare)

## Common misdiagnosis paths (avoid)

| Symptom | Wrong first move | Right first move |
|---------|-----------------|------------------|
| Agent silent on Telegram | Probe provider (`hermes --profile X chat`) | Check gateway (`hermes profile list`) |
| CLI probe works, Telegram dead | Assume config/provider problem | Check gateway column for `stopped` |
| Gateway shows `stopped` | Edit config.yaml / swap providers | `hermes gateway start --profile X` |

## Bob-specific (04 June 2026)

Bob was on `gpt-5.5 / openai-codex`. CLI probe returned `"Ready when you are."` instantly. Gateway showed `stopped` while all other profiles were `running`. One command fixed it: `hermes gateway start --profile bobbuilder`.
