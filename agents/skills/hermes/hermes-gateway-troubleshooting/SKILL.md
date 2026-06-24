---
name: hermes-gateway-troubleshooting
description: Diagnose and fix Hermes gateway platform connectivity issues — Telegram, Discord, Email, and other messaging platforms that stop responding despite the gateway appearing healthy.
version: 1.0.0
---

# Hermes Gateway Troubleshooting

When a messaging platform (Telegram, Discord, etc.) stops responding but the gateway process appears healthy, follow this systematic diagnostic path. Do not trust `hermes status --all` alone — it reports configuration state, not live connection state.

## Quick Diagnostic Sequence

1. **Check gateway process:** `hermes gateway status` — verify PID is running
2. **Check recent logs:** `grep -i "Connected to\|Disconnected from" ~/.hermes/logs/gateway.log | tail -10`
3. **Verify bot token (Telegram):** `curl -s "https://api.telegram.org/bot<TOKEN>/getMe"`
4. **If platform disconnected with no reconnect:** Restart the gateway

## Signature Pattern: Silent Platform Disconnect

**Symptoms:**
- User messages go unanswered on the platform
- `hermes gateway status` shows gateway running with valid PID
- `hermes status --all` shows platform as "✓ configured"
- No errors in `gateway.error.log` related to the platform

**Root cause:** The gateway process restarted (manual, crash, or update) and the platform adapter never reinitialised. The gateway process is alive, other platforms may work, but the affected platform is dead.

**Diagnosis (example for Telegram):**
```bash
grep -i "telegram" ~/.hermes/logs/gateway.log | tail -20
```

Look for the last event. If the last event is "Disconnected from Telegram" with NO subsequent "Connected to Telegram (polling mode)" or "✓ telegram connected", the adapter is dead despite the gateway running.

**Fix:**
```bash
hermes gateway restart
```

Then verify reconnection:
```bash
grep -i "Connected to\|Disconnected from" ~/.hermes/logs/gateway.log | tail -5
```

## `hermes status --all` is Configuration, Not Connection

The "✓ configured" status for a messaging platform means the platform is wired in config — it does NOT mean the adapter is currently connected and polling. Always cross-check with live logs.

## Per-Platform Verification

### Telegram
```bash
# Verify bot token is valid
source ~/.hermes/.env 2>/dev/null
curl -s "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getMe"

# Check connection in logs
grep "telegram connected\|Disconnected from Telegram" ~/.hermes/logs/gateway.log | tail -5
```

### Email
```bash
# Check connection in logs
grep "Email\] Connected\|Email\] Disconnected" ~/.hermes/logs/gateway.log | tail -5
```

## Pitfalls

- **Do not trust `hermes status --all` alone** for platform health. It reports config state, not live adapter state.
- **"✓ configured" ≠ connected.** A platform can show as configured while its adapter thread is dead.
- **Gateway restart can produce a partial recovery.** Some platforms reconnect, others don't. Check each one individually after a restart.
- **The gateway PID being alive does not mean all platform adapters are alive.** Each adapter runs its own connection lifecycle within the gateway process.
- **Email IMAP errors in logs are often red herrings.** They can pile up without affecting other platforms. Focus on the specific platform that's silent.
