# Antigravity + Ollama local models

Use this when Jared wants to use a downloaded Ollama model, usually Qwen, from Antigravity on a Mac.

## Key correction from session

If Jared says the model is already downloaded, do not start by re-downloading, installing, or over-explaining. First help him list and use the exact local model name.

```bash
ollama list
ollama ps
```

Use the exact `NAME` from `ollama list`, including the tag.

Example:

```text
qwen3-coder:30b
qwen3.6:latest
```

Small differences trigger fresh pulls. For example, `qwen3-coder` and `qwen3-coder:30b` can be treated as different models.

## Terminal basics for Jared

When Ollama is already installed:

```bash
ollama list
ollama run qwen3-coder:30b
ollama ps
ollama stop qwen3-coder:30b
```

Inside an `ollama run` chat session:

```text
/bye
```

exits the chat. `Control + C` is the force-exit fallback.

## What goes where

Do not tell Jared to paste Antigravity settings into Terminal. Make the boundary explicit:

```text
Terminal = runs Ollama/Qwen
Antigravity = connects to Ollama/Qwen
```

Ollama exposes the local OpenAI-compatible API here:

```text
http://localhost:11434/v1
```

Full chat endpoint if requested:

```text
http://localhost:11434/v1/chat/completions
```

Common settings:

| Field | Value |
|---|---|
| Provider | OpenAI compatible |
| Base URL | `http://localhost:11434/v1` |
| API key | `ollama` |
| Model | exact name from `ollama list` |

## Antigravity path one: Cline extension

If Antigravity's built-in model screen only shows cloud model usage or quotas, do not keep hunting there. Use the Cline extension.

Flow:

```text
Antigravity → Extensions → Cline → Cline Settings → API Provider → Ollama → model name
```

If Cline asks for host:

```text
http://localhost:11434
```

If Cline asks for OpenAI-compatible fields:

```text
Base URL: http://localhost:11434/v1
API key: ollama
Model: qwen3-coder:30b
```

Explain simply:

```text
Ollama runs Qwen
Cline connects to Ollama
Cline runs inside Antigravity
```

## Antigravity path two: DeepSeek Harness beside Antigravity

DeepSeek Harness is not an Antigravity extension. It runs beside Antigravity as a fuller agent harness.

Use it when Jared asks for an alternative to Cline or a more serious local agent setup.

Flow:

```text
Ollama runs Qwen
DeepSeek Harness connects to Ollama
Jared works in DeepSeek Harness as the agent workspace
```

Start Harness:

```bash
npx @deepseek-ai/dsh web
```

It opens:

```text
http://127.0.0.1:3080
```

Custom provider fields:

| Field | Value |
|---|---|
| Provider ID | `ollama` |
| Base URL | `http://127.0.0.1:11434/v1` |
| API protocol | `openai-completions` |
| API key | blank or `ollama` |
| Model ID | exact name from `ollama list` |

Verify first from the same environment running Harness:

```bash
curl http://127.0.0.1:11434/v1/models
ollama list
```

Important: `localhost` belongs to the host process running Harness. If Harness runs inside Docker, WSL, a VM, or another machine, `127.0.0.1` may not be the Mac's Ollama server.

## Recommendation framing

For a normal business owner:

```text
Cline first
DeepSeek Harness later
```

Cline is the easiest local AI worker inside the editor. DeepSeek Harness is a more advanced local agent platform with plugins, traces, tools, and workflows.

## Style for live walkthroughs

When Jared is mid-setup:

- Give one action at a time.
- Do not mix Terminal commands with UI field values in the same block unless clearly labelled.
- If Jared sends a screenshot, describe exactly what is visible and name the next click.
- If he says stop, stop the current path and answer only the immediate question.
