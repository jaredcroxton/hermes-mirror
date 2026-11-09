# PerformOS Sub-Agent Ecosystem

Added June 2026. Polly (PerformOS product agent) now orchestrates six specialist sub-agents, each an expert on one PerformOS product or offering.

## The six sub-agents

| Agent | Soul file | Product | Status |
|---|---|---|---|
| OnboardOS | onboardos-soul.md | $499 12-week AI course | Planned |
| AgentOS | agenthos-soul.md | Private AI team for business | Product dev |
| Pocket Customer | pocketcustomer-soul.md | AI voice roleplay coach | Live |
| PulseCheck360 | pulsecheck360-soul.md | Flight-risk detection | Paused |
| Performolytics | performolytics-soul.md | AI business intelligence | Build in progress |
| LearnOS | learnos-soul.md | Custom LMS | Live |

Souls live at: `/Users/jc/Desktop/Obsidian/Agents/`

## Product catalogue order

The four PerformOS instruments (catalogue positions):
1. **Performolytics** — data intelligence
2. **Pocket Customer** — sales intelligence
3. **PulseCheck360** — people intelligence
4. **LearnOS** — learning intelligence

Plus two offerings that sit alongside the instruments:
- **OnboardOS** — $499 direct-to-consumer AI course (entry point)
- **AgentOS** — private AI team for businesses (enterprise product)

## Routing logic

- Route product-specific deep questions to the specialist sub-agent
- Polly handles cross-product and suite-level questions directly
- Sub-agents do not invoke each other — orchestration goes through Polly
- Brock can route to any sub-agent during cross-agent workflows

## When to create a new sub-agent

Create a new sub-agent when:
- A product gets its own pricing, positioning, and audience
- The product knowledge exceeds what Polly's soul can hold
- The product has distinct brand visuals and voice rules
- Jared asks product-specific questions that need a dedicated expert
