# Playbook-backed orchestrators

Use this pattern when Jared wants a specialist capability with multiple sub-domains, but he will only ever use one front door.

## When it fits

- The user does not need to talk directly to the sub-specialists.
- The sub-domains are expertise modules, not independent operators.
- The Mac or gateway already runs many agents and more bots would add maintenance overhead.
- The output is advice, prompts, analysis, or structured artefacts that one orchestrator can produce by loading the right playbook.

## Architecture

Build one persistent Hermes profile as the orchestrator. Store each specialist domain as a markdown playbook under the agent folder, usually:

`/Users/jc/Desktop/Obsidian/Agents/<Agent_Name>/playbooks/<domain>.md`

The orchestrator soul should say:

- It is the single front door.
- It names the playbook used before producing output.
- It does not perform downstream execution outside its remit.
- It asks one clarifying question at a time when model, output format, or definition of done is missing.
- It keeps reusable outputs in a prompt or artefact library.

## File set

Minimum package:

- `<Agent_Name>-Soul.md`
- `<Agent_Name>/README.md`
- `<Agent_Name>/props-prompt.md` or equivalent operating prompt
- `<Agent_Name>/playbooks/*.md`
- `<Agent_Name>/prompt-library/README.md` when outputs should be reused
- Setup prompts for Hermes profile creation and Telegram/gateway wiring
- Updates to the parent orchestrator soul and Agent Registry

## Quality gates

- Do not create six bots when one front door plus playbooks gives the same user experience.
- Each playbook needs a live model or knowledge table that can be updated without rewriting the soul.
- The orchestrator must not pretend to run downstream generation. It prepares the prompt or plan, then hands it back.
- Verify the profile identity with a small probe after wiring the SOUL symlink.
- Package the deliverable and run a zip integrity test before handoff when Jared asks to upload everything.

## Example

PROP became `Piper_PromptOps`: one prompt operations orchestrator with playbooks for research, image, video, learning, voice/audio, agent/system prompts, marketing/SEO, and business strategy. The design avoided six extra Telegram bots while preserving specialist output quality.