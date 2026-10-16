# Profile-specific design MCP servers: Google Stitch pattern

Use this when Jared wants a specialist profile, especially `bobbuilder`, to use a design-generation tool such as Google Stitch as the UI/UX source of truth.

## Core distinction

A product URL like `https://stitch.withgoogle.com` is the web app, not the MCP connection.

To connect Hermes/Bob, you need one of:

- a stdio MCP server config from another client such as Antigravity
- an HTTP MCP server URL
- API documentation plus an API key that a wrapper/tool can call
- manual export from Stitch when no API/MCP server is available

An API key alone is not enough unless there is an MCP server or API client that knows how to use it.

## Target operating model

Stitch owns:

- UI direction
- UX flow
- screens
- visual hierarchy
- component feel
- spacing, colour, and interaction direction

Bob owns:

- BLAST execution
- code implementation
- GitHub
- Vercel
- integration and wiring
- responsive QA
- overflow/clipping fixes
- final deployment

Short rule: Stitch creates the taste. Bob creates the product.

## Connecting to a profile

Add the MCP server to the specialist profile config, not only the default profile:

`/Users/jc/.hermes/profiles/bobbuilder/config.yaml`

Stdio pattern:

```yaml
mcp_servers:
  stitch:
    command: npx
    args:
      - -y
      - <stitch-mcp-package>
    env:
      STITCH_API_KEY: ${STITCH_API_KEY}
    timeout: 180
    connect_timeout: 60
```

HTTP pattern:

```yaml
mcp_servers:
  stitch:
    url: <stitch-mcp-url>
    headers:
      Authorization: Bearer ${STITCH_API_KEY}
    timeout: 180
    connect_timeout: 60
```

Store the key in the profile `.env`:

```text
/Users/jc/.hermes/profiles/bobbuilder/.env
STITCH_API_KEY=...
```

Restart the profile gateway after config changes:

```bash
bob_builder gateway restart
```

Then inspect tool names. They should follow the pattern:

```text
mcp_stitch_<tool_name>
```

## Finding the MCP config from Antigravity

Look for a JSON or settings entry with one of these shapes:

```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "<package>"]
    }
  }
}
```

or:

```json
{
  "mcpServers": {
    "stitch": {
      "url": "https://.../mcp"
    }
  }
}
```

Likely places on Jared's macOS setup:

- `/Users/jc/Library/Application Support/Antigravity/User/settings.json`
- Antigravity workspace `.vscode/settings.json`
- Antigravity MCP settings UI
- extension/global storage if the client stores MCP server state outside settings

Do not treat website scrape output as an MCP config.

## Bob SOUL / skill rule to add

When Stitch is connected or a Stitch export/link is provided, Bob should be instructed:

```text
For app, dashboard, landing page, product page, mobile UI, or web app builds, bob_builder must use Stitch as the UI/UX source of truth when a Stitch design, Stitch link, or Stitch MCP output is available.

Bob must not freestyle the UI unless Stitch is unavailable or Jared explicitly asks for a non-Stitch design.

BLAST controls build execution. Stitch controls UI/UX direction.
```

## Manual fallback

If there is no Stitch MCP or API access, ask Jared for a Stitch export or design artefact:

- public/shared Stitch link
- exported HTML or React
- screenshot set
- component notes
- design tokens
- screen flow notes

Then treat those artefacts as the UI/UX source of truth and have Bob build faithfully from them.