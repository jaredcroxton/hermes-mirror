# Supabase Region Migration Reference

## Available AWS Regions

| Region | AWS Code | Supabase Label |
|---|---|---|
| East US (North Virginia) | `us-east-1` | Americas (general) |
| East US (Ohio) | `us-east-2` | — |
| West US (North California) | `us-west-1` | — |
| West US (Oregon) | `us-west-2` | — |
| Canada (Central) | `ca-central-1` | — |
| West EU (Ireland) | `eu-west-1` | — |
| West Europe (London) | `eu-west-2` | — |
| West EU (Paris) | `eu-west-3` | — |
| Central EU (Frankfurt) | `eu-central-1` | Europe (general) |
| Central Europe (Zurich) | `eu-central-2` | — |
| North EU (Stockholm) | `eu-north-1` | — |
| South Asia (Mumbai) | `ap-south-1` | — |
| Southeast Asia (Singapore) | `ap-southeast-1` | APAC (general) |
| Northeast Asia (Tokyo) | `ap-northeast-1` | — |
| Northeast Asia (Seoul) | `ap-northeast-2` | — |
| **Oceania (Sydney)** | **`ap-southeast-2`** | **—** |
| South America (São Paulo) | `sa-east-1` | — |

## Pooler Hostname Format

```
aws-0-<region>.pooler.supabase.com
```

Examples:
- Tokyo: `aws-0-ap-northeast-1.pooler.supabase.com`
- Sydney: `aws-0-ap-southeast-2.pooler.supabase.com`
- Singapore: `aws-0-ap-southeast-1.pooler.supabase.com`

**Pooler hosts are for app runtime connections only. They do NOT support pg_dump/supabase db dump.**

## Migration Checklist (End-to-End)

1. Create new project in target region
2. Get direct DB host from Settings → Database for BOTH projects
3. Dump roles, schema, data from source
4. Restore into target
5. (Optional) Migrate `supabase_migrations` schema history
6. Redeploy Edge Functions
7. Migrate Storage objects (official Node script)
8. Reconfigure Auth providers, secrets, webhooks, custom domains
9. Update app env vars (URL, anon key, service key)
10. Smoke test: login, read/write, storage, functions
11. Keep source project as fallback for observation period
12. Decommission source after confidence period

## Real-World Example: Tokyo → Sydney (June 2026)

- Source: `jaredcroxton's Project` in `ap-northeast-1` (Tokyo), ref: `hbdjicqmcqgfyckgkbzoyu`
- Destination: `LearnOS SYD` in `ap-southeast-2` (Sydney), ref: `blkqkmyojgoiskfmhzrx`
- Plan: Pro (micro compute on both)
- Method: `supabase db dump` + `psql` restore (not "Restore to new project" — that feature cannot change regions)
- Status: Migration in progress — psql installed, awaiting DB host from dashboard to execute
- Gotchas encountered:
  - `db.<ref>.supabase.com` does NOT resolve — must get actual host from Settings → Database
  - Pooler host `aws-0-ap-northeast-1.pooler.supabase.com` resolves but rejects `pg_dump` connections
  - Supabase dashboard requires login — cannot be scraped by agent
  - AI-generated runbooks may contain wrong host formats — always verify against dashboard

## Official Docs

- Regions: https://supabase.com/docs/guides/platform/regions
- Migrating within Supabase: https://supabase.com/docs/guides/platform/migrating-within-supabase
- Backup/Restore CLI: https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore
- Clone project (same region only): https://supabase.com/docs/guides/platform/clone-project
- Change region (troubleshooting): https://supabase.com/docs/guides/troubleshooting/change-project-region-eWJo5Z
