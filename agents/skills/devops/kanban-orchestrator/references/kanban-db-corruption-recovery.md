# Kanban DB Corruption Recovery — Session Log

## 02 June 2026 — performos-ai-team board, second corruption

### Symptoms
- `kanban_create` refused: `sqlite refused to open file: database disk image is malformed`
- Polly profile had 52 crash runs, all `pid not alive`, task `t_8592ccfe` stuck in `blocked`
- `launchctl list` showed `LastExitStatus = 256` for `ai.hermes.gateway-pollyperformos`
- Gateway error log: `kanban notifier tick failed: no such table: kanban_notify_subs`

### Recovery procedure

```bash
# 1. Verify recovered DB integrity
sqlite3 ~/.hermes/kanban/boards/<board>/kanban.recovered.db "PRAGMA integrity_check;"
# Must return: ok

# 2. Remove corrupt DB and WAL files
rm -f ~/.hermes/kanban/boards/<board>/kanban.db
rm -f ~/.hermes/kanban/boards/<board>/kanban.db-wal
rm -f ~/.hermes/kanban/boards/<board>/kanban.db.shm

# 3. Build fresh DB from recovery SQL (ignore "table already exists" parse errors)
sqlite3 ~/.hermes/kanban/boards/<board>/kanban.db < ~/.hermes/kanban/boards/<board>/kanban.recover.sql

# 4. Import events and links from old recovered DB
sqlite3 ~/.hermes/kanban/boards/<board>/kanban.db "
ATTACH '~/.hermes/kanban/boards/<board>/kanban.recovered.db' AS src;
INSERT OR IGNORE INTO task_events SELECT * FROM src.task_events;
INSERT OR IGNORE INTO task_links SELECT * FROM src.task_links;
DETACH src;
"

# 5. Restart gateway (MUST use launchctl, NOT hermes gateway restart)
launchctl unload ~/Library/LaunchAgents/ai.hermes.gateway-<profile>.plist
sleep 2
launchctl load ~/Library/LaunchAgents/ai.hermes.gateway-<profile>.plist
```

### Notes
- `hermes gateway restart` from inside the gateway is blocked to prevent loops. Use `launchctl unload/load`.
- Do NOT use `sqlite3 .recover` — it drops tables Hermes expects.
- This was the second corruption on this board. Investigate root cause if it happens again.

## 03 June 2026 — performos-ai-team board, third corruption

Third corruption in 24 hours on the same board. Pattern is now confirmed as recurring. Root cause unknown — likely WAL/journal issues during forced process termination.

### Updated recovery procedure (broader table import)

The previous import only covered `task_events` and `task_links`. The 03 June recovery added `task_comments`, `kanban_notify_subs`, and `task_attachments`:

```bash
# 4. Import ALL metadata tables from recovered DB
sqlite3 ~/.hermes/kanban/boards/<board>/kanban.db "
ATTACH '~/.hermes/kanban/boards/<board>/kanban.recovered.db' AS rec;
INSERT OR IGNORE INTO task_events SELECT * FROM rec.task_events;
INSERT OR IGNORE INTO task_links SELECT * FROM rec.task_links;
INSERT OR IGNORE INTO task_comments SELECT * FROM rec.task_comments;
INSERT OR IGNORE INTO kanban_notify_subs SELECT * FROM rec.kanban_notify_subs;
INSERT OR IGNORE INTO task_attachments SELECT * FROM rec.task_attachments;
SELECT 'events:' || COUNT(*) FROM task_events;
SELECT 'links:' || COUNT(*) FROM task_links;
SELECT 'comments:' || COUNT(*) FROM task_comments;
SELECT 'notify:' || COUNT(*) FROM kanban_notify_subs;
DETACH rec;
"
```

### Strategic decision

At three corruptions in 24 hours, Brock stopped creating new Kanban tasks for that session and switched to `delegate_task` directly. For urgent single-task routing where the kanban DB is unreliable, `delegate_task` is the fallback path. This avoids losing task context to corruption during the session.