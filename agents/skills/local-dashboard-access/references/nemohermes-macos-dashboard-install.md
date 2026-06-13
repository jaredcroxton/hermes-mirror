# NemoHermes macOS dashboard and install notes

Use this reference when installing or operating NemoClaw's Hermes variant on a MacBook or when trying to open the NemoHermes dashboard/API.

## What NemoHermes creates

NemoHermes is the Hermes-specific alias for NemoClaw. It creates an OpenShell sandbox that runs Hermes.

Expected local ports after successful onboarding:

- Hermes dashboard: `http://127.0.0.1:18789/`
- OpenAI-compatible API base: `http://127.0.0.1:8642/v1`
- API health check: `curl -sf http://127.0.0.1:8642/health`

Useful commands:

```bash
nemohermes list
nemohermes <sandbox-name> status
nemohermes <sandbox-name> dashboard-url --quiet
nemohermes <sandbox-name> logs --follow
nemohermes <sandbox-name> connect
nemohermes <sandbox-name> destroy
```

## MacBook install reality

macOS is supported, but Docker must be running first.

Minimum requirements from the docs are modest, but Docker Desktop resource allocation matters. If Docker is allocated only around 8GB memory, onboarding can work but image builds/pulls may be slow or appear stalled.

Recommended for a smoother MacBook test:

- Docker Desktop running.
- Docker memory at least 8GB, preferably 10GB to 12GB on a 24GB Mac.
- Enough disk for container images and local models.
- Expect the first Hermes sandbox base image pull/build to take time.

## Provider choices for a quick laptop proof

For a low-risk local proof, local Ollama can be used with a small model such as `qwen2.5:7b`. This is a smoke-test path, not the final AgentOS model strategy.

If Hermes Provider OAuth fails during onboarding with a message like session key minting retired, do not treat NemoClaw itself as broken. Use another provider path for the test, such as local Ollama, NVIDIA Endpoints, OpenAI-compatible endpoint, or update/sign in through the current Hermes path before retrying.

## Resource profile prompt pitfall

During onboarding, the resource profile screen can show:

```text
6) No profile (OpenShell defaults)
Choose [6]:
```

In one run, pressing Enter at this prompt was rejected as an invalid selection. To avoid this, either type `6` explicitly or set:

```bash
export NEMOCLAW_RESOURCE_PROFILE=default
```

For under-provisioned Docker warning loops during a deliberate laptop proof, this can also be set:

```bash
export NEMOCLAW_IGNORE_RUNTIME_RESOURCES=1
```

Use that as a test convenience, not as proof that production resources are adequate.

## Dashboard access rule

`localhost` means the machine where NemoHermes is running.

- If NemoHermes runs on the MacBook, open `http://127.0.0.1:18789/` on the MacBook.
- If NemoHermes runs on a remote NVIDIA/Brev/DGX host, use SSH port forwarding, Tailscale, or a proper tunnel before opening the dashboard locally.

For SSH local forwarding:

```bash
ssh -L 18789:localhost:18789 -L 8642:localhost:8642 user@host
```

Then open:

```text
http://127.0.0.1:18789/
```

## Verification checklist

After install, verify all of these before calling it working:

```bash
nemohermes list
nemohermes <sandbox-name> status
nemohermes <sandbox-name> dashboard-url --quiet
curl -sf http://127.0.0.1:8642/health
```

Then open the dashboard in Chrome and confirm the page title/content is Hermes, not a different local dashboard.
