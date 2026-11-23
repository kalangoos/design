# Como contribuir com o Design System

Obrigado por ajudar o KalangoOS a ter uma só linguagem visual. Este repo é **só design**: fonte FigCraft, exports, tokens, marca e ícones.

## O que você precisa

- [FigCraft](https://github.com/storytold/figcraft/releases) (desktop) para editar a fonte
- `git` + [Git LFS](https://git-lfs.com) (`git lfs install` uma vez)
- `figcraft-cli` no PATH (vem com o FigCraft / releases) para regenerar PNGs

Quem só revisa visual: GitHub + os PNGs em `exports/vitrine/` bastam.

## Fluxo

1. **Issue** — use o modelo "Nova tela" ou "Ajuste de token". Descreva a tela, o app e o estado (vazio, erro, claro/escuro).
2. **Branch** a partir de `main`.
3. **Edite** `KalangoOS-DesignSystem.figcraft` no FigCraft.
   - Siga tokens e componentes existentes (não invente cor fora da paleta).
   - Telas do sistema: cantos 8 / cartões 6 / controles 4; sem sombras.
   - Identificadores novos de componente em inglês quando forem nomes técnicos; textos de UI em português no arquivo (o código usa `tr("English")` depois).
4. **Um PR, um autor no `.figcraft`.** Duas pessoas editando o binário na mesma branch geram conflito impossível de mergear com qualidade. Coordene na issue.
5. **Exporte** as páginas que mudaram:
   ```sh
   ./scripts/exportar-telas.sh
   # ou só algumas:
   PAGES="05 · Telas do sistema e apps" ./scripts/exportar-telas.sh
   ```
6. **PR** — descreva o que mudou; anexe ou deixe os PNGs em `exports/` para o review visual. Se tokens mudaram, diga explicitamente (precisa sync no monorepo).

## Tokens

- Arquivos públicos: `tokens/tokens.json`, `tokens-dark.css`, `tokens-light.css`.
- `./scripts/exportar-tokens.sh` grava o JSON cru das variáveis (`tokens/_variables.json`) quando o CLI cooperar; a folha GTK ainda é curada.
- Depois de merge com tokens novos: PR em `kalangoos/kalangoos` atualizando só `design/tokens/`.

## O que não fazer

- Não usar o Figma (ou Community) como fonte — no máximo espelho só leitura, depois.
- Não depender de sessão ao vivo do FigCraft como histórico; a verdade é o Git.
- Não abrir PR só com o `.figcraft` sem PNGs quando a mudança for visível em página da vitrine.
- Não alterar a marca (logo/mascote) sem acordo nos maintainers — ver LICENSE-brand.txt.

## Código de conduta

[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

**English.** Edit the `.figcraft` source with FigCraft, one author per PR on that binary, regenerate showcase PNGs with `./scripts/exportar-telas.sh`, and call out token changes so they can sync to `kalangoos/kalangoos` `design/tokens/`.

## Espelhos

Figma / `.fig` e sessões view-only: [ESPELHOS.md](ESPELHOS.md).
