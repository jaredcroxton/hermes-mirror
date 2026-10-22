# Firecrawl GitHub Trending scrape (alternative to gh api)

Use when `gh api search/repositories` is unavailable, you want the actual human-facing GitHub Trending page data (not search results), or you need growth numbers ("stars this week") that `gh api` does not surface.

## Method

```
firecrawl_scrape → url: "https://github.com/trending?since=weekly" → formats: ["markdown"] → onlyMainContent: true
```

The markdown output is parseable. Each repo entry follows this structure:

```
## [owner /  repo-name](https://github.com/owner/repo-name)

Description text...

Language[star_count](stargazers link) [fork_count](forks link)
Built by... [avatar list]
X,XXX stars this week
```

## What you get vs gh api

| Field | gh api search | Firecrawl Trending |
|---|---|---|
| Stars | ✅ | ✅ |
| Description | Only if in repo metadata | ✅ Full description |
| Growth (stars this week) | ❌ Not available | ✅ "X,XXX stars this week" |
| Language | ✅ | ✅ |
| Forks | ✅ | ✅ |
| Contributors | ❌ | ✅ Avatars listed |
| Trending rank | ❌ | ✅ Implicit from order |

## Cross-referencing with HN and Product Hunt

Firecrawl can scrape HN front page and Product Hunt in parallel for signal badges. But in practice, GitHub trending repos rarely appear on HN or PH front pages simultaneously. HN features mostly non-repo content (articles, Show HN). PH features products, not raw repos.

**Recommendation:** scrape HN and PH for cross-reference, but expect near-zero matches. Include `hn_rank: null` and `ph_upvotes: null` in the batch JSON. The scraping is cheap (1 credit each) and occasionally catches a match.

## Pitfalls

- **Firecrawl cache.** The response may be cached (look for `cacheState: "hit"` in metadata). For a weekly cron job, the cache is usually fresh enough. For same-day re-scrapes, the cached result may be stale — force a fresh scrape if the data looks identical to a previous run.
- **Stars vs growth.** The page shows total stars and "stars this week." The "stars this week" number is the growth metric. Do not confuse total stars for growth.
- **Repo count.** The trending page shows 25 repos. Only the top 15-20 have meaningful descriptions. Parse what you can and discard repos with empty or near-empty descriptions.
