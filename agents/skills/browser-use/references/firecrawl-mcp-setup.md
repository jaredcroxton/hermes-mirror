# Firecrawl MCP Setup

Firecrawl MCP is a scraping API that runs as an MCP server in Hermes, giving all agents access to web extraction tools.

## Package

```bash
npx firecrawl-mcp
```

NOT `@anthropic/firecrawl-mcp` — that package does not exist.

## Setup (already done on Jared's machine)

```bash
# 1. Get API key from https://firecrawl.dev
# 2. Add to .env (uncommented):
echo 'FIRECRAWL_API_KEY=***' >> ~/.hermes/.env

# 3. Clean any commented-out duplicate keys in .env
# 4. Register MCP server with env var:
hermes mcp add firecrawl --command npx --args '-y firecrawl-mcp'
# Then edit config.yaml to add env.FIRECRAWL_API_KEY and set enabled: true

# 5. Test:
hermes mcp test firecrawl
```

## Config (in ~/.hermes/config.yaml)

```yaml
mcp_servers:
  firecrawl:
    command: npx
    args:
      - '-y'
      - 'firecrawl-mcp'
    enabled: true
    env:
      FIRECRAWL_API_KEY: REDACTED
```

## Tools available

- `firecrawl_scrape` — single URL content extraction
- `firecrawl_map` — discover all URLs on a site
- `firecrawl_search` — web search with content extraction
- `firecrawl_crawl` — full site crawl
- `firecrawl_extract` — LLM-powered structured extraction
- `firecrawl_agent` — autonomous web research agent
- `firecrawl_agent_status` — check agent job status
- `firecrawl_browser_create/execute/delete/list` — CDP browser sessions

## Free tier

500 credits/month. Sufficient for single-page scrapes and moderate crawling. Runs out fast on full-site crawls.
