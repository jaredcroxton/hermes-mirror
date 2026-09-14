# Vercel Project Transfer Options

## The problem
Moving a Vercel project from one account to another without paying for a Team plan.

## Option A: Add collaborator (fastest, free)

1. In your Vercel project → Settings → General → Manage Collaborators
2. Add their email
3. They accept the invite

Result: they see the project, domains, and deployments. No teams, no paid plans, no transfer. Domain stays in your account but they have full access.

Works when: both parties just need access to the same project.

## Option B: Delete and redeploy (cleanest, free)

**You:**
1. Delete the project from your Vercel account

**They:**
1. Log into their Vercel account
2. New Project → Import Git Repository
3. Connect the same GitHub repo
4. Set environment variables
5. Add the domain
6. Deploy

Result: project fully in their account. GitHub repo untouched. DNS unchanged. Zero cost.

Works when: the recipient should own the project fully.

## Option C: Vercel Team transfer (paid)

Settings → General → Transfer Project → choose target team.

Requires: Owner on source, Member on target. Target team needs valid payment method. Pro Trial works for 14 days, then paid.

Avoid for test/personal projects unless client is paying.

## Pitfalls

- **Pro Trial trap:** Vercel pushes Pro Trial when creating a team. It's free for 14 days then auto-converts to paid. For test projects, prefer Options A or B.
- **Domain release:** When you delete a project, the domain is released. The recipient must add it fresh in their account. DNS records at the registrar (Squarespace, etc.) are unaffected.
