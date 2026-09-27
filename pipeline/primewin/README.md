# Prime Win — Reels de convencimento (automação de operações)

Mesmo motor do TikTok (`../make_video.py`, custo zero). O que muda é o **conteúdo** e a **identidade visual**.

## Padrão aprovado (vídeo-teste 27/09/2026)
- **Objetivo:** convencer, não ensinar. A ideia central é "você pode não precisar mais operar manualmente, se optar por uma automação" / "já pensou em nunca mais clicar em comprar ou vender?".
- **Argumentos:** perdas, quebra de conta, emocional (medo, ganância, revanche, entrar atrasado, segurar prejuízo), disciplina do robô (segue a estratégia, respeita o stop, não hesita) e liberdade de tempo. Varie o ângulo a cada vídeo.
- **Anúncio da Prime Win:** automatiza estratégias, e toda automação é testada em ambiente de conta real antes de chegar ao cliente.
- **5PI:** mesa proprietária que libera até cem mil reais para operar na Profit. Mantenha sempre.
- **CTA:** "Comenta PRIME aqui embaixo que a gente te manda as informações no direct". **Nunca** "link na bio".
- **Conformidade (CVM/Meta):**
  - Sem prometer lucro, sem percentuais ou valores de ganho, sem "renda garantida".
  - Sempre feche com "operar envolve risco, resultado passado não garante resultado futuro".
  - O gráfico abstrato leva "Simulação ilustrativa".
- **Pronúncia:** o nome se lê "PRAIME win". O `make_video.py` troca Prime→Praime **só na voz** (a legenda continua "PRIME"). Para outras palavras, use `"pronuncia": {"Palavra":"Como falar"}` no spec.
- **Gráfico por mais tempo (pedido de 27/09):**
  - O clipe do gráfico tem 13s por padrão.
  - A `intro` deve ter **3 frases** (12–15s sobre o gráfico) e o `recap` **3 frases**.
  - Mais de 1/3 do vídeo fica no gráfico.
- **Variar o gráfico a cada vídeo (rodízio, registre no histórico):**
  - `--estilo linha` ou `--estilo candles`. Candles em pelo menos metade dos vídeos.
  - `--cenario ondas`: 3 operações maiores, compra no fundo e saída no topo.
  - `--cenario tendencia_alta` / `tendencia_baixa`: várias entradas num único movimento, cada uma ganhando poucos pontos, com contador "N operações +X pontos". Nesses vídeos, a narração deve comentar isso, por exemplo: "numa única tendência o robô fez várias entradas curtas, pegando poucos pontos em cada uma, sem cansaço e sem hesitar".
  - Nunca repita a mesma combinação estilo+cenário do vídeo anterior.
- **Técnico:**
  - Voz pm_santa acelerada, 61–72s.
  - `music_mood: "alegre"`.
  - Paleta azul-marinho/roxo + ciano #3fe0ff + amarelo #ffd23f.
  - Cartão final PRIME/WIN.

## Estrutura (seções do spec)
1. `intro` (2 frases): gancho sobre a animação `primewin/explainer_primewin.py` (entradas e saídas automáticas).
2. `meio` (5–7 frases): dores e argumentos, sobre 3–4 fotos reais do Canva (alternando dor e alívio).
3. `recap` (2 frases): Prime Win + testado em conta real, de volta à animação.
4. `final_5pi` (1–2 frases): foto de dinheiro.
5. `final_fim` (2 frases): Comenta PRIME + aviso de risco, sobre o cartão final.

O roteiro deve ter de 190 a 205 palavras. Modelo completo em `spec_exemplo.json` (copie o `endcard`, as cores e as palavras-chave).

## Horários
Tarefa agendada "Prime Win: 2 Reels por dia no Instagram": 10:05 e 18:05 (picos de audiência de finanças no Instagram, dados do Metricool). Ela publica na hora via Zapier. O TikTok roda às 10:40 e 17:40; os horários não se cruzam, para as duas tarefas não gravarem o branch media ao mesmo tempo.

## Passos
1. Rode `bash ../setup.sh`.
2. Escolha o ângulo do dia e registre-o em `historico_primewin.json`. Não repita o ângulo dos últimos 7 dias.
3. Gere a animação no WORKDIR: `python3 explainer_primewin.py --estilo candles --cenario tendencia_alta "TÍTULO 1" "TÍTULO 2"`.
   - Varie os títulos, por exemplo "SEM CLICAR" / "EM COMPRAR OU VENDER", ou "VÁRIAS ENTRADAS" / "NUMA SÓ TENDÊNCIA".
   - Se der "operação negativa", troque `--seed`.
   - Verifique `explicativo_final.png` com Read.
4. **Clipes de vídeo reais (obrigatório, pedido de 27/09):** no bloco `meio` e na 5PI, use **principalmente clipes em movimento**. Fotos paradas são apenas complemento, no máximo 1–2 por vídeo.
   - `git clone -q --depth 1 --branch clipes https://github.com/traderdaylle-videos/v-deos- /tmp/clipes` e escolha pelo `../clipes_catalogo.json`.
   - Use 5–6 itens no `meio`, um por frase, cada um com 4–6s. Combine a cena com a fala (estressado na dor, gráfico caindo na perda, liberdade no final).
   - Não repita a mesma sequência do vídeo anterior.
   - O `make_video.py` monta cada clipe com fundo desfocado e o vídeo nítido no centro. Escolha o trecho com `"clip_offset": {"arquivo.mp4": segundos}`.
   - **Clipes novos** (1–2 por dia, para variar):
     - Ache o ID no Mixkit com WebSearch "mixkit free stock video <tema>". O ID é o número no fim da URL.
     - Dispare o workflow: `curl -s -X POST -H "Accept: application/vnd.github+json" -H "Content-Type: application/json" https://api.github.com/repos/traderdaylle-videos/V-deos-/actions/workflows/baixar-clipes.yml/dispatches -d '{"ref":"main","inputs":{"itens":"<nome>-<ID>.mp4 https://assets.mixkit.co/videos/<ID>/<ID>-1080.mp4"}}'` (itens separados por quebra de linha).
     - Espere cerca de 1 min, clone o branch `clipes` de novo e adicione a descrição ao `clipes_catalogo.json`.
   - Canva: o conector não busca na biblioteca de vídeos do Canva. Se o usuário puser vídeos numa pasta do Canva, dá para exportá-los em MP4 (export-design) e passar a URL ao mesmo workflow.
5. Fotos (complemento):
   - Reutilize as de `../fotos/` (trader-estressado, homem-relaxado-automacao, trader-monitores-noite, celular-grafico, dinheiro-reais).
   - Ou gere novas no Canva: `generate-image` → design Phone Wallpaper → `insert_fill` 1080x1920 → pegue o PNG da miniatura do `edit-design` em tool-results.
6. Escreva `spec.json` e rode `python3 ../make_video.py WORKDIR`. Confira de 4 a 6 quadros.
7. Hospede o vídeo no branch `media` (órfão, force-push, mantendo os 3 últimos dias) em `primewin/<data>-<slug>.mp4`. A URL fica `https://raw.githubusercontent.com/traderdaylle-videos/V-deos-/media/primewin/<arquivo>`.
8. Publique como Reels via Zapier `instagram_for_business` publish_video:
   - instagramPageId `17841422795242601`;
   - conexão `0276af1e-2b83-8acf-966c-8e21fb820c5d`;
   - legenda com "Comente PRIME", hashtags e o aviso de risco.
