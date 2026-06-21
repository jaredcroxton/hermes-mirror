# Photon iMessage Setup — Built into Hermes v0.17.0+

## What Photon is

Photon Spectrum is Hermes' built-in iMessage platform adapter. No BlueBubbles. No Messages.app relay. No third-party bridge for Apple to flag as malware. Hermes sends and receives iMessage directly through Photon's managed line pool. Free to start. Nothing to self-host.

## Setup (5 minutes)

```bash
hermes photon setup
```

Follow the prompts:
1. Authenticate via browser (device code flow)
2. Project auto-created
3. Spectrum credentials provisioned
4. Enter your phone number in E.164 format (e.g. `+61412345678`)
5. Sidecar deps auto-installed

After setup, your agent gets a dedicated US iMessage number. Text that number from your phone to talk to your agent.

## Start the gateway

```bash
hermes gateway start
```

## What the other person sees

A normal iMessage conversation. Blue bubbles. Your agent number at the top. "Delivered" and "Read" receipts. They never know an agent wrote the reply. Files (Excel, PDF, images) attach natively.

## Important: your MacBook does NOT need to be awake

Unlike BlueBubbles (which required Messages.app running on an always-on Mac), Photon routes through Photon's cloud infrastructure. Your MacBook can sleep. iMessage still works.

## Common pitfalls

- **Wrong command:** `hermes photon login` does not exist. The correct command is `hermes photon setup`.
- **Gateway not started:** After setup, run `hermes gateway start`. Without the gateway running, messages get the Photon fallback reply ("agent isn't online right now").
- **Phone format:** E.164 required. For Australia, remove the leading zero: `0412 345 678` → `+61412345678`.
