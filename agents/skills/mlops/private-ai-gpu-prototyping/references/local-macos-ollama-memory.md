# Local macOS Ollama memory and launch pattern

Session-derived pattern from testing `ollama run gemma4:e4b` on Jared's Mac.

## What happened

- `ollama run gemma4:e4b` triggered a first-time model pull.
- The model was 9.6 GB.
- A foreground terminal run timed out after 120 seconds while the pull continued partway through.
- Running `ollama pull gemma4:e4b` with a longer timeout resumed the partial download and completed successfully.
- Verification used a direct one-shot prompt:

```bash
ollama run gemma4:e4b 'Reply with exactly: Gemma is ready.'
```

Expected verification output:

```text
Gemma is ready.
```

## Recommended local sequence

Use this when Jared asks to run or test a new Ollama model locally:

```bash
# Pull first, with a long timeout if using tools
ollama pull <model>

# Verify it responds without entering a long interactive chat
ollama run <model> 'Reply with exactly: Model is ready.'

# Confirm install
ollama list | grep -E '^(<model>|NAME)'
```

Prefer `ollama pull` before `ollama run` for large models. It gives a clean install step and avoids treating an interactive `run` timeout as a model failure.

## RAM interpretation on macOS

Large local models can make macOS memory look full immediately after launch. In this session, after loading a 9.6 GB model, memory moved to approximately:

```text
PhysMem: 23G used, 97M unused
```

That is expected for a large model on a 24 GB Mac. Explain simply: the model is now sitting in memory so it can answer locally.

When checking memory:

```bash
top -l 1 -s 0 | grep PhysMem
```

For process-level investigation:

```bash
top -l 1 -o mem -stats pid,command,mem,cmprs,purg,user | head -n 35
ps -axo pid,user,%mem,rss,comm | sort -nrk3 | head -n 25
```

Important distinction: `top` can show compressed memory that is not the same as live resident memory. Cross-check with `ps` RSS before telling Jared one helper process is truly using gigabytes.

## App cleanup before local model runs

If Jared wants to free memory before running a local model, quit obvious heavy apps first:

```bash
osascript -e 'tell application "Wispr Flow" to quit' 2>/dev/null || true
osascript -e 'tell application "Antigravity" to quit' 2>/dev/null || true
```

Then verify:

```bash
pgrep -afil 'Wispr Flow|Antigravity' || true
top -l 1 -s 0 | grep PhysMem
```

Tiny remaining crashpad or update helper processes are not the main issue. Focus on main app processes and real resident memory.
