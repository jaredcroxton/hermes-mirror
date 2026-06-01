---
name: performos-agent-package
description: Use when Jared asks about selling or positioning the PerformOS agent package to clients. Covers cloud (Orgo) and local editions, two-tier Standard/Advanced pricing, "up to 10 fully customisable agents" positioning, security framing, compliance checklist, proposal structure, and internal financial model.
tags: [performos, sales, pricing, agent-package, commercial, zapier]
---

# PerformOS 5-Agent Package — Commercial Model

## Trigger
Use when Jared asks about selling agent packages to businesses, positioning PerformOS to clients, updating proposal PDFs, discussing pricing and margins, or building Zapier-powered automations for clients.

## Two Product Variants

PerformOS sells TWO distinct product lines. Do not confuse them or blend details between documents.

### Variant 1: Cloud-Hosted (Orgo + Zapier)
- Hosted on Orgo.ai Scale infrastructure
- Tools connected through Zapier Enterprise MCP
- Pricing: $4,995 AUD/mo + $3,000 setup
- 50M+ token budget, 5 agents (expandable)
- 4 hours/month support included
- SOC 2 Type II via Orgo + Zapier
- Communication: "managed cloud AI team"
- Detailed financial model in `references/pricing-model.md`

## Local Edition (PerformOS-Owned Managed Appliance)

Private-cloud GPU alternative: when Jared is testing or positioning AWS-hosted Ollama/Hermes rather than a client-site appliance, use `references/aws-private-cloud-gpu-stack.md`. Keep the language clear: AWS GPU = PerformOS Private Cloud AI Team, not Local Appliance.

AWS private-cloud and Ollama deployment guidance lives in `references/aws-private-cloud-ollama.md`. Use it when Jared is comparing Lightsail, EC2 GPU, client-site Mac, and always-on Ollama model hosting for the PerformOS AI Team offer. — Updated June 2026
- Runs locally on a PerformOS-owned managed appliance placed in the client's approved environment
- Client does **not** own the appliance; PerformOS retains ownership and the contract must cover custody, return, damage, wipe, and recovery
- Client IT can security-review, approve, connect, and govern the appliance through their network and login standards
- MCP servers connect to client-approved tools (email, CRM, internal systems)
- All inference local, zero data leaves the approved local environment unless the client chooses an approved integration path
- Pre-built agent profiles, soul files, tool configurations included
- **Two client-facing tiers: Standard ($3,000 setup) and Advanced ($6,000 setup)**
- Monthly retainer: $4,999 AUD/mo (same for both tiers)
- Up to 10 fully customisable agents included; additional at $500/agent/mo
- 1-hour monthly optimisation call included
- 3-month quarterly refresher (2 hours) included
- Ad-hoc optimisation beyond included hours: $350/hour
- **6-month minimum engagement** (changed from 12-month, June 2026)
- Travel for face-to-face onboarding available (costs additional)
- Curated upskilling course links included
- Communication: "your private AI team, running locally"

### Key Differentiators for Local Edition
- Zero data retention: all processing on client hardware, encrypted at rest
- No API costs: unlimited local inference, no per-token billing
- No vendor lock-in: runs on commodity Mac hardware (Mac Studio / MacBook Pro)
- Customizable, not just configurable: 4-hour deep discovery during onboarding customizes every agent to the client's business
- "You do not get a template. You get a team that knows your business."

### Local Edition — Client-Facing Tier Structure

**RULE: Never mention Mac Mini, Mac hardware, Ollama, or model parameter sizes in client-facing materials.** The client buys "Standard" or "Advanced." That is all they need to know. Hardware and model specifics stay in internal docs only.

**AgentOS pricing page pattern:** when turning this tier structure into website copy, use `references/agentos-pricing-page-pattern.md`. Lead with "Private AI team for business leaders" and frame the two tiers as reasoning depth, not agent count. Do not make 8B vs 14B-70B the headline. Use "Standard = everyday business support" and "Advanced = complex leadership reasoning" first, then explain model sizes in a technical FAQ if needed.

