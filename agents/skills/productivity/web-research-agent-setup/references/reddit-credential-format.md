# Reddit rdt-cli credential format

The exact JSON format `rdt-cli` expects at `~/.config/rdt-cli/credential.json`:

```json
{
  "cookies": {"reddit_session": "<paste-cookie-value>"},
  "source": "manual",
  "username": "<your-reddit-username>",
  "modhash": null,
  "saved_at": 0,
  "last_verified_at": null
}
```

## Why this format

- The `cookies` wrapper key is mandatory. Agent Reach's `_check_rdt()` method looks for `credential.get("cookies", {}).get("reddit_session")`.
- `source: "manual"` tells rdt-cli not to attempt browser auto-extraction (which would trigger the Keychain prompt).
- `username` is the Reddit username (e.g., `t2_a0clhhlb` from the JWT `sub` claim).
- `saved_at` and `last_verified_at` can be 0/null — they are metadata fields.

## What does NOT work

A flat format without the `cookies` wrapper will be silently ignored:
```json
{"reddit_session": "..."}
```

## How to get the cookie value

1. Open reddit.com in Chrome, logged in
2. Developer Tools (`Command + Option + I`)
3. Application tab → Cookies → `https://www.reddit.com`
4. Find `reddit_session` in the Name column
5. Double-click the Value column to select the full JWT
6. Copy with `Command + C`

## How to get the username

The `reddit_session` cookie is a JWT. Decode the payload (middle segment between the dots) to find the `sub` claim, which is the Reddit user ID (e.g., `t2_a0clhhlb`). This is the username to use in the credential file.
