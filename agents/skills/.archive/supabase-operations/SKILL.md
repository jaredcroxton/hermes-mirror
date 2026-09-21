---
name: supabase-operations
description: Use when working with Supabase projects — migrations between regions, backups, restores, Edge Functions deployment, Storage migration, Auth configuration, or any Supabase platform operation. Covers CLI usage, connection strings, dump/restore, and common pitfalls.
---

# Supabase Operations

## Connection Strings

Supabase provides multiple connection options. Use the right one for the job:

| Use case | Connection type | Port | Notes |
|---|---|---|---|
| `supabase db dump` / `pg_dump` | Direct DB host | 5432 | From Settings → Database → Database host |
| App runtime (server) | Session pooler | 5432 | `aws-0-<region>.pooler.supabase.com` |
| App runtime (client) | Transaction pooler | 6543 | For serverless/edge functions |
| Supabase CLI linked projects | `supabase link` | — | Uses project ref, not raw URL |

**CRITICAL: The pooler hostnames do NOT support `pg_dump` or `supabase db dump`.** You must use the direct database host from the dashboard for any dump/restore operation.

## Region Migration (Changing AWS Regions)

Supabase does NOT support in-place region migration. The "Restore to new project" beta feature **always keeps the same region as the source project**. There is no region selector.

**The only way to move to a different region is:**

1. Create a new project in the target region
2. Dump from source project
3. Restore into target project
4. Migrate non-database assets manually

### Dump and Restore

```bash
# Set variables
export OLD_DB_URL="postgresql://postgres:<OLD_PASSWORD>@<OLD_DIRECT_HOST>:5432/postgres"
export NEW_DB_URL="postgresql://postgres:<NEW_PASSWORD>@<NEW_DIRECT_HOST>:5432/postgres"

# Dump
mkdir -p supabase-migration && cd supabase-migration
supabase db dump --db-url "$OLD_DB_URL" -f roles.sql --role-only
supabase db dump --db-url "$OLD_DB_URL" -f schema.sql
supabase db dump --db-url "$OLD_DB_URL" -f data.sql --use-copy --data-only

# Restore
psql \
  --single-transaction \
  --variable ON_ERROR_STOP=1 \
  --file roles.sql \
  --file schema.sql \
  --command 'SET session_replication_role = replica' \
  --file data.sql \
  --dbname "$NEW_DB_URL"
```

### What Migrates Automatically

- Database schema (tables, views, procedures)
- All data and indexes
- Database roles, permissions, and users
- Auth user accounts (hashed passwords, auth records)
- Extensions (copied with schema)

### What Needs Manual Reconfiguration

- Storage objects and buckets (S3 files are NOT copied)
- Edge Functions (must redeploy)
- Auth settings and API keys
- Realtime settings and publications
- Database extensions settings (especially pg_net, pg_cron, wrappers — disable after clone to avoid duplicate external calls)
- Custom domains and redirects
- Secrets and environment variables
- Webhooks
- SMTP/email templates

## Edge Functions Migration

```bash
supabase login
supabase functions list --project-ref <OLD_REF>
supabase functions download <function_name> --project-ref <OLD_REF>
supabase functions deploy --project-ref <NEW_REF>
```

## Storage Migration

Use the official Supabase storage migration script. See the "Migrating storage objects" section in the backup/restore docs. This is a Node.js script that copies all buckets and files project-to-project.

## Auth Token Behavior After Migration

If you want existing sessions/tokens to remain valid after cutover, set the same JWT secret in the new project. Otherwise, all users will need to log in again.

## Common Pitfalls

1. **Pooler vs direct host for dumps.** The session/transaction pooler URLs will fail with `pg_dump`. Always use the direct DB host from Settings → Database.
2. **"Restore to new project" does not change region.** It explicitly states "Project region will stay the same." Do not use it for region migration.
3. **Extensions with external side effects.** After restore, disable pg_net, pg_cron, wrappers in the new project until you confirm they should be re-enabled, to avoid duplicate external operations.
4. **AI-generated runbooks may contain errors.** Verify pooler URLs, exclusion flags, and command flags against official Supabase docs before running.

## References

- `references/region-migration.md` — Detailed region migration notes and AWS region codes
