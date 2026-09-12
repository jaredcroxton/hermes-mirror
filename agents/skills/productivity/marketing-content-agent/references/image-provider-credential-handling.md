# Image provider credential handling

## Durable lesson

For marketing content agents, image-model credentials are part of the agent runtime, not the brand prompt or content pack. Keep them out of chat exports, workflow JSON, Obsidian briefs, and Claude packages.

## Preferred storage

For a profile-backed creative agent such as Mira:

```bash
/Users/jc/.hermes/profiles/miracreative/.env
```

Common provider variables:

```bash
FAL_KEY=<api_key>
FAL_API_KEY=<api_key>
```

Use the variable name expected by the actual generation script/provider. If unsure, store both only when the provider docs or implementation supports both aliases.

## Safe intake order

1. Best: user adds the key to the profile-local `.env` themselves and tells you it is done.
2. Good: open the profile `.env` in TextEdit for the user:

```bash
open -a TextEdit /Users/jc/.hermes/profiles/miracreative/.env
```

3. Last resort: if the user pastes the key into chat, write it directly to the profile `.env`, never repeat it back, verify only presence/length, and recommend rotating if it was exposed broadly.

## Verification standard

Verify without exposing the secret:

```text
token/key configured: true
length: <n>
has expected shape: true
```

Do not print the key, partial key, or bearer token in replies.

## Package/export rule

When exporting n8n/Nano Banana/Seedream/fal workflows for Claude or GitHub:

- remove live bearer tokens
- replace with `API_KEY`
- document required env vars separately
- keep the workflow structure, not the secret
