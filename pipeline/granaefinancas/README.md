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
- **Voz (atualizada em 30/09):** Piper **Faber** dinâmico — ver "Voz aprovada em 30/09" abaixo. (O Jeff lento foi substituído.)
- **Visual:**
  - Clipes reais em tela cheia com gradação escura esverdeada (paleta do Instagram: #04342C, dourado #E8B84A).
  - Frases de impacto no meio da tela e legendas no terço inferior.
  - O final fica sobre imagem real (dinheiro).
  - Nunca use imagem religiosa (igreja, santos, crucifixo). Para "antiguidade" use teatro-romano, corredor-colunas-estatuas, mapa-antigo-vela, fonte-roma.
- **Trilha:** `musica_cinema.py` (escura, com impactos nas viradas do texto).
- **CTA:**
  - Vídeo curto: "Manda pra alguém que precisa ouvir isso" e "segue a Grana e Finanças".
  - Vídeo longo: pedir inscrição e perguntar "qual princípio você vai aplicar primeiro?".

## Preferências de 29/09: AULA DE EDUCAÇÃO FINANCEIRA SOBRE A NOTÍCIA (substituem o foco no estoicismo)
Voz, clipes, trilha, overlays e configurações continuam iguais (aprovados). O que muda é o **texto**, no curto e no longo:
- **O ensinamento é EDUCAÇÃO FINANCEIRA, não estoicismo.** Parta de uma notícia financeira do dia (pesquisada, com fonte) e dê uma **aula** sobre ela: o que aconteceu, **por que** acontece e **o que isso muda no bolso** da pessoa.
  - Exemplo: "Hoje o dólar subiu 5%":
    - o que isso influencia: importações, preço de combustível, eletrônicos e alimentos, inflação, juros;
    - por que acontece: juros e mercado americano, fluxo de capital, risco fiscal, commodities;
    - o que fazer com o próprio dinheiro.
- **O estoicismo fica só como a IDEIA de fundo:** a postura de assumir a responsabilidade pelo próprio dinheiro ("não controlo o dólar, mas controlo o que faço com o meu dinheiro"; "a culpa do meu orçamento é minha"). Use no máximo 1 referência estoica curta por vídeo, nunca como tema principal. Nada de "3 princípios estoicos".
- **Curto (~60s):** gancho com o número da notícia → o que aconteceu → por que acontece (1–2 causas simples) → o que muda no seu bolso (2–3 efeitos concretos) → virada de responsabilidade (a ideia estoica, 1 frase) → ação prática → pergunta → CTA.
- **Longo (~4,5 min):** aula completa sobre a notícia:
  - o fato e os números;
  - as causas explicadas passo a passo;
  - os efeitos em cadeia (importação → inflação → juros → crédito → seu bolso);
  - quem ganha e quem perde;
  - o que fazer (reserva, dívidas, consumo);
  - fechamento com a postura de responsabilidade e o CTA.
  - Capítulos pelos tópicos da aula, e não "Princípio 1/2/3".
- Títulos, legendas e descrições refletem a notícia e a aula (ex.: "Dólar subiu 5%: o que muda no seu bolso"), não o estoicismo.

## Preferências aprovadas em 28/09 (valem para todos os vídeos)
- **Skills de roteiro:** as skills `/ig-*` adaptadas ao canal estão em `skills/` (perfil da marca em `skills/voice.md`).
  - Use o método do `skills/ig-reel/SKILL.md` para o roteiro curto.
  - Escreva 3 ganchos com fórmulas diferentes de `skills/ig-reel/hooks.json` e pontue com `python3 skills/ig-reel/hookscore.py ganchos.txt` (entende pt-BR).
  - Escolha o de maior nota (mínimo 70, STRONG). O gancho abre com um **número concreto tirado de fonte pesquisada no dia** (ex.: "Seus mil reais parados viram novecentos e cinquenta e dois em um ano", conta feita a partir do Focus).
  - Confira o ritmo com `skills/ig-reel/beats.py` e o texto com `skills/ig-human/detect.py`.
- **Estrutura do curto aprovado (~60s):** gancho com número → dado da fonte → frases curtas com pausas → frase de virada ("Guardar não é proteger") → princípio estoico em paráfrase fiel → pergunta-espelho → ferramenta prática ("abra o seu extrato e pergunte: esse dinheiro tem um destino?") → CTA "Manda pra alguém que precisa ouvir isso. E segue a Grana e Finanças."
- **Overlays:** número gigante (`Num`) nos dados, 1 frase de impacto (`Tit`), citação/pergunta em `Sub`, handle no final.
- **Números falados por extenso** na narração; na tela, em algarismos.
- **Legenda do Reels:** revise com `python3 skills/ig-caption/caption.py legenda.txt --keywords "..."` até dar READY. Ela deve ter:
  - 1ª linha com o número e uma pergunta ("Me conta 👇");
  - corpo curto com a fonte;
  - "📩 Manda esse vídeo pra alguém…";
  - "👉 Segue @granaefinancas…";
  - até 5 hashtags de finanças.
- **Não refaça nada do zero:** voz, clipes e montagem vêm sempre deste pipeline.

## Dois vídeos por tema
1. **Curto (9:16, 45–65s):** vai para o Instagram @granaefinancas como Reels e para o YouTube Shorts. Modelos: `spec_cine_inflacao_aprovado.json` ("sensacional", 28/09) e `spec_cine_exemplo.json`.
2. **Longo (16:9, ~4,5 min):** só YouTube (o usuário pediu ~4,5 min em 28/09; roteiro de ~550–600 palavras e 3 princípios; `target` [240, 330]). Modelos: `roteiro_longo_inflacao.py` (3 princípios, ~4,5 min, o formato atual) e `roteiro_longo_endividamento.py`; eles geram o `spec.json`. Estrutura:
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

## Preferências de 30/09 (capa e ordem do feed)
- **Capa obrigatória em todo Reels/Short:** coloque `"capa": "<título curto da notícia>"` no spec (ex.: "Dólar subiu 5%: o que muda no seu bolso"). O `make_gf_cine.py` gera `<video>_capa.jpg`: quadro do vídeo escurecido, faixa verde petróleo com o título (1ª linha dourada) e @granaefinancas, na faixa central (aparece inteira no grid do perfil). Hospede o jpg no branch media junto do vídeo e passe a URL raw em `videoThumbnailUrl` no Metricool (Reels e Short).
- **Ordem do feed (nunca 2 Reels seguidos):** manhã = post único → meio-dia = Reels 1 → tarde = carrossel → noite = Reels 2. Assim o feed alterna post, vídeo, carrossel, vídeo.

## Voz aprovada em 30/09: FABER dinâmico
- O usuário achou o Jeff lento e suave demais e escolheu o **Faber** (pt_BR-faber-medium, no branch clipes): mais dinâmico e com som real.
- Já é o padrão do `make_gf_cine.py`: length_scale 0,86 (ajuste automático entre 0,80 e 0,92), dicção limpa (noise_scale 0,55, noise_w 0,6), pausas de vírgula encurtadas para ~0,12 s e entre frases no máximo 0,18 s, sem engrossar o tom, presença nos médios e compressão. O `"voice"` dos specs/roteiros antigos é ignorado.
- **Roteiro mais longo para manter a duração:** curto (45–65 s) com **~190–210 palavras**; longo (240–330 s) com **~850–950 palavras**. Se der erro de duração, acrescente ou corte frases (nunca desacelere a voz).

## Trilha nova em 30/09: INSPIRADORA (mais alegre e atrativa)
- O usuário pediu música mais atrativa e um pouco mais alegre. O padrão do `make_gf_cine.py` agora é `musica_inspira.py`: tom maior (~104 BPM), arpejo brilhante, baixo pulsando, bateria leve que entra após a abertura e prato/riser nas viradas (`impactos_seg`).
- Alterne `music_seed` 0/1 entre os vídeos (duas progressões diferentes). A trilha escura antiga só com `"trilha": "cinema"` no spec (não usar por padrão).
