# Profile-backed specialist Hermes agents

Use this pattern when the user wants a named specialist agent (for example, a build/deploy worker) that can be launched independently from the main Hermes assistant.

## Pattern

1. Create or clone a dedicated profile:
   ```bash
   hermes profile create <profile-name> --clone-all
   # or clone selectively if isolation is preferred
   hermes profile create <profile-name> --clone <source-profile>
   ```
2. Put the persona/operating contract in the profile's `SOUL.md`:
   ```text
   ~/.hermes/profiles/<profile-name>/SOUL.md
   ```
   If the user keeps specialist souls in an Obsidian vault, symlink the profile `SOUL.md` to the vault file so future edits happen in one source of truth. Before symlinking, validate any file paths named in the soul, especially context exports and brand-library folders. If a referenced path is missing, search the likely vault/product folder, patch the soul to the real path, and only then link it into the profile. This prevents a new specialist from starting every session with stale context-path instructions.
3. If the agent should always use a class skill, encode that in `SOUL.md` and/or launch with `--skills <skill-name>`. If you created or updated a user-local skill after cloning the profile, also copy or install that skill into the profile's own skills tree so the specialist profile can load it independently:
   ```bash
   mkdir -p ~/.hermes/profiles/<profile-name>/skills/<category>/<skill-name>
   cp ~/.hermes/skills/<category>/<skill-name>/SKILL.md \
      ~/.hermes/profiles/<profile-name>/skills/<category>/<skill-name>/SKILL.md
   ```
4. Create a wrapper alias for human-friendly launch:
   ```bash
   hermes profile alias <profile-name>
   ```
   If the desired shell command differs from the profile name, create a small wrapper manually and make it executable:
   ```bash
   cat > ~/.local/bin/<desired_alias> <<'SH'
   #!/bin/sh
   exec hermes -p <profile-name> "$@"
   SH
   chmod +x ~/.local/bin/<desired_alias>
   ```
5. Verify both interactive and one-shot launch paths. For skill-backed agents, the one-shot should prove both identity and workflow/skill recognition, not just persona text:
   ```bash
   <alias> chat -q "Identify yourself and your primary skill."
   hermes --profile <profile-name> chat -q "Identify yourself and your primary skill."
   <alias> chat -q "State your name, primary skill, and the first operational steps in order only."
   ```
6. If the setup should be reproducible publicly, mirror only sanitized specs: persona summary, launch command, profile name, and skills. Do not mirror `.env`, auth files, tokens, private session logs, or user PII. When mirroring, include both the agent spec and any sanitized skill spec needed to reproduce the profile.

## Example shape

- Profile: `bobbuilder`
- Alias: `bob_builder`
- Persona: build-and-ship specialist
- Primary skill: `claude-code-builder`
- Verification prompt: `Identify yourself and your primary skill.`

## Renaming an existing specialist profile

When the user wants an agent name reversed or otherwise corrected (for example `Notebook_Nelly` → `Nelly_Notebook`), treat it as a profile identity migration, not just a shell alias change:

1. Rename the profile:
   ```bash
   hermes profile rename <old-profile> <new-profile>
   ```
2. Create the exact desired human alias:
   ```bash
   hermes profile alias <new-profile> --name <desired_alias>
   ```
3. Remove stale wrapper scripts that point at the old profile or old alias, after checking they are old wrappers:
   ```bash
   grep -q '<old-profile>' ~/.local/bin/<old_alias> && rm ~/.local/bin/<old_alias>
   ```
4. Patch `~/.hermes/profiles/<new-profile>/SOUL.md` so the display name, identity statement, local operating requirements, profile name, and alias all match the new naming.
5. Verify no old-name references remain in the active `SOUL.md` or wrapper, then run a one-shot identity smoke test:
   ```bash
   <desired_alias> chat -q 'Reply with only your name and profile alias.' -Q
   ```
6. Update durable memory and any sanitized public mirror/spec that documents the specialist.

## Specialist review gates

When a specialist profile produces work that affects people, money, reputation, executive alignment, external submission, or the user's time, encode the review requirement in the specialist's canonical `SOUL.md`, not just in chat. For mandatory review classes such as DOE or executive/business submissions:

1. Add a local operating requirement that the specialist must not submit, send, publish, or present the artefact as final until the named reviewer approves it.
2. Require the specialist to mark the output as `Pending <reviewer> review` while waiting.
3. Require a short review handoff block with source agent, what it is, audience, decision needed, recommended action, main risk, assumptions, link/file path, and what the reviewer should challenge.
4. Update any Agent Registry note or public sanitized spec so the runtime governance is visible outside the `SOUL.md`.
5. Restart the profile gateway if it is already running, then verify the profile still starts and the symlinked/canonical `SOUL.md` contains the gate.

This keeps the specialist productive while preventing accidental final submission of material that needs CEO-level pressure-testing.

## Telegram strategy for specialist profiles

Specialists can each have their own Telegram bot, but this adds BotFather tokens, per-profile gateway setup, and one gateway process/service per agent. Prefer this decision rule:

- Use the default assistant as the command centre/orchestrator when the specialist is occasional, when multiple agents need coordination, or when the user wants one conversation thread.
- Give a specialist its own Telegram bot when it is highly conversational or receives forwarded files/links directly (for example a study tutor or NotebookLM ingestion agent).
- For each profile-specific Telegram bot: create a separate BotFather bot/token, run `<alias> gateway setup`, then `<alias> gateway start`; keep tokens in the profile `.env`/gateway config, never in chat or public mirrors.

## Pitfalls

- Profiles are isolated; do not assume the child profile has the same tools, memory, env vars, or skills unless cloned or configured.
- Public mirrors are useful for reproducibility, but sanitize aggressively. Store secrets in `.env` or credential stores only.
- Treat the main assistant as orchestrator and the named profile as the specialist worker; avoid mixing long-lived specialist instructions into the default profile unless the user explicitly wants that.
- Preserve the user's requested agent name exactly. Do not reinterpret a profile/alias into a different display identity because the persona text sounds like a brand name. If the user says the agent name should be `bob_builder`, `Nelly_Notebook`, or another exact string, the `SOUL.md` `## Name`, identity statement, mirror spec, and verification prompt must all use that exact name.
- Avoid relying on the auto-generated profile wrapper when the user chose a friendlier alias. Create the exact alias they named and verify `command -v <alias>` before reporting success.