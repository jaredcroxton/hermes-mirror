# Zapier MCP — Accor Plus HR Automation Patterns

## Config
- File: `/Users/jc/config/mcporter.json`
- Base URL: `https://mcp.zapier.com/api/v1/connect`
- Auth: Bearer token (refresh at https://zapier.com/mcp when 401)

## Auth lifecycle
1. Token expires → mcporter returns `401 / SSE error: Non-200 status code`
2. Fix: Go to https://zapier.com/mcp → re-authorise the named connection ("hermes") → copy new token
3. Update mcporter.json Authorization header with new Bearer value
4. Verify: `npx -y mcporter --config /Users/jc/config/mcporter.json list-tools zapier` should return 78 tools

## How tools appear
Zapier MCP does NOT auto-expose all app actions. After auth, only `get_configuration_url` appears until you explicitly add actions in the Zapier MCP dashboard. Jared must add:
- Gmail: Send Email, Create Draft
- Google Sheets: Lookup Spreadsheet Row, Update Spreadsheet Row
- Google Calendar: Create Event, Find Events
- (Optional) Zendesk: Create Ticket, or Email by Zapier: Send Email

## Key MCP tool signatures
`gmail_send_email(instructions, output_hint, to, subject, body, cc, bcc, file, from, body_type, from_name, ...)`
- `output_hint` and `instructions` are REQUIRED on every call
- `to` must be a real email address — no @example.com or guesses
- `body` defaults to HTML unless `body_type` is set

`google_sheets_lookup_spreadsheet_row(instructions, output_hint, spreadsheet_id, sheet_name, lookup_column, lookup_value, ...)`
- Used to find a specific hire record by matching a column value

`google_sheets_update_spreadsheet_row(instructions, output_hint, spreadsheet_id, sheet_name, row_id, ...)`
- Used to change Status column when hiring moves to next stage

`google_calendar_create_event(instructions, output_hint, calendarid, summary, start_time, end_time, ...)`
- Used for induction session scheduling

## Data privacy (verified with Jared 29 May 2026)
Hermes processes all Zapier MCP data in RAM during the conversation only.
- Email addresses, spreadsheet values, message content exist only for that conversation turn
- Hermes session logs are stored locally on Mac (SQLite, encrypted) — on-device only
- Zapier retains whatever their platform logs (their privacy policy applies)
- The LLM model does NOT store, learn from, or share the data
- No data is sent to any external AI model provider beyond the conversation context

## Planned Zap: Accor Plus New Hire Onboarding (status: pending)
**Flow 1** — New hire confirmed: Google Sheets new row → Gmail send to L&D
**Flow 2** — Onboarding steps: Same trigger → IT ticket + manager checklist email + calendar event
**Flow 3** — Hiring complete: Sheet status change → Gmail send to Jared (Director)

## Key pitfall
Zapier MCP tools require `output_hint` on every single call. Always include a natural-language description of what you want back.
