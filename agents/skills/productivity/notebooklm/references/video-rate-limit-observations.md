# NotebookLM Video Generation — Rate Limit Observations

**Date:** 22 June 2026
**Source:** Live session generating video from YouTube source (Ethan Mollick interview)

## What happened

1. First video generation attempt: artifact created, status `in_progress`, then disappeared from server after ~3 minutes. Error: "artifact was removed from the list by the server."
2. Second attempt with a fresh notebook: same result — artifact disappeared after ~5 minutes with identical error.
3. Conclusion: the first failed attempt consumed the daily quota. The quota is **account-level**, not notebook-level. A fresh notebook does not reset it.

## Key findings

- Daily video quota is extremely low (likely 1-2 per day per account)
- Failed generations still count against the quota
- Retrying in the same session with a fresh notebook does NOT work
- The `notebooklm artifact wait` command with `--timeout 2700` fails in foreground terminal mode (max 600s timeout). Use background mode + manual polling instead.
- Web UI has a separate quota pool from the API/CLI

## Recommended workflow

1. Before generating video, warn the user about the low daily quota
2. If the first attempt fails, do NOT retry — advise the user to try the web UI or wait until the next day
3. For long waits, use background process + `notebooklm artifact list --json` polling
4. Prefer audio generation (podcast) when possible — it has higher rate limits and is more reliable

## Delete command correction

The delete command is `notebooklm delete <id>` (NOT `notebooklm notebook delete <id>`).
