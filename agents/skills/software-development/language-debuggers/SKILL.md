---
name: language-debuggers
description: "Interactive debugging of Python (pdb/debugpy) and Node.js (--inspect/CDP) runtimes — breakpoints, stepping, remote attach, Hermes-specific process debugging."
version: 1.0.0
author: Hermes Agent (unified from python-debugpy + node-inspect-debugger)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, python, nodejs, pdb, debugpy, cdp, breakpoints]
    related_skills: [systematic-debugging]
---

# Language Debuggers

Interactive debugging of Python and Node.js runtimes. When `print()`/`console.log` isn't enough and you need breakpoints, stepping, call-stack walking, scope inspection, or remote attach to a running process.

**Start with the simplest tool that works.** `breakpoint()` in Python, `node inspect` in Node.js.

## When to Use

- A test fails and the traceback doesn't reveal why a value is wrong
- You need to step through a function and watch state mutate
- A long-running process (Hermes gateway, daemon, dev server) misbehaves
- Post-mortem: an exception fired in prod-ish code and you want to inspect locals
- A subprocess / child worker is the actual bug site

**Don't use for:** things `print()`/`logging.debug` or `console.log` solve in under a minute, or things `pytest -vv --tb=long --showlocals` already reveals.

---

## Python Debugger (pdb + debugpy)

Three tools, picked by situation:

| Tool | When |
|---|---|
| **`breakpoint()` + pdb** | Local, interactive, simplest. Add `breakpoint()` in source, run normally, get a REPL. |
| **`python -m pdb`** | Launch an existing script under pdb with no source edits. |
| **`debugpy`** | Remote / headless / attach to already-running process. DAP protocol, scriptable. |

### pdb Quick Reference

| Command | Action |
|---|---|
| `h` / `h cmd` | help |
| `n` | next line (step over) |
| `s` | step into |
| `r` | return from current function |
| `c` | continue |
| `unt N` | continue until line N |
| `l` / `ll` | list source / full function |
| `w` | where (stack trace) |
| `u` / `d` | move up / down stack |
| `a` | print args of current function |
| `p expr` / `pp expr` | print / pretty-print |
| `b file:line` | set breakpoint |
| `b func` | break on function entry |
| `cl N` | clear breakpoint N |
| `!stmt` | execute Python |
| `interact` | drop into full REPL in current scope |
| `q` | quit |

### Common Recipes

**Local breakpoint:**
```python
def compute(x, y):
    result = some_helper(x)
    breakpoint()  # drops into pdb here
    return result + y
```
Don't forget to remove `breakpoint()` before committing.

**Debug a pytest test:**
```bash
scripts/run_tests.sh tests/path/to/test_file.py::test_name --pdb -p no:xdist
```
pdb does NOT work under xdist. Always add `-p no:xdist` or `-n 0`.

**Post-mortem on any exception:**
```python
import pdb, sys
try:
    run_the_thing()
except Exception:
    pdb.post_mortem(sys.exc_info()[2])
```

**Remote debug with debugpy (attach to running process):**
```bash
pip install debugpy
```
```python
import debugpy
debugpy.listen(("127.0.0.1", 5678))
debugpy.wait_for_client()
debugpy.breakpoint()
```

**Remote debug without source edits:**
```bash
python -m debugpy --listen 127.0.0.1:5678 --wait-for-client your_script.py
```

**Attach to already-running process:**
```bash
python -m debugpy --listen 127.0.0.1:5678 --pid <pid>
```

**Simpler alternative: remote-pdb**
```bash
pip install remote-pdb
```
```python
from remote_pdb import set_trace
set_trace(host="127.0.0.1", port=4444)
```
Then: `nc 127.0.0.1 4444`

### Python Pitfalls
- pdb under pytest-xdist silently does nothing — always use `-p no:xdist`
- `breakpoint()` in CI / non-TTY contexts hangs — never commit it
- `PYTHONBREAKPOINT=0` disables all `breakpoint()` calls
- `debugpy.listen` blocks only with `wait_for_client()`
- Attach to PID fails on hardened kernels (`ptrace_scope=1`)
- `scripts/run_tests.sh` strips credentials and sets `HOME=<tmpdir>` — debug with raw `pytest` first

