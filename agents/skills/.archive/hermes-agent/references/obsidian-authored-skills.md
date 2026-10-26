# Obsidian-authored skills for live Hermes agents

Use this when Jared says a specialist should "use this skill" and the better version lives in the Obsidian vault rather than the live Hermes skill library.

## Trigger

- Jared points to a skill note under `/Users/jc/Desktop/Obsidian/Skills/`
- The live Hermes skill is weaker or outdated
- A specialist agent should start using the Obsidian-authored version immediately

## Pattern

1. Find the canonical Obsidian skill note, usually under:
   - `/Users/jc/Desktop/Obsidian/Skills/<name>.md`
2. Back up the live Hermes skill before replacing it:
   - `~/.hermes/skills/<category>/<skill>/SKILL.md.bak-<timestamp>`
3. Copy the Obsidian note over the live Hermes `SKILL.md`.
4. Verify the live skill content now reflects the Obsidian version.
5. Restart the relevant profile gateway so new sessions load the updated skill.
6. Tell Jared plainly that existing live conversations may still hold old context, but new sessions will use the updated skill.

## Jared-specific note

If Jared says he updated a skill in Obsidian and wants Nelly or another specialist to use it now, do not just explain the difference between Obsidian and Hermes. Perform the replacement, keep a timestamped backup, restart the profile gateway, and confirm the skill is live.

## Pitfalls

- Updating only the Obsidian note does not update the live Hermes skill automatically.
- Replacing a live skill without a backup makes rollback harder.
- Restarting the profile gateway matters for specialist bots so future turns pick up the new skill file.
- This pattern is for durable skill content, not secrets or tokens.
