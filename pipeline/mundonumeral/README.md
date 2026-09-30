# @mundonumeral: rankings e comparações animadas (TikTok)

## Padrão (29/09)
- **Formato:** ranking em **contagem regressiva do 10º ao 1º**.
  - A lista começa com "?" e cada posição é revelada com barra crescendo e valor contando.
  - Um cartão grande mostra a posição atual.
  - O Brasil aparece destacado em verde, para gerar identificação.
  - O suspense vai até o 1º lugar, o que prende a pessoa até o fim.
- **Gancho (0–3 s):** contraste ou surpresa ("o mesmo sanduíche pode custar o dobro") + "QUEM FICA EM 1º?" na tela + "fica até o final".
- **Paleta:** a mesma da foto de perfil (azul-marinho noturno, luzes de cidade douradas, dourado #F5B83D, destaque verde para o Brasil). Fontes Anton e Montserrat.
- **Voz:** pm_santa (Kokoro) **mais grave**: pitch 0,90 com reforço de graves. Velocidade ~1,12.
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

## Passos
1. Rode `bash ../setup.sh` e pesquise o tema e os dados, com a fonte.
2. Escreva o `spec.json` (modelo: `spec_exemplo.json`, com intro, 10 itens com fala e outro) e rode `python3 make_ranking.py WORKDIR`. Confira 4–6 quadros.
3. Hospede no branch `media` em `mundonumeral/<data>-<turno>-<slug>.mp4` e agende no Metricool, na marca do Mundo Numeral: rede tiktok, tiktokData com title, isAigc true e PUBLIC_TO_EVERYONE.
