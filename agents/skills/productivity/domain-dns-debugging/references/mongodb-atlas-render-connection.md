# MongoDB Atlas → Render Connection

## Connection string construction

Get the template from **MongoDB Atlas → Database → Connect → Drivers**.

Template:
```
mongodb+srv://<user>:<password>@<cluster>.<id>.mongodb.net/?retryWrites=true&w=majority&appName=<app>
```

Replace placeholders:
- `<user>` → database username
- `<password>` → real password (no angle brackets, no special chars if possible)
- `<cluster>` → cluster name (e.g. `cluster0`)
- `<id>` → cluster ID from Atlas (e.g. `abcde`)

Add database name after `.net/`:
```
mongodb+srv://jared:REDACTED_EMAIL/trainrtech?retryWrites=true&w=majority&appName=Cluster0
```

## Network access (most common failure)

**MongoDB Atlas → Network Access → Add IP Address**

For test/dev: add `0.0.0.0/0` (Allow Access From Anywhere).

For production: add Render's outbound IPs from https://render.com/docs/outbound-ip-addresses.

Without this, Render cannot reach the database.

## Render environment variable

**Render Dashboard → Service → Environment → Add Environment Variable**

- Key: `MONGODB_URI`
- Value: the full connection string with real password

Then: **Manual Deploy → Deploy latest commit**.

## Code pattern

Server must use the environment variable, not localhost:

```js
// CORRECT
mongoose.connect(process.env.MONGODB_URI)

// WRONG — will fail on Render
mongoose.connect("mongodb://localhost:27017/mydb")
```

## Password hygiene

If password contains special characters (`@`, `#`, `/`, `%`), either:
- URL-encode them in the connection string, or
- Change the database password to alphanumeric only for dev/test

Example clean password: `TrainrTech2026` (no symbols, no encoding needed).

## No-cost Render setup

Render Hobby tier is free forever. Pro Trial is 14 days free then paid. For test projects, stay on Hobby or downgrade before trial ends.
