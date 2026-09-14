# Brev NemoHermes Clean Onboarding Pattern — 14 June 2026

Use this when setting up Hermes in NemoClaw on a Brev/cloud GPU instance after one or more failed attempts.

## Key lessons

- Type the full word `yes` at the license prompt. `y` cancels the installer.
- Use model option `1`: `nvidia/nemotron-3-super-120b-a12b`. Avoid `openai/gpt-oss-120b` for Hermes tool use because it can reject tool descriptions.
- At Messaging, press `1` to toggle Telegram, then press Enter. Pressing Enter first skips Telegram.
- For group-chat safety, answer `Y` to `Reply only when @mentioned?`.
- Enter the correct numeric Telegram user ID for DM allowlisting. Do not confuse this with a chat ID from another bot or an old test run.
- Sandbox names must be lowercase with hyphens only, e.g. `my-assistant`. No spaces or capitals.
- After the installer has installed `nemohermes`, prefer `nemohermes onboard --fresh` for retries. Do not keep rerunning the full `curl | bash` installer because the upgrade stage may start a gateway and then onboarding complains that the same port is already occupied.

## Clean retry sequence after failed onboarding

From the cloud host prompt (`shadeform@shadecloud:~$`):

```bash
export PATH="/home/shadeform/.local/bin:$PATH"

# Stop stale gateway service/processes if port 8080 or 8081 is blocked
systemctl --user stop openclaw-gateway.service 2>/dev/null
systemctl --user disable openclaw-gateway.service 2>/dev/null
sudo killall openshell openshell-gateway 2>/dev/null
sudo lsof -i :8080
sudo lsof -i :8081
```

If a PID still appears, kill it directly:

```bash
sudo kill -9 <PID>
```

If port 8080 keeps respawning, switch to 8081:

```bash
export NEMOCLAW_AGENT=hermes
export NEMOCLAW_GATEWAY_PORT=8081
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8081 proto tcp
nemohermes onboard --fresh
```

## Prompt answers for the successful path

- Resume or fresh: `f`
- Provider: `1` NVIDIA Endpoints
- API key: paste NVIDIA key
- Model: `1` Nemotron 3 Super 120B
- Sandbox name: `my-assistant` or another lowercase hyphenated name
- Apply configuration: `y`
- Messaging channels: press `1`, then Enter
- Telegram bot token: paste token from BotFather
- Reply only when @mentioned: `Y`
- Telegram User ID: enter Jared's numeric Telegram user ID, not a bot ID
- Resource profile: `6`
- Policy tier: Balanced for normal use; Restricted only for governance stress tests

## Existing sandbox conflict

If onboarding says another sandbox uses the same Telegram credential, do not continue. Destroy the old sandbox first:

```bash
nemohermes <old-sandbox-name> destroy
```

If it asks whether to destroy the shared gateway and this is the last/broken sandbox, choose `yes`.

## Host vs sandbox prompt

- Host prompt: `shadeform@shadecloud:~$`
- Sandbox prompt: `sandbox@<container>:~$`

Run `nemohermes onboard`, `nemohermes <name> destroy`, and gateway commands from the host. Run `hermes` only after connecting into the sandbox:

```bash
nemohermes my-assistant connect
hermes
```

## Localhost access

For API access from the Mac, forward port 8642 from the Mac terminal:

```bash
brev port-forward <instance-name> -p 8642:8642
```

Then open:

```text
http://127.0.0.1:8642/v1/models
```

The dashboard path remains unreliable for Hermes sandboxes. Terminal chat and the API path are the reliable checks.
