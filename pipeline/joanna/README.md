# @delíciadajoanna: receitas no TikTok (custo zero)

## Padrão (definido pelo usuário em 29/09)
- **Receitas pouco comuns feitas com ingredientes populares.** Exemplos: rösti de batata com queijo, pão de frigideira de iogurte, nhoque de abóbora de frigideira, omelete suflê, bolinho de arroz crocante. Não repetir receita (`historico.json`).
- **Voz:** feminina e suave (Kokoro `pf_dora`, velocidade perto de 0,95). A duração fica em **61–72 s** (exigência de monetização: vídeo com mais de 1 minuto). O roteiro deve ter de 170 a 185 palavras.
- **Paleta suave:** creme, rosa-blush, sálvia e pêssego. Trilha suave lo-fi (`musica_suave.py`), que abaixa sob a voz.
- **Mínimo de texto na tela:**
  - título pequeno só no começo;
  - etiqueta curta de cada ingrediente (quantidade);
  - número do passo;
  - cartão final "Delícia da Joanna / Salva pra fazer depois".
  - **Legenda SEMPRE** na parte de baixo, com destaques em rosa.
- **Estrutura para prender a atenção:**
  1. **Gancho** com o prato pronto (queijo puxando, crocância) + frase curiosa ("Você nunca comeu batata desse jeito").
  2. **O que é** a receita + promessa (tempo, poucos ingredientes).
  3. **Ingredientes:** 1 imagem de IA por ingrediente (Canva, estilo suave e minimalista, fundo de linho creme), com etiqueta de quantidade.
  4. **Passos numerados** sobre clipes reais (branch `clipes`, arquivos `receita-*`), com o **segredo** da receita destacado no meio (gera retenção).
  5. **Prato pronto** de novo (recompensa) + pergunta para comentar.
  6. **CTA:** salvar e seguir. Uma barra de progresso fina no topo ajuda a pessoa a assistir até o fim.
- **Legenda do post:**
  - nome da receita + gancho;
  - lista curta de ingredientes;
  - pergunta;
  - "Salva pra fazer depois 💛";
  - 5–8 hashtags (#receita #receitafacil #receitasimples #comidacaseira #dicasdecozinha + específicas).
  - Marcar **isAigc: true** (conteúdo com IA).

## Monetização (TikTok Creator Rewards)
- O vídeo precisa ter mais de 1 minuto. A conta precisa de 10 mil seguidores e 100 mil views em 30 dias, e o dono deve ter 18 anos ou mais.
- **Conteúdo com IA deve ser rotulado** (isAigc). O TikTok não paga vídeos "100% gerados por IA" (visual e voz). Para reduzir esse risco:
  - roteiro original;
  - clipes reais de preparo;
  - edição própria;
  - receita testável e correta.
  - O ideal é o usuário gravar a narração ou as mãos no futuro.
- Sem marcas de terceiros, sem música com direitos autorais (a trilha é gerada por código) e sem promessas de saúde ou emagrecimento.

## Passos
1. Rode `bash ../setup.sh` e clone os clipes: `git clone -q --depth 1 --branch clipes https://github.com/traderdaylle-videos/v-deos- /tmp/clipes`.
2. Escolha a receita e escreva o roteiro (confira quantidades e tempos: a receita tem que funcionar).
3. Gere no Canva 1 imagem de IA por ingrediente e 1 do prato pronto. Use `generate-image`, PORTRAIT_9_16, e este estilo de prompt: "Soft minimalist food photography, [ingrediente] on a light cream linen cloth, pastel peach and sage tones, soft daylight, top-down, negative space, no text". Pegue a miniatura 338x600 com o truque do design Phone Wallpaper (`update_fill`) e salve em `fotos/`.
4. Se faltar clipe para algum passo, baixe do Mixkit pelo workflow `baixar-clipes` com o prefixo `receita-`.
5. Rode `python3 make_joanna.py WORKDIR` com o `spec.json` (modelo: `spec_exemplo.json`) e confira 4–6 quadros.
6. Hospede no branch `media` em `joanna/<data>-<turno>-<slug>.mp4`, mantendo as outras pastas.
7. Agende no Metricool, na marca da @delíciadajoanna, com rede tiktok e `tiktokData`: title, isAigc true e privacyOption PUBLIC_TO_EVERYONE.
