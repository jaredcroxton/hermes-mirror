---
name: apple-ecosystem
description: "Use when managing Apple apps and device workflows from Hermes on macOS: Notes, Reminders, iMessage/SMS, Find My, and safe background desktop automation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [apple, macos, notes, reminders, imessage, findmy, automation]
    related_skills: [macos-computer-use]
---

# Apple Ecosystem Operations

## Overview

Use this umbrella when the task touches Apple-native personal productivity or device workflows on Jared's Mac. Prefer the dedicated CLI path first (`memo`, `remindctl`, `imsg`), then fall back to macOS UI automation only when no CLI/API exists.

## When to Use

- Create, search, or update Apple Notes.
- Add, list, or complete Apple Reminders.
- Send or inspect iMessage/SMS conversations.
- Locate Apple devices or AirTags through Find My.
- Coordinate these actions with background-safe desktop automation.

## Workflow by domain

### Notes (`memo`)
- Verify the memo CLI exists before claiming Apple Notes support.
- Use search before creating duplicate notes.
- Preserve note titles and folder intent exactly; Apple Notes formatting support is limited.

### Reminders (`remindctl`)
- Use natural-language dates only when the CLI supports them; otherwise convert to explicit due dates.
- Confirm the target list exists before adding important reminders.
- For completion, list matching reminders first to avoid closing the wrong task.

### iMessage/SMS (`imsg` and Photon)

Two paths exist for iMessage from Hermes:

**Photon Spectrum (recommended, Hermes v0.17.0+):** Built-in platform adapter. No BlueBubbles, no Messages.app relay, no Apple malware flag. `hermes photon setup` → `hermes gateway start`. See `references/photon-imessage-setup.md` for full setup.

**imsg CLI (legacy):** Local Messages.app bridge. Prefer chat IDs or exact recipient identifiers. Avoid Markdown/format assumptions; SMS/iMessage sends plain user-visible text. For attachments, verify the file path exists before sending.

### Find My
- There is no stable public CLI. Use AppleScript/UI automation and screenshots.
- Do not guess device location from stale UI; refresh/open Find My and inspect current text or screenshot.
- Use `macos-computer-use` when interacting with the desktop so the user's cursor/focus is not stolen.

## Common Pitfalls

1. **Treating all Apple apps as scriptable.** Notes/Reminders/messages may have CLI helpers; Find My often needs UI automation.
2. **Skipping verification.** Always read back the created note/reminder/message result or inspect the UI/logs.
3. **Foreground disruption.** For UI tasks, load `macos-computer-use` and use background-safe capture/action patterns.

## Verification Checklist

- [ ] Required helper command is installed or a UI fallback was used.
- [ ] Target account/list/contact/device was verified before action.
- [ ] The final state was read back or visually confirmed.
