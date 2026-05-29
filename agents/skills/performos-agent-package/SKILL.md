---
name: performos-agent-package
description: Use when Jared asks about selling or positioning the PerformOS 5-agent bundle to clients. Covers pricing model, token budget, security framing, compliance checklist, proposal structure, and internal financial model.
tags: [performos, sales, pricing, agent-package, commercial, zapier]
---

# PerformOS 5-Agent Package — Commercial Model

## Trigger
Use when Jared asks about selling agent packages to businesses, positioning PerformOS to clients, updating proposal PDFs, discussing pricing and margins, or building Zapier-powered automations for clients.

## The offering

PerformOS sells a managed 5-agent team to enterprise clients. The client gets pre-built specialist AI agents running on their own infrastructure, with their own data and tool connections.

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

## Do not confuse with

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

- **Security is the lead, not the footnote.** Enterprise clients will reject proposals that lead with features and bury security. Always lead with data governance, approval gates, and compliance.
- **"Yes correct" is not confirmation.** Jared often says "yes correct" to acknowledge a framing question without actually answering follow-up inputs. Always verify you have ALL required data before building. Unanswered questions = wait.
- **Triple-party risk.** The chain is Client → PerformOS → Orgo.ai. Each is a separate security surface. Name the data flow explicitly.
- **Token costs are deceptively low.** With caching, 56M tokens costs ~$9/mo. This is the margin lever. Do not frame tokens as the cost driver.
- **Zapier pricing is in GBP.** When converting for Australian clients, apply current exchange rate. Note the currency difference clearly.
- **Two-document discipline.** Always produce both documents when asked for a proposal. External and internal are never the same file. Do not accidentally leak internal margins to a client.

## References

- `references/pricing-model.md` — detailed financial model with sensitivity analysis, token cost breakdown, setup payback period, and model pricing assumptions
- `references/zapier-pricing.md` — current Zapier Platform and Enterprise pricing in GBP

## Version

Locked 29 May 2026 by Jared Croxton. Updated with 200 interactions/agent/day model, two-document proposal pattern, Zapier authorisation flow, and Obsidian naming rule.
