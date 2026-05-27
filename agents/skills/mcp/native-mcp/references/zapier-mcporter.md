# Zapier MCP via mcporter for Hermes

Use this when the user asks to set up Zapier MCP for Hermes or when a remote Zapier MCP server needs to be exposed to Hermes' native MCP client.

## Known-good setup

1. Verify mcporter is available:

```bash
npx -y mcporter --version
```

2. Add the Zapier server to mcporter:

```bash
npx -y mcporter config add zapier \
  --url "https://mcp.zapier.com/api/v1/connect" \
  --client-name "hermes"
```

3. Ensure the mcporter entry is daemon/serve compatible. `mcporter serve --servers zapier --stdio` requires the server lifecycle to be keep-alive. In the mcporter config, the Zapier entry should include:

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

Default observed path on macOS for project config: `/Users/jc/config/mcporter.json`. Do not hardcode this for other users; run `npx -y mcporter config list` to see the active path.

4. Configure Hermes native MCP to use mcporter over stdio:

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

If mcporter is using a non-default config location, make the Hermes server invocation point at that same config (for example by adding mcporter's `--config <path>` arguments before `serve`, if supported by the installed mcporter version, or by setting the relevant mcporter config/env option). Do this for **each Hermes profile** that needs Zapier; the default profile and specialist profiles have separate `config.yaml` files, so fixing one does not automatically fix the others.

5. Verify both layers and every relevant profile:

```bash
npx -y mcporter list zapier --schema
hermes mcp test zapier
# for profile-backed agents, use the profile alias too:
<agent_alias> mcp test zapier
```

Expected Hermes result: connected, with Zapier tools discovered (observed: 14 tools). For specialist agents, restart that profile's gateway after changing MCP config or the profile's SOUL:

```bash
<agent_alias> gateway restart
<agent_alias> gateway status
```

## Pitfall: `Connection closed` from `hermes mcp test zapier`

If `hermes mcp test zapier` fails with `Connection closed`, run the mcporter stdio bridge directly. A common stderr is:

```text
Server 'zapier' is not configured for keep-alive and cannot be served by the daemon bridge.
```

Fix by adding `"lifecycle": "keep-alive"` to the Zapier entry in `mcporter.json`, then retry `hermes mcp test zapier`.

## Pitfall: Zapier says `Missing authorization header or token query parameter`

If `mcporter list zapier --schema` or `hermes mcp test zapier` reaches Zapier but returns:

```text
Missing authorization header or token query parameter
```

then the configured Zapier URL is only the public base endpoint, for example:

```text
https://mcp.zapier.com/api/v1/connect
```

That is not enough for tool discovery. Zapier needs either a valid OAuth credential in mcporter's credential vault or the full authenticated MCP connection URL/token from Zapier. Do not treat this as a generic Hermes or MCP failure.

Resolution path:

1. Ask the user for the authenticated Zapier MCP connection URL from Zapier's MCP settings, not just the base `/connect` URL.
2. Update the mcporter Zapier config to use that authenticated URL, or re-run `mcporter auth zapier` if the browser-based OAuth flow is available on the machine.
3. Verify with `mcporter --config <path> list zapier --schema`.
4. Verify Hermes with `hermes mcp test zapier` and, for profile-backed agents, `<alias> mcp test zapier`.
5. Only after tool discovery succeeds, list enabled Zapier actions and confirm whether Gmail exposes Create Draft with attachment.

## Onboarding workflow

After the MCP server is connected and tools are listed:

1. Call `zapier.list_zapier_skills()`.
2. Fetch `zapier-mcp-onboarding` with `zapier.get_zapier_skill({"name":"zapier-mcp-onboarding"})`.
3. Follow that skill's dialogue:
   - call `list_enabled_zapier_actions` first;
   - if apps exist, summarize apps and suggest outcome-focused use cases;
   - if no apps exist, call `auto_provision_mcp`, then guide the user to connect apps based on outcomes, not app names.

## Zapier Gmail draft actions for specialist agents

When a profile-backed specialist agent needs to deliver a document through email, prefer a **draft-only** Zapier workflow unless the user explicitly asks to send immediately:

1. Create the deliverable file (for example Word, PDF, or Excel).
2. Re-open or otherwise quality-check the file before email handoff.
3. Use Zapier MCP Gmail **Create Draft** (`draft_v2`) via `execute_zapier_write_action`.
4. Fill `to`, `cc`/`bcc` if needed, `subject`, `body`, `body_type`, and attach the file through the action's `file` field.
5. Never auto-send; return the draft ID/link so the user can review.
6. If this is intended as the specialist's standing workflow, patch the profile's canonical SOUL with the draft-only rule and restart the profile gateway.

Known observed Gmail Create Draft fields include: `to`, `cc`, `bcc`, `subject`, `body`, `body_type`, `file`, `from`, `from_name`, and `signature`.

## Safety

Zapier MCP can expose write/create/delete actions for apps. For actions that modify external state (send email, create/update/delete calendar events, edit Sheets, etc.), show the intended action and ask for confirmation before executing. Creating a Gmail draft is lower-risk than sending, but still creates external state; if the recipient/content/attachment was not explicitly specified, confirm before creating it.
