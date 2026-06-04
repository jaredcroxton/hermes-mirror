# Telegram runtime model verification

Use this when Jared says a Telegram agent is still showing the wrong model/provider after a profile config change.

## Lesson
A direct CLI probe proves the profile brain can answer with the configured provider. It does **not** prove the Telegram runtime Jared is messaging has refreshed its gateway, session metadata, footer, or cached process state.

Do not say "confirmed" from CLI output alone when the user's symptom is in Telegram.

## Required verification levels
1. **Config:** inspect the target profile's `model.provider`, `model.default`, and `model.base_url`.
2. **Gateway process:** restart the relevant gateway and confirm the live profile gateway is running.
3. **Direct brain probe:** run `hermes --profile <profile> chat -q "Reply exactly <TOKEN>" --quiet`.
4. **Telegram/live transport:** verify the same profile is answering through Telegram, or inspect the gateway log/session metadata proving the Telegram message was handled after restart.
5. **Footer/session state:** if the user sees an old provider in the footer, treat it as a runtime/session verification issue until a fresh Telegram turn shows the new provider.

## Pitfall
Existing gateway conversations can display stale provider/session metadata after config changes. The fix is usually a gateway restart plus a fresh Telegram turn, not another CLI probe.

## Reporting standard
Report each layer separately:

- Config says: `<provider>/<model>`
- Gateway says: `<running/stopped/restarted>`
- CLI probe says: `<token returned or failed>`
- Telegram/live path says: `<fresh message verified or not verified>`

If the terminal/process inspection is blocked by approval, say that plainly and do not claim the Telegram path is fixed.