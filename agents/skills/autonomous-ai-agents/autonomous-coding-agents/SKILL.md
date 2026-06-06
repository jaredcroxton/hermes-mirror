---
name: autonomous-coding-agents
description: Use when delegating coding, PR review, or implementation work to external coding-agent CLIs such as Claude Code, Codex, or OpenCode from Hermes.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [coding-agents, claude-code, codex, opencode, delegation, tmux, pty]
    related_skills: [hermes-agent]
---

# Autonomous Coding Agents

## Overview

This umbrella covers running external coding-agent CLIs from Hermes. The class-level workflow is the same across Claude Code, Codex, and OpenCode: choose one-shot vs interactive mode, isolate the workspace, launch with the right terminal/PTY behavior, monitor output, and verify the produced code yourself before reporting success.

## When to Use

- The user asks to delegate implementation or PR review to Claude Code, Codex, or OpenCode.
- A task is large enough to benefit from an independent agent process.
- You need a long-running coding subprocess that can continue while Hermes monitors it.

## Universal workflow

1. **Choose mode.** Use one-shot CLI mode for bounded tasks; use a PTY/tmux/background process for interactive agents.
2. **Isolate.** Prefer a git worktree or dedicated workspace for edits to avoid conflict with the parent session.
3. **Pass a complete brief.** Include repo path, branch, acceptance criteria, tests, and constraints.
4. **Monitor.** Poll/capture the process; answer prompts only with grounded context.
5. **Verify independently.** Inspect diffs and run tests yourself. Never trust a child agent's self-report as proof.

## Agent-specific notes

### Claude Code
- Best for broad feature implementation and iterative codebase work.
- Use tmux/PTY when the CLI expects an interactive terminal.
- Watch for permission prompts; configure bypass only when the user/session permits it.

### Codex
- Good for concise code changes, PR review, and structured one-shot tasks.
- Background PTY mode works well when Codex may ask follow-up questions.
- Keep prompts explicit about file boundaries and test commands.

### OpenCode
- Resolve the binary path first; installations vary.
- Use interactive background sessions for multi-turn implementation or review.
- Exit or kill cleanly after collecting the result.

## Common Pitfalls

1. **Delegating verification.** The parent Hermes session must run tests/read diffs before claiming completion.
2. **No workspace isolation.** Parallel agents editing the same tree cause conflicts.
3. **Launching interactive CLIs without PTY.** Use tmux or `terminal(..., pty=true/background=true)` patterns.
4. **Underspecified prompts.** External agents do worse when repo path, target files, and done criteria are missing.

## Verification Checklist

- [ ] Agent command launched successfully and produced inspectable output.
- [ ] Diffs/files were read back in Hermes.
- [ ] Tests or equivalent checks were run by Hermes.
- [ ] Any remaining prompts or failures were surfaced honestly.
