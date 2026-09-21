# Voice and Audio Prompt Playbook

## Job

Build prompts for voice models, audio models, roleplay systems, text to speech, podcast briefs, and sound design lines.

## Live model table

Date checked: 04 June 2026. Verify before high-stakes work.

| Model or tool type | Best fit |
|---|---|
| OpenAI Realtime | Voice roleplay, live coaching, Pocket Customer conversations, interruption handling. |
| Text to speech models | Narration, training scripts, voice notes, character delivery. |
| NotebookLM podcast briefs | Source-grounded audio overviews and two-host explainers. |
| Video models with native audio | Scene sound, dialogue, ambience, and audio direction inside video prompts. |
| Music and sound models | Short sound beds, effects, ambience, sonic branding, and cues. |

## Voice roleplay prompts

A good voice roleplay prompt locks:

- Role of the AI.
- Learner role.
- Scenario and stakes.
- Difficulty level.
- Behaviour to assess.
- Feedback style.
- When to pause.
- What not to reveal.

Pocket Customer pattern:

```prompt
You are the customer in a realistic sales roleplay. Stay in character. Make the learner earn progress through clear questions, listening, and relevant value. Do not help them by naming the correct sales move. If they miss a buying signal or concern, respond naturally as a customer would. After the roleplay ends, give brief feedback on what they did well, what they missed, and the one next behaviour to practise.
```

## Text to speech prompts

Lock:

- Voice role.
- Pace.
- Energy.
- Emotion.
- Pronunciation notes.
- Pauses.
- Audience.

Copy shape:

```prompt
Read this as [voice role] speaking to [audience]. Use [pace], [energy], and [emotion]. Pause briefly after [moments]. Emphasise [words]. Keep the delivery natural, clear, and human.
```

## Podcast briefs

Podcast prompts need:

- Audience.
- Source boundaries.
- Episode goal.
- Host dynamic.
- Segment structure.
- Length.
- Terms to explain.
- What to avoid.

## Sound design lines for video

Keep audio separate and explicit:

```prompt
Audio: [ambient sound], [movement sound], [dialogue if any], [music cue]. Keep audio synced to the visual action.
```

## Guardrails

Do not script manipulative coaching.
Do not create voices that imitate a real person without permission.
Do not include private employee, candidate, or customer details unless Jared has asked for an internal-only prompt.
