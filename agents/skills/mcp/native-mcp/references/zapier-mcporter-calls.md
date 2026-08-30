# Zapier MCP — positional-call recipe and gotchas

Use this when calling Zapier MCP tools through `mcporter call`. The actual endpoints and field shapes come from `mcporter list zapier` at call time — this file records the calling convention and the pitfalls that bit us, not an authoritative Zapier schema.

## Token handling in chat

Jared usually pastes the Zapier URL and token together on one line:

```text
https://mcp.zapier.com/api/v1/connect Y2QzN2Q5NDgtNTRlYS00ZmM5LThmMzUtZWM2NWMyOTI3NTEwOkdLZGdrSVBjRHc0ZGpVdC9EcnNUall2a0plSUlxV1dxdHpjK0lsMWxpT1k9
```

- The token is the **second whitespace-delimited token** on that line.
- Store it raw (do not base64-decode) in `/Users/jc/config/mcporter.json` as the Bearer value.
- After updating the token, re-run `list zapier` before assuming any tools are still available.

## Calling convention

Zapier MCP tools through mcporter are called with **positional string arguments**, not a named JSON body.

```bash
npx -y mcporter --config /Users/jc/config/mcporter.json list zapier

npx -y mcporter --config /Users/jc/config/mcporter.json call zapier gmail_find_email \
  'Find last 5 inbox emails' \
  'subject from date' \
  'in:inbox'

npx -y mcporter --config /Users/jc/config/mcporter.json call zapier gmail_create_draft \
  'Create a draft email to jaredcroxton@gmail.com with subject test and body Just testing if everything is okay from your end.' \
  'message_id subject'
```

Rules:

- `instructions` is always the first positional arg and is required by Zapier.
- `output_hint` is the second positional arg; keep it short (`subject from date`).
- Tool-specific parameters, if required, follow as further positional strings.
- Prefer letting Zapier LLM-guess structured params from the natural-language `instructions` string. Explicit positional params for `to`/`cc`/`bcc` failed in our session because Zapier's schema expects arrays — passing a bare string triggered `expected array, received string`.
- Do **not** pass a single JSON object as the argument; mcporter rejects it.
- Gmail/Calendar/Sheets/Sheet write actions require explicit user confirmation before running.
- Timeout: Gmail calls took 45-60s on first run after token refresh; use at least 60s.

## Observed tool shapes (May 2026 snapshot)

These are working call shapes from the session, not a complete catalog.

### `gmail_find_email`

```bash
npx -y mcporter --config /Users/jc/config/mcporter.json call zapier gmail_find_email 'Find last 5 inbox emails' 'subject from date' 'in:inbox'
```

Returns `results[]` with `{subject, date, sender, ...}`. Zapier may return more rows than requested; slice client-side.

### `gmail_create_draft`

Let Zapier infer `to`/`subject`/`body`:

```bash
npx -y mcporter --config /Users/jc/config/mcporter.json call zapier gmail_create_draft \
  'Create a draft email to jaredcroxton@gmail.com with subject test and body Just testing if everything is okay from your end.' \
  'message_id subject'
```

Returns `{message_id, subject}`. Draft-only is the safe default; do not auto-send.

## Performance note

Direct mcporter calls are slower than a local native email tool (30-60s per call, multiple billing tasks). This is the correct "works right now" path when Himalaya/local email is unconfigured, but it is not the performance tier Jared prefers. Recommend Himalaya IMAP setup as the fast local path and keep Zapier MCP as fallback when only a few ad-hoc reads/writes are needed.

## Himalaya fallback note

Himalaya v1.2 config format was unreliable during this session — the config parsed OK but backends showed as empty and IMAP auth failed with the supplied App Password. Do not retry Himalaya from skill guidance alone; when Himalaya is requested, run `himalaya account list` and `himalaya envelope list -s 5 -w 120 --debug` only after the user has confirmed 2FA and App Password at `https://myaccount.google.com/apppasswords` and IMAP is enabled at Gmail settings Forwarding and POP/IMAP.
