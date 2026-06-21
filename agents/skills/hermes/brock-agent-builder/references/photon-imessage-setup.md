# Photon Spectrum iMessage Setup (Hermes v0.17.0+)

Replaces BlueBubbles entirely. No Mac relay. No Messages.app. No Apple Gatekeeper malware flag.

## One-command setup

```bash
hermes photon setup
```

Walk through the prompts:

1. Opens browser for device-code authentication. Click **Approve**.
2. Creates Photon project "Hermes Agent" automatically.
3. Provisions Spectrum credentials (secret saved to `~/.hermes/auth.json`).
4. Asks for iMessage phone number in E.164 format. **Australia: `+61` then mobile number without the leading zero.** Example: `0412 345 678` → `+61412345678`.
5. Phone auto-allowlisted and DM set as cron home channel.
6. Agent's iMessage number displayed on screen (US number, e.g. `+1 (628) 264-9335`).
7. Node sidecar deps installed automatically.
8. Complete. Start gateway: `hermes gateway start`.

## What the other person sees

Normal iMessage. Blue bubbles. Your name/photo. No indication Hermes is involved.

## What works

- Text messaging (Markdown stripped for clean iMessage)
- File attachments (PDF, Excel, Word, images, voice, video)
- Group chat with mention gating
- Cron delivery to iMessage

## Key difference from BlueBubbles

- No Mac relay needed. MacBook can sleep.
- No third-party bridge for Apple to flag as malware.
- Direct Photon managed line pool.
- Free to start. Nothing to self-host.

## Post-setup commands

```bash
hermes gateway start       # Start the gateway
hermes gateway status      # Check connection status
hermes photon status       # Photon-specific status
hermes photon telemetry    # Usage stats
```

## Troubleshooting

**"agent isn't online" fallback message:** Gateway is not running. Run `hermes gateway start`.
**Gateway bootstrap failed (5: Input/output error):** Normal on first start. Run `hermes gateway start` again — it reloads the launchd service definition and succeeds.
**Phone number already registered:** Expected if you set up Photon before. The setup detects this and skips re-registration.