| Tier | What the client gets | Setup | Monthly |
|---|---|---|---|
| Standard | Up to 10 fully customisable AI agents. 8B parameter models. Built for everyday business tasks — writing, analysis, coaching, research, admin, HR, learning design, talent acquisition, marketing, churn management. 24GB RAM provisioned during onboarding. | $3,000 | $4,999 |
| Advanced | Up to 10 fully customisable AI agents. Larger models (14B to 70B). Built for complex reasoning, strategic thinking, heavyweight analysis, and nuanced judgement. Same 10 agents, significantly more capability per agent. 48GB RAM provisioned during onboarding due to larger model sizes. | $6,000 | $4,999 |

**Both tiers include:** Same 10 agents. Same onboarding (10 hours). Same monthly optimisation call. Same quarterly refresher. Same curated upskilling links. **6-month minimum term** (changed from 12-month, June 2026).

**10 agents included in both tiers (reordered June 2026):**

| # | Agent | Business function |
|---|---|---|
| 1 | CEO Advisor | Strategic thinking partner — board prep, decision framing, stakeholder prep |
| 2 | HR and Compliance | Employment law, workplace incidents, APAC market legislation |
| 3 | Talent Acquisition | Recruitment pipelines, no-show reduction, hiring quality, source tracking |
| 4 | Churn and Acquisition Expert | Retention analysis, customer acquisition strategy, churn prediction |
| 5 | Learning Designer | Training programmes, onboarding, L&D content, learner/manager packs |
| 6 | Builder and Deployer | Dashboards, automations, internal tools, web apps |
| 7 | Research and Synthesis | Document digestion, market intelligence, competitive analysis |
| 8 | Chief of Staff | Email triage, meeting prep, operations, travel, follow-up tracking |
| 9 | Marketing and SEO Strategist | SEO, content strategy, AI-powered website optimisation, marketing campaigns |
| 10 | Growth Optimiser | New agent implementation, ongoing optimisation, performance analytics |

**Key positioning points:**
- BOTH tiers run up to 10 agents. The difference is model capability, not agent count.
- Both tiers are fully customisable — every agent is tailored to the client's business.
- Setup fee is the same regardless of how many agents the client actually uses (up to 10).
- Monthly retainer is the same for both tiers.
- **Do not say "8B" or "14B to 70B" in client-facing materials unless the prospect is technical.** Use "Standard models for everyday tasks" and "Advanced models with significantly more processing capacity for complex reasoning" as default framing. If they ask for specifics, explain in plain language: parameter count = number of learned connections, more parameters = stronger reasoning on complex problems. See `references/tier-comparison-deck-language.md` for exact wording.

**Internal hardware reference (NEVER shared with clients):**

| Tier | Internal machine | RAM | SSD | Internal cost (AUD) |
|---|---|---|---|---|
| Standard | Mac Mini M4 (10c CPU/GPU) | 24 GB | 512 GB | A$1,599 |
| Advanced | Mac Mini M4 Pro (14c/20c) | 48 GB | 1 TB | A$3,399 |

**Verified pricing source:** Apple Australia Store, May–June 2026. M4 24GB 512GB = A$1,599. M4 Pro 14c/20c 48GB 1TB = A$3,399. Always verify current pricing at apple.com/au before quoting — do not estimate from memory.

## The offering

PerformOS sells a managed AI team to business clients. The client gets pre-built and customised specialist AI agents running on approved infrastructure, with their own data, governance, and tool connections.

### AgentOS naming and product architecture

When Jared asks what to call the private AI team product, default recommendation is **AgentOS by PerformOS**.

Brand architecture:
- **PerformOS** — parent company / performance operating system
- **LearnOS** — learning and capability product
- **PulseCheck 360** — feedback and diagnostic product
- **AgentOS** — private AI agent team product

Preferred positioning:
- "Your private AI team, built for work."
- "AgentOS gives your business a private AI team inside the tools your people already use."
- "Turn AI from a monthly subscription into a managed team of private business agents."

Avoid positioning it as "10 bots" or "Google Chat bots." Google Chat is only the front door. The product is the managed agent layer: role design, business knowledge, permissions, tools, governance, and ongoing optimisation.

### Google Chat delivery model

When Jared asks how AgentOS works inside Google Chat, explain it simply:

**Leader → Google Chat → PerformOS agent layer → AI model + business knowledge + approved tools**

Three practical setup models:
1. **One Google Chat space per agent** — simplest for pilots. Example: AI CEO Advisor, AI Sales Coach, AI HR Advisor.
2. **One Google Chat app with agent selection** — cleaner at scale. Backend routes user messages to the right agent.
3. **Private DMs for personalised leader agents** — premium executive experience.

