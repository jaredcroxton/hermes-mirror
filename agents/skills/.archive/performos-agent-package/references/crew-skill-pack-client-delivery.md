# Crew Skill Pack — Client Email Delivery Pattern

Use this when sending Crew skill packs to a client who needs to install them into Claude Code. Captured 17 June 2026 from the Taron delivery.

## The dead-simple install flow

The client never touches terminal. The client never hunts for hidden folders. The client never drags and drops in Finder.

1. Client downloads the zip from email.
2. Client moves zip from Downloads to Desktop.
3. Client double-clicks zip to unzip.
4. Client opens Claude Code in their project.
5. Client pastes two commands into Claude Code:

```
Copy every folder from ~/Desktop/FolderName/01-core/ into .claude/skills/
Copy every folder from ~/Desktop/FolderName/02-sales/ into .claude/skills/
```

6. Client restarts Claude Code. Skills are discovered automatically.

Claude Code has file system access. It creates `.claude/skills/` if needed and copies the folders. No terminal. No Finder. No drag and drop.

## Zip preparation

Before attaching to email:

```bash
cd "/path/to/parent/folder"
zip -r "Crew-Skills-Core-and-Sales.zip" "Taron Crew Skills/" -x "*.fixture.md"
```

Exclude test fixtures to keep the zip light. Include `crew-method.md` and `CREDITS.md` so the client can read the methodology if they choose, but they never need to.

## Email structure

The email must include:

1. **Subject line:** "Crew skills for Claude Code — ready to install"
2. **Attachment:** the zip file
3. **Install steps:** the 6-step flow above (download, move to Desktop, unzip, open Claude Code, paste two commands, restart)
4. **Full slash-command list:** every skill with its slash command and a one-line description
5. **Chain explanation:** how the skills connect (lead research → prospect brief → outreach → follow-up → proposal → pipeline review → CRM cleanup)
6. **Methodology note:** brief line that the 8 standards + 5 loops run invisibly inside every skill; `crew-method.md` documents everything if they want to read it
7. **One test:** a specific slash command and input they can paste to confirm the install works

## Slash-command reference format

For each skill:

```
/crew-sales-lead-research — Researches a target company before a first call. Returns a structured brief with company summary, likely pain points, and decision-maker notes.
```

Group by pack (Core first, then Sales). Keep each description to one sentence. The client scans the list and knows what they can invoke.

## What not to include

- No internal agent names (Brock, Bob, Lara, etc.)
- No runtime names (Hermes, NemoClaw, Claude Code internals)
- No Superpowers or G-Stack links
- No terminal commands
- No Finder hidden-folder instructions
- No methodology deep-dive unless the client asks

The client's experience is: unzip, paste two commands into Claude Code, restart, type a slash command. Everything else is invisible.

## Concrete email template (Taron, 17 June 2026)

Below is the exact email sent to Taron with Core + Sales packs. Replace the folder name and pack list for other clients.

---

Subject: Crew skills for Claude Code — ready to install

---

[Name],

Attached: [FolderName].zip

14 skills. Core (7) plus Sales (7). Built for Claude Code.

---

How to install (8 steps, about 2 minutes)

1. Open this email.

2. Download the attached zip file to your Downloads folder.

3. Move the zip from Downloads to your Desktop.

4. Double-click the zip on your Desktop. It unzips into a folder called "[FolderName]".

5. Open Claude Code in your project.

6. Paste this first command:

Copy every folder from ~/Desktop/[FolderName]/01-core/ into .claude/skills/

7. Paste this second command:

Copy every folder from ~/Desktop/[FolderName]/02-sales/ into .claude/skills/

8. Restart Claude Code. Done.

---

[Full slash-command list per pack — one line per skill with description]

---

How the [Pack] skills chain together

[chain diagram]

Each skill saves a handoff file so the next one knows what happened. When you chain them, the context carries forward automatically.

---

Quick test to confirm it works

Open Claude Code. Paste:

/slash-command

[specific test input]

If it returns [expected output shape], everything is installed correctly.

---

Any questions, just text me.

Jared

---

## Anti-pattern: do not overcomplicate install

When the user pushes back on complicated install instructions (Finder, hidden folders, terminal), the correct response is: "You are right. Here is the simpler way." Then give the two Claude Code copy commands. Do not defend the complicated version. Do not offer multiple options. The dead-simple path is the only path for client delivery.

Captured 17 June 2026 when Jared said: "Can't I just go to Claude code, open a file, and say, Import these skills, learn them, and save them as your skill files? You're making that very difficult."
