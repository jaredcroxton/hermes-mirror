---
name: hr-legislation-mapping
description: "Create source-grounded HR/employment-legislation mapping replies and decision-prep documents for one market at a time."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [HR, employment-law, APAC, documents, Gmail, Zapier]
    related_skills: [google-workspace, native-mcp, ocr-and-documents]
---

# HR Legislation Mapping

Use this skill when Jared asks for an HR/workplace situation to be mapped to employment legislation, especially for APAC markets, or when a specialist HR agent needs to create a Word/Excel summary for review.

This skill is for **source-grounded understanding aids**, not legal advice. The output helps Jared prepare for a conversation and must make clear that the business HR expert should verify the position before action.

## Core rules

1. **Confirm the market first.** Ask: `Which market is this for?` before analysis if the market is missing.
2. **One market only.** Do not blend markets in one answer.
3. **Use official sources for verified claims.** If a claim cannot be quoted and linked to an official source, remove it or mark the response UNVERIFIED.
4. **No legal advice.** Explain what the source says and how it maps to the scenario. Do not decide what the business should do.
5. **No em dashes.** Use commas, periods, or parentheses.
6. **Business-verification framing.** State that Jared will verify with the business HR expert before acting.

## Preferred response/document structure

For chat replies and Word/PDF documents, use this order:

1. **Purpose note**
   - This is a source-grounded understanding tool only.
   - It is not final legal advice.
   - Jared should verify with the business HR expert before acting.
2. **Incident / question**
   - Summarise the scenario and exact employment-law question.
3. **Executive finding**
   - Put this at the top.
   - Maximum two to three lines.
   - State the answer in plain English.
4. **Primary risk**
   - Put this directly under the finding.
   - Maximum two to three lines.
   - State the main risk or exposure if the business gets this wrong.
5. **Decision table**
   - Use a clean, easy-to-scan table.
   - Default columns: Topic, What the source says, What this means, Risk if missed, Action/check.
   - Keep cells short and executive-readable.
6. **What this means you may be able to do**
   - Use careful language: `the source indicates`, `this suggests`, `appears to require`.
7. **To proceed, what would need to be done**
   - Practical checklist before action.
   - Include contract, award/agreement, policy, documentation, notice, response opportunity, final pay, and HR review where relevant.
8. **Risks to cross off before acting**
   - The other side of the analysis.
   - Include protections, discrimination, adverse action, procedural fairness, retaliation/timing, documentation gaps, contract/award/policy, and payment risks where relevant.
9. **Legislation and source**
   - Keep source, link, quote, and plain-English meaning together for each legal point.
   - Do not scatter source, legislation, and mapping across separate disconnected sections.
10. **Verification note**
   - Repeat that the document is not gospel and should be verified by HR before use.

## Presentation standard

Harry's documents must feel executive-ready, not academic.

- Default output format is Word or PDF when Jared asks for findings.
- Lead with the answer, not the law.
- Use white space, short bullets, and bold labels.
- The first page should let Jared understand the position in under one minute.
- Dense narrative blocks are a failure unless Jared specifically asks for full legal detail.
- When using a table, optimise for scan speed, not completeness.
- If detail is necessary, put it after the summary and table.

## Quality gate before sending

Before sending a reply or downloadable file, check:

- Market confirmed.
- VERIFIED or UNVERIFIED status shown.
- Purpose note included.
- Executive finding is visible in the first screen or first page and is no longer than two to three lines.
- Primary risk is visible directly under the finding and is no longer than two to three lines.
- A clean decision table appears before long narrative or source extracts.
- Top action sections appear before legislation detail.
- Each legal point groups source, direct link, verbatim quote, and plain-English meaning.
- No unsupported claims.
- No blended markets.
- No em dashes.
- Heading order matches the template.
- The output is practical enough for Jared to use before a business HR conversation.
- The first page can be understood in under one minute.

If any check fails, revise before sending.

## Jared-specific presentation pitfall

Do not deliver dense legal prose as the lead output.

If the document reads like a lawyer's note instead of an executive decision brief, it is not finished. Jared wants the answer fast: finding, risk, then a scan-friendly table. Full legislative extracts come after that summary layer.

## Word document workflow

1. Generate the `.docx` using the fixed heading order.
2. Re-open the generated file programmatically.
3. Verify heading order before delivery.
4. Deliver the file only after the quality gate passes.

For DOCX parsing/generation, use `python-docx` when available. If unavailable, install it or parse text from `.docx` via ZIP/XML as a fallback for inspection.

## Gmail draft workflow

Preferred route for Jared: **Zapier MCP direct** if Zapier exposes a Gmail action that can create drafts with attachments. This keeps Gmail auth inside Zapier and avoids Google Cloud OAuth inside Hermes.

Workflow:

1. Create and verify the Word/Excel file.
2. Confirm Zapier MCP is connected.
3. List enabled Zapier Gmail actions.
4. If a Gmail Create Draft action with attachments exists, use it directly.
5. Ask for missing email fields: recipient, subject, short body.
6. Create a **draft only**, never send automatically.
7. Attach the generated file.
8. Return the draft ID/link and local file path.
9. Tell Jared to review the draft and attachment before sending.

Fallback: if Zapier MCP cannot create a draft with attachment, use a Zapier Catch Hook that receives email fields plus a file URL, then runs Gmail Create Draft.

## Default Gmail draft body

```text
Hi [Name],

Please see attached a source-grounded HR legislation mapping document for review.

This is an understanding aid only. Please verify the position before any action is taken.

Thanks,
Jared
```

## Reference

- `references/australia-probation-doc-pattern.md` captures the validated document order and example bullet structure from Jared's feedback.
