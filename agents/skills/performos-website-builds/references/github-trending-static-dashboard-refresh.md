# GitHub trending static dashboard refresh pattern

Use when Jared asks to update an existing live dashboard with "new GitHubs", repos released recently, or repos trending in the last few days.

## Durable pattern

1. Treat the dashboard as a data refresh first, not a redesign.
2. Locate the existing repo and inspect both the rendered HTML and any data mirror such as `data/sample.json`.
3. Pull candidates from GitHub with `gh api search/repositories`, using date-bounded queries such as:
   - `created:>=YYYY-MM-DD image generation stars:>3`
   - `created:>=YYYY-MM-DD video generation stars:>3`
   - `created:>=YYYY-MM-DD ComfyUI stars:>0`
   - `created:>=YYYY-MM-DD ai agents stars:>3`
   - `created:>=YYYY-MM-DD llm stars:>3`
4. De-duplicate by `full_name` and filter obvious spam, adult-content bait, jailbreak bait, tinyurl-heavy descriptions, archived repos, disabled repos, and private repos.
5. Prefer a balanced editorial set, not only raw stars. For Jared's AI pulse dashboards, include image generation, video generation, audio/TTS, agents, local AI, LLM, MCP, GPU, and dev-tool repos where relevant.
6. Update both the external JSON file and the embedded `RAW_DATA` payload in the HTML. Re-embed from the final JSON last, after all copy/date replacements, so the embedded payload cannot drift from the source data.
7. Update visible UI language so the dashboard clearly shows it is now a GitHub repo pulse, not a story/news pulse. Example labels: `repos tracked`, `View repo`, `Search repos...`, `GitHub pulse`.
8. Add or update topic filters to match the new dataset. Example filters: Image Gen, Video Gen, Audio, Agents, LLM, Local, Dev Tools.
9. Verify locally with DOM checks before deploying:
   - card count equals JSON count
   - all links are GitHub links
   - visible date is current
   - old story terms are absent
   - topic filters return the expected subset count
   - browser console has no JS errors
10. Deploy with Vercel production from the repo and verify the clean alias with a cache-busting URL.
11. Commit and push only the intended tracked files after deployment. Leave unrelated untracked files alone.

## Alternative data source: Firecrawl Trending scrape

When `gh api` is unavailable or you want the human-facing GitHub Trending page data (with "stars this week" growth numbers), use Firecrawl MCP to scrape `https://github.com/trending?since=weekly` directly. See `references/firecrawl-github-trending-scrape.md` for the full method, field mapping, and HN/PH cross-reference notes. The Firecrawl approach surfaces growth data that `gh api` cannot provide.

## Pitfall

Do not use broad text replacements after embedding JSON if the replacement target could appear inside the data payload. If you must replace visible copy after embedding, re-embed the final JSON again before verification.