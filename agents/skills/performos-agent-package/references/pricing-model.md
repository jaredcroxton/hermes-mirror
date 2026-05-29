# PerformOS 5-Agent Package — Pricing Model & Research

## Current model (locked 29 May 2026)

Based on live pricing from Orgo.ai and OpenRouter.

### Costs per client per month

| Cost item | Amount | Source |
|---|---|---|
| Orgo Scale plan | $224/mo | Orgo.ai pricing (200GB RAM, client-ready) |
| Orgo AI credits | $100/mo | Included with Scale plan (covers GPU/compute) |
| Subtotal Orgo | $324/mo | |
| AI token usage (56M tokens, 90% cached) | ~$9/mo | DeepSeek V3 via OpenRouter: $0.28/M input, $1.12/M output |
| Support (4h × $75/h) | $300/mo | Internal loaded cost |
| **Total monthly cost** | **~$633/mo** | |

### Setup (one-time)

| Cost item | Amount |
|---|---|
| Build 5 agents (5 × 8h × $75/h) | $3,000 |

### Margin analysis

| Price point | Gross margin | Margin % |
|---|---|---|
| $4,995/mo | $4,367/mo | 87% |
| $3,995/mo | $3,362/mo | 67% |
| $3,500/mo | $2,867/mo | 57% |
| $2,995/mo | $2,362/mo | 47% |
| $2,633/mo | $2,000/mo | 40% (minimum viable) |

Jared wants at least $2,000/mo margin, ideally $3,000+. $4,995/mo delivers ~$4,367/mo.

### Token budget breakdown

- 5 agents × 20 interactions/day × 22 working days = 2,200 interactions (conservative)
- 5 agents × 20 interactions/day × 30 days = 3,000 interactions (generous)
- Avg 15K input + 2K output tokens per interaction
- 90% cache hit rate (prompt caching on repeated context)
- Monthly: ~45M cached input + ~5M uncached input + ~6M output = ~56M total tokens
- At double usage: ~112M tokens, ~$18/mo AI cost, still profitable at $4,995 price

### Token cost sensitivity

| Multiplier | Monthly tokens | AI cost | Margin at $4,995 |
|---|---|---|---|
| 0.5x (light) | 28M | ~$5 | $4,371 |
| 1x (baseline) | 56M | ~$9 | $4,367 |
| 2x (heavy) | 112M | ~$18 | $4,358 |
| 5x (extreme) | 280M | ~$46 | $4,320 |

Token costs are NOT the margin risk. Orgo plan cost + support hours are fixed. Token usage is essentially free at current pricing.

## Orgo.ai pricing tiers (verified 29 May 2026)

| Plan | Monthly (billed yearly) | RAM | AI credits | Use case |
|---|---|---|---|---|
| Hacker | $29/mo ($351/yr) | 20GB total | $10/mo | Single agent, building |
| Team | $112/mo ($1,341/yr) | 80GB total | $30/mo | Team production agents |
| Scale | $224/mo ($2,691/yr) | 200GB total | $100/mo | Client-ready agent fleets |

Scale is the right plan for client deployments: 200GB RAM allows 5+ agents with headroom, $100 AI credits covers compute, and "client-ready" is their positioning.

## Zapier pricing context (verified 29 May 2026)

Zapier is NOT part of the PerformOS package cost — clients bring their own Zapier plan. But Zapier pricing is relevant for the proposal because it affects the client's total cost of ownership and because Zapier Enterprise is the recommended governance layer.

### Zapier Platform plans (GBP, billed yearly)

| Plan | Price/mo | Tasks/mo | Users | Key features |
|---|---|---|---|---|
| Free | £0 | 100 | 1 | Zaps, Tables, Forms, MCP included |
| Professional | £15.21 | From 2K | 1 | Multi-step Zaps, Premium apps, Webhooks |
| Team | £52.51 | From 2K | 25 | Shared workspaces, SAML SSO, Premier Support |
| Enterprise | Contact sales | Custom | Custom | AI Guardrails, BYOM, SCIM, log streaming |

**Key insight:** Zapier MCP is now included on ALL plans including Free. Any client can connect AI agents to their Zapier tools without paying extra for MCP.

### Zapier Enterprise features relevant to agent governance

1. **AI Guardrails** — safety checks that block sensitive data before AI outputs reach systems
2. **BYOM (Bring Your Own Model)** — run AI through client's own AWS Bedrock infrastructure
3. **Managed Connections** — IT owns app connections, not individuals
4. **Domain Restrictions** — block personal accounts from business systems
5. **Log Streaming** — real-time workflow data to Datadog/Splunk/SIEM
6. **SCIM Provisioning** — auto-provision users through identity provider
7. **Action Restrictions** — granular endpoint-level control per app
8. **SOC 2 Type II/III, GDPR, CCPA** — annually audited
9. **99.9% uptime SLA**

### Strategic recommendation for PerformOS proposal

Lead with Zapier Enterprise as the optional governance layer. It addresses the three biggest procurement objections:
1. "How do we control what the AI does?" → Action Restrictions + App Access Controls
2. "How do we prevent data leaks?" → AI Guardrails + Domain Restrictions
3. "Can we see what happened?" → Log Streaming + Asset History API

Client cost impact: Enterprise is custom-priced (~£500-2,000/mo depending on seats). Budget £500/mo for planning purposes. This is the client's cost, not PerformOS's, but it should be discussed openly in the proposal.

### Task budgeting for agent workflows

If an agent triggers a 3-step Zap 20 times/day across 5 agents:
- 3 × 20 × 5 = 300 tasks/day = ~9,000 tasks/mo
- Fits comfortably on Professional plan (£15/mo) if single-user
- Small businesses not hitting team-sharing needs stay on Professional

For larger deployments or clients who want governance features, Enterprise is the right fit.

## Sources

- Orgo.ai pricing: https://www.orgo.ai/pricing (verified 29 May 2026)
- Zapier pricing: https://zapier.com/pricing (verified 29 May 2026)
- Zapier Enterprise: https://zapier.com/enterprise (verified 29 May 2026)
- Live token usage data: OpenRouter dashboard (27 May 2026 — 59.6M tokens, 98.4% cache hit)
- PerformOS token model: execute_code Python model run 29 May 2026
