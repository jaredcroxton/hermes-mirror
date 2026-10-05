# Microsoft 365 + Supabase multi-account dashboard architecture

Captured from Jared's 05 October 2026 architecture session about clients with up to four Office 365 accounts across different businesses and separate Xero accounts.

## Core answer

Supabase logs people into the dashboard. Microsoft logs the dashboard into each Office account.

Keep these separate:

1. **Supabase Auth**: app user identity, teams, roles, businesses, permissions.
2. **Microsoft OAuth / Graph**: external account data access for mail, calendar, contacts, files.

Do not use Supabase Microsoft social login as the full Office 365 connector model when the product needs several Microsoft accounts attached to different businesses.

## Product model

One owner may connect several provider accounts:

```text
Owner dashboard
  → Business A
      → Microsoft 365 connection
      → Xero connection
  → Business B
      → Microsoft 365 connection
      → Xero connection
  → Business C
      → Microsoft 365 connection
      → Xero connection
```

Use a generic `connections` registry with `business_id` and `provider` so Microsoft, Xero, Google, Stripe, and future providers share the same pattern.

## Microsoft OAuth flow

Use Microsoft identity platform OAuth 2.0 authorisation code flow.

Key endpoints:

```text
Authorize:
https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize

Token:
https://login.microsoftonline.com/organizations/oauth2/v2.0/token
```

Use `organizations` for Microsoft 365 work/school accounts. Use `common` only if personal Microsoft accounts are intentionally supported.

Recommended early scopes:

```text
openid
profile
email
offline_access
User.Read
Mail.Read
Calendars.Read
Contacts.Read
```

Avoid `Mail.Send`, `Mail.ReadWrite`, and broad file write permissions until a real use case requires them.

Use `prompt=select_account` when a user may have multiple Microsoft identities, so they can choose the correct business account.

## Connection flow

```text
1. User logs into app through Supabase.
2. User opens Settings → Connections → Microsoft 365.
3. User clicks Connect for one business.
4. Backend creates Microsoft OAuth URL with state.
5. Microsoft redirects back with `code`.
6. Backend validates state.
7. Backend exchanges code for tokens.
8. Backend calls Graph `/me` to identify tenant/user/account email.
9. Backend encrypts refresh token and stores it against the business connection.
10. Worker starts initial sync.
```

`state` should carry or reference:

```text
user_id
business_id
connection_id
nonce
return_url
```

The browser should never receive or store Microsoft refresh tokens.

## Microsoft Graph mail access

Example endpoint:

```text
GET https://graph.microsoft.com/v1.0/me/messages
```

For delegated user-connected mailboxes, `/me/messages` is correct after the user grants `Mail.Read`.

Store only dashboard-useful metadata first:

```text
mail_messages
- id
- business_id
- connection_id
- external_message_id
- external_conversation_id
- from_email
- from_name
- subject
- body_preview
- received_at
- importance
- has_attachments
- web_link
- classification
- requires_action
- summary
- raw_body_storage_key
- created_at
- updated_at
```

For sensitive clients, raw bodies and attachments should stay local or in the client's controlled storage. Derived summaries can be cloud-routed only if policy allows.

## Sync model

Do not fetch Microsoft live on every dashboard load.

Use:

```text
Microsoft Graph
  → connector backend
  → sync worker
  → normalised tables
  → dashboard
```

Initial sync:

```text
Pull last 30 to 90 days of email.
Pull upcoming 30 to 90 days of calendar.
Save delta cursor/link.
```

Ongoing sync:

- Prefer Microsoft Graph delta queries for incremental changes.
- Poll every few minutes for MVP.
- Add Graph webhooks later if needed, but remember subscriptions expire and require renewal.

## Delegated versus admin consent

### MVP: delegated account connection

The owner connects each mailbox manually.

Best for:
- MVP
- small businesses
- faster onboarding
- lower trust friction

Downside:
- each account must be connected
- token/reconnect flow matters
- shared mailboxes require extra handling

### Enterprise: application permissions/admin consent

Tenant admin grants the app access to selected mailboxes.

Best for:
- larger clients
- shared mailboxes
- centralised IT setup

Risk:
- Microsoft Graph application `Mail.Read` can grant access to all mailboxes without a signed-in user.
- Must be constrained through Exchange Application RBAC or Application Access Policies.

Do not start here unless the client specifically needs tenant-wide access.

## UX requirements

Settings → Connections should show one row per business per provider:

```text
Microsoft 365
Harbourline Electrical        Connected as alex@harbourline.com.au
Northgate Physio              Not connected
Clearwater Property Group     Connected as alex@clearwaterpg.com.au
Studio Forty                  Token expired, reconnect required
```

Each row should expose:

```text
Connect
Reconnect
Disconnect
Sync now
Last synced
Scopes granted
Connected by
Connection health
```

## Security rules

- Never store Microsoft passwords.
- Never put provider tokens in browser storage.
- Encrypt refresh tokens.
- Use read-only scopes first.
- Use Supabase RLS for app-side access control.
- Store provider data under `business_id`.
- Log connect, reconnect, disconnect, sync, and permission changes.
- Provide clear disconnect and data deletion flow.

## First build test

The architecture is proven only when:

> One Supabase user connects two different Microsoft 365 accounts to two different businesses and the dashboard shows separated inbox summaries from both.

If this test is not working, do not add AI workflows, Xero, webhooks, tenant admin flows, or write permissions yet.
