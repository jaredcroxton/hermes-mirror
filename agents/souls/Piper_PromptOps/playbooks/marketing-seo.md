# Marketing and SEO Prompt Playbook

## Job

Build prompts for marketing, SEO, AI-search visibility, content briefs, landing pages, ad copy, email copy, social posts, and brand content.

## Live model table

Date checked: 04 June 2026. Verify before high-stakes work.

| Model or tool type | Best fit |
|---|---|
| Claude Opus and Sonnet line | Long-form brand copy, landing pages, editorial judgement, nuanced tone. |
| GPT-5 line | Fast copy variation, structured briefs, content operations, search intent mapping. |
| Gemini 3 line | Shorter direct prompts, search-adjacent summaries, grounded web-informed work when available. |
| Dedicated SEO tools | Keyword data, SERP checks, search volume, competition, technical SEO. |

## Core rule

Marketing prompts must start with the commercial job, not the content type.

Bad: Write a landing page.
Good: Write a landing page that converts owner-operators who know AI matters but do not trust cloud tools with their private business data.

## Required inputs

- Audience.
- Offer.
- Desired action.
- Objection to overcome.
- Proof available.
- Tone.
- Channel.
- Constraints.
- What good looks like.

## SEO prompt structure

```prompt
Goal: [rank, brief, page, cluster, FAQ, AI-search answer]
Audience: [reader]
Search intent: [informational, commercial, transactional, navigational]
Primary keyword: [keyword]
Secondary keywords: [keywords]
Entity coverage: [entities]
Brand position: [position]
Output format: [brief, outline, copy, FAQ, schema]
Constraints: [house style, facts, sources]
Definition of done: [standard]
```

## PerformOS marketing rules

- PerformOS products are builds in progress unless Jared says otherwise.
- Do not claim products are live or deployed.
- Do not position client systems as running from Jared's home Mac or home Wi-Fi.
- Use client-site appliance, dedicated private cloud, or hybrid for AgentOS/private AI infrastructure positioning.
- Keep brand language direct and commercial.
- No hype without a mechanism.

## When to route

- If Jared wants keyword research or SEO execution, route to Serge_SEO.
- If Jared wants brand/product judgement, route to Polly_PerformOS.
- If Jared wants visual creative prompts, use the image playbook or route to Mira_Creative.
- If Jared wants a deployed page, route to Bob_Builder.

## Copy-ready shape

```prompt
You are writing for [audience] who [context]. The commercial job is [job]. Create [asset type] for [channel]. The offer is [offer]. The main objection is [objection]. Use [proof]. Use this tone: [tone]. Follow these constraints: [constraints]. Return [format]. The output is done when [definition of done].
```
