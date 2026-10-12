# OwnerOS v5 CREW to Hermes rollout guardrails

Use this when reviewing or building OwnerOS v5, CREW workshop wiring, Hermes CREW install, Personas, Workforce SOP drawers, or one-brain demos.

## Core invariant

The cabinet remains `~/.claude/crew-state/`.

Do not create, migrate to, or rewrite skills toward `~/.hermes/crew-state/` for OwnerOS v5. The `.claude` name is historical. The behaviour is runtime-independent because every runtime reads and writes the same home-global cabinet.

## Workshop safety principle

Before the 29 August workshop:

- Read more.
- Delete nothing unless Jared explicitly approves the destructive operation.
- Rewrite nothing in the cabinet.
- Validate before showing.
- Fallback instead of crashing.

Do not clean counts by hard-deleting invalid skill folders. Prefer ignoring invalid skill roots that lack a valid `SKILL.md`, then archive after the workshop if Jared approves.

## Hermes install facts

Hermes walks nested skills with `os.walk(..., followlinks=True)`, so `install.sh --target ~/.hermes/skills/crew` is a valid category install pattern. Skill names come from the containing directory, so names remain like `crew-sales-outreach-draft`.

Hermes truncates skill descriptions in the prompt index to roughly 57 visible characters. CREW trigger language often appears later in the description. Do not rely on Hermes auto-routing for workshop demos. Every kickoff prompt should name the exact skill.

Hermes loads skills as reference documents. It does not guarantee CREW Step 0 or Final Step will execute unless the prompt explicitly asks for them. The on-camera one-brain demo must name both.

## One-brain demo prompt shape

Use this pattern for any Hermes CREW proof:

```text
Use the CREW skill `crew-sales-prospect-brief`.
Follow it exactly, including Step 0 Context Recovery and the Final Step Handoff Save.
Read the brand context at ~/.claude/crew-state/brand-context.md.
Write the handoff into ~/.claude/crew-state/projects/workshop-01-brisbane-aug29/.
[real input]
```

Then prove:

1. The handoff appears in OwnerOS Projects without OwnerOS being told.
2. `~/.hermes/crew-state` is still absent.

If Hermes cannot write to the cabinet, CREW skills should stage the handoff inline and mark it blocked. OwnerOS will not show staged output, so rehearse the full path before the workshop.

## Play library drift

OwnerOS, the installed skill, and the source repo can drift:

- Source repo: `packs/01-core/crew-core-using-crew/references/plays.md`
- Installed skill: `~/.claude/skills/crew-core-using-crew/references/plays.md`
- OwnerOS app copy: `/Users/jc/OS System/playbook.md`

For OwnerOS v5, prefer source-first but fallback-safe behaviour:

1. Update or install the corrected play library before building Personas.
2. Point OwnerOS at the installed skill file only if it parses and validates.
3. Parse both `# Chain plays` and `## Chain plays` heading forms.
4. Handle steps with and without the `crew-` prefix.
5. Fall back to the app copy if the installed file is missing or invalid.
6. Show a visible `Play library fallback active` warning when fallback is used.
7. Personas must not generate from unresolved or invalid chains.

## Legacy handoff records

Legacy pack folders under `~/.claude/crew-state/` may contain real handoff records from before the Projects model. Do not migrate them before the workshop.

Best display model:

- `project runs` from `projects/`
- `legacy records` from old pack folders
- never inflate current activity with legacy history
- never claim `never run` when legacy evidence exists

If legacy records are left invisible for time, remove every `never run` style claim. Use `No project runs recorded`, not `0 runs` or `never run`.

## Dangerous stale references

Older CREW-to-Hermes migration notes used commands like:

```bash
sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' .../SKILL.md
```

For OwnerOS v5, this is wrong. It breaks the one-brain design and can also mangle absolute paths because the pattern is unanchored. Any reference containing this pattern needs a loud OwnerOS v5 warning before an agent follows it.

## Visual direction for the workshop reference reel

When Jared asks for the "next level" reel look while keeping Apple polish, brief the builder as:

**Apple shell. Dark engine stage.**

Meaning:

- App chrome stays Apple: SF/system typography, clean nav, disciplined spacing, blue only for true primary action, no random colours, no clutter.
- Engine surfaces become cinematic: black and graphite canvas, faint blueprint grid, thin technical hairlines, luminous nodes, radial or tiered agent diagrams, inspector panels, small mono labels.
- Use cyan and soft green as live-system glow colours. Use magenta or ember only for risk, vacancy, or attention.
- Keep structure readable: tiering, ladders, grouped lists, and hierarchy beat hairballs.
- No force-directed physics, no random starfield, no gaming UI, no unreadable glow mess.
- Start with `/hermes` first. Do not reskin every room in one hit.

Use the reel as an energy reference, not a layout reference. The target sentence is: **Apple built a private AI command centre for a business owner.**

## Sessions and proof row

Once a Hermes CREW demo passes, OwnerOS should not leave the connection row hardcoded to false.

The proof row must be evidence-based, not time-based only:

- Find a CREW handoff under `~/.claude/crew-state/projects/**`.
- Correlate it with a Hermes root `state.db` session.
- The Hermes session must name the skill in its own recorded messages. Timing alone is not enough.
- Do not render message bodies, raw prompts, or assistant output in OwnerOS.
- Keep the demo evidence project, such as `hermes-handoff-demo`, unless Jared knowingly removes it. If removed, the row should honestly return to not proven.

For a Sessions room, keep it read-only metadata only: title, side, agent/profile, source, model, dates, tool count, upload/doc count, and safe folder labels. No transcript browser before the workshop. No full private paths in screen-share rows. Costs hidden by default.

## Workshop Display Mode

If Jared asks about “display”, “screen share”, or visual uplift before the workshop, prefer `?display=1` on key rooms over a new presentation deck.

Display Mode rules:

- It is a screen-share layer only. No new data, no logic changes, no cabinet writes.
- Hide nav clutter, full paths, costs, debug copy, and tiny internal footnotes.
- Enlarge headings, proof cards, status chips, diagrams, and primary numbers.
- Keep truth claims API-driven.
- Keep the privacy line: local, read-only, not uploaded.
- Use **Apple shell. Dark engine stage.** The normal app stays clean; cinematic treatment belongs on proof/diagram moments.
- Verify desktop screenshots at 1440 and 1920. This is projector polish, not mobile-first redesign.

## Acceptance gates

- `test ! -d ~/.hermes/crew-state` before install, after install, and after demo.
- `bash install.sh --doctor --target ~/.hermes/skills/crew` passes.
- `hermes skills list | grep crew-core-using-crew` finds the skill.
- `/api/role` returns SOP steps without Final Step boilerplate.
- `/api/skill-file` blocks traversal and only accepts `format=md|zip`.
- `/api/personas` validates every chain step against real skills.
- `/api/hermes` is honest: default Hermes may have CREW installed, named profiles are not wired unless their profile skills actually contain CREW.
- `/api/connections` says the Hermes proof is true only when evidence exists in both the cabinet and Hermes session store.
- `/api/sessions` is metadata-only and screen-share safe.
