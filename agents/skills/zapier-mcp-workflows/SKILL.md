---
name: zapier-mcp-workflows
description: Use when building Zapier MCP automated workflows for Accor Plus (HR, TA, sales ops). Covers auth lifecycle, tool discovery, data privacy explanation, Zapier Enterprise governance features, and planned automation patterns. Triggered when Jared asks to "build a Zap" or "set up an automation".
tags: [zapier, mcp, automation, accor-plus, hr, onboarding, governance]
---

# Zapier MCP — Accor Plus Workflow Builder

## When to use
Use when Jared asks to build Zapier-powered automations through MCP. This includes onboarding flows, notification chains, sales KPI tracking, interview booking, and any workflow where Zapier MCP tools are called via mcporter.

## Fallback rule: use Zapier MCP first when it is already working

This session (01 Jun 2026) established the workflow lesson: when a better tool (Himalaya for email) is not yet configured and the user wants a result, use the already-working Zapier MCP immediately. Do not spend 20+ minutes debugging setup while the user waits.

**Rule:** When the user asks for something that works through an already-authenticated Zapier MCP connection, answer via Zapier MCP first. Log the better tool as a follow-up. Do not lead with setup when the user's actual ask is "show me X."

## mcporter positional arg syntax — the detail that matters

Every Zapier MCP tool is called as: `zapier.<toolname>` (namespaced).

**Working pattern (always use this):**
```
npx -y mcporter --config /Users/jc/config/mcporter.json call zapier gmail_create_draft \
  'Clear natural language instructions including to, subject, body' \
  'output_hint fields'
```

- First arg: `instructions` — full natural language sentence, Zapier's LLM extracts structured params from it
- Second arg: `output_hint` — comma-separated fields you want back
- Third+ args: optional positional params for search queries, message IDs, etc.

**Do NOT use:**
- `--params '{"key":"value"}'` — fails when tools expect arrays (to, cc, bcc). Zapier's resolver handles array inference from instructions text.
- `--param key value` flags — mcporter parses them wrong for MCP tools

**Gmail array inference:** Writing `"Create a draft to jaredcroxton@gmail.com"` in instructions is enough. Zapier resolves `to: ["jaredcroxton@gmail.com"]` automatically. You do not pass `to:` separately.

## Config and auth
- Config file: `/Users/jc/config/mcporter.json`
- Base URL: `https://mcp.zapier.com/api/v1/connect`
- Auth: Bearer token (base64-encoded `client_id:client_secret`)

### Auth lifecycle
1. Token expires → mcporter returns `401 / SSE error: Non-200 status code`
2. Fix: Go to https://zapier.com/mcp → re-authorise the connection → copy new token
3. Paste the full `client_id:client_secret` string into mcporter.json (NOT just client_id)
4. Verify: `npx -y mcporter --config /Users/jc/config/mcporter.json list zapier`
5. Expected: 77+ tools listed

### Adding tools to the MCP server
After auth, only `get_configuration_url` appears. Jared must add specific actions at https://zapier.com/mcp:
- Gmail: Send Email, Create Draft
- Google Sheets: Lookup Spreadsheet Row, Update Spreadsheet Row, New Spreadsheet Row trigger
- Google Calendar: Create Event, Find Events
- (Optional) Zendesk: Create Ticket, or Email by Zapier: Send Email

## MCP tool call pattern
Every Zapier MCP tool requires these parameters:
- `instructions` (REQUIRED): What to do, in natural language. This is the FIRST positional parameter.
- `output_hint` (REQUIRED): What data you want back, e.g. "just the row ID and column values"

Omitting `output_hint` causes call failure. Always include both.

### CRITICAL: Zapier MCP tools are conversational, NOT raw API proxies
`google_sheets_make_api_mutating_request` does NOT execute raw Google Sheets API calls. It is a conversational tool that asks follow-up questions and requires the spreadsheet ID before it will act. **You cannot create a new Google Sheet through this tool.**

**Fallback to create a Google Sheet:**
1. Generate a CSV on Desktop: `python3 -c "import csv,os; ..."`
2. Save to `~/Desktop/[name].csv`
3. Jared uploads to Google Drive → opens as Google Sheets
4. Then Zapier MCP tools work on the resulting sheet

**Also note:** Google Workspace OAuth is not set up on Jared's Mac (no `~/.hermes/google_token.json` or `google_client_secret.json`). The `gws` CLI cannot create Sheets directly. The CSV fallback is the fastest path unless Jared wants to do the OAuth setup (see `google-workspace` skill).

## Key tool signatures
`gmail_send_email(instructions, output_hint, to, subject, body, cc, bcc, file, from, body_type, from_name, ...)`
- `to` must be a real email address — no @example.com, no guesses
- `body` defaults to HTML

`google_sheets_lookup_spreadsheet_row(...)` — find a row by column match
`google_sheets_update_spreadsheet_row(...)` — update Status column
`google_calendar_create_event(...)` — schedule induction session

