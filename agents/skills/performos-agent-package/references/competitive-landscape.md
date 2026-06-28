# Competitive Landscape — Local AI Agent Deployment

## Purpose
This reference file contains the competitive landscape analysis for PerformOS Local Edition. Use it when building competitor comparison slides, validating pricing, or positioning against alternatives.

## Direct Competitors (Local/On-Prem AI Agent Deployment)

| Company | Pricing | Deployment | Focus | Agents |
|---|---|---|---|---|
| PerformOS | $4,999 AUD/mo | On-prem | Full business team | Up to 10 |
| Factory AI | Custom enterprise | Cloud or on-prem | "Droids" platform | Custom |
| Tessl | $19-$99/user/mo | Cloud or on-prem | Agent registry | Custom |
| Sourcegraph | Custom enterprise | Cloud or on-prem | Code intelligence | 1 |
| Augment Code | $60-$200/user/mo | Cloud | Code review | 1 |
| Cursor | $20-$40/user/mo | Cloud | AI coding IDE | 1 |
| Cognition (Devin) | $500/user/mo | Cloud | Autonomous coding | 1 |

## Key Positioning Insights

1. **No one serves mid-market with a full AI team at a flat price.** Cursor/Augment/Cognition are per-user and code-only. Factory AI/Sourcegraph are enterprise-only.
2. **Zero data retention is your moat.** Every cloud competitor stores data. For legal/health/finance/government, this is a deal-breaker.
3. **Per-token costs destroy cloud budgets.** GPT-5.5 at ~$10K-$20K/mo. Claude Opus 4 at ~$6K-$12K/mo. PerformOS is $4,999 flat.
4. **You provide agents, not tools.** LangChain requires clients to build everything. PerformOS provides 10 business-ready agents with onboarding.

## Built Assets

- `/Users/jc/Desktop/competitor-dashboard.html` — full HTML competitor comparison dashboard with pricing cards and feature table
- Slide deck at https://performos-ai-team-deck.vercel.app (slide 2 = comparison table)

---

## Agent Runtime & Platform Landscape

This section covers the platforms CREW skills could run on — a different dimension from the local-deployment competitors above. Updated 28 June 2026.

### OpenCode (anomalyco/opencode)

- **What it is:** Terminal-native open-source AI coding agent. MIT licensed.
- **Traction:** 180k GitHub stars, 22.1k forks, 958 contributors, 7.5M MAU, 828+ releases.
- **Team:** Built by the SST/Serverless Stack team (Dax, Frank, Jay).
- **Interface:** CLI. Keyboard-first. Two built-in agents: build (full-access) and plan (read-only).
- **Model stance:** Provider-agnostic. 75+ models. Bring your own keys.
- **CREW relevance:** Direct skill port possible via AGENTS.md/CONTEXT.md config. 7.5M MAU is the distribution opportunity. But OpenCode users are developers seeking coding help — CREW's business-domain skills (sales coaching, HR compliance, learning design) may be a category mismatch unless intentionally packaged for developer-adjacent workflows.
- **Business model angle for CREW:** Marketplace (one-time purchase per pack) or platform (subscription for cross-runtime compatibility). OpenCode's growth validates that open-source agent tooling is winning — developers want MIT-licensed, terminal-native, model-agnostic tools.

### Google Antigravity

- **What it is:** Google's agentic development platform and IDE. Announced at I/O 2026. Web-based at antigravity.google.
- **Architecture:** Full graphical IDE with multi-agent orchestration. Manager assigns work to sub-agents. Uses AGENTS.md for project config.
- **Model stance:** Google ecosystem. Built for Gemini. Runs on Google Cloud.
- **License:** Not open source. Platform service.
- **CREW relevance:** Integration would require Google's agent framework (likely A2A protocol or Gemini API). Massive distribution via Google's reach. But CREW would be building on rented land — Google owns the runtime, the model access, and the agent orchestration layer.
- **Risk:** Platform dependency. Google controls the ecosystem.

### Hermes (current CREW runtime)

- **What it is:** Agent platform — persistent agents with memory, Kanban orchestration, cron jobs, specialist profiles.
- **Architecture:** Agent OS, not a coding tool. Agents like Brock, Lara, Harry, Nelly remember context across sessions and operate as specialist team members.
- **Interface:** CLI + dashboard. Profile-based agent deployment.
- **Model stance:** Provider-agnostic.
- **CREW relevance:** Current primary runtime for CREW specialist agents. Closer to OpenCode philosophically (run it yourself, own the stack) but adds durable memory, orchestration, and specialist routing that OpenCode and Antigravity do not have.

### Claude Code (current CREW skill runtime)

- **What it is:** Anthropic's terminal coding agent. Proprietary.
- **CREW relevance:** Current runtime for the 93 gold skills and 14 packs. The distribution bottleneck — skills only work inside Claude Code.

### Strategic insight for CREW

**Open-source agent tooling is winning.** OpenCode's 180k stars, Hermes' local-first architecture, and the broad rejection of vendor lock-in all point the same direction.

**The CREW opportunity:** If CREW skills are runtime-agnostic — portable files that load into any agent platform — then every platform's growth expands CREW's addressable market. If CREW skills remain bound to Claude Code, OpenCode's 7.5M users are irrelevant.

**Two business models:**

| Model | How it works | Revenue | Risk |
|---|---|---|---|
| **Marketplace** | One-time purchase per skill pack. Buyer downloads, loads into their agent of choice. | High margin, no recurring. | Constant new packs or new customers needed. |
| **Platform** | Subscription for full library access. CREW handles versioning, updates, cross-runtime compatibility. | Recurring, predictable, compounds. | Infrastructure needed: distribution, auth, payment. |

**Recommended sequence:** Validate marketplace first (landing page + payment link + download). If traction, layer platform subscription on top.

**The core bet:** Whether business-domain skills — sales coaching, HR compliance, learning design — are a category anyone will pay for, or whether the market only values coding-focused skills.
