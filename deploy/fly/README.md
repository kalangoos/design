# figcraft-server on Fly.io (KalangoOS)

Self-hosted [figcraft-server](https://github.com/storytold/figcraft/blob/main/docs/server.md) for view-only / live share of the Design System. **Not** the Git source of truth — that stays `KalangoOS-DesignSystem.figcraft` in this repo.

## Why Fly (not Pages / Worker / Render)

GitHub Pages and the Cloudflare Worker cannot run a long-lived native process with disk and WebSockets. Fly gives TLS (`wss://`), a volume, and WebSocket proxying. Render’s free tier sleeps; we keep `auto_stop_machines = "off"` so shares stay up (uses the Free plan’s ~$5/mo credit after a card is on file).

## Cost (Free plan)

- Machine `shared-cpu-1x` **1024 MB** always on (needed to publish the ~170 MiB `.figcraft`) — likely uses most or all of the **$5/mo** Free credit after a card is added; watch the bill.
- Volume **1 GB** without a card (enough for one Design System publish); >1 GB needs a payment method.
- Without a card: only ~$1 starter credit, then it stops.
- Server is **private** (`open_publish = false`): only the server key publishes; share **view** links with the community.

## Deploy

```sh
export PATH="$HOME/.fly/bin:$PATH"
cd deploy/fly
fly auth login          # browser
fly apps create kalangoos-figcraft   # once
fly volumes create figcraft_data --region iad --size 1
fly deploy --ha=false
curl -fsS https://kalangoos-figcraft.fly.dev/healthz   # expect: ok
```

**Status (2026-11-23):** app no ar, health `ok`, volume 1 GB em `iad`.

Print the **server key** (keep private; used to manage files — never commit it):

```sh
fly ssh console -a kalangoos-figcraft -C '/usr/local/bin/figcraft-server --config /etc/figcraft-server/server.toml key'
```

## Publish the Design System

1. FigCraft desktop → Preferences → Server for online sharing → `wss://kalangoos-figcraft.fly.dev/`
2. Open `KalangoOS-DesignSystem.figcraft` → **Share ▸ Online** (or **File ▸ Publish to server…**).
3. Copy the **view** link/code for contributors; put it in `ESPELHOS.md` / members area when stable.
4. Edits that matter still go through Git LFS + `exports/vitrine/` PRs.

## Ops

```sh
fly status
fly logs
fly ssh console
fly scale memory 1024   # if publishing the big file OOMs
```

Do not commit the server key. Rotate by regenerating data volume only as a last resort (wipes published files).
