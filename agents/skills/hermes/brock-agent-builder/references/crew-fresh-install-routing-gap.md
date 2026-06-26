# Crew Fresh-Install Routing Gap

## The problem

When a business clones the Crew repo and invokes a skill directly from the filesystem (without installing plugins), Step 0 runs and tries to route to `crew-core-brand-context` when brand-context.md is missing. The brand-context skill is not registered as a plugin, so Claude Code cannot find it. The skill fails to onboard the business.

This was discovered on a Mac Mini fresh-install test (26 June 2026). The FAQ Builder was invoked from the repo path with no plugins installed.

## Root cause

Skills reference each other by name in Step 0 ("run `crew-core-brand-context`") but on a fresh filesystem install, there is no plugin registry. Claude Code does not know where to find the named skill.

## The error path

1. Business clones repo
2. Business opens Claude Code in repo directory
3. Business invokes a skill via `Read packs/.../SKILL.md`
4. Skill's Step 0 finds no brand-context.md
5. Step 0 says "run `crew-core-brand-context`"
6. Claude Code has no registered skill called `crew-core-brand-context`
7. Routing fails

## Temporary bypass

Tell the skill to ask the 11 questions inline instead of routing:

```
Read crew-skill-packs/packs/07-support/crew-support-faq-builder/SKILL.md. I need an FAQ. Do not route to brand-context. Ask me the 11 onboarding questions yourself, then build the FAQ.
```

## Permanent fix candidates

1. **Inline fallback in Step 0.** Every skill's Step 0 should have a fallback: "If crew-core-brand-context is not installed, ask the 11 questions inline." This makes skills self-sufficient on fresh install.

2. **Install script creates brand-context.** The install.sh or package.sh could scaffold a blank brand-context.md template so Step 0 always finds something.

3. **Plugin install as prerequisite.** Require `claude plugins install crew-core` before any other skill is invoked. Document this as the first step.

4. **Single-file onboarding.** Bundle the 11 questions into a standalone script that runs before any skill, independent of the plugin system.

## Related gap: README brand leak

When a business opens Claude Code inside the crew-skill-packs repo directory, Claude reads the README.md and CLAUDE.md automatically. If these files mention the creator's brand (PerformOS, Jared Croxton), Claude offers that business name as context before any skill loads.

Fix applied: stripped all brand identification from README.md. CLAUDE.md was not present in the repo but may exist in parent directories. The brand-context skill's Discovery section now explicitly says "Do not scan the repo, README, or any other file for business clues."
