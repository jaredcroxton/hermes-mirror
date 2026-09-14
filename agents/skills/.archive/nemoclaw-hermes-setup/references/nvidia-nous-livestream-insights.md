# NVIDIA Neutron Labs Livestream — NemoClaw Hermes Demo Insights

**Date:** June 2026
**Source:** https://www.youtube.com/live/pgQDbRMa2Eg
**Presenters:** Johnny (Nous Research), Karan (Nous Research co-founder), Chris (NVIDIA)

## Key architecture clarification

- **NemoClaw** = blueprint/launcher for wrapping Hermes Agent in OpenShell
- **OpenShell** = secure sandbox runtime that locks down the agent
- **Hermes Agent** = the agent doing the actual work
- **NemoHermes** = the CLI tool (`nemohermes`) that orchestrates the setup

## Enterprise deployment model (what they actually demoed)

Johnny used a **custom onboarding script**, not the `nemohermes onboard` wizard. The script:

1. Programmatically creates OpenShell sandboxes for users (Alice, Bob)
2. Injects API tokens as **masked environment variables** through Open Shell
3. Pre-configures network policies (GitHub, Telegram, Discord)
4. Creates sandboxes in parallel
5. Handles the onboarding flow without interactive prompts

### Token masking (critical security pattern)

Inside the sandbox, `echo $GITHUB_TOKEN` shows an OpenShell placeholder — not the real token. The OpenShell gateway substitutes real tokens at egress when traffic matches an allowed policy. The agent never has access to raw credentials.

This is the pattern the `nemohermes onboard` wizard does NOT replicate — it skips messaging configuration and requires manual intervention.

## What worked in the demo

- GitHub PR review workflow with skill creation
- Session search across sandbox sessions
- Memory persistence (agent remembers rules across turns)
- Skill self-creation (agent crystallizes a workflow into a reusable skill)
- Policy hot-swapping (add a network policy, takes effect immediately, no restart)
- Multi-user sandboxes (Alice and Bob running in parallel)
- GPU passthrough to sandbox (verified via nvidia-smi inside)

## What they acknowledged as alpha

Karan (Nous co-founder): *"This is basically the prototype and beginning, very transparently to you guys, of an enterprise solution for Hermes."*

- Enterprise security, policy controls, admin observability are in active development
- Skill sharing between users is on the roadmap but not yet built
- Hermes Desktop (Electron app) shown as personal-use alternative — not the enterprise path
- NemoClaw blueprints are the enterprise direction

## Hermes agent features highlighted

- **Skills index injection**: Only skill names/descriptions in context, full body loaded on demand (prevents bloat)
- **Curator**: Autonomous background service that prunes, consolidates, and compresses the skill library
- **Session search**: Cross-session recall without rehashing context
- **Memory**: Persistent across sessions, relevant memories auto-injected
- **Self-evolving**: Agent creates skills from workflows, improving with use

## Direct implications for PerformOS/AgentOS

1. The enterprise path is custom onboarding scripts + OpenShell policy management, not the interactive wizard
2. Telegram/Discord/WhatsApp messaging works when tokens are injected at the Open Shell layer
3. The dashboard gap is real — there's no polished web UI for the Hermes agent path yet
4. NemoClaw blueprint = reference architecture, not a finished product
5. Nous Research is building this as their enterprise layer — timing aligns with AgentOS product roadmap
