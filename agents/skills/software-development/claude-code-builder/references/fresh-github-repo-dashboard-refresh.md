# Fresh GitHub repo dashboard refresh pattern

Use when Jared asks to refresh a live dashboard with new GitHub repositories, especially when he says nothing should be copied from the previous version and the content must be from the last five days.

## Trigger language

- Update this with new GitHubs.
- Nothing copied from before.
- Released in the last five days.
- Trending in the last five days.
- Include image generation, video generation, AI tools, agents, or similar.

## Source strategy

Prefer GitHub's repository search API through `gh api` for structured freshness checks:

```bash
gh api -X GET search/repositories \
  -f q='created:>=YYYY-MM-DD image generation stars:>3' \
  -f sort=stars \
  -f order=desc \
  -f per_page=30
```

Run multiple targeted queries, then deduplicate by `full_name`:

- `created:>=YYYY-MM-DD image generation stars:>3`
- `created:>=YYYY-MM-DD video generation stars:>3`
- `created:>=YYYY-MM-DD image-to-video stars:>3`
- `created:>=YYYY-MM-DD ComfyUI stars:>3`
- `created:>=YYYY-MM-DD diffusion stars:>3`
- `created:>=YYYY-MM-DD ai agents stars:>3`
- `created:>=YYYY-MM-DD llm stars:>3`
- `created:>=YYYY-MM-DD mcp stars:>3`
- `created:>=YYYY-MM-DD local ai stars:>3`

Use the current date to calculate the five-day window. For example, on 09 June 2026, use `created:>=2026-06-04`.

## Curation rules

- Exclude repositories with obvious spam, adult/NSFW bait, piracy, cracks, or jailbreak bait in the name or description.
- Prefer repos with meaningful descriptions, recent `pushed_at`, and clear relevance to AI tooling.
- Include a visible mix of categories, not only agent tooling:
  - image generation
  - video generation
  - audio/TTS
  - agents
  - LLM/local models
  - MCP/dev tools
  - GPU/inference where relevant
- Do not reuse old links from the previous dashboard. Compare against the previous source data before writing.

## Data replacement rules

For static single-file dashboards, update both:

1. the source data file, for example `data/sample.json`
2. the embedded HTML data payload, for example `var RAW_DATA = [...]`

Also update visible UI language from story/news language to repository language:

- `stories` → `repos`
- `Read story` → `View repo`
- `Search stories...` → `Search repos...`
- date marker → current DD Month YYYY

Add or update topic filters to match the new category set:

- Image Gen
- Video Gen
- Audio
- Agents
- LLM
- Local
- Dev Tools

## Verification checklist

Before deployment:

- JSON parses.
- Expected item count renders, usually 30.
- All links start with `https://github.com/`.
- Old story terms are absent from HTML and data.
- Created dates fall within the requested freshness window.
- Image/video generation counts are non-trivial if requested.
- Embedded HTML data matches the source JSON, not stale substituted dates.
- Em dash count is zero.

After deployment:

- Production alias returns HTTP 200.
- Browser DOM check shows the expected number of cards.
- Browser DOM check shows the expected number of GitHub links.
- Cache-busted URL shows the new date marker.
- A category filter such as Video Gen reduces the visible count and every visible card carries that tag.
- Browser console has no JavaScript errors.
- Commit and push only intended source/data files.
