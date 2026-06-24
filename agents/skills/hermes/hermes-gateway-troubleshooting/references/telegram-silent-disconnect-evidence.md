# Telegram Silent Disconnect: Real Log Evidence

Date: 24 June 2026
Root cause: Gateway restart on 23 June 2026 at 18:29 — Telegram adapter never reconnected.

## What `hermes status --all` showed (misleading)

```
◆ Messaging Platforms
  Telegram      ✓ configured (home: 8647481186)
  Email         ✓ configured

◆ Gateway Service
  Status:       ✓ running
  PID(s):       31190
```

Everything looked healthy. Telegram was not actually connected.

## What gateway logs showed (diagnostic)

The last few Telegram events before the shutdown:
```
2026-06-23 18:29:34,925 INFO gateway.platforms.telegram: [Telegram] Disconnected from Telegram
2026-06-23 18:29:34,926 INFO gateway.run: ✓ telegram disconnected (4.07s)
2026-06-23 18:29:34,939 INFO gateway.run: Gateway stopped (total teardown 4.11s)
```

After the gateway came back up, there was NO "Connected to Telegram" entry. All subsequent logs were Email IMAP errors:
```
2026-06-23 21:48:44,568 ERROR gateway.platforms.email: [Email] IMAP fetch error: The read operation timed out
2026-06-23 23:50:52,337 ERROR gateway.platforms.email: [Email] IMAP fetch error: command: SELECT => socket error: EOF
(etc.)
```

Email was connected (and producing errors), Telegram was dead. No Telegram errors — just silence.

## After fix (gateway restart)

```
2026-06-24 17:20:56,233 INFO gateway.run: Connecting to telegram...
2026-06-24 17:20:59,992 INFO hermes_plugins.telegram_platform.adapter: [Telegram] Connected to Telegram (polling mode)
2026-06-24 17:20:59,997 INFO gateway.run: ✓ telegram connected
```

## Bot token verification

```json
{"ok":true,"result":{"id":8773055542,"is_bot":true,"first_name":"Brock The CEO","username":"Brockthe_ceobot"}}
```

Token was valid the entire time — this was purely an adapter initialisation failure after restart.
