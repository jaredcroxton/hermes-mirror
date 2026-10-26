# Specialist agent output contracts

Use this reference when updating a profile-backed specialist agent's SOUL.md after Jared corrects the format of that agent's deliverables.

## Principle

When a specialist agent produces downloadable outputs, the SOUL should encode the desired decision workflow, not just the data fields. Jared often wants documents that help him prepare for a business conversation, not a raw evidence table.

## HR/legal-source mapping pattern

For Harry_HR-style employment legislation mapping, use a decision-prep structure:

1. **Purpose note** — state the document is a source-grounded understanding tool, not final legal advice, and Jared will verify with the business HR expert before acting.
2. **Incident / question** — summarise the workplace situation and the precise legal question.
3. **Legislation and source** — keep the official source, direct link, verbatim quote, and plain-English meaning together for each legal point. Do not scatter source, quote, and interpretation across separate sections.
4. **What this means you may be able to do** — practical interpretation of what the source appears to permit or require, without giving legal advice.
5. **To proceed, what would need to be done** — checklist of verification and process steps before action.
6. **Risks to cross off before acting** — the other side of the analysis: exceptions, missing checks, protected attributes, general protections/adverse action, procedural fairness, documentation gaps, contract/award/policy issues, final pay, retaliation or timing risks.
7. **Verification note** — explicit reminder that the document is not gospel and final action should be verified with the business HR expert.

## SOUL patching guidance

When Jared corrects a specialist agent's output format:

- Patch the agent's canonical Obsidian SOUL file, not just memory.
- Patch both the chat response format and downloadable output format if both exist.
- Restart that profile's gateway so the updated SOUL is active.
- If the profile SOUL is symlinked from `~/.hermes/profiles/<profile>/SOUL.md`, patch the Obsidian target path.
- Where helpful, regenerate the last deliverable in the corrected format as a concrete example.

## Avoid

- Do not leave source, quote, and interpretation in three disconnected sections when the user needs a decision-prep document.
- Do not present these outputs as final legal advice.
- Do not encode a one-off incident as a permanent rule. Encode the reusable document shape and verification workflow.