# mcporter + Zapier MCP keep-alive bridge

## Context

Zapier's remote MCP endpoint can be added to mcporter and then exposed to Hermes as a stdio MCP server through `mcporter serve`.

Working local mcporter entry shape:

```json
{
  "mcpServers": {
    "zapier": {
      "baseUrl": "https://mcp.zapier.com/api/v1/connect",
      "clientName": "hermes",
      "lifecycle": "keep-alive"
    }
  }
}
```

Hermes config shape:

```yaml
mcp_servers:
  zapier:
    command: npx
    args:
      - -y
      - mcporter
      - serve
      - --servers
      - zapier
      - --stdio
    timeout: 120
    connect_timeout: 60
```

## Setup and verification

```bash
npx -y mcporter config add zapier --url "https://mcp.zapier.com/api/v1/connect" --client-name "hermes"
```

Then ensure the generated mcporter JSON includes:

```json
"lifecycle": "keep-alive"
```

Verify remote Zapier tools directly:

```bash
npx -y mcporter list zapier --schema
```

Verify Hermes native MCP discovery:

```bash
hermes mcp test zapier
```

A successful Hermes test should connect over stdio and discover Zapier tools such as `zapier__discover_zapier_actions`, `zapier__list_enabled_zapier_actions`, and `zapier__get_zapier_skill`.

## Pitfall

If `hermes mcp test zapier` fails with `Connection closed`, run the mcporter bridge directly to inspect stderr:

```bash
npx -y mcporter serve --servers zapier --stdio
```

If stderr says the server is not configured for keep-alive and cannot be served by the daemon bridge, add the `"lifecycle": "keep-alive"` field to the Zapier entry in mcporter config and retry.

## Auth note

`mcporter list zapier --schema` may report a transient 401 or suggest `mcporter auth zapier` while `hermes mcp test zapier` still succeeds after keep-alive is configured. Prefer the Hermes MCP test as the final verification for Hermes availability, then call Zapier tools through the MCP bridge or mcporter as needed.
