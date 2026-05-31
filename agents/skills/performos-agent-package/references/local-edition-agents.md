# Local Edition — Agent Details and Use Cases
# Full spec: ~/Desktop/Obsidian/PerformOS/AI-Team-Package-Local-Spec.md
# Live deck: https://performos-ai-team-deck.vercel.app

## The 10 Agents

| # | Agent | Model Rec | Role |
|---|---|---|---|
| 1 | CEO Advisor | Phi-4 14B | Board prep, strategic alignment, decision framing |
| 2 | HR and Compliance | Llama 3.1 8B | Employment law, incident mapping, 7 APAC markets |
| 3 | Learning Designer | Phi-4 14B | Training programmes, assessments, facilitation guides |
| 4 | Builder and Deployer | Qwen 2.5 14B | Dashboards, automations, HTML tools, slide decks |
| 5 | Research and Synthesis | Llama 3.1 8B | Document digestion, synthesis, knowledge bases |
| 6 | Chief of Staff | Llama 3.1 8B | Email triage, meeting prep, follow-up tracking |
| 7 | Sales Coach | Llama 3.1 8B | AI roleplay, objection handling, scored feedback |
| 8 | Legal Advisor | Phi-4 14B | Contract review, risk flagging, IP and privacy |
| 9 | Study Partner | Llama 3.1 8B | Academic support, assignments, study plans |
| 10 | SEO Strategist | Llama 3.1 8B | Keyword research, content plans, audits, drafts |

## Model Selection Rationale
- Phi-4 14B for complex reasoning: CEO Advisor, Learning Designer, Legal Advisor
- Qwen 2.5 14B for code and build tasks: Builder and Deployer
- Llama 3.1 8B for all others: reliable, fast, low memory

## Hardware Requirements
| Tier | Machine | RAM | Agents | Total Model RAM |
|---|---|---|---|---|
| Standard | MacBook Air M5 | 24 GB | 5 agents | ~30 GB (swap) |
| Professional | MacBook Pro M5 Pro | 48 GB | 10 agents | ~42 GB |
| Enterprise | Mac Studio M5 Ultra | 128 GB | 10+ agents | ~42 GB (comfortable) |

## MCP Server Connections
- Gmail / Google Workspace — email, calendar, docs, sheets
- Slack / Teams — internal communications
- CRM (HubSpot, Salesforce, custom) — customer data
- File system — local documents, policies, procedures
- Web search — research and market intelligence
- Internal databases — via custom MCP connectors

## Onboarding Process (10 Hours)
1. Discovery call (2 hrs) — business context, priorities, tool mapping
2. Agent configuration (2 hrs) — MCP connections, soul files, model selection
3. Integration and testing (2 hrs) — real data, approval gates, audit logging
4. Team training (2 hrs) — operations handover, prompt engineering basics
5. Go-live (2 hrs) — stakeholder demo, documentation, schedule first call

## Pricing
- Standard setup: $3,000 AUD
- Advanced setup: $6,000 AUD
- Monthly retainer: $4,999 AUD (up to 10 agents, unlimited local inference)
- Additional agents: $500/agent/month
- Monthly optimisation call: 1 hour included
- Quarterly refresher: 2 hours included
- Ad-hoc optimisation: $350/hour beyond included hours
- Minimum engagement: 6 months
- PerformOS owns the managed local appliance; client does not own hardware. Contract must cover custody, damage, return, recovery, and wipe process.