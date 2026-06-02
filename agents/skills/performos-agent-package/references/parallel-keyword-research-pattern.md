# Parallel Sub-Agent Keyword Research for Google Ads

Captured 02 June 2026 from the AgentOS keyword research task.

## Pattern: Two parallel keyword research tasks, one synthesis

When researching Google Ads keywords for a new product:

1. **Delegate two parallel tasks** via `delegate_task` (tasks array, two items).
2. **Task 1: Core positioning keywords.** Research keywords that match the product's exact positioning. Use web_search and firecrawl tools. Focus on commercial intent, search volume, competition, and CPC.
3. **Task 2: Decision-maker / alternative keywords.** Research keywords targeting buyers looking for alternatives or making purchase decisions. Focus on enterprise/premium intent keywords.
4. **Synthesize in Brock** — combine both results into one report. Structure as tiers (blue-ocean differentiators, core category, volume drivers). Add campaign structure, negative keywords, budget estimates, and ROI projections.

## Sub-agent task spec

Each sub-agent gets:
- Short context paragraph about the product (what it is, price, target market)
- Clear goal statement ("Research the top 15 keywords...")
- Specific output format request ("Return as a structured table")
- Toolset: ["web", "terminal"]
- Target market modifier (e.g. "Australian market")

## Synthesis structure

The final report should include:
1. Market benchmark table (CPC, CTR, CPA by industry)
2. 30 keywords ranked and tiered
3. Campaign structure (3 ad groups with bid ranges and landing pages)
4. Negative keyword list
5. Budget and ROI projection
6. Key strategic insight (what to bid on first)

## What worked

- Running two research agents in parallel cut total time in half vs sequential
- Each agent found different keyword angles — one found the "blue ocean" terms, the other found the "ChatGPT alternative" angle
- Synthesis produced richer output than either agent alone
- Firecrawl agent tool was used for deep research but timed out — web_search + web_extract were the reliable fallback

## What to avoid

- Don't delegate a single monolithic keyword research task — the sub-agent will spend too long and may time out
- Don't ask sub-agents to produce the final formatted report — leave synthesis to the orchestrator
- Always specify the target market in the sub-agent context (country, language, currency)
