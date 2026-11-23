# Espelhos e visualização (fase 2)

A **fonte** continua sendo `KalangoOS-DesignSystem.figcraft` neste repositório. Tudo abaixo é derivado.

## Espelho `.fig` (Figma e apps compatíveis)

- Arquivo: [`mirrors/KalangoOS-DesignSystem.fig`](mirrors/KalangoOS-DesignSystem.fig) (Git LFS).
- Gerado com `figcraft-cli export … --format fig` (experimental).
- **Só leitura / referência.** Não aceite PRs que editem o `.fig` e pedem para virar fonte. Contribuições entram no `.figcraft`.
- O export omite variáveis, vários estilos compartilhados, anotações de Dev Mode e parte das molas — o FigCraft avisa isso no terminal.

Regenerar:

```sh
mkdir -p mirrors
figcraft-cli export KalangoOS-DesignSystem.figcraft -o mirrors/KalangoOS-DesignSystem.fig --format fig
```

## Ver ao vivo (view-only)

O FigCraft (desktop ou build web) permite **Share ▸ Online** com link só de visualização. Isso é uma sessão temporária (servidor padrão ou o da org), **não** substitui o Git:

1. Mantenedor abre a fonte, inicia share em modo view.
2. Cola o link na issue/PR para critique.
3. Ao terminar, **Stop sharing**; as mudanças de verdade vão num PR com o `.figcraft` + PNGs.

Servidor da org (preview): **Fly.io** — `wss://kalangoos-figcraft.fly.dev/` (health: `https://kalangoos-figcraft.fly.dev/healthz`). Empacotamento em [deploy/fly/](deploy/fly/). Publish só com a **server key** (privada; `fly ssh console … key`). Depois de publicar o `.figcraft`, anunciar aqui o **link/código só de visualização**. A verdade versionada continua no Git LFS.

## Vitrine PNG

`exports/vitrine/` — o que o site e o review no GitHub usam. Regenerar com `./scripts/exportar-telas.sh`.