---

## Node.js Inspect Debugger

Two tools: `node inspect` (built-in CLI REPL) and CDP via `chrome-remote-interface` (scriptable automation).

### Quick Reference: `node inspect` REPL

```bash
node inspect path/to/script.js
# or with tsx
node --inspect-brk $(which tsx) path/to/script.ts
```

| Command | Action |
|---|---|
| `c` / `cont` | continue |
| `n` / `next` | step over |
| `s` / `step` | step into |
| `o` / `out` | step out |
| `pause` | pause running code |
| `sb('file.js', 42)` | set breakpoint |
| `cb('file.js', 42)` | clear breakpoint |
| `breakpoints` | list breakpoints |
| `bt` | backtrace |
| `list(5)` | show 5 lines around current position |
| `repl` | drop into REPL in current scope |
| `exec expr` | evaluate expression |
| `kill` | kill script |
| `.exit` | quit |

### Attaching to Running Process

```bash
kill -SIGUSR1 <pid>           # enable inspector
node inspect -p <pid>          # attach
```

Start with inspector from launch:
```bash
node --inspect script.js       # listen, keep running
node --inspect-brk script.js   # listen AND pause on first line
```

For TypeScript via tsx:
```bash
node --inspect-brk --import tsx script.ts
```

### Programmatic CDP

```bash
npm i -g chrome-remote-interface
```

Driver script pattern:
```javascript
const CDP = require('chrome-remote-interface');
(async () => {
  const client = await CDP({ port: 9229 });
  const { Debugger, Runtime } = client;
  Debugger.paused(async ({ callFrames }) => { /* inspect, then resume */ });
  await Runtime.enable();
  await Debugger.enable();
  await Debugger.setBreakpointByUrl({ urlRegex: '.*app\\.tsx$', lineNumber: 119 });
  await Runtime.runIfWaitingForDebugger();
})();
```

### Debugging Hermes ui-tui

```bash
cd /home/bb/hermes-agent/ui-tui
npm run build
node --inspect-brk dist/entry.js
# In another terminal:
node inspect -p <pid>
```

For running `hermes --tui`:
```bash
hermes --tui &
TUI_PID=$(pgrep -f 'ui-tui/dist/entry' | head -1)
kill -SIGUSR1 "$TUI_PID"
curl -s http://127.0.0.1:9229/json/list | jq -r '.[0].webSocketDebuggerUrl'
node inspect ws://127.0.0.1:9229/<uuid>
```

### Running Vitest Under Debugger

```bash
node --inspect-brk ./node_modules/vitest/vitest.mjs run --no-file-parallelism src/app/foo.test.tsx
```

### Node.js Pitfalls

- Wrong line numbers in TS source — breakpoints hit emitted JS, not `.ts`. Use `--enable-source-maps`.
- `--inspect` vs `--inspect-brk` — the former doesn't pause; script races past breakpoints.
- Port collisions on 9229 — use `--inspect=0` for random port.
- Child processes — `--inspect` on parent does NOT inspect children. Use `NODE_OPTIONS='--inspect-brk'`.
- Background kills — if you Ctrl+C out of `node inspect` while target is paused, target stays paused.
- Security — `--inspect=0.0.0.0:9229` exposes arbitrary code execution. Always bind to `127.0.0.1`.

---

## Verification Checklist

**Python:**
- [ ] `pip install debugpy` confirmed with `python -c "import debugpy; print(debugpy.__version__)"`
- [ ] Remote debug port listening: `ss -tlnp | grep 5678`
- [ ] First breakpoint hits (check `PYTHONBREAKPOINT=0`, xdist, or execution finished before attach)
- [ ] `where` / `w` shows expected call stack
- [ ] No stray `breakpoint()` / `set_trace()` left in committed code

**Node.js:**
- [ ] `curl -s http://127.0.0.1:9229/json/list` returns expected target
- [ ] First breakpoint hits (check `--inspect-brk`, attach timing)
- [ ] Source listing at pause shows right file
- [ ] `exec process.pid` in `repl` returns expected PID