The backend must identify the user, check permission, route to the right agent, call the model and tools, and return the answer to Google Chat.

### Personalisation structure

Do not sell personalisation as just changing the agent name. Each personalised agent needs:
- agent identity and purpose
- user or leader context
- business context
- behaviour rules
- approved knowledge sources
- approved tools
- access controls
- escalation rules

Knowledge should be separated into zones:
- company-wide knowledge available to all agents
- function knowledge available only to relevant agents
- leader-specific knowledge available only to that leader's private agent

Recommended commercial framing:
- **Standard** — up to 10 business-function agents for shared team use
- **Advanced / Leadership personalisation** — up to 10 personalised leader agents, with higher setup fee because discovery, permissions, and tuning take more time

Default strategic advice: sell the 10-agent business team first, then offer leader-personalised agents as the premium setup.

### The 5 agents

| # | Agent | Role |
|---|---|---|
| 1 | Strategic Advisor | CEO-level thinking partner. Analyses decisions, prepares briefs, challenges assumptions. |
| 2 | Builder & Deployer | Builds dashboards, automations, HTML tools. Deploys to client environments. |
| 3 | Learning Designer | Designs training programmes, builds learner/manager content packs, assessments, Kirkpatrick frameworks. |
| 4 | HR & Compliance Advisor | Interprets employment law across client's markets. Maps incidents against local legislation. |
| 5 | Research & Synthesis | Digests documents, synthesises sources, builds knowledge bases, produces briefing packs. |

### Financial model (locked 29 May 2026)

| Item | Amount |
|---|---|
| Package price (monthly) | $4,995 AUD/mo |
| One-time setup | $3,000 AUD |
| Monthly token budget | ~56M tokens included, no overage |
| Interactions included | 200 per agent per day (~30,000/month total) |
| Orgo Scale plan cost (internal) | $324/mo (dedicated environment, 200GB RAM) |
| AI token cost (56M tokens, cached, internal) | ~$9/mo |
| Support (4 hours/month) | Included |
| Total monthly cost to PerformOS (internal) | ~$633/mo |
| Gross margin per client (internal) | ~$4,367/mo (87%) |
| At 2x usage (internal) | ~$4,350/mo margin |

**Margin target:** at least $2,000/mo per client, ideally $3,000+. Current model delivers ~$4,367/mo — well above target.

### Token budget sizing logic

- 5 agents × 200 interactions/day × 30 days = 30,000 interactions/month
- Avg 15K input + 2K output tokens per interaction
- 90% cache hit rate on input tokens
- Using DeepSeek V3 pricing ($0.28/M input cache miss, $0.028/M cache hit, $1.12/M output)
- Even at double usage (400 interactions/agent/day), cost only doubles to ~$18/mo
- No overage charges — client never faces surprise bills

### Architecture

1. Client gets a dedicated Orgo Scale environment ($224/mo + $100/mo AI credits)
2. 5 agent computers run 24/7
3. Client provides MCP tokens for their tools (email, CRM, calendar, internal systems) via their own Zapier Enterprise account
4. PerformOS builds and configures agents in Orgo terminal
5. Client owns all data, tokens, and agent configurations
6. Client can revoke MCP access at any time — all agent access terminates within 60 seconds

### Zapier authorisation flow (for client proposals)

The client never shares passwords or admin access. The flow is:

1. Client signs up for Zapier Enterprise (or upgrades existing account)
2. Client connects their tools inside Zapier (Gmail, Sheets, CRM, Calendar) — their own credentials
3. Client generates scoped MCP tokens — choosing which apps each token can access
4. Client provides the token to PerformOS through a secure channel
5. PerformOS configures agents with the token
6. Client verifies and monitors all access from their Zapier dashboard

PerformOS NEVER logs into the client's Zapier account. Only the scoped token is shared. Client can revoke at any time.

### Zapier Enterprise governance

Every agent action flows through Zapier Enterprise. Key features:

- **AI Guardrails** — block sensitive data before AI outputs reach systems
- **Action Restrictions** — define which actions are allowed per app
- **Domain Restrictions** — block personal accounts from business systems
- **Log Streaming** — real-time workflow data to Datadog/Splunk/SIEM
- **BYOM** — run AI through client's own AWS Bedrock/Azure OpenAI
- **SCIM Provisioning** — auto-provision through Azure AD/Okta
- **Managed Connections** — IT owns app connections, not individuals
- **SOC 2 Type II/III, GDPR, CCPA** — annually audited

