# CREW local-first privacy language

Use this reference when Jared asks how to explain CREW, Claude Code, local folders, customer spreadsheets, offshore disclosure, or privacy positioning in social posts, sales copy, or client conversations.

## Core distinction

Do not frame CREW as simply "Claude comes in, leaves, and forgets." That sounds intuitive but is not technically clean enough.

Use this distinction instead:

- **Cloud chatbot upload:** the user uploads customer spreadsheets or company documents into a cloud chatbot, project, or knowledge base as stored content.
- **CREW local-first workflow:** company files stay in approved local folders, and the agent is given controlled access to the information needed for the task.
- **Fully local inference:** if the model itself runs locally, the files stay local and the model call does not need to send customer data offshore for inference.

## Safe wording

Use:

> CREW uses a local-first file workflow. Your company files can stay in approved local folders, and the AI only works with the files it is given access to.

Use:

> That is different from dumping private customer spreadsheets into a cloud chatbot as attachments or project knowledge.

Use, only for a true local-model setup:

> In the fully local version, the files stay local, the model runs local, and customer data does not need to be sent overseas for inference.

## What not to say

Avoid:

> Nothing is sent overseas.

Unless the model, tools, telemetry, logs, integrations, and inference path are confirmed local or approved.

Avoid:

> Claude comes into an office view, leaves, and forgets.

Better:

> Local-first. Controlled access. No bulk upload.

## Claude Code nuance

If CREW is running through Claude Code with Anthropic's cloud model, do not claim there is no offshore processing. The better wording is:

> The files are locally staged and selectively processed, rather than bulk-uploaded into a cloud workspace.

When Claude needs to reason over a file, relevant content may still be sent to Anthropic's model for processing unless using a fully local model or an enterprise zero-retention setup.

## Video line

> There are two very different ways to use AI with company data. One is uploading spreadsheets, customer records, and internal documents straight into a cloud chatbot. The other is a local-first workflow, where your files stay in approved folders and the AI only works with the information it needs for the task. And if you run the model locally, that goes further again. The work can happen without sending the data offshore.

## Strategic framing

The message is control, not absolute compliance.

Use:

> CREW is designed to reduce uncontrolled data movement.

Do not use:

> CREW makes you compliant.

Use:

> The difference is control. Are you dumping data into a chatbot, or giving an agent controlled access to approved local files?
