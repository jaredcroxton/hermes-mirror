# SOUL file audit checklist

Four-point review for any agent SOUL file before deployment or after a significant update. Run this against every new or revised SOUL.

## 1. Consultation pattern realism

Does the SOUL describe how consultations with other agents actually work in the ecosystem?

- If the SOUL says "Serge routes to Polly for brand review" but the workflow requires Jared to manually copy-paste prompts between Telegram bots, the consultation pattern is aspirational, not real.
- Fix: describe the actual agent-to-agent path, including where Jared is the courier. Example: "Serge → Jared → Polly → Jared → Serge" is honest. "Serge spawns Polly via delegate_task" is wrong if Polly is a separate profile.
- Check every "consults" and "routes to" entry against the actual integration mechanism (Telegram bot, delegate_task, handoff prompt, Jared as middleman).

## 2. Internal contradictions

Read every section that describes operating rhythm or cadence.

- Does one section say "on spawn only, no proactive cadence" and another list monthly scheduled tasks? That is a contradiction.
- Does the trigger discipline list keywords that overlap with another agent's lane?
- Does the "never allow" list contradict a job specification? Example: "never publish" but a job says "post the draft to the blog."

Fix: pick one truth and remove the contradictory line. Ambiguity in a SOUL is worse than being wrong.

## 3. Stale file paths

Every file path in the SOUL must resolve to a real file at the time of audit.

- Check every `/Users/jc/Desktop/Obsidian/...` path
- Check every template reference
- Check every vault path under "Files Serge should know" or equivalent
- If files were moved during cleanup (e.g. templates from Agents/ to SEO/templates/), update all references

Pitfall: Claude and other JIT agents often create SOUL files with paths that were correct at creation time but become stale after folder reorganisation. Always re-verify paths before deployment.

## 4. Redundancy

Does the same rule appear in two different sections?

- "Hard lines" + "What X should never do" are the most common duplicate pair
- "Output contract" + "How X reports back" often overlap
- "Trigger discipline: when I should refuse" + "Out of scope" in the charter often repeat

Fix: keep the stronger version. Delete the weaker one. A shorter SOUL with no duplicates is more likely to be followed than a long one where the same rule appears twice with slightly different wording.

## Bonus: Brock escalation realism

If the SOUL has a "when to escalate to Brock" section, check:

- Are the thresholds concrete or vague? "When something feels strategically significant" is weak. "When a keyword priority decision shifts which audience PerformOS targets" is strong.
- Are there too many escalation triggers? If everything escalates, nothing does. Aim for three to five specific thresholds.
- Does the escalation format (flag note) match the ecosystem standard?

## Quick pass/fail

A SOUL passes audit when:
- Every consultation path describes a real integration mechanism
- No two sections contradict each other
- Every file path resolves
- No rule appears twice

If any of the four fail, fix before deployment.
