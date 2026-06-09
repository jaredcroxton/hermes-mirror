# Kie GPT Image 2 Hermes provider setup

Use this when a marketing/creative agent needs Hermes `image_generate` to route through Kie.ai GPT Image 2 instead of OpenAI API or Codex auth.

## Durable pattern

Create a Hermes image provider plugin under the Hermes agent source:

```text
plugins/image_gen/kie/plugin.yaml
plugins/image_gen/kie/__init__.py
```

The provider should implement the normal `ImageGenProvider` interface and register with:

```python
def register(ctx) -> None:
    ctx.register_image_gen_provider(KieImageGenProvider())
```

## Kie flow

Kie GPT Image 2 text-to-image is async:

```text
POST https://api.kie.ai/api/v1/jobs/createTask
→ returns data.taskId
→ poll GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
→ extract generated image URL
→ download to $HERMES_HOME/cache/images/
→ return local image path from image_generate
```

Auth comes from the active profile env:

```text
KIE_API_KEY=REDACTED
```

Do not store the key in Obsidian, plugin files, docs, or chat summaries.

## Mira profile config

```yaml
image_gen:
  provider: kie
  model: gpt-image-2-text-to-image
  kie:
    resolution: 1K
    timeout_seconds: 180
    poll_interval_seconds: 5
```

Use `1K` as the safe default. Kie docs note that `auto` aspect ratio or omitted aspect ratio only supports `1K`; explicit aspect ratios are safer.

## Aspect mapping

Hermes standard aspect values can map to Kie values:

```text
landscape → 16:9
square → 1:1
portrait → 9:16
```

## Error handling lessons

- `code=433` means the API key has exceeded its daily usage or sub-key limit. The provider is working; the account limit is the blocker.
- `recordInfo is null` immediately after task creation can be treated as not-ready during the polling window.
- Keep `openai-codex` as the fallback route when Kie credits, daily limits, or provider availability block generation.

## Verification sequence

1. Compile the plugin file.
2. Set the profile image provider to `kie`.
3. Restart the target profile gateway. If `hermes gateway restart` returns `Refusing to restart the gateway from inside the gateway process`, use `launchctl bootout gui/$(id -u) <plist>` then `launchctl bootstrap gui/$(id -u) <plist>`. This is expected — Hermes blocks self-restart to prevent loops.
4. Run a real `image_generate` smoke test.
5. If the smoke test fails with `code=433`, the active API sub-key has hit its daily usage cap. This is not a credit-balance problem. The user may have credits but the key-level daily limit needs lifting in the Kie dashboard at `https://kie.ai/api-key`. Do not reconfigure back to another provider unless Jared asks for fallback.
6. If the user tops up credits and generation is still blocked, check whether the active key is the same key that was topped up. Compare key fingerprint (prefix/suffix) against the Kie dashboard.

## Positioning

For Mira_Creative, Kie GPT Image 2 is the primary text-to-image engine. Uploaded-reference-image workflows still need the Kie image-to-image endpoint or a separate image-edit route.