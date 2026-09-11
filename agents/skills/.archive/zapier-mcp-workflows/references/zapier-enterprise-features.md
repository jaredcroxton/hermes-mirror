# Zapier Enterprise — Governance Features for PerformOS Proposals

## Source
https://zapier.com/enterprise (verified 29 May 2026)

## Positioning
Zapier's enterprise pitch: "AI makes everyone a builder. Governance makes it safe."
They position as the AI governance layer that lets companies deploy AI automation safely at scale.

## The three pillars

### 1. CONTROL — Define what runs
- **Action Restrictions** — specify exactly which actions are allowed per app
- **BYOM (Bring Your Own Model)** — run AI through own infrastructure (AWS Bedrock etc). Client keeps existing security and compliance controls
- **Managed Connections** — IT owns the app connections, not individuals. Automations keep running when staff leave
- **Domain Restrictions** — block personal accounts from touching business systems. Prevents data leaving the environment
- **App Access Controls** — allow or block entire apps from the workspace

### 2. DELEGATION — Give teams space
- **Workspaces** — dedicated environments per team with inherited guardrails
- **Guided Templates** — pre-approved starting points so teams build within boundaries
- **Role-Based Access** — control who can view, build, or manage workflows
- **SCIM Provisioning** — auto-provision users through identity provider (Azure AD, Okta)

### 3. VISIBILITY — See everything
- **Asset History** — full audit trail via API (programmatic access to audit data)
- **AI Guardrails** — automatic safety checks that block sensitive data and detect risky inputs before AI outputs reach systems
- **Log Streaming** — real-time workflow data to Datadog, Splunk, or SIEM
- **Canvas Documentation** — auto-generated documentation for every workflow

## Security credentials
- SOC 2 Type II and SOC 3 (annually audited)
- GDPR and CCPA compliant
- 99.9% uptime SLA
- Enterprise SSO via SAML 2.0 + SCIM

## Pricing
Custom/enterprise-sales. Not published publicly. Industry norm for this tier: £500-2,000/mo depending on seats and task volume. Budget £500/mo for proposal planning purposes.

## Why this matters for PerformOS
Enterprise client procurement teams will ask how AI agents are governed in their environment. Zapier Enterprise is the off-the-shelf answer. If a client already uses Zapier (many do), the integration path is trivial and the governance story is easy.

Positioning options:
- **Option A (recommended):** Propose Zapier Enterprise as the governance layer. Agents run on Orgo, connect through Zapier MCP, Zapier handles audit/guardrails/access control.
- **Option B:** Position PerformOS as the governance layer, use only Zapier Professional (£15/mo) for MCP tool connections. Lower client cost but PerformOS carries compliance responsibility.

## Procurement answer map

| Client concern | Zapier Enterprise answer |
|---|---|
| "How do you stop the AI from acting without approval?" | Action Restrictions + Role-Based Access |
| "How do you prevent data leaks?" | AI Guardrails + Domain Restrictions |
| "Where does the AI run?" | BYOM → client's own AWS infrastructure |
| "Can we see what happened?" | Log Streaming + Asset History API |
| "What if someone leaves the company?" | SCIM Provisioning + Managed Connections |
| "Is it audited?" | SOC 2 Type II/III, annual |
| "What's the uptime guarantee?" | 99.9% SLA |
