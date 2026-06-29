# Port Verification Pattern

When a battle-tested protocol is ported into CREW (like Express → app-builder), verification runs in two layers, not one. The standard Brock review covers CREW compliance. A second layer confirms the protocol's DNA survived.

## Layer 1: Standard CREW gold checks

From the Brock review checklist:

| Check | Command |
|---|---|
| Size | `wc -c SKILL.md` |
| Sections (15 min) | `grep -c '^## ' SKILL.md` |
| Banned terms | `grep -cin 'Accor\|Sarah\|PerformOS\|Brock\|Bob\|Lara\|Hermes[^s]' SKILL.md` |
| Residual old branding | `grep -cin '<old-name>\|<old-term>\|<old-path>' SKILL.md` |
| Em dashes | `grep -c '—' SKILL.md` (must be 0) |
| Harness | Step 0, Final Step, handoff path, output header, Guardrails contains "em dash", frontmatter exactly two keys |
| Fixture | Cases A, B, C all present |
| Off-ramps | Register skills have "when this is the WRONG lens" guard |

## Layer 2: Protocol preservation checks

Identify the protocol's signature elements BEFORE verification. For the Express → app-builder port, these were:

| Element | Check |
|---|---|
| Five phases | `grep -c 'Blueprint\|Link\|Architect\|Stylize\|Trigger' SKILL.md` |
| A.N.T. architecture | `grep -c 'A\.N\.T\.\|\bANT\b\|data-first\|schema before code' SKILL.md` |
| Self-annealing loop | `grep -c 'self-anneal' SKILL.md` |
| Five discovery questions | Read the Discovery section — confirm all five present, in order |
| Data-first rule | Confirm "schema before code" and the three schema questions present |
| File structure | Confirm renamed paths match (execution/ → tools/, CLAUDE.md → app-spec.md) |

**The rule:** before declaring a port done, list the protocol's signature moves, then grep for each one. A zero on any signature element means the protocol DNA was lost in the port and needs repair.
