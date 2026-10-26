# Profile agents with Obsidian-hosted SOUL files

Use this pattern when Jared defines a specialist Hermes agent in the Obsidian vault and wants the agent's persistent contract editable from Obsidian.

## Pattern

- Keep the canonical SOUL file in Obsidian, usually under:
  `/Users/jc/Desktop/Obsidian/Agents/<agent-name>-soul.md`
- Symlink the profile's `SOUL.md` to that canonical vault file:

```bash
profile=/Users/jc/.hermes/profiles/<profile>/SOUL.md
target=/Users/jc/Desktop/Obsidian/Agents/<agent-name>-soul.md

# Back up existing profile SOUL if it is a normal file.
[ -f "$profile" ] && [ ! -L "$profile" ] && cp "$profile" "$profile.bak-before-obsidian-soul"
rm -f "$profile"
ln -s "$target" "$profile"
```

- Restart the profile gateway after changing the SOUL symlink or major identity contract:

```bash
<agent_alias> gateway restart
<agent_alias> gateway status
```

- Verify with a one-shot identity prompt:

```bash
<agent_alias> chat -q 'Reply with only your name and scope.' -Q
```

## Updating the parent agent's ecosystem routing

When Jared adds a new specialist agent and asks another agent (for example Brock) to include it in their ecosystem:

1. Locate the parent agent's Obsidian SOUL file under `/Users/jc/Desktop/Obsidian/Agents/` rather than assuming the filename from the user's wording. Filenames may use display-case variants such as `Brock_CEO-Soul.md` or `Harry_Hr-Soul.md`.
2. Search for an existing section like `Agent ecosystem <agent> operates in`. If it is missing, add a concise section before the "What <agent> is not" or equivalent boundary.
3. Add the new specialist as a routing entry with: agent name, what they do, when to route to them, explicit non-goals, and the SOUL file path.
4. Preserve the parent agent's role boundary. For Brock, this means he stays CEO-level strategy and routes specialist execution or domain analysis to the correct agent.
5. If the user gives a canonical lowercase path but the live Obsidian note exists under different casing, create a symlink at the user's stated path pointing to the live file so future tools and notes can resolve either path.
6. Save a compact memory entry for durable ecosystem routing only if it will reduce future steering. If memory is full, replace/compress an existing agent-ecosystem entry rather than adding a new one.

## Multiple aliases

A profile can have more than one useful wrapper alias. For example, a legacy alias can remain while adding a more specific name:

```bash
hermes profile alias <profile> --name <new_alias>
```

This creates another wrapper script pointing at the same profile; it does not rename the profile.

## Pitfalls

- If the Obsidian SOUL path the user gives does not exist, create it with the full specialist contract before symlinking.
- When cloning from the default profile, inspect the new profile's config and `.env` for inherited gateway or Telegram settings before starting anything. Remove cloned Telegram bot tokens, allowed-user settings, or gateway service assumptions unless the user explicitly wants that specialist wired to its own bot. This prevents a new specialist from accidentally reusing Brock/default Telegram credentials.
- Do not store tokens or private credentials in the Obsidian SOUL file or any mirrored public spec.
- For profile-backed agents that must write Google Sheets/Drive files, authenticate Google Workspace under that profile's `HERMES_HOME`, not only the default Hermes home.
