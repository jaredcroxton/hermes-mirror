# AgentOS — Injecting PerformOS Agent Profiles into Client Sandboxes

Prepared 14 June 2026. This is the product architecture for installing Hermes agents backed by PerformOS specialist souls into client NemoClaw sandboxes.

## The architecture

```
Client Company
├── NemoClaw Sandbox "acme-hr" (Restricted policy, CPU)
│   └── Hermes Agent + PerformOS profiles (Brock, Lara, Harry, etc.)
├── NemoClaw Sandbox "acme-sales" (Balanced policy, GPU)
│   └── Hermes Agent + same profiles, different policy
└── NemoClaw Sandbox "acme-exec" (Restricted, audit-only)
    └── Hermes Agent + Brock, Leo, read-only tools

          ▲ Managed by:
AgentOS Control Plane (PerformOS)
├── Agent Profiles (Brock, Lara, Bob, Harry, Polly, Nelly, Sam, Leo)
├── Skill Library (L&D, HR legislation, SEO, content, build)
├── Onboarding Script (automated per-client sandbox creation)
└── Client Dashboard (usage, policy, audit)
```

## Three injection layers

### Layer 1: Agent profiles (soul files)

Agent souls live in Obsidian: `/Users/jc/Desktop/Obsidian/Agents/[agent]-soul.md`

To inject into a client sandbox:
```bash
mkdir -p /sandbox/.hermes/profiles/{brock,lara,bob,harry,polly,nelly,sam,leo}
cp agent-profiles/brock-agent.md /sandbox/.hermes/profiles/brock/SYSTEM.md
```

Hermes loads profiles from `~/.hermes/profiles/<name>/`. The sandbox maps this to `/sandbox/.hermes/profiles/`.

### Layer 2: Skills (specialist toolkits)

PerformOS skills are Hermes-compatible `SKILL.md` format files. Drop into `/sandbox/.hermes/skills/agentos/` inside the sandbox image.

### Layer 3: Memory (long-term context)

Pre-seed `/sandbox/.hermes/memories/MEMORY.md` with:
- Client company context
- Role descriptions for each agent
- Compliance rules
- Output standards and brand voice
- Agent ecosystem routing table

## Token masking principle

Tokens must be injected at the OpenShell layer as environment variables, never written to disk inside the sandbox. The agent sees only masked placeholders (`openshell_secret_abc123`). Real tokens are substituted at egress only when network policy allows the connection.

```bash
nemoclaw hermes create \
  --name "$CLIENT" \
  --env TELEGRAM_BOT_TOKEN="$TOKEN" \
  --env TELEGRAM_CHAT_ID="$CHAT_ID" \
  --policy client-policy.yaml
```

## Onboarding script pattern

```bash
#!/bin/bash
# agentos-onboard.sh

CLIENT=$1
CLIENT_MODEL="nvidia/nemotron-3-super-120b-a12b"

nemoclaw hermes create \
  --name "$CLIENT" \
  --from /opt/agentos/docker/Dockerfile.client \
  --policy /opt/agentos/policies/client-policy.yaml \
  --model "$CLIENT_MODEL" \
  --provider nvidia-prod

# Inject profiles
for agent in brock lara bob harry polly nelly sam leo; do
  openshell cp "/opt/agentos/profiles/${agent}.md" "$CLIENT:/sandbox/.hermes/profiles/${agent}/SYSTEM.md"
done

# Inject skills
openshell exec "$CLIENT" -- cp -r /opt/agentos/skills/* /sandbox/.hermes/skills/agentos/

# Pre-seed memory
openshell exec "$CLIENT" -- bash -c "
  cat > /sandbox/.hermes/memories/MEMORY.md << 'MEMEOF'
# $CLIENT Agent Team
Agent ecosystem: brock, lara, bob, harry, polly, nelly, sam, leo.
Brock is CEO-level strategy. Route high-level decisions to Brock.
Lara handles learning design. Route training programme builds to Lara.
Bob handles builds and deployments. Route code/dashboard work to Bob.
Harry handles HR legislation. Route workplace compliance to Harry.
MEMEOF
"
```

## What NVIDIA/Nous are NOT building

| They build | PerformOS builds |
|---|---|
| Sandbox runtime | Agent profiles (Brock, Lara, Bob, etc.) |
| Network policies | Skill library for specific industries |
| Inference routing | Client onboarding automation |
| OpenShell masking | Team dashboards and audit views |
| Hermes agent | Managed agent operations and support |

## The product differentiator

The NemoClaw sandbox provides:
- Token masking (client never exposes API keys to agents)
- Policy gating (agents cannot talk to unapproved endpoints)
- Per-user sandboxes (different permissions per team member)
- Audit trail (every action inside sandbox is observable)

PerformOS wraps that with agents, skills, profiles, onboarding, and dashboards.
