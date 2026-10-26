# Profile gateway RAM / capacity checks

Use this when the user asks whether the machine can support another always-on Hermes specialist agent, or asks how much RAM is left while multiple profile gateways are running.

## Quick probe on macOS

Run a single grouped probe so the answer is based on live state:

```bash
printf 'Memory pressure:\n'; memory_pressure
printf '\nVM swap:\n'; sysctl vm.swapusage
printf '\nTop memory summary:\n'; top -l 1 -s 0 | sed -n '1,12p'
printf '\nPhysical memory bytes:\n'; sysctl hw.memsize
printf '\nHermes profiles:\n'; hermes profile list
printf '\nHermes gateway RSS:\n'; ps -axo pid,rss,command | grep -E 'hermes_cli.main.*gateway run' | grep -v grep | sort -k2 -nr
```

If using `awk` for RSS formatting, avoid nested quoting mistakes from tool wrappers; a plain `ps` list is usually enough. Convert RSS KB to MB mentally only after using a calculation tool if exact values matter.

## How to interpret results

- macOS `top` may show very low `unused` RAM while the system is still healthy because file cache, inactive pages, and compressed pages are reclaimable.
- Do not equate literal `unused` RAM with safe capacity. Also report:
  - `memory_pressure` free/available percentage or pressure status
  - swap used / swapins / swapouts
  - compressed memory
  - wired memory
  - per-gateway RSS
- If swap used is `0` and memory pressure is healthy, one more idle profile gateway is usually safe even if `top` reports little `unused` memory.
- If swap is active, compressor is very high, or pressure is elevated, recommend stopping idle specialist gateways before adding another always-on bot.

## Typical Hermes profile gateway overhead

In Jared's macOS setup, idle profile gateways commonly sat around ~130 MB RSS each, while the default gateway was larger (~235 MB). Treat these as observations, not constants: always re-measure live before advising.

## User-facing answer style

Give both numbers and the practical conclusion:

- Total RAM
- Literal unused/free RAM
- Swap used
- Compression/wired memory if notable
- Whether it is safe to add another profile-backed agent
- Which stopped/running profiles matter

Avoid over-explaining macOS memory internals unless the user asks. A concise caveat like “literal unused RAM is low, but macOS has reclaimable/compressed memory and swap is still 0” is enough.

## Bot token safety note

If the capacity check is adjacent to creating a Telegram-backed profile and the user pasted a BotFather token in chat, do not repeat the token in the final answer. Store it only in the relevant profile `.env` as `TELEGRAM_BOT_TOKEN`, verify with Telegram `getMe`, set `TELEGRAM_ALLOWED_USERS`, then restart that profile gateway. If the token was exposed somewhere unintended, advise rotating it with BotFather.
