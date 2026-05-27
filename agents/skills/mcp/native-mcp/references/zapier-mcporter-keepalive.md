# Zapier via mcporter keep-alive setup

When connecting Zapier MCP to Hermes through mcporter, `mcporter list zapier --schema` can succeed while `hermes mcp test zapier` fails with `Connection closed`.

Root cause observed: `mcporter serve --servers zapier --stdio` only serves daemon-managed keep-alive servers. A plain HTTP mcporter entry like:

```json
{
  "mcpServers": {
    "zapier": {
      "baseUrl": "https://mcp.zapier.com/api/v1/connect",
      "clientName": "hermes"
    }
  }
}
```

fails under `mcporter serve` with:

```text
[mcporter] Server 'zapier' is not configured for keep-alive and cannot be served by the daemon bridge.
```

## Fix

Add `"lifecycle": "keep-alive"` to the Zapier entry in the mcporter config, typically `~/config/mcporter.json`:

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

Then configure Hermes native MCP to run mcporter over stdio:

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

Verify both layers:

```bash
npx -y mcporter list zapier --schema
hermes mcp test zapier
```

A successful Hermes test should report connection success and discover Zapier tools such as `zapier__discover_zapier_actions`, `zapier__list_enabled_zapier_actions`, `zapier__execute_zapier_read_action`, and `zapier__get_zapier_skill`.

## Onboarding handoff

After tool discovery succeeds, load Zapier's own onboarding skill through the MCP server:

```bash
npx -y mcporter call 'zapier.list_zapier_skills()'
npx -y mcporter call 'zapier.get_zapier_skill({"name":"zapier-mcp-onboarding"})'
```

Follow its dialogue: check enabled actions first, auto-provision only if nothing is enabled, then guide the user by outcomes/use cases rather than app/action names.