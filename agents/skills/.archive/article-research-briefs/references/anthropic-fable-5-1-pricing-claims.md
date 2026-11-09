# Anthropic Fable 5.1 pricing claims research

Session date: 02 September 2026

## Core finding

Fable 5.1 was widely described as cheaper, lower cost, or up to 45% cheaper, but credible coverage did not support a clean claim that the whole model or base API price is 50% cheaper.

Official pricing:
- Fable 5.1 base input: $10 / MTok
- Fable 5.1 base output: $50 / MTok
- Fable 5.1 cache reads: $0.25 / MTok
- Fable 5 cache reads: $1 / MTok
- Cache-read cut: 75%
- Anthropic estimated practical savings: around 25% for typical workloads, up to around 45% for highly agentic workloads

The durable angle: Anthropic did not cut Fable's sticker price. It cut the cost of repeated context. This is pricing for agentic workloads, not normal chat.

## Strong references

### Anthropic official announcement
URL: https://www.anthropic.com/claude-fable-and-mythos-5-1
Claim: Fable 5.1 costs an estimated 25% less than Fable 5 for typical workloads because cache reads are cheaper. Highly agentic work can save up to around 45%. Cache reads cost $0.25 per million tokens, 75% less.
Classification: accurate, primary source.

### Anthropic pricing page
URL: https://platform.claude.com/docs/en/about-claude/pricing
Claim: Fable 5.1 is $10 input / $50 output per MTok. Cache hits are $0.25 / MTok. Fable 5 cache hits were $1 / MTok. Fable 5.1 and Mythos 5.1 use 0.025x base input for cache reads, while most other models use 0.1x.
Classification: accurate, primary source.

### VentureBeat
URL: https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads
Claim: Headline says 75% cost reduction for Fable cache reads. Article notes ordinary input and output remain $10/$50, while effective cost drops around 25% for typical workloads and roughly 45% for highly agentic workloads.
Classification: accurate and useful.

### TechCrunch
URL: https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/
Claim: Headline says Fable release is cheaper and less restrictive. Description says Fable 5.1 includes changes meant to reduce token cost and false-positive restrictions.
Classification: broad but defensible. Useful example of simplified media framing.

### The New Stack
URL: https://thenewstack.io/anthropic-fable-5-1-launch/
Claim: Headline says Fable 5.1 is a bit cheaper. Article says pricing remains unchanged at $10/$50, but cache reads are now $0.25 per million, down 75%.
Classification: accurate and nuanced.

### MarkTechPost
URL: https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/
Claim: 75% cheaper cache reads, roughly 25% lower cost on typical workloads, up to 45% on agentic ones, base input/output unchanged at $10/$50.
Classification: accurate.

### The Decoder
URL: https://the-decoder.com/anthropics-claude-fable-5-1-promises-better-coding-and-research-at-up-to-45-percent-less/
Claim: Up to 45% less, about 25% less for typical workloads, cache reads cut from $1 to $0.25, all other API prices unchanged at $10/$50.
Classification: accurate.

### MacRumors
URL: https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/
Claim: Fable 5.1 costs approximately 25% less for typical workloads and up to 45% for highly agentic work. Base pricing remains the same.
Classification: accurate.

### Neowin
URL: https://www.neowin.net/news/anthropic-launches-claude-fable-51-and-mythos-51-with-lower-costs-and-fewer-restrictions/
Claim: Lower costs, cache reads cut by 75%, around 25% cheaper than Fable 5 for average workload, up to 45% savings.
Classification: mostly accurate, headline is broad.

### Firstpost
URL: https://www.firstpost.com/tech/anthropic-bets-on-lower-costs-and-stronger-coding-with-claude-fable-5-1-and-mythos-5-1-14042506.html
Claim: Fable 5.1 would cost an estimated 25% less for typical workloads, up to around 45% for highly agentic work, cache reads reduced by 75%.
Classification: broad but grounded.

### USA Herald
URL: https://usaherald.com/fable-5-1-launch-slashes-prices-while-doubling-science-benchmark-scores/
Claim: Headline says slashes prices. Body says cache reads drop 75% to $0.25, translating to 25% lower costs for typical workloads and up to 45% for agentic tasks.
Classification: headline loose, body accurate.

## 50% or half-price drift

### Anthropic Opus 5 announcement
URL: https://www.anthropic.com/news/claude-opus-5
Claim: Opus 5 comes close to frontier intelligence of Fable 5 at half the price.
Classification: official but adjacent. This is Opus 5 versus Fable 5, not Fable 5.1.

### Coding Beauty / Beehiiv
URLs:
- https://medium.com/coding-beauty/new-claude-opus-5-89213eb8ba64
- https://codingbeautydev.beehiiv.com/p/claude-opus-5-just-changed-everything
Claim: Opus 5 is more powerful than Fable 5 in several critical areas, yet 50% cheaper.
Classification: adjacent. Not evidence that Fable 5.1 is 50% cheaper.

### Social posts surfaced by Firecrawl
Examples:
- https://www.instagram.com/reel/DZYdGEByI3Q/
- https://www.instagram.com/reel/DZYfrpYjIWt/
- https://www.threads.com/@anferneeck/post/DZY4dgmlgwO/claude-fable-and-claude-mythos-fable-and-mythos-can-work-autonomously-for/
Claims included: 50% cheaper, same $5/$25, Opus 5 competitor, Fable 5.1 could be dropping.
Classification: misleading or adjacent. These appear to conflate Opus 5 pricing with Fable/Fable 5.1.

## Recommended framing for Jared

Avoid: "Fable 5.1 is 50% cheaper."

Use: "People are calling Fable 5.1 cheaper, and some are drifting into half-price language. But the real story is more interesting. Anthropic did not cut the model's sticker price. It cut the cost of repeated context. That tells you the product is no longer chat. It is agents."

Short line:
"Fable 5.1 is not a 50% API price cut. It is a 75% cache-read cut that makes agentic workloads cheaper."

## Research workflow lesson

For live pricing claims:
1. Search exact claim strings first, including quoted phrases such as "50% cheaper", "half the cost", "up to 45%", and "75% cheaper cache reads".
2. Scrape primary pricing pages and official launch pages before evaluating secondary articles.
3. Classify sources as accurate, misleading, or adjacent.
4. Separate sticker/base API price from effective workload cost, cache-hit cost, batch discount, and cost per benchmark task.
5. For social posts, treat search snippets as lead signals only. Do not make them authoritative unless the page content is directly accessible and the claim can be quoted.