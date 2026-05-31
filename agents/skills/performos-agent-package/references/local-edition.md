# PerformOS AI Team Package — Local Edition Reference

## What Changed (30 May 2026)

The original skill covered the **cloud-hosted Orgo edition**. This reference file covers the **local deployment edition** — a separate product variant that runs entirely on client hardware.

## Architecture Difference

| Aspect | Cloud (Orgo) Edition | Local Edition |
|---|---|---|
| Hosting | Orgo Scale ($324/mo) | PerformOS-owned managed local appliance |
| Ownership | Cloud environment | PerformOS owns hardware; client has approved custody during engagement |
| Models | Cloud API (DeepSeek, etc.) | Local inference (Llama, Phi, Qwen) |
| Data | Orgo infrastructure | Approved local environment only |
| Token cost | ~$9-18/mo | $0 (local inference) |
| MCP | Zapier Enterprise | Client-approved MCP servers and local connectors |
| Setup | Build in Orgo terminal | PerformOS configures appliance, client IT reviews and connects |
| Internet | Required | Depends on tool integrations; local inference can work offline |

## Hardware Tiers

| Tier | Machine | RAM | Agents | Models |
|---|---|---|---|---|
| Standard | MacBook Air M5 | 24 GB | 5 agents | Llama 3.1 8B |
| Professional | MacBook Pro M5 Pro | 48 GB | 10 agents | Mix 8B + 14B |
| Enterprise | Mac Studio M5 Ultra | 128 GB | 10+ agents | Phi-4 14B + Qwen 2.5 14B |

## Model Selection by Agent

| Agent | Model | RAM |
|---|---|---|
| CEO / Strategic Advisor | Phi-4 14B Q4_K_M | ~10 GB |
| HR & Compliance | Llama 3.1 8B Q4_K_M | ~6 GB |
| Learning Designer | Phi-4 14B Q4_K_M | ~10 GB |
| Builder | Qwen 2.5 14B Q4_K_M | ~10 GB |
| Research | Llama 3.1 8B Q4_K_M | ~6 GB |
| Personal Assistant | Llama 3.1 8B Q4_K_M | ~6 GB |
| Sales Coach | Llama 3.1 8B Q4_K_M | ~6 GB |
| Legal Advisor | Phi-4 14B Q4_K_M | ~10 GB |
| Study Partner | Llama 3.1 8B Q4_K_M | ~6 GB |
| SEO Strategist | Llama 3.1 8B Q4_K_M | ~6 GB |

Total RAM at full load: ~78 GB. Ollama model swapping means 48GB machines handle 10 agents by loading on demand.

## Internal Cost Model — Local Edition

| Item | Monthly |
|---|---|
| Jared's time (~1 hr call + ad-hoc) | ~$500 |
| Course curation | ~$50 |
| Ollama + Hermes (open source) | $0 |
| MCP maintenance | ~$100 |
| **Total** | **~$650** |
| **Revenue** | **$4,999** |
| **Margin** | **~$4,349 (87%)** |

No Orgo hosting costs. No token costs. Margin is higher than the cloud edition.

## Full Spec Location

The complete product spec including all 10 agent use cases, Business Needs Questionnaire, onboarding process, and competitive positioning is at:

`/Users/jc/Desktop/Obsidian/PerformOS/AI-Team-Package-Local-Spec.md`

## When to Pitch Local vs Cloud

- **Local edition:** Client has "no external AI" policy, data sovereignty requirements, healthcare/financial/government sectors, wants zero ongoing token costs
- **Cloud (Orgo) edition:** Client wants fully managed hosting, does not want to maintain hardware, needs agents available on multiple devices

## Sales Note

Lead with data governance. The opening line: "You would not send your company data to ChatGPT. Why would you send it to an AI agent service?"

## The 10 Agents — Quick Reference

1. CEO / Strategic Advisor — board prep, decision framing, stakeholder pressure-testing
2. HR & Compliance — employment law, incident mapping, legislation quoting (AU/NZ/IN/ID/PH/TH/VN)
3. Learning Designer — full programme build, assessments, facilitation guides, PDF packs
4. Builder & Deployer — dashboards, automations, internal tools, slide decks
5. Research & Synthesis — document digestion, briefing packs, market intel
6. Personal Assistant — email triage, meeting prep, follow-up tracking
7. Sales Coach — AI roleplay, objection handling, scored feedback
8. Legal & Commercial — contract review, risk flagging, IP and privacy
9. Study & Development Partner — academic support, assignment structuring, study plans
10. SEO & Content Strategist — keyword research, content plans, audits, drafts
