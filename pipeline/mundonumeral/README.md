# @mundonumeral: rankings e comparações animadas (TikTok)

## Padrão (29/09)
- **Formato:** ranking em **contagem regressiva do 10º ao 1º**.
  - A lista começa com "?" e cada posição é revelada com barra crescendo e valor contando.
  - Um cartão grande mostra a posição atual.
  - O Brasil aparece destacado em verde, para gerar identificação.
  - O suspense vai até o 1º lugar, o que prende a pessoa até o fim.
- **Gancho (0–3 s):** contraste ou surpresa ("o mesmo sanduíche pode custar o dobro") + "QUEM FICA EM 1º?" na tela + "fica até o final".
- **Clipes reais (30/09):**
  - Um painel com moldura dourada no topo mostra, em cada posição, um clipe real do país: bandeira tremulando ou cidade (branch `clipes`, arquivos `mn-*`).
  - Na abertura, o painel mostra clipes do tema (comida, produto, cidade).
  - O cartão da posição fica sobre o painel, e a lista compacta fica embaixo.
  - Para baixar bandeiras e cidades novas do Mixkit, use o workflow `baixar-clipes` (busque "mixkit <país> flag").
  - Se não houver clipe do país, use um de cidade genérica.
- **Música ALEGRE e interativa** (`music_mood: "alegre"`, volume 0,34), com um "whoosh" a cada revelação.
- **Voz mais rápida:** Santa grave, velocidade 1,28–1,32 (ajuste automático). Para manter 61–72 s, o roteiro deve ter ~245–255 palavras: cada posição com 1 curiosidade curta.
- **Fundo:** SEMPRE um clipe em movimento ligado ao tema (ex.: bandeira do país/produto do ranking, em close tremulando), levemente desfocado sob um véu azul-marinho leve (spec `bg_clip`). Nunca fundo parado/pesado.
- **Paleta:** a mesma da foto de perfil (azul-marinho noturno, luzes de cidade douradas, dourado #F5B83D, destaque verde para o Brasil). Fontes Anton e Montserrat.
- **Voz:** pm_santa (Kokoro) **mais grave**: pitch 0,90 (rubberband) com reforço de graves.
- **Duração:** 61–72 s (monetização exige mais de 1 minuto).
- **Legendas SEMPRE**, com destaque em verde para "BRASIL".
- **Dados reais com fonte na tela** (The Economist, Banco Mundial, FMI, OCDE, IBGE…). Confira os números na fonte do dia; nunca invente.
- **Final:** pergunta para comentar ("qual ranking você quer ver amanhã?") + "segue o Mundo Numeral".
- **Legenda do post (interativa):**
  - gancho + pergunta ("Você esperava…? Comenta 👇");
  - 1 linha com a fonte;
  - "Segue pra um ranking novo todo dia";
  - 3–5 hashtags: 1 ampla + nicho (#ranking #curiosidades #mundo #economia #[tema]).
  - Marque isAigc: true, porque a voz é sintética.
- **Ideias de tema (não repetir, `historico.json`):**
  - salário mínimo;
  - horas de trabalho para comprar um iPhone;
  - gasolina mais cara;
  - países mais visitados;
  - maiores economias (2000 vs hoje);
  - custo de vida nas capitais;
  - preço do café;
  - maiores empresas;
  - idade média;
  - expectativa de vida;
  - internet mais rápida;
  - impostos.

## Rotina (aprovada em 30/09): 4 posts por dia
- 2 disparos por dia; cada disparo produz **2 vídeos com temas diferentes** e agenda os 2 no Metricool (marca Mundo Numeral, brandId 7160301).
  - Manhã → posts do turno "manha" (~07:30) e "almoco" (~12:30).
  - Tarde → posts do turno "tarde" (~18:30) e "noite" (~21:30).
  - Ajuste os horários com `getBestTimeToPostByNetwork` (tiktok) quando a conta já tiver dados; nunca agende no passado.
- **Fila aprovada:** antes de produzir, veja `fila/*.json` com `"aprovado": true`. Cada um já tem vídeo hospedado e legenda: agende-o no lugar de 1 vídeo novo e apague o arquivo da fila.
- Temas variados (economia, preços, viagens, tecnologia, esportes, população, curiosidades…) sempre com dados reais e fonte; não repetir os últimos 30 temas do `historico.json`.
- Antes de produzir, confira que a marca 7160301 tem o TikTok conectado (`getBrandSettings`, `networksData.tiktokData`). Se não tiver, não produza nada (economia) e avise no resumo.

## Passos
1. Rode `bash ../setup.sh` e pesquise o tema e os dados, com a fonte.
2. Escreva o `spec.json` (modelo: `spec_exemplo.json`, com intro, 10 itens com fala e outro) e rode `python3 make_ranking.py WORKDIR`. Confira 4–6 quadros.
3. Hospede no branch `media` em `mundonumeral/<data>-<turno>-<slug>.mp4` e agende no Metricool, na marca do Mundo Numeral: rede tiktok, tiktokData com title, isAigc true e PUBLIC_TO_EVERYONE.

## Narração que flui (30/09)
- O script corrige a vogal fantasma do espeak ("quar-ə-to", "Ar-ə-gentina") e tira o acento secundário: isso eliminava as "vírgulas" no meio das frases.
- Voz grave via rubberband (pitch 0.90), sem o atempo que picotava.
- Velocidade máxima 1.32 (acima disso o Kokoro engole sílabas). Roteiro de ~245–255 palavras.
- Escrever frases corridas: "Em quarto vem a Noruega, com seis e sessenta e sete." Evitar dois-pontos e vírgulas em excesso ("Quarto, a Noruega: seis..."). No máximo 1 vírgula por frase curta.
