# Pipeline de vídeos TikTok @traderdaylle (custo zero)

Roteiro que a tarefa agendada segue a cada disparo. Tudo roda no workspace do Claude; nada de ElevenLabs/Descript.

## 0. Preparar
```bash
bash pipeline/setup.sh          # voz Piper pt-BR em /tmp/piper + libs
W=/tmp/job && rm -rf $W && mkdir -p $W
```

## 1. Tema
Leia `pipeline/historico.json` e escolha um tema que NÃO esteja nos últimos 10 (padrões de candle, tendência,
suporte/resistência, Fibonacci, médias, RSI, volume, gestão de risco, etc.).

## 2. Roteiro (spec.json)
Português do Brasil, falado, frases curtas. Total de narração ~80–100s (o vídeo PRECISA passar de 60s).
Seções, nesta ordem obrigatória:
- `intro` (3–5 frases): gancho + explicação clara do conceito/estratégia.
- `meio` (5–7 frases): exemplo genérico de "zona de compra/venda" ("é aqui que muitos analistas técnicos costumam observar..."),
  cuidados/sinais falsos e UMA pergunta ao espectador ("Me conta aqui nos comentários: ...").
- `recap` (1–2 frases): "Recapitulando: ...".
- `final_5pi` (2 frases): "Se você quer colocar esse estudo em prática com capital de verdade, a 5PI é uma mesa proprietária que libera até cem mil reais de capital pra você operar, direto na plataforma Profit." + "O link tá aqui na descrição do vídeo."
- `final_fim` (2 frases): "Segue aqui pra mais dicas de análise técnica." + "Lembrando: este vídeo é apenas educacional e não é recomendação de investimento."
Nunca prometer lucro, nunca sinal em tempo real, nunca recomendação personalizada. Escreva números por extenso ("cem mil").

## 3. Clipe explicativo (abstrato e MUITO claro)
Copie e adapte `pipeline/explainer_exemplo_cruzamento_medias.py` para o tema: fundo #0d1117, título grande, subtítulo com a regra,
legenda de cores, gráfico com dados sintéticos limpos que mostram o padrão de forma óbvia, ponto-chave marcado com rótulo grande,
frase de destaque abaixo do gráfico e o QUARTO INFERIOR VAZIO (legendas). Gera `explicativo_anim.mp4` (8s, 1080x1920) e
`explicativo_final.png`. Rode dentro de $W. Extraia 2 quadros e CONFIRA com a ferramenta Read (legível, sem sobreposição).

## 4. Fotos reais
Banco em `pipeline/fotos/` (1080x1920 ou 9:16). A cada vídeo, gere 1–2 fotos NOVAS ligadas ao tema no Canva para variar:
1. `generate-image` (aspectRatio PORTRAIT_9_16, foto realista, pessoas/dinheiro/gráficos, sem texto) → `get-generate-image-job` → media id.
2. `create-design` (format "Phone Wallpaper", brief "blank dark background, no text") → `get-create-design-async-job` → design id.
3. `read-design` com open_transaction:true → `edit-design` página 1 `insert_fill` (top 0, left 0, width 1080, height 1920) com o media id;
   para uma 2ª foto use `add_page` (1080x1920) + ler o id da página 2 + `insert_fill`.
4. O thumbnail devolvido pelo `edit-design` (338x600) fica salvo em
   `~/.claude/projects/*/tool-results/mcp-Canva-blob-*.png` → pegue o mais recente (`ls -t`), confira com Read, copie para
   `pipeline/fotos/<nome-descritivo>.png`. Depois `edit-design` finalize:"commit".
(O workspace não consegue baixar o export em alta do Canva; o thumbnail é a fonte.)
Escolha 3 fotos para `photos_meio` (inclua as novas) e `pipeline/fotos/dinheiro-reais.png` (ou outra de dinheiro) para `photo_5pi`.
Copie as escolhidas para $W.

## 5. Montar
```bash
python3 pipeline/make_video.py $W     # imprime {"output","duration","size_mb"}
```
Confirme duração > 60s. Extraia 4–6 quadros e confira com Read (ordem: explicativo → fotos → explicativo → dinheiro → cartão final).

## 6. Hospedar no GitHub (branch `media`)
```bash
git -C pipeline/.. fetch origin media 2>/dev/null || true
```
Publique o mp4 em `tiktok/AAAA-MM-DD-slug.mp4` na branch `media` (crie como órfã se não existir; mantenha só os vídeos dos
últimos 3 dias nessa branch para o repositório não crescer — os anteriores já foram copiados pelo Metricool).
URL pública: `https://raw.githubusercontent.com/traderdaylle-videos/V-deos-/media/tiktok/<arquivo>.mp4`
Também faça commit em `main` das fotos novas e do `historico.json` atualizado.

## 7. Agendar no Metricool
`createScheduledPost` blogId 7082205, rede tiktok, data = agora + 5 min (America/Sao_Paulo), media = URL raw acima,
`tiktokData`: title (curto), isAigc:true, commercialContentThirdParty:true (divulgação da parceria 5PI), privacy PUBLIC_TO_EVERYONE.
Legenda: gancho + resumo + pergunta de engajamento + "Quer operar com capital de verdade? Conheça a 5PI, mesa proprietária parceira:
https://www.5pi.com.br/parceiros/prime-win" + "Segue @traderdaylle pra mais dicas de análise técnica." + "⚠️ Conteúdo educacional.
Não é recomendação de investimento." + 6–9 hashtags. Se o Metricool recusar a mídia, NÃO repita em loop: relate o erro.
