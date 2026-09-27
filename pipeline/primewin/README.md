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

## Passos
1. Rode `bash ../setup.sh`.
2. Escolha o ângulo do dia e registre-o em `historico_primewin.json`. Não repita o ângulo dos últimos 7 dias.
3. Gere a animação: `python3 explainer_primewin.py "TÍTULO 1" "TÍTULO 2"`, rodado no WORKDIR. Varie os títulos, por exemplo "SEM CLICAR" / "EM COMPRAR OU VENDER". Verifique `explicativo_final.png` com Read.
4. Fotos:
   - Reutilize as de `../fotos/` (trader-estressado, homem-relaxado-automacao, trader-monitores-noite, celular-grafico, dinheiro-reais).
   - Ou gere novas no Canva: `generate-image` → design Phone Wallpaper → `insert_fill` 1080x1920 → pegue o PNG da miniatura do `edit-design` em tool-results.
5. Escreva `spec.json` e rode `python3 ../make_video.py WORKDIR`. Confira de 4 a 6 quadros.
6. Hospede o vídeo no branch `media` (órfão, force-push, mantendo os 3 últimos dias) em `primewin/<data>-<slug>.mp4`. A URL fica `https://raw.githubusercontent.com/traderdaylle-videos/V-deos-/media/primewin/<arquivo>`.
7. Publique como Reels via Zapier `instagram_for_business` publish_video:
   - instagramPageId `17841422795242601`;
   - conexão `0276af1e-2b83-8acf-966c-8e21fb820c5d`;
   - legenda com "Comente PRIME", hashtags e o aviso de risco.
