# Local workshop model demo on 24GB Apple Silicon

Use this reference when Jared wants to demo a local LLM through Hermes, Claude Code, or an IDE-style agent on a MacBook Air / Apple Silicon machine with around 24GB unified memory.

## Recommended model choice

For a 24GB MacBook Air, prioritise reliability over peak benchmark quality.

Recommended primary file:

```text
unsloth/Qwen3.8-27B-GGUF
Qwen3.8-27B-Q4_K_M.gguf
```

Observed Hugging Face HEAD size during the session: about 15.93GB.

Avoid Q5 for live demos on 24GB machines. `Qwen3.8-27B-Q5_K_M.gguf` was about 18.47GB, which leaves too little headroom once context, the agent wrapper, macOS, and UI apps are active.

Fallback if speed or thermal pressure matters more than quality:

```text
Qwen3.8-27B-IQ4_XS.gguf
```

Observed size: about 14.63GB.

Optional image support:

```text
mmproj-F16.gguf
```

Observed size: about 0.86GB.

## Runtime posture

For workshop demos, use LM Studio as the local OpenAI-compatible server unless Jared specifically asks for a terminal-native setup.

Recommended settings:

| Setting | Value |
|---|---:|
| Context length | 4096 for agent/coding demos, 8192 max |
| GPU offload | Max / Metal on |
| Temperature | 0.3 to 0.4 |
| Max output | 400 to 700 tokens |
| Keep model loaded | On |
| Server port | 1234 |

Key judgement: do not maximise context on a 24GB laptop just because the model supports it. Agent wrappers add hidden prompt/tool overhead, and large context slows the demo.

## Demo sequencing

Do not run Hermes, Claude Code, and Antigravity heavy-agent workflows simultaneously on a 24GB Air. Use one LM Studio model server and demonstrate one client at a time.

Suggested story:

1. Hermes creates a simple markdown file.
2. Claude Code improves or diffs that file.
3. Antigravity or another IDE agent reviews the same file or suggests improvements only.

The workshop message:

```text
This is not the most powerful AI model in the world. That is not the point. The point is that useful AI can run locally, respond fast enough to be useful, and work with files without sending working material to a cloud model.
```

## Hermes against LM Studio

Use a clean demo profile so the main agent setup is untouched:

```bash
hermes profile create qwen-demo
hermes --profile qwen-demo config set model.provider lmstudio
hermes --profile qwen-demo config set model.base_url http://localhost:1234/v1
hermes --profile qwen-demo config set model.api_key lmstudio
curl http://localhost:1234/v1/models
hermes --profile qwen-demo config set model.default "<MODEL_ID_FROM_LM_STUDIO>"
hermes --profile qwen-demo chat -q "Reply exactly LOCAL_OK" --quiet
```

Keep the Hermes demo small and concrete, for example creating a Desktop markdown file. Avoid loading unnecessary tools for a local 27B model.

## Claude Code against LM Studio

LM Studio documents using Claude Code with its local server by setting Anthropic environment variables:

```bash
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
export ANTHROPIC_API_KEY=
claude --model "<LM_STUDIO_MODEL_ID>"
```

Use small file edits or markdown diffs for the live demo. Do not ask Claude Code to build a full app live on a 24GB Air.

## Large model download discipline

Before downloading a 15GB+ GGUF, check available disk. Target at least 8 to 10GB more free space than the model file requires, because partial downloads, caches, and companion files need room.

Use resumable curl:

```bash
mkdir -p "$HOME/Models/Qwen3.8-27B-GGUF"
cd "$HOME/Models/Qwen3.8-27B-GGUF"
curl -L --fail --continue-at - --retry 5 --retry-delay 10 \
  --output Qwen3.8-27B-Q4_K_M.gguf \
  "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/resolve/main/Qwen3.8-27B-Q4_K_M.gguf"
```

If download fails close to completion with a write error, check disk space before retrying. Do not delete Downloads/Desktop files without explicit user approval. Safe cache cleanup may be appropriate, but still ask before deleting.