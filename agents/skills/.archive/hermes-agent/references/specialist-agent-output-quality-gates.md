# Specialist agent output quality gates

Use this when Jared refines a profile-backed specialist agent's output format or asks how to guarantee the same quality every time.

## Pattern

For profile-backed specialist agents with canonical SOUL files in Obsidian:

1. Patch the canonical Obsidian SOUL file, not only the current chat prompt.
2. Add an explicit quality gate before the agent sends replies or files.
3. Make the gate concrete and checkable, for example required headings, source rules, unsupported-claim rules, and verification steps.
4. If the output is a generated file, require the agent to re-open or inspect the file after generation and verify structure before sending.
5. Generate or update one exemplar output file if useful, then verify the key headings or sections programmatically.
6. Restart the profile gateway so the changed SOUL is active.

## Jared preference observed

For HR legislation mapping docs, Jared prefers the practical decision-prep sections near the top, before detailed legislation:

1. Purpose note
2. Incident / question
3. What this means you may be able to do
4. To proceed, what would need to be done
5. Risks to cross off before acting
6. Legislation and source
7. Verification note

Keep legislation and source together for each legal point: source, direct link, quote, and plain-English meaning. Do not scatter source, legislation, and action mapping into separate unrelated sections.

## Pitfalls

- Do not treat a good one-off output as guaranteed. Encode the format in the SOUL plus a pre-send quality gate.
- Do not rely on memory alone for specialist-agent formatting. The specialist profile reads its own SOUL.
- Do not create Gmail drafts or other external side effects until recipient, subject, and body are known and the user has confirmed draft creation scope.