### Zapier pricing (for client budgeting)

Prices are in GBP. Zapier MCP is now included on ALL plans including Free.

| Plan | Price/mo (billed yearly) | Tasks/mo | Users | Best For |
|---|---|---|---|---|
| Free | £0 | 100 | 1 | Trial |
| Professional | £15.21 | From 2K | 1 | Small teams |
| Team | £52.51 | From 2K | 25 | Shared workspaces, SAML SSO |
| Enterprise | Contact sales | Custom | Custom | Full governance suite |

Typical usage estimate: 3-step Zap × 20 runs/day × 5 agents = ~9,000 tasks/mo. Fits on Professional at £15/mo.

### Security model

- **Least-privilege scoping:** each agent gets only the tools it needs
- **Approval gates:** external emails and record changes require human approval before execution
- **Kill switch:** client revokes MCP tokens → all access terminates in under 60 seconds
- **Audit logging:** every agent action logged with timestamp, tool, outcome (12-month retention)
- **No data storage:** client data flows through their own MCP connections, not stored on PerformOS systems
- **No model training:** client data passes through the AI model transiently and is never used to train or improve any AI model
- **Anti-spam compliance:** outbound communications comply with Spam Act 2003 (AU), CAN-SPAM, CASL
- **Insurance:** professional indemnity and cyber liability — certificate available on request

### Data sovereignty commitments (for client proposals)

Six commitments that protect the client:

1. **No model training** — client data is never used to train, fine-tune, or improve any AI model
2. **Local session logs** — conversation history logs are stored only on the client's own infrastructure
3. **Client-owned tokens** — client generates and owns all MCP tokens; can revoke at any time
4. **Data residency** — agent processing occurs on Orgo.ai in the client's chosen region; tool data flows through client's own connections
5. **Right to deletion** — client can request complete deletion of agent configurations and stored data at any time
6. **Sub-processor disclosure** — client's data may pass through Orgo.ai (hosting) and Zapier (tools); both maintain SOC 2

### What client procurement requires

Any enterprise procurement/review team will ask for:
1. SOC 2 Type II report (PerformOS + Orgo)
2. Data Processing Agreement (DPA) with purpose limitation, sub-processor disclosure, breach SLA
3. Cyber liability insurance certificate ($5M+ recommended)
4. Architecture diagram showing data flows, storage locations, access controls
5. Kill switch + approval gate documentation
6. Compliance mapping to client's regulatory obligations
7. RACI matrix for liability assignment
8. Termination clause with token revocation and data destruction process

### Onboarding process (2-week sprint)

Week 1:
- Client provisions Orgo Scale account and Zapier Enterprise account
- Client connects tools and generates scoped MCP tokens
- PerformOS builds and configures all 5 agents in Orgo
- MCP tool scoping and testing
- Zapier AI Guardrails and log streaming activation
- Approval workflow setup

Week 2:
- Role-based access configuration
- 2-hour training session for client operations team
- UAT period with client stakeholders
- Go-live

### Support

- 4 hours per month included (performance monitoring, prompt tuning, tool access updates, monthly report)
- Additional hours at $150 AUD/hour

### Proposal output — TWO DOCUMENTS

When Jared asks for proposal materials, produce TWO separate PDFs:

#### Document 1: Client Proposal (external)
- Business-facing, send to prospective clients
- NO internal costs, margins, or cost breakdowns
- Pricing: clearly state $4,995/mo + $3,000 setup
- Include Zapier Enterprise governance table
- Include authorisation flow diagram
- Include 6-step data sovereignty commitments
- Include compliance framework
- Include Zapier pricing for client budgeting (GBP)
- **Do NOT include:** Orgo costs, AI token costs, support costs, margin calculations, or any internal financial data
- **Do NOT name Obsidian** or any specific local tool. Use "local session logging on client infrastructure" or "encrypted local conversation storage"

#### Document 2: Internal Financial Model
- Jared's eyes only — never send to clients
- Full cost breakdown: Orgo hosting, AI token usage, support hours
- Gross margin per client
- Sensitivity analysis at 1x, 2x, 3x usage
- Scale scenarios: 1, 5, 10, 20 clients
- Setup payback period

