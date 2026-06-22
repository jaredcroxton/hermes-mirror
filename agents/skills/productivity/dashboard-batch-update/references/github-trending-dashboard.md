# GitHub Trending Dashboard — Session Reference

## Dashboard File
`/Users/jc/Desktop/hermes_builds/github-ai-dashboard/dashboard.html`

## Batch JSON Pattern
Saved as: `/Users/jc/Desktop/hermes_builds/github-ai-dashboard/batch_YYYYMMDD.json`

Each batch JSON contains:
- `batch_id`: e.g., "batch5"
- `label`: e.g., "Week 22 June 2026"
- `date`: ISO date
- `repos`: Array of 15 repo objects with name, description, stars, growth, url, why, signal
- `cross_signals`: Object with `hacker_news` and `product_hunt` notes

## HTML Template Key Anchors for Patching

### Tab nav anchor:
New tab button goes FIRST inside `<div class="tab-nav">`, marked `active`. Old active loses `active`.

### Tab panel anchor:
New `<div class="tab-panel active" id="batchN"></div>` goes FIRST. Old active loses `active`.

### BATCHES object anchor:
New batch key goes FIRST in the BATCHES object: `'batchN': [ ... ],` inserted before current top batch.

### renderTab anchor:
New `renderTab('batchN');` goes FIRST in the renderTab sequence.

### Timestamp anchor:
`Last updated: DD Month YYYY | Live scrape from GitHub Trending (weekly)`

## GitHub Trending Scrape Notes

- URL: `https://github.com/trending?since=weekly`
- `firecrawl_scrape` with `formats: ["markdown"]`, `maxAge: 300`, `onlyMainContent: true`
- Parse "X,XXX stars this week" for growth numbers
- Repo URL: `https://github.com/{owner}/{repo}`

## HN Scrape Notes

- URL: `https://news.ycombinator.com`
- Cross-reference repo names against HN story titles
- Format: "HN #RANK, POINTS points"

## Product Hunt Scrape Notes

- URL: `https://www.producthunt.com`
- Direct repo matches are rare; note related agent/AI products as context
- Format: "PH #RANK, UPVOTES upvotes"

## Batch History

| Batch | Label | Date |
|-------|-------|------|
| batch1 | Week 01 June 2026 | 2026-06-01 |
| batch3 | Week 08 June 2026 | 2026-06-08 |
| batch4 | Week 15 June 2026 | 2026-06-15 |
| batch5 | Week 22 June 2026 | 2026-06-22 |
