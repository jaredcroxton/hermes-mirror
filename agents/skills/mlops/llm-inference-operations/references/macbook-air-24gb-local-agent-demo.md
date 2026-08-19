# MacBook Air 24GB local agent demo

Use this when Jared wants to demo a local LLM through agent tools such as Hermes, Claude Code, or Antigravity on a 24GB Apple Silicon MacBook Air.

## Recommended model choice

For a 24GB MacBook Air, prioritise reliability and responsiveness over maximum quant quality.

Recommended primary model:

- `unsloth/Qwen3.8-27B-GGUF`
- File: `Qwen3.8-27B-Q4_K_M.gguf`
- Approx size checked during session: 15.93GB

Useful fallback:

- File: `Qwen3.8-27B-IQ4_XS.gguf`
- Approx size checked during session: 14.63GB
- Use if the demo feels hot, slow, or memory pressured.

Avoid for live workshop on 24GB:

- `Qwen3.8-27B-Q5_K_M.gguf`, approx 18.47GB. It may fit, but leaves too little practical headroom once macOS, context/KV cache, LM Studio, and agent wrappers are included.
- Q2 or Q3 quants for public demos unless there is no alternative. The quality drop is more visible than the speed gain.

## LM Studio serving settings

Use LM Studio as the shared local model server for a workshop demo.

Recommended settings:

- Server: on
- Port: `1234`
- Base URL for OpenAI-compatible clients: `http://localhost:1234/v1`
- Context length: `4096` for coding-agent demos, `8192` maximum for plain chat demos
- GPU offload: max
- Temperature: `0.3` to `0.4`
- Max response: `400` to `700` tokens
- Keep model loaded: on

Pre-warm before the audience sees it by running one throwaway prompt after loading the model.

## Demo operating principle

For workshops, reliability beats raw benchmark quality. Agent wrappers add tool schemas, file context, instructions, planning loops, diffs, and hidden overhead. On 24GB, do not run multiple heavy agents against the model at once.

Recommended sequence:

1. Hermes creates a simple file.
2. Claude Code improves or reviews that file.
3. Antigravity suggests improvements or reviews the same file.

Do not use a real app repo for the live demo. Use a tiny folder or a markdown file.

## Hermes setup pattern

Create a separate demo profile so Jared's main Brock setup is not touched:

```bash
hermes profile create qwen-demo
hermes --profile qwen-demo config set model.provider lmstudio
hermes --profile qwen-demo config set model.base_url http://localhost:1234/v1
hermes --profile qwen-demo config set model.api_key lmstudio
curl http://localhost:1234/v1/models
hermes --profile qwen-demo config set model.default "<MODEL_ID_FROM_LM_STUDIO>"
hermes --profile qwen-demo chat -q "Reply exactly LOCAL_OK" --quiet
```

Keep tool use simple and visible. Good demo prompt:

```text
Create a Desktop markdown file called local-ai-workshop-demo.md. Include five practical local AI use cases for L&D, recruitment, and sales coaching. Keep it executive-ready and plain English.
```

## Claude Code setup pattern

Point Claude Code at the same LM Studio server:

```bash
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
export ANTHROPIC_API_KEY=
claude --model "<LM_STUDIO_MODEL_ID>"
```

Good demo prompt:

```text
Open local-ai-workshop-demo.md. Improve the structure for a workshop audience, tighten the wording, and show me the diff before saving.
```

## Antigravity pattern

If Antigravity exposes OpenAI-compatible custom provider settings, use:

- Provider: OpenAI compatible
- Base URL: `http://localhost:1234/v1`
- Chat completions URL: `http://localhost:1234/v1/chat/completions`
- API key: `lmstudio`
- Model: `<LM_STUDIO_MODEL_ID>`

Use Antigravity for suggestions or review in this demo, not full app generation. Good prompt:

```text
Review this markdown file and suggest three ways to make it clearer for non-technical business leaders.
```

## Talk track

Use this framing:

> This is one local model running on a MacBook Air. I can point different agent tools at it. Hermes for everyday agent work. Claude Code for file and code workflows. Antigravity for IDE-style exploration. The point is not that it beats Claude. The point is that useful AI can run locally without sending working material to the cloud.