#### PDF build instructions
1. Use ReportLab (previous builds at `/Users/jc/Desktop/build_client_proposal.py` and `/Users/jc/Desktop/build_internal_financial.py`)
2. Navy (#0B1E3D), red (#E63946), dark (#1A1A2E) colour scheme
3. Send both via Telegram with MEDIA: path
4. Label clearly: "CLIENT PROPOSAL" and "INTERNAL — Financial Model"

## AgentOS page copy and positioning patterns

AgentOS is the product name for the private AI team offer: **AgentOS by PerformOS**.

Category line: **Private AI team for business leaders.**

When creating AgentOS website copy, pricing pages, security pages, solution pages, or hero/demo sections, use `references/agentos-page-copy-patterns.md`. It captures the current pricing, security, solution architecture, and hero conversation animation pattern.

Key rule: do not sell AgentOS as "10 bots" or another AI subscription. Sell it as a managed private AI team built around the client's roles, workflows, approved sources, infrastructure boundary, and leadership rhythm.

## Local Deployment Edition (Updated — June 2026)

A second variant of the package runs on a PerformOS-owned managed local appliance placed in the client's approved environment. No cloud APIs are required for inference, and zero data leaves the approved local environment unless the client chooses an approved integration path. This is a separate product from the Orgo-hosted cloud edition.

**Key differences at a glance:**
- Cloud edition uses Orgo hosting ($324/mo cost) + DeepSeek API tokens
- Local edition uses a PerformOS-owned managed appliance + local inference
- Client does not buy or own the appliance; they provide approved access, custody, and IT governance during the engagement
- Local edition has no per-token costs — unlimited inference
- Local edition can work offline depending on tool integrations
- Two tiers: Standard ($3K setup) and Advanced ($6K setup)
- Both tiers: $4,999/mo, up to 10 fully customisable agents
- 6-month minimum term

**Full product document:** `/Users/jc/Desktop/Obsidian/PerformOS/AI-Team-Package-Local-Spec.md`

**When to pitch local vs cloud:** Local is for clients with data sovereignty requirements, "no external AI" policies, or healthcare/financial/government sectors. Cloud is for clients who want fully managed hosting and multi-device access.

## AI Image Generation for Marketing (New Capability — June 2026)

The Marketing and SEO Strategist agent can generate brand-consistent marketing images.

**How it works:**
1. Feed the agent brand guidelines: logo, colour palette, fonts, reference images
2. Agent builds a brand prompt template from these assets
3. When requested, agent constructs a generation prompt from template + specific brief
4. Fires image generation API, returns result, iterates on feedback

**Image generation API options:**

| Tool | Cost per image | Strengths |
|---|---|---|
| Flux (FAL/Black Forest Labs) | $0.01-$0.05 | Fast, cheap, very good quality |
| OpenAI DALL-E 3 | $0.04-$0.08 | Great quality, good prompt following |
| Midjourney API | $0.04-$0.10 | Best for artistic/marketing visuals |
| Ideogram | $0.02-$0.08 | Best for text in images |

**For brand consistency:** Use image-to-image generation with 3-4 reference images. The model learns the visual style and applies it to new prompts.

**Cost to business:** ~$0.05-$0.10/image. At 50 assets/month = $2.50-$5.00/month.
**Potential revenue add-on:** $200-$500/month per client for "AI marketing asset generator" agent.

**Pitfall:** Client must own or have rights to reference images they provide. Never scrape competitor images for brand training — copyright and trademark risk.

## Cloud Cost Comparison (for client-facing slide decks)

When pitching the Local Edition against cloud AI alternatives, use these verified figures:

**GPT-5.5 API (OpenAI) — 10 agents, heavy use (~2B tokens/month):**
- Input: $15/1M tokens × ~1.5B = ~$22,500
- Output: $60/1M tokens × ~500M = ~$30,000
- Total: ~$10,000-$20,000/month (varies with caching)

**Claude Opus 4 API (Anthropic) — 10 agents, heavy use (~2B tokens/month):**
- Input: $15/1M tokens × ~1.5B = ~$22,500
- Output: $75/1M tokens × ~500M = ~$37,500
- Total: ~$6,000-$12,000/month (varies with caching)

**What the client pays for PerformOS Local: $4,999/month flat.**

**WhatsApp Business API cost reference (if client wants messenger integration):**
- Service rate (cheapest): $0.01-$0.03/conversation (varies by country)
- Marketing rate: $0.06-$0.12/conversation
- 1,000 conversations/month in Australia: ~$20-$95
- Need a BSP (Twilio, WATI, Interakt) adding 10-30% markup
- First 1,000 conversations often free for new accounts (30-90 day window)
- Compare to Telegram API: $0, unlimited messages, no per-conversation cost

## Dashboard and Remote Access Networking

When a client needs to access their agent dashboard from outside their local network:

**Option A — Tailscale Funnel (recommended for most clients):**
- Install Tailscale on the Mac mini + client devices
- Tailscale Funnel exposes the local dashboard via a public HTTPS URL
- Traffic encrypted through Tailscale WireGuard tunnel
- No inbound firewall rules needed on client network
- Free for personal use; Teams plan $15/user/month for business
- Client just opens a URL — no VPN app friction for basic access
- Best balance of security and usability

**Option B — Tailscale Mesh VPN (for technical clients):**
- Install Tailscale on all devices
- Client accesses dashboard via Tailscale private IP
- End-to-end encrypted, zero third-party data exposure
- Free for up to 3 users per network
- Requires client to install and authenticate Tailscale app

**Option C — ngrok (demos and proof-of-concept only):**
- `ngrok http 8081 --host-header=rewrite`
- Gives a public HTTPS URL in seconds
- Free tier: random URL on each restart, rate limited
- Paid: $25/month for reserved domains
- Not suitable for production client use

**Option D — Cloud-hosted dashboard (for clients without strict data policies):**
- Host dashboard frontend on Vercel or DigitalDashboard
- Dashboard talks to Mac mini via outbound connection from Mac mini
- Lowest friction for end users (just a URL)
- Data in transit between cloud and local — some clients will reject this

**Do NOT recommend:** Static-site-only approaches (Cloudflare Pages, pure Vercel) for the chat interface. Chat requires a live connection to Hermes/Ollama on the Mac mini. Static sites cannot proxy interactive AI conversations without a backend relay.

**Practical rollout plan:**
1. Phase 1: Self-contained dashboard + server on Mac mini, local URL only
2. Phase 2: Add Tailscale Funnel for remote access with clean HTTPS URL
3. Phase 3: For enterprise clients, deploy private cloud relay behind their domain

## Lightsail, Ollama, and remote appliance operations

When Jared asks whether Amazon Lightsail should run Hermes agents, Ollama, or part of the PerformOS Local AI Team infrastructure, use `references/lightsail-ollama-hosting.md`.

When Jared asks how to edit, support, troubleshoot, or remotely maintain a client-site Mac/local appliance, use `references/managed-local-appliance-remote-support.md`.

Short answer:
- Lightsail is a good always-on **agent hosting and cloud control layer**.
- Lightsail is not the default AI engine for the Local Edition.
- Start with $24 USD/month for Hermes hosting.
- Test Ollama only on $84 or $168 tiers first for small models.
- For a 19 GB Ollama model, treat 32 GB RAM as tight minimum and 64 GB RAM as comfortable; the $384 USD/month General Purpose Lightsail tier is the first normal Lightsail plan worth serious consideration.
- Treat the $384 USD/month tier as a serious control layer and CPU-only model test host, not an automatic first purchase.
- Keep client-private inference and data sovereignty workflows on the PerformOS-owned local appliance unless the client explicitly approves a cloud integration path.
- Never position a client system as running from Jared's home Mac or home Wi-Fi. Use client-site appliance, private cloud, or hybrid model only.

- **performos-website-builds** — that skill is about building PerformOS-branded website pages as markdown deliverables. This skill is about selling agent packages to clients.
- **lara-programme-build** — that skill is about building training programmes. This skill may reference the Learning Designer agent as one of the 5, but does not cover programme build methodology.
- **zapier-mcp-workflows** — that skill covers Zapier MCP auth, tool signatures, and Accor Plus-specific workflows. This skill references Zapier Enterprise as a governance layer for client proposals.

## Vercel deployment pattern (for quick site-to-live-URL)

When Jared sends "build me a website" or similar and wants a live URL on his phone later:

1. Build the HTML/CSS/JS as a self-contained file
2. Save to `~/Desktop/[site-name]/index.html`
3. `cd ~/Desktop/[site-name] && git init && git add . && git commit -m "Initial"`
4. `gh repo create [site-name] --public --description "..." --source=. --push`
5. `vercel --prod --yes` (from the same directory)
6. Send the Vercel URL to Jared via Telegram — he opens it on his phone

Prerequisites: `gh` CLI authenticated, Vercel CLI logged in, both tested and working as of 29 May 2026.
Jared's Vercel project is under `jaredcroxtons-projects`.

## Hard lines

- **Never scrape competitor websites for branding or product content.** Copyright, trademark, ToS, and hosting-platform violations all apply. Refuse clearly and offer the original-build alternative.
- **Do not use "unlimited contacts" framing.** Drop this language entirely from any client-facing material. It creates spam liability exposure. Use generous usage caps with no overage charges instead.
- **Never include internal costs in client-facing documents.** When Jared says "this is the external one" — strip ALL cost data. Only the package price ($4,995/mo) and setup fee ($3,000) belong in the client document.
- **Never name Obsidian in client documents.** The client does not need to know the specific tools used for local infrastructure. Use generic professional language.

## Pitfalls

- **Two product variants exist.** Cloud (Orgo) edition and Local (Ollama) edition are separate products with different architectures. Always confirm which variant the client needs before pitching. Local is for data sovereignty; Cloud is for fully managed.
- **Security is the lead, not the footnote.** Enterprise clients will reject proposals that lead with features and bury security. Always lead with data governance, approval gates, and compliance.
- **"Yes correct" is not confirmation.** Jared often says "yes correct" to acknowledge a framing question without actually answering follow-up inputs. Always verify you have ALL required data before building. Unanswered questions = wait.
- **Triple-party risk.** The chain is Client → PerformOS → Orgo.ai (cloud edition). Each is a separate security surface. Name the data flow explicitly. Local edition has two main surfaces: Client environment → PerformOS-owned managed appliance. If Lightsail is added as a cloud control layer, name it separately and explain what data does and does not pass through it.
- **Mac Mini over MacBook:** Always recommend Mac Mini for local deployments. It is cheaper (A$1,599 vs ~$2,100+ for MacBook Air with equivalent RAM), designed for always-on desk use, and the client never needs to carry a server. A laptop is the wrong form factor for a dedicated AI agent machine.
- **Token costs are deceptively low (cloud edition).** With caching, 56M tokens costs ~$9/mo. This is the margin lever. Do not frame tokens as the cost driver.
- **Zapier pricing is in GBP.** When converting for Australian clients, apply current exchange rate. Note the currency difference clearly.
- **Two-document discipline.** Always produce both documents when asked for a proposal. External and internal are never the same file. Do not accidentally leak internal margins to a client.

## References

- `references/pricing-model.md` — detailed financial model with sensitivity analysis, token cost breakdown, setup payback period, and model pricing assumptions (Cloud/Orgo edition)
- `references/zapier-pricing.md` — current Zapier Platform and Enterprise pricing in GBP
- `references/local-edition-agents.md` — full agent list, use cases, model selection, hardware tiers, and MCP connections for the Local Edition
- `references/local-edition-governance.md` — Google Drive folder structure, naming conventions, and retention policy for client governance docs
- `references/tier-comparison-deck-language.md` — exact plain-language framing for Standard vs Advanced tiers in client-facing decks and one-pagers. Includes deck layout pattern, pricing display rule, and what never appears in client materials. Written June 2026.
- `references/agentos-pricing-page-pattern.md` — pricing page copy pattern for AgentOS: Standard vs Advanced cards, comparison table language, setup fee explanation, FAQ, and the rule that tiering is reasoning depth, not agent count.

- `references/lightsail-ollama-hosting.md` — Amazon Lightsail guidance for Hermes hosting, Ollama testing, $24/$84/$168/$384 tier logic, 19 GB model sizing, and the strategic split between cloud control layer and PerformOS-owned local appliance.
- `references/managed-local-appliance-remote-support.md` — client-site appliance remote admin, Git-backed agent updates, support escalation, MDM, and the no-home-Wi-Fi positioning rule.

## Version

Locked 06 June 2026 by Jared Croxton. Updated June 2026 with: confirmed AU Mac Mini pricing (M4 24GB/512GB = A$1,599, M4 Pro 48GB/1TB = A$3,399), two-tier Standard/Advanced client-facing deck layout pattern with plain-language model tier descriptions, and reference file for tier comparison language in `references/tier-comparison-deck-language.md`.
