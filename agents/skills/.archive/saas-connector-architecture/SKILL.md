---
name: saas-connector-architecture
description: Use when Jared needs CEO-level or product-architecture guidance for SaaS integrations, OAuth connectors, multi-account dashboards, source-of-truth design, provider sync models, token storage, or app-versus-provider authentication. Especially useful for Supabase-backed dashboards that connect to Microsoft 365, Xero, Google, Stripe, or similar external systems.
version: 1.0.0
author: PerformOS / Jared Croxton
license: MIT
metadata:
  hermes:
    tags: [saas, oauth, architecture, connectors, supabase, microsoft-graph, dashboards, integrations]
    related_skills: [claude-code-builder, local-dashboard-access, n8n-local-operations]
---

# SaaS Connector Architecture

## Trigger

Use this skill when Jared asks how to connect external business systems into a dashboard, CRM, agent workspace, or PerformOS-style product.

Typical prompts:
- "How do we connect multiple Office 365 accounts?"
- "Can Supabase authenticate them and get their emails?"
- "How should Xero/Microsoft/Google connect into one dashboard?"
- "What is the architecture for multi-client integrations?"
- "How do we store tokens, sync data, and show it safely?"

## Brock's role

Brock should stay at the architecture and commercial-risk level.

Do:
- explain the system clearly
- separate app login from provider connection
- define the source of truth
- name permission, consent, and trust risks
- give a build sequence Bob can execute
- pressure-test MVP versus enterprise architecture

Do not:
- write production code
- collapse into Bob's build lane
- over-spec enterprise admin flows before proving the MVP
- imply PerformOS products are deployed or approved anywhere

## Core principle

Most integration dashboards have two different auth layers:

1. **App identity**
   - Who is logged into the product?
   - Which organisation/team/business can they access?
   - What role do they have?
   - Usually Supabase Auth or similar.

2. **Provider connection**
   - Which external account has authorised data access?
   - Which business does that connection belong to?
   - What scopes were granted?
   - Usually OAuth to Microsoft, Xero, Google, Stripe, etc.

Never blur these into one vague "login" flow.

## Recommended answer shape

Use this structure:

1. **Plain-English answer first**
   - "Supabase logs people into your dashboard. Microsoft logs the dashboard into each Office account."

2. **Architecture diagram**
   - Short text diagram showing user → Supabase → backend → provider OAuth → token vault → sync worker → dashboard data.

3. **Source of truth**
   - Tables/entities: organisations, businesses, memberships, connections, sync jobs, audit logs.

4. **Connection flow**
   - User clicks Connect
   - backend creates OAuth URL
   - provider redirects back with code
   - backend exchanges code for tokens
   - token stored server-side only
   - worker syncs data

5. **MVP decision**
   - Prefer delegated user-connected accounts first.
   - Avoid tenant-wide admin consent until enterprise need is proven.

6. **Security posture**
   - No passwords stored
   - no tokens in browser storage
   - refresh tokens encrypted
   - read-only scopes first
   - disconnect and audit flows

7. **Build sequence**
   - prove one provider across two businesses before adding workflows, AI, or multi-provider complexity.

## Product modelling pattern

Use a generic `connections` model instead of provider-specific tables as the main source of truth.

Minimum fields:

```text
connections
- id
- organization_id
- business_id
- provider
- provider_account_name
- provider_account_email
- provider_tenant_id
- provider_user_id
- status
- scopes
- encrypted_refresh_token
- access_token_expires_at
- last_sync_at
- sync_cursor
- created_by
- created_at
- updated_at
```

Provider-specific data can live in secondary tables, but the dashboard should reason from the generic connection registry.

## Sync pattern

Do not make the dashboard fetch live provider data on every page load.

Preferred pattern:

```text
Provider API
  → backend connector
  → sync worker
  → normalised database
  → dashboard reads prepared data
```

This is faster, safer, easier to audit, and easier to route through local/cloud AI policies.

## MVP rule

The first proof should be small and testable:

> One app user connects two different provider accounts to two different businesses, and the dashboard shows separated data for each business.

For Microsoft 365, the proof is:

> One PerformOS user connects two Microsoft 365 accounts to two different businesses, and the dashboard shows separated inbox summaries from both.

If that fails, nothing bigger matters.

## Common pitfalls

### Pitfall: treating Supabase OAuth as the whole connector

Supabase social login can authenticate a user, but that does not automatically solve multi-account provider data access for a dashboard.

Use Supabase for app identity. Use provider OAuth for data connections.

### Pitfall: connecting from the browser

Do not call Microsoft Graph, Xero, Google, or Stripe directly from browser JavaScript for server-side products.

The browser calls your backend. The backend owns token exchange, token refresh, sync, audit, and provider error handling.

### Pitfall: asking for broad permissions too early

Start read-only. Add write/send/admin scopes only when the use case demands it.

### Pitfall: tenant-wide admin consent too early

Tenant-wide app permissions can create a major trust and compliance problem. For MVP, prefer user-delegated connections. Add admin consent only for larger clients that need shared or tenant-wide access.

## Handoff to Bob

When the architecture needs to become a build, hand off to Bob with:
- provider to connect
- MVP success test
- required entities/tables
- callback URLs
- scopes
- token storage rule
- sync rule
- dashboard UX state
- verification requirement

Use `claude-code-builder` for the actual build/deploy work.

## References

- `references/microsoft-365-supabase-dashboard-architecture.md` contains the Microsoft 365 + Supabase multi-account pattern captured from the 05 October 2026 Office 365 dashboard architecture session.
