# Support Pack Testing Protocol

Proven smoke tests for all 6 support skills. Each test is designed to trigger the skill's actual workflow — not bypass it.

**Test format:** Fresh chat. Paste once. The test gives the skill real source material and lets it execute its full workflow. Do NOT pre-process the input. Do NOT write the output for the skill. The test proves the skill works end-to-end.

## FAQ Builder (critical: use raw source material, not pre-written questions)

Jared corrected this on 24 June 2026. Giving the FAQ Builder pre-written questions skips its core workflow. The skill's `## Question sourcing` section extracts questions from raw material — tickets, chats, reviews. The tester's job is to provide raw material, not processed questions.

**Correct test:**

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-faq-builder/SKILL.md completely. Then build an FAQ for a meal delivery service called "Field." Source the questions from these support tickets:

"can i skip next week my family is away" — answered by support
"my delivery was missing two meals and the ice packs were warm" — resolved
"do you have vegetarian options for kids" — answered
"I want to cancel my subscription right now" — pending
"how do I change from 3 meals to 5 meals per week" — answered
"the app says my delivery is today but nothing arrived" — escalated
"can I pick what meals I get or is it random" — answered
"are the containers recyclable" — answered
"can I pause for a month or only skip one week at a time" — answered
"do you deliver to apartment buildings" — answered

Known policies: skip with 48 hours notice, change meal count in account settings, no long-term pause (week-by-week only), containers fully recyclable, apartments and houses both delivered, meals are customer-chosen from 12 weekly options."
```

**Why this works:** The skill gets raw tickets with varying statuses (answered, resolved, pending, escalated). It must extract questions, tally frequencies, group by intent, answer from known policies, and flag the escalated/unanswered ones as "Needs answer." This tests every step of the workflow.

**Wrong approach (do not use):**
- "Build an FAQ with these 5 questions: Can I skip a week?..." — bypasses question sourcing entirely
- "Turn these into an FAQ page..." — the skill's job is to extract the questions, not format pre-written ones

## Ticket Triage

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-ticket-triage/SKILL.md completely. Then sort these 8 tickets by urgency and assign owners:

Ticket 1: "I can't log in. Password reset isn't working. I've tried three times." — submitted 10 minutes ago
Ticket 2: "Where can I find my invoice for last month?" — submitted 2 hours ago
Ticket 3: "Your app crashed and I lost two hours of work. This is the third time this week." — submitted 15 minutes ago
Ticket 4: "Do you offer a student discount?" — submitted yesterday
Ticket 5: "I need to add a team member but the button is greyed out." — submitted 1 hour ago
Ticket 6: "My credit card was charged twice this month." — submitted 30 minutes ago
Ticket 7: "Just wanted to say your product changed my life. Thank you." — submitted 3 hours ago
Ticket 8: "GDPR data deletion request. Please confirm receipt." — submitted 1 hour ago

Team: Maria (billing/account), Dev (technical), Priya (complaints/legal), Leo (general)
```

## Reply Builder

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-reply-builder/SKILL.md completely. Then draft a reply to this customer:

"I've been a customer for three years and I'm honestly about to leave. My last four support tickets got canned responses that didn't solve the problem. Now my integration is broken again — the same thing that happened in March. I need someone to actually read this and tell me what's going on, not send me another link to the docs."

Customer: Jamie, on the Pro plan. The March issue was a webhook timeout (ticket #4427). Current issue: same symptoms. Tone: warm, competent, never defensive.
```

## Escalation Review

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-escalation-review/SKILL.md completely. Then review this for escalation:

Customer: Enterprise client (50+ seats, $2,500/month). Issue: SSO login has been broken for 4 hours. 47 users locked out. Support has replied twice with troubleshooting steps. Customer says they've followed all steps. Last message: "We have a board meeting in 2 hours. Our investors will be looking at the dashboard. This needs to be fixed NOW."

Grade severity. Who should own this. Response timeline.
```

## Help Document Generator

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-help-document-generator/SKILL.md completely. Then write a help article for a project management tool called "Base." Topic: How to set up your first project. User just signed up. Empty workspace. Steps: create project, add sections, invite team, set deadline. Reading level: never used PM software. Include screenshots where helpful. Numbered steps.
```

## Feedback Summary

```
Read /Users/jc/Desktop/cluade/crew-skill-packs/packs/07-support/crew-support-feedback-summary/SKILL.md completely. Then summarise this customer feedback:

30 customer interviews about invoicing feature. Key themes:
- PDF exports look unprofessional (16 mentions)
- Clients can't pay directly from invoice (22 mentions)
- Currency selector resets every time (11 mentions)
- People love recurring invoice automation (28 mentions)
- Two customers gave detailed redesign suggestions
- One customer requested cryptocurrency payments

What to fix first? What's working? What's an outlier?
```
