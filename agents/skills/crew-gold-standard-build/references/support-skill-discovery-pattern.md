# Support Skill Discovery Pattern

Every support skill must ask discovery questions before executing. The user's explicit feedback (25 June 2026): "you would think that all of our skills have a discovery section. All the skills that I had in Claude before that, that were migrating into this pack, had a discovery question, because how do you build the skill without discovery?"

## The 5-question discovery template

1. **What's the product or service?** The thing customers are asking about or having issues with.

2. **Who asks the questions?** New customers, paying customers, prospects, internal team?

3. **Where do the questions live?** Support tickets, app store reviews, Reddit, Instagram comments, search queries, chat transcripts, email threads?

4. **What answers do you already have?** Docs, policies, pricing, known fixes? Any existing knowledge base?

5. **What's the one question you're sick of answering?** This goes to the top of the output.

## Per-skill adaptations

**FAQ Builder:** Questions 1-5 as-is. The skill sources real questions from the material provided in Q3. Never give the FAQ Builder pre-written questions — that skips its core workflow. Give it raw source material (ticket dumps, chat transcripts) and let it extract, group, and answer. Jared corrected this directly: "why are you giving the 5 questions?"

**Ticket Triage:** Q1 becomes "What channel did these tickets come from?" Q4 becomes "What SLAs are in place?" Q5 becomes "What's the most common ticket type?"

**Support Reply Builder:** Q1-2 as-is. Q3 becomes "What's the customer's situation? Show me their email or describe the issue." Q4 becomes "What's the resolution? What can we actually do for them?" Q5 removed.

**Help Document Generator:** Q1-3 as-is. Q4 becomes "What's the reader's technical level? Never used this before, or power user?" Q5 removed.

**Escalation Review:** Q1-2 as-is. Q3 becomes "What's happened so far? Show me the ticket trail." Q4 becomes "What's our escalation policy?" Q5 becomes "What's the deadline or SLA pressure?"

**Feedback Summary:** Q1-2 as-is. Q3 becomes "How much raw feedback do we have? How many responses?" Q4 becomes "What are we trying to learn from this?" Q5 removed.
