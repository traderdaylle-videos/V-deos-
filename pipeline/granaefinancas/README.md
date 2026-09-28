# Grana e Finanças: vídeos diários (Instagram Reels + YouTube Shorts + YouTube longo)

Canal de **educação financeira psicológica com base no estoicismo**. Tom **dramático e cinematográfico do começo ao fim**, estilo documentário escuro, como o canal Hábito Estoico. Custo zero. É um canal separado do TikTok @traderdaylle e da Prime Win.

## Regras do usuário (obrigatórias)
- **Tema do dia:**
  - Pesquise o assunto financeiro em alta no Brasil hoje.
  - Transforme-o em uma lição de psicologia financeira com princípios estoicos reais: Epicteto, Sêneca, Marco Aurélio, a dicotomia do controle, a premeditação dos males, o desconforto voluntário, a revisão noturna e o hábito.
  - Não repita um tema dos últimos 7 dias (veja `historico.json`).
- **Palavras:**
  - Escreva como especialista em comunicação.
  - Frases curtas com gancho e pausas dramáticas.
  - Faça perguntas que confrontam o espectador ("até onde isso é culpa do país? E onde começa a sua parte?").
  - Termine com uma ferramenta prática e uma pergunta-espelho.
- **Citações:** só frases que o autor realmente escreveu (ou paráfrase fiel, sem aspas). Nunca invente citação.
- **Proibido:**
  - O aviso "não é recomendação de investimento". Ele é só do TikTok e da Prime Win.
  - A palavra "robô".
  - Promessa de ganho.
- **Voz:** Piper **Jeff** (pt_BR-jeff-medium), NATURAL, sem acelerar (length_scale ~1.0), com o tratamento de narrador do `make_gf_cine.py`.
- **Visual:**
  - Clipes reais em tela cheia com gradação escura esverdeada (paleta do Instagram: #04342C, dourado #E8B84A).
  - Frases de impacto no meio da tela e legendas no terço inferior.
  - O final fica sobre imagem real (dinheiro).
  - Nunca use imagem religiosa (igreja, santos, crucifixo). Para "antiguidade" use teatro-romano, corredor-colunas-estatuas, mapa-antigo-vela, fonte-roma.
- **Trilha:** `musica_cinema.py` (escura, com impactos nas viradas do texto).
- **CTA:**
  - Vídeo curto: "Manda pra alguém que precisa ouvir isso" e "segue a Grana e Finanças".
  - Vídeo longo: pedir inscrição e perguntar "qual princípio você vai aplicar primeiro?".

## Dois vídeos por tema
1. **Curto (9:16, 45–65s):** vai para o Instagram @granaefinancas como Reels e para o YouTube Shorts. Modelo: `spec_cine_exemplo.json`, aprovado pelo usuário em 28/09.
2. **Longo (16:9, 5–8 min):** só YouTube. Modelo: `roteiro_longo_endividamento.py`, que gera o `spec.json`. Estrutura:
   - abertura com o gancho do curto;
   - "há dois mil anos…";
   - promessa dos N princípios;
   - um capítulo por princípio (cartão "PRINCÍPIO N", citação na tela, dica prática);
   - conclusão com a pergunta-espelho e o CTA.

## Passos
```bash
pip install piper-tts scipy matplotlib pillow numpy --break-system-packages -q
git clone -q --depth 1 --branch clipes https://github.com/traderdaylle-videos/v-deos- /tmp/clipes   # clipes + voz Jeff
```
1. **Pesquisa:** use WebSearch e confira os números nas fontes.
2. **Vídeo curto:**
   - Escreva `spec.json` em `/tmp/gf/` e copie os clipes usados de `/tmp/clipes/clipes/`.
   - Rode `python3 pipeline/granaefinancas/make_gf_cine.py /tmp/gf`, que leva ~10 min.
   - Quando um comando puder passar de 10 min, rode com `nohup … &` e acompanhe.
3. **Vídeo longo:**
   - Copie `roteiro_longo_endividamento.py`, reescreva as frases, os clipes e os overlays para o tema, e rode-o em `/tmp/gfl/` (gera `spec.json` com `"formato": "16:9"`).
   - Rode `nohup python3 pipeline/granaefinancas/make_gf_cine.py /tmp/gfl > /tmp/gfl/log.txt 2>&1 &`, que leva ~50 min, e acompanhe com `sleep`.
   - Reencode para caber no GitHub (<95 MB): 2 passes com `-b:v 1850k`, áudio aac 128k.
4. **Conferir:**
   - Extraia 10–12 quadros de cada vídeo e veja com Read: texto legível, nada preto demais, sem imagem religiosa, legendas sem sobreposição.
   - Confira também a duração.
5. **Miniatura do longo:**
   - 1280x720, a partir de um quadro escurecido.
   - Número ou frase de impacto em Anton dourado, subtítulo em Montserrat, "GRANA E FINANÇAS" no rodapé.
6. **Hospedar no branch `media`:**
   - Clone o branch, adicione `granaefinancas/<data>-<slug>-curto.mp4` e `youtube/<data>-<slug>.mp4`.
   - Mantenha as pastas de outras tarefas e apague só arquivos das suas pastas com mais de 3 dias.
   - Commit órfão e `push -f` só no branch media.
   - Confira as URLs raw com `curl -sI`.
7. **Agendar no Metricool** (brandId 7082205, America/Sao_Paulo):
   - **Reels:** `instagramData {type: REEL, showReelOnFeed: true, isAiGenerated: true}`.
     - Legenda: gancho, texto curto, pergunta de comentário, "📩 Manda esse vídeo pra alguém…", "👉 Segue @granaefinancas…" e hashtags.
   - **YouTube Short:** o mesmo vídeo curto, no mesmo horário do Reels.
     - `youtubeData {type: short, title: "... #shorts", category: EDUCATION, madeForKids: false, isAiGeneratedContent: true}`.
   - **YouTube longo:** melhor horário do YouTube (`getBestTimeToPostByNetwork` youtube), normalmente à tarde.
     - `youtubeData {type: video, title chamativo ≤100 caracteres, tags, category: EDUCATION, madeForKids: false, isAiGeneratedContent: true}`.
     - Descrição com os capítulos em minuto:segundo (use `_tempos.json`).
8. **Registrar:** grave em `historico.json` a data, o tema, os princípios, os arquivos e os ids do Metricool. Faça commit e push em `main`.
