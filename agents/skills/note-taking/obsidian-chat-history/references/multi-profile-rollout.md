# Multi-profile rollout notes

Use this when Jared wants every specialist agent to follow the same Obsidian chat-history capture standard.

## Why it matters

A skill saved only in the active/default profile does not automatically teach other profile-backed agents. Each specialist profile needs access to the skill, otherwise capture standards drift between Brock, Bob, Lara, Sam, Polly, Harry, Nelly, and other agents.

## Rollout pattern

1. Treat the default profile copy as the source of truth unless Jared names another source.
2. Copy the complete `obsidian-chat-history` skill directory into each specialist profile's `skills/` tree.
3. Preserve support files, not just `SKILL.md`.
4. Verify each target profile contains the skill path and readable `SKILL.md`.
5. Restart the specialist gateway or bot process so the profile reloads its skill library.
6. Report exactly which profiles were updated and which were not.

## Quality bar

- Do not create one narrow skill per agent. Keep one class-level `obsidian-chat-history` skill and distribute it.
- If a profile cannot be updated, report the profile name and reason. Do not imply global coverage.
- Separate procedure from automation: this skill gives agents the closing discipline, but true capture of every message requires a gateway or session-store export hook.

## Verification language

Use a concrete completion line such as:

`Verified: obsidian-chat-history exists in <profile> and gateway restarted.`

Avoid vague claims like:

`All agents should now know this.`
