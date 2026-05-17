# hermes-mirror

Agent Backup and reproducibility mirror for Jared Croxton's Hermes setup.

This public repository stores sanitized setup notes, agent specs, reusable skills, and recovery documentation.

## Security policy

This repo is public. Do not commit:

- `.env` files
- API keys or tokens
- OAuth credential files
- cookies
- SSH private keys
- raw private emails
- raw calendar data
- sensitive PII

Use templates, examples, and documentation instead.

## Current mirrored agents and skills

- `agents/BLAST.md` — BLAST build-and-ship agent spec.
- `agents/Bob_Builder.md` - bob_builder dedicated build-and-ship sub-agent profile spec.
- `agents/Notebook_Nelly.md` - Notebook_Nelly NotebookLM research and content generation profile spec.
- `skills/claude-code-builder/SKILL.md` — sanitized public copy of the local Hermes BLAST skill.
- `skills/notebooklm/SKILL.md` - sanitized public copy of the local Hermes NotebookLM skill.
