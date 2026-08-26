# Antigravity + Ollama + Qwen on macOS

Use this when Jared is setting up Qwen in Antigravity through Ollama, especially on a new MacBook.

## Core mechanic

Antigravity does not load the model directly.

```text
Antigravity
↓
OpenAI-compatible local endpoint
↓
Ollama
↓
Qwen model on the Mac
```

Ollama exposes the local OpenAI-compatible endpoint at:

```text
http://localhost:11434/v1
```

If a tool asks for the full chat endpoint, use:

```text
http://localhost:11434/v1/chat/completions
```

## Fast check

Ask Jared to run:

```bash
ollama list
```

Use the exact first-column model name in Antigravity.

Example:

```text
qwen3-coder:30b
qwen3.6:latest
```

For Antigravity coding, prefer:

```text
qwen3-coder:30b
```

## Start and verify the model

In Terminal:

```bash
ollama run qwen3-coder:30b
```

Replace with the exact model name from `ollama list`.

Once the `Send a message` prompt appears, the local model is alive. A verbose reply is still a valid proof that Qwen is running, even if it does not follow an exact-response instruction perfectly.

Leave that Terminal window open during setup.

## Antigravity settings

Inside Antigravity, not Terminal:

| Field | Value |
|---|---|
| Provider | OpenAI compatible |
| Base URL | `http://localhost:11434/v1` |
| API key | `ollama` |
| Model name | Exact name from `ollama list`, for example `qwen3-coder:30b` |

If Antigravity asks for endpoint instead of base URL:

```text
http://localhost:11434/v1/chat/completions
```

## Common pitfall

Jared may paste the settings into the Ollama chat prompt by mistake. Correct this plainly:

```text
Terminal runs Ollama/Qwen.
Antigravity is where you paste the Base URL, API key, and model name.
```

Do not keep explaining Python client examples unless Jared asks. That output is usually the model responding inside Terminal, not Antigravity confirming setup.

## New MacBook note

If `ollama run <model>` starts pulling layers, it is downloading on that Mac. This usually means:

- the model is not on the new Mac yet, or
- a different tag was used than the one already downloaded.

After the pull succeeds, run:

```bash
ollama list
```

Then use the exact name shown.

## Communication style for this task

Jared wants a hands-on walkthrough, not a course.

When he says he already downloaded the model, stop discussing download or install paths and move straight to Antigravity settings.

Avoid labels that look like shell commands. If giving Terminal commands, only put actual commands in code blocks. Put Antigravity field values in a table or clearly say "inside Antigravity, not Terminal."