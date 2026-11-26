<p align="center">
  <img src=".github/assets/cabecalho.png" alt="KalangoOS · Design System: marca, tokens e ícones" width="100%">
</p>

# Design System do KalangoOS

Fonte visual do [KalangoOS](https://github.com/kalangoos/kalangoos): o arquivo FigCraft, os tokens exportados, a marca e os ícones dos apps. Este repositório é o lugar certo para **contribuir com telas e componentes** sem clonar o monorepo de código.

<p align="center"><img src="guia/marca.png" alt="Página Marca do Design System: logos, símbolo, ícones, cores e regras de uso" width="80%"></p>

| Pasta / arquivo | O quê |
|---|---|
| `KalangoOS-DesignSystem.figcraft` | **Fonte** (FigCraft). Versionada com Git LFS — edite aqui. |
| `exports/vitrine/` | PNGs de páginas-chave para review no GitHub e para o site |
| `tokens/` | `tokens-dark.css`, `tokens-light.css` (`@define-color` GTK) e `tokens.json` |
| `marca/` | Logo, símbolo, ícone e variantes (PNG/SVG) |
| `icones/` | Os 19 ícones dos apps do sistema |
| `guia/marca.png` | Página "Marca": cores, tamanhos e regras de uso |
| `scripts/` | Exportar telas e variáveis com `figcraft-cli` |

## Kalango Train (página 38)

Todas as telas do [Kalango Train](https://github.com/kalangoos/kalango-train) (treino do assistente com os dados da própria pessoa) ficam numa página só, `38 · Kalango Train`, organizada como a do Kalango Cast: cada tela com o título em cima, em seções, na ordem abaixo. Largo (janela de 1640 px na área de trabalho) e estreito (janela de 480 px) lado a lado; as versões em modo claro ficam no fim da página, em "Modo claro". PNGs em `exports/vitrine/38-Kalango_Train/`.

| Seção | Conteúdo |
|---|---|
| Base e primeiro uso | Visão geral, primeiro uso, componentes novos, ícone do app e logo de marketing |
| Consentimento e aprovação | Fila de aprovação (original × limpo), aprovação em lote, consentimento de treino, trilha, regras de coleta, cessão da GPU |
| Promoção de modelo | Modelos, critérios da promoção, ponto de restauração, modelo de fábrica, comparar A × B |
| Rastros | Lista, árvore de chamadas e cascata, sessões, gerações, prompts, pontuações |
| Curadoria | Conjuntos, filtros, duplicatas, divisões, contaminação, versões |
| Compor trabalho | Compositor único para todos os tipos de trabalho, YAML, recompensas |
| Execução | Trabalhos e monitor ao vivo (curvas, GPU, VRAM, cede a GPU, retomada) |
| Avaliações e exportação | Avaliação congelada, suíte de segurança, exportação GGUF |
| Backends remotos | Local, SLURM, Modal e Kubernetes, com as marcas de "não verificado" |
| Ajustes e ambiente | Configurações e ambiente Python (não instalado, instalando, falha de hash, sem espaço) |
| Laboratório e linha do tempo | Pipeline vivo do treino e rio de versões dos modelos |
| Movimento | Molas por gesto, durações, reduzir movimento |
| Fluxos animados e microinterações | Quatro fluxos de protótipo (smart animate) e microinterações em laço |
| Princípios de design | O que o Train não negocia |
| Modo claro | Versões em modo claro das telas principais |

## Como contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md). Resumo:

1. Instale o [FigCraft](https://github.com/storytold/figcraft/releases) e faça `git lfs install` + clone deste repo.
2. Abra uma issue (tela nova ou ajuste).
3. Edite o `.figcraft` numa branch (**um autor por PR** no arquivo fonte — merge binário não funciona bem).
4. Rode `./scripts/exportar-telas.sh` e envie o PR com os PNGs atualizados.

Quem só quer comentar o visual pode abrir o PR e olhar `exports/vitrine/` — não precisa do FigCraft.

## Regras da marca

- **Cores** só da paleta: Lavanda `#A5A1E2`, Menta `#8ED2C3`, Azul `#7CC3DF`, Creme `#F1DDB0`, Ouro `#E5C98C`,
  Coral `#EFA2A6`, Carvão `#16171B`; no tema claro, Verde `#34CB79` e Roxo `#322153`.
- **Sem sombra, brilho ou degradê.** Não esticar, não girar, não redesenhar o mascote.
- **Área de respiro** igual à altura da letra "O" do nome. **Tamanho mínimo:** logo principal com 96 px de altura,
  horizontal com 120 px de largura; abaixo disso, o ícone (mínimo 24 px).
- **Fundo escuro:** logo principal ou creme. **Fundo claro:** tema claro ou a versão escura de uma cor.

Fontes do Design System (não incluídas): Inter (texto), URW Gothic (títulos) e JetBrains Mono (código).

## Espelhos e view-only

Ver [ESPELHOS.md](ESPELHOS.md): arquivo `.fig` unidirecional e como usar share só de visualização.

## Sync com o código

O monorepo [`kalangoos/kalangoos`](https://github.com/kalangoos/kalangoos) consome uma cópia em `design/tokens/`.
Quando este repo mudar tokens, abra (ou peça) um PR lá só com esses arquivos.

## Licenças

- `tokens/` e o trabalho de UI no `.figcraft` (exceto marca): **GPL-3.0-or-later** ([LICENSE](LICENSE)), como o código do KalangoOS.
- `marca/`, `icones/`, `guia/` e a página "Marca" no FigCraft: **marca do KalangoOS**, fora de licença aberta ([LICENSE-brand.txt](LICENSE-brand.txt)).

A marca e os ícones foram gerados com IA (Higgsfield, modelo GPT Image) a partir de descrições escritas pelo projeto,
em novembro de 2026, e vetorizados (`vtracer`). Detalhes em [ATTRIBUTION.md](ATTRIBUTION.md).

---

**English.** Source FigCraft file (Git LFS), exported tokens (GTK CSS + JSON; GPL-3.0-or-later), brand pack and system app icons (brand licence: LICENSE-brand.txt). Contribute screens here — see CONTRIBUTING.md. Figma is not the source of truth; optional mirrors may appear later as one-way exports only.
