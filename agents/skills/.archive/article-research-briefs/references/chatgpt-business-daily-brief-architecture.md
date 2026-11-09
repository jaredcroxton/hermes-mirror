# ChatGPT business daily brief architecture research notes

Use when Jared asks for the best way to create a business daily brief inside ChatGPT using Projects, email, SharePoint, Microsoft 365, or connected apps.

## Core recommendation pattern

Do not treat ChatGPT Projects as the system of record. Use Projects as the shared working interface and instruction layer. Use Microsoft 365 as the source of truth.

Best architecture:
1. Microsoft 365 source layer: SharePoint project site, shared project mailbox, shared/project calendar, optional Microsoft List for decisions and risks.
2. Daily Brief engine: Microsoft Graph, Power Automate/Azure Logic Apps, or a custom MCP app reads approved sources and generates one canonical brief.
3. ChatGPT surface: shared Project or custom ChatGPT app lets staff ask for the latest brief, meeting prep, risks, decisions, and source-backed follow-ups.
4. Output store: save the generated daily brief back into SharePoint so the business has one version of truth.

## Key OpenAI documentation findings

### Projects
Source: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt

Relevant findings:
- Projects are smart workspaces for long-running efforts.
- Business, Enterprise, and Edu users can share projects with teammates.
- Shared projects use project-only memory.
- File limits vary by plan. Business and Enterprise support up to 40 files per project.
- Important limitation: if a scheduled task is created in a project, it cannot access uploaded files or files stored in that project.

Implication:
Projects are good for instructions, working context, prompts, and team discussion. They are not enough for a reliable business-wide daily brief engine.

### Scheduled Tasks
Source: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt

Relevant findings:
- Scheduled tasks can run one-time or recurring tasks and monitoring tasks.
- Paid plans can run recurring tasks up to once per hour.
- Active task limits apply by plan. Business and Edu: 10. Enterprise and Pro: 15.
- Event-triggered tasks currently support Gmail, Slack, and GitHub activity where eligible.
- Shared task links do not include creator name, chat history, previous task results, saved memories, custom instructions, attached files, connected app data, or connected app credentials. Recipients use their own account permissions and connected app access.
- Scheduled tasks can use supported apps including Gmail, Slack, and GitHub when available for account/workspace.

Implication:
Scheduled tasks are useful for lightweight or personal workflows, but they are weak as a canonical team daily brief where everyone needs the same answer.

### SharePoint
Source: https://help.openai.com/en/articles/12143177

Relevant findings:
- SharePoint app lets ChatGPT search and reference SharePoint and supported OneDrive for work or school content that the Microsoft account can already access.
- Personal OneDrive is not supported by the SharePoint app.
- Administrator-managed SharePoint sync is available only in eligible Enterprise and Edu workspaces and supported regions.
- Individual and personal accounts cannot configure SharePoint sync.
- Connecting a Microsoft account gives live access, but does not create a personal synced index.
- Administrator-managed sync indexes selected SharePoint content and respects existing Microsoft 365 permissions.
- Only one administrator-managed SharePoint sync connection is supported per workspace.
- Common supported file types include .txt, .pdf, .docx, .pptx, .xlsx, and .csv.
- Initial indexing can take hours or longer. Updates to files, group memberships, or permissions may take time to appear.
- Live SharePoint actions and administrator-managed sync can be enabled together, but they use different authorization paths and controls.

Implication:
For Enterprise/Edu, admin-managed SharePoint sync is the strongest native knowledge layer. For Business, use live SharePoint connections or a custom Microsoft Graph layer.

### Outlook Email and Calendar
Source: https://help.openai.com/en/articles/12512241-outlook-email-and-calendar-apps-in-chatgpt

Relevant findings:
- Outlook Email and Calendar apps connect ChatGPT to supported Microsoft account information.
- Available actions depend on account permissions, Microsoft Entra consent, workspace settings, and the selected app.
- For shared or delegated mailboxes/calendars, connect the Microsoft account that already has access. ChatGPT does not grant Microsoft sharing or delegation permissions.
- Outlook Email can search and retrieve messages from the signed-in user's mailbox, including subject, sender, recipients, timestamps, and plain-text body.
- It supports keyword and structured searches such as from:, subject:, and date filters.
- Broad searches may return incomplete results or errors. Split large requests into smaller date ranges.

Implication:
Do not aggregate private inboxes as the daily brief source. Use a shared project mailbox or delegated mailbox with approved access.

### Company Knowledge
Source: https://help.openai.com/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu

Relevant findings:
- Company Knowledge helps ChatGPT answer organisation-specific questions using supported knowledge sources available to the user.
- Available on ChatGPT Business, Enterprise, and Edu.
- Works with supported connected apps and custom apps built with MCP.
- Installing Company Knowledge does not connect app accounts or grant access to source data.
- App access and provider authorisation still apply.
- The plugin does not override workspace access controls or app permissions.

Implication:
Company Knowledge is useful as a querying layer, not the operating model by itself.

### Developer mode and MCP apps
Source: https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt

Relevant findings:
- Business, Enterprise, and Edu customers can build/test/deploy MCP-powered apps in ChatGPT web.
- Full MCP support with modify/write actions is rolling out in beta to Business, Enterprise, and Edu.
- Only admins/owners can publish apps.
- Enterprise/Edu can use RBAC for access controls.
- OpenAI-built apps are search-only today and do not support write actions. Use custom MCP apps for write/modify capabilities.
- Deep research can use custom apps for read/fetch actions only, not write actions.

Implication:
A custom read-only Daily Brief MCP app is the clean ChatGPT-native production path. Start read-only. Add write actions only after trust and governance are established.

### Deep Research
Source: https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt

Relevant findings:
- Deep research is for multi-step, multi-source questions with citations or source links.
- It respects workspace app enablement, role access, and connected-account permissions.
- Only apps that support deep research and are available to the account can be used as research sources.
- Use search for quick facts, deep research for depth and thoroughness.

Implication:
Deep Research can help investigate business issues, but it is not the daily operating cadence by itself.

## Daily brief output shape

Use the same structure each day:

- Date
- Audience
- Coverage window
- Executive summary
- What changed
- Email signals
- Today’s meetings
- Decisions needed
- Risks and blockers
- Actions
- Source links

Every important claim should link back to source email, file, meeting, or document.

## Recommendation language

Use this judgement:

"The best solution is a Microsoft 365-backed Daily Brief app inside ChatGPT, using SharePoint and Outlook as the source of truth, with a custom MCP app or Microsoft Graph automation producing one shared daily brief. Use ChatGPT Projects as the workspace, not the database."

## Research workaround used in this session

When Firecrawl search/extract is unavailable and browser hits Cloudflare on OpenAI Help Center, use Jina Reader with the known article URL:

`https://r.jina.ai/http://help.openai.com/en/articles/<article-id>`

The Help Center collection page can also be read with:

`https://r.jina.ai/http://help.openai.com/en/collections/<collection-id>`

This produced readable markdown for OpenAI Help Center pages while the browser showed a Cloudflare challenge.