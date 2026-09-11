**Enabling XAI / Grok image generation**

Add or update the auxiliary section in `~/.hermes/config.yaml`:

```yaml
auxiliary:
  image_gen:
    provider: xai
    model: grok-2-image
    base_url: https://api.x.ai/v1
    api_key: REDACTED
    timeout: 120
```

**After editing:**

1. Save and exit the editor.
2. Run `/reset` in the active session (critical — the change is not picked up until the session restarts).
3. Test with a direct request such as:
   > Generate a motivational image of a sunrise with the text "Today is yours."

The `image_gen` tool will now route through your connected Grok OAuth session instead of FAL. One OAuth login gives access to chat, TTS, and image generation.