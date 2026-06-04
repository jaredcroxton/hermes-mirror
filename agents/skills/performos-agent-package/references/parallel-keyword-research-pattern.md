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

## Handling partial results

When one subagent times out (600s limit) or is interrupted:

- Do not block synthesis waiting for the missing agent. The surviving agents usually return enough keyword data to build the report.
- Note which agent timed out in the final report as a data limitation.
- If the timed-out agent was doing deep competitor scraping, the competition ratings can still be estimated from SERP clues gathered by the keyword agent.
- If the timed-out agent was doing trend research, note that search history data is unavailable and rely on SERP evidence and related-query logic.
- The orchestrator should never retry the same monolithic task that timed out — it will likely time out again.
- **SERP/competitor deep-dive subagents can time out at 600s when they make too many firecrawl scrape calls.** If the task asks for scraping 10+ competitor sites plus SERP analysis in one subagent, it will likely exceed the timeout. Split into: (a) SERP discovery via firecrawl_search only, and (b) deep-dive scraping of the top 3-5 competitors in a separate subagent. Example from AgentOS keyword research 02 June 2026: one subagent completed in 90s (search-only), the SERP/competitor landscape subagent hit 317s and was interrupted mid-work after 7 searches and 14 scrapes.

## Hermes agents keyword research findings (03 June 2026)

When researching keywords for "Hermes agents" / private AI agents in Australia, the parallel subagent approach produced 35 keywords across 5 clusters. Key findings:

- **"Hermes agents" alone is ambiguous** — requires negative keywords for courier, fashion, mythology, and open-source traffic. Use "Hermes AI agents" or "Hermes agents for business" as the primary branded terms.
- **Highest commercial intent:** "custom AI agents Australia", "custom AI agents for business", "AI agent development Australia", "managed AI agents for business", "private AI agents for business".
- **Blue-ocean positioning:** "AI team for business", "AI employee for business", "AI employees Australia" — less crowded, strong fit for AgentOS positioning.
- **Bridge terms** (from known categories): "secure ChatGPT for business Australia", "custom GPT for business Australia", "AI assistant for company data".
- **Three research angles that worked:** (1) core positioning keywords, (2) competitor/SERP landscape, (3) search history/trend signals. All three in parallel, synthesized by Brock.