## Data privacy reference (for when Jared asks)
- Hermes processes all MCP data in RAM during the conversation only
- Session logs stored locally on Mac (SQLite, encrypted) — on-device only
- Zapier retains what their platform logs (Zapier's privacy policy applies)
- The LLM model does NOT store, learn from, or share the data from tool calls
- No data is sent to any external model provider beyond the active conversation context
- **Note:** Jared typically asks this twice in different wording. Be patient and answer fully each time with all three points above.

## Planned: New Hire Onboarding Zap (pending Jared inputs)
Jared approved this design on 29 May 2026. Needs:
1. Spreadsheet name and exact column headers (build CSV if needed, let Jared upload to Google Sheets)
2. L&D email address (one inbox or per-market?)
3. IT ticket destination (Zendesk or direct email?)
4. Status column trigger word for "hiring finished"
5. Welcome email content (existing or draft new?)

**Flow 1** — New row in sheet → email to L&D confirming hire
**Flow 2** — Same trigger → IT ticket + manager checklist + calendar event
**Flow 3** — Status change to "finished" → email to Jared (Director)

**IMPORTANT:** Jared said "yes correct" when asked if column assumptions were right, but this was NOT actual confirmation — he did not provide the details. Do NOT assume the Zap is ready to build. Always get the four inputs listed above before constructing the actual Zap calls.

## Pitfalls

- **Zapier MCP tools are conversational, not raw API.** They ask follow-up questions. Use natural language `instructions` and always include `output_hint`. Cannot create spreadsheets — use CSV fallback.
- **Google Workspace OAuth is not configured.** No `gws` CLI access to Google Sheets. Use CSV → manual upload path.
- **"Yes correct" is not confirmation.** Jared often says "yes correct" to acknowledge a framing question ("do you mean X?") without actually answering the follow-up inputs. Always verify you have ALL required data before building. Four unanswered questions = wait.
- **Token privacy explanation takes multiple rounds.** Jared typically asks "does Hermes save data?" and then asks again in different wording ("what about your brain?"). Be patient and answer fully each time. The three-part answer: (1) Hermes stores conversation locally on Mac, (2) Zapier keeps what their platform logs, (3) the LLM model does NOT store or learn from the data.
- **Zapier MCP auth tokens expire silently.** When mcporter returns 401 with "SSE error: Non-200 status code", the token has expired. Go to https://zapier.com/mcp and re-auth. Token format is Bearer <base64 string>.

## Zapier Enterprise governance features (for enterprise clients)

When pitching to corporate clients with serious security requirements, Zapier Enterprise provides:
- **AI Guardrails** — safety checks that block sensitive data before AI outputs reach systems
- **BYOM (Bring Your Own Model)** — run AI through client's own AWS Bedrock infrastructure
- **Managed Connections** — IT owns app connections, not individuals
- **Domain Restrictions** — block personal accounts from business systems
- **Log Streaming** — real-time workflow data to Datadog/Splunk/SIEM
- **SCIM Provisioning** — auto-provision users through identity provider (Azure AD, Okta)
- **Action Restrictions** — granular endpoint-level control per app
- **SOC 2 Type II/III, GDPR, CCPA** — annually audited
- **99.9% uptime SLA**

Enterprise is custom-priced (~£500-2,000/mo). Budget £500/mo for planning purposes. This is the client's cost, not PerformOS's.

Easy procurement answers:
1. "How do we control what the AI does?" → Action Restrictions + App Access Controls
2. "How do we prevent data leaks?" → AI Guardrails + Domain Restrictions
3. "Can we see what happened?" → Log Streaming + Asset History API

## Zapier Platform pricing (for client cost-of-ownership discussions)

| Plan | Price/mo (billed yearly) | Tasks/mo | Users | Key features |
|---|---|---|---|---|
| Free | £0 | 100 | 1 | Zaps, Tables, Forms, MCP included |
| Professional | £15.21 | From 2K | 1 | Multi-step Zaps, Premium apps, Webhooks |
| Team | £52.51 | From 2K | 25 | Shared workspaces, SAML SSO, Premier Support |
| Enterprise | Contact sales | Custom | Custom | Full governance suite |

Zapier MCP is now included on ALL plans including Free. Task budgeting: a 3-step Zap running 20x/day across 5 agents = ~9,000 tasks/mo, fitting comfortably on Professional at £15/mo.

Sources: https://zapier.com/pricing + https://zapier.com/enterprise (verified 29 May 2026).

## Interaction tier context (for PerformOS client proposals)

The PerformOS 5-agent package targets 200 interactions per agent per day. This equals approximately 30,000 total monthly interactions across 5 agents. This is the standard usage tier for pricing and capacity planning.

For Accor Plus internal use, workloads are typically lower — 20 interactions/agent/day was the original planning estimate. Adjust token estimates accordingly per client.

## Reference files
- `references/mcp-accorplus-patterns.md` — Auth walkthrough, full tool list, data privacy details
- `references/zapier-enterprise-features.md` — Enterprise governance feature details for proposals

## Version

Created 29 May 2026. Updated with: conversational MCP tool behavior pitfall, CSV fallback for sheet creation, Google Workspace OAuth gap note, auth lifecycle notes, and pitfalls.