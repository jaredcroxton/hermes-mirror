---
name: github-workflows
description: "Use when doing GitHub operations end-to-end: authentication, repository management, codebase inspection, issues, pull requests, CI triage, releases, and code review."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, git, gh, pull-requests, issues, review, repositories, ci]
    related_skills: []
---

# GitHub Workflows

## Overview

This umbrella covers GitHub work as one operational class. Start by establishing authentication and repo context, then choose the relevant lane: repository management, codebase inspection, issue triage, PR lifecycle, code review, CI/release handling.

## When to Use

- Configure `gh`, HTTPS tokens, SSH keys, or git credentials.
- Clone, create, fork, mirror, or release repositories.
- Inspect codebase size/language mix before planning work.
- Create or triage GitHub issues.
- Branch, commit, push, open PRs, monitor CI, merge, or close PRs.
- Review a PR or local diff and leave comments.

## Universal preflight

1. Run `git status` and identify repo root/branch.
2. Check remotes and auth (`gh auth status` when available).
3. Confirm default branch and whether the working tree is clean.
4. Choose `gh` CLI when authenticated; otherwise use git/REST fallbacks.
5. Never claim a PR/issue/release exists without reading back the URL/number.

## Lane quick-reference

### Authentication
- Prefer `gh auth login/status` when available.
- For git-only environments, configure credential helpers or SSH keys deliberately.
- Avoid embedding tokens in URLs unless the user explicitly accepts the risk.

### Repository management
- Clone/fork/create repos, manage remotes, and releases.
- For backup/mirror repositories, keep secrets, sessions, caches, auth files, and runtime databases out of the mirror.
- For scheduled mirror backups that reuse `/tmp` workspaces, verify `origin`, branch, and working tree before copying. If the workspace has a missing remote, unexplained deletions, or stale untracked cache files, delete and freshly clone rather than pulling into a dirty mirror.
- Before committing a public mirror backup, run a positive secret scan across the staged workspace for provider token patterns, not only the one token named in the task. Redact examples too when they match real token prefixes such as `ghp_`, `sk-`, `xoxb-`, or Google API-key shapes.
- When mirroring Hermes skills, check for symlinks after copy. If a skill path points outside `~/.hermes/skills`, resolve and copy the real skill directory rather than committing a repository symlink. See `references/hermes-mirror-backup.md`.

### Codebase inspection
- Use tools such as `pygount`/language counters to establish LOC, language mix, and dependency footprint before large plans.
- Exclude generated/vendor/cache directories.

### Issues
- Use templates for feature requests and bugs.
- Include reproduction steps, expected behavior, and labels/assignees when known.

### Pull requests and CI
- Use conventional commits and a clear PR body with test plan.
- Monitor CI after opening; troubleshoot failures before declaring done.

### Code review
- Review the diff, not only summaries.
- Flag correctness, security, tests, maintainability, and user-impact risks.
- For inline comments, verify the line positions match the current PR diff.

## Verification Checklist

- [ ] Auth path was verified or limitation stated.
- [ ] Target repo/branch/remotes were confirmed.
- [ ] Created resources were read back with URL/number.
- [ ] CI/tests/review evidence was included in the final response.
