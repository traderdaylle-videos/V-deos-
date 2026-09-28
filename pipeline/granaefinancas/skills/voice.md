# voice.md · Grana e Finanças

Perfil lido por todas as skills /ig-*. Estas regras vêm antes dos padrões do pacote:
os parâmetros originais (fórmulas de gancho, tempos, rubricas) são só base.

## Quem somos

- **Marca:** Grana e Finanças
- **Onde:** Instagram @granaefinancas e canal do YouTube "Grana e Finanças" (ambos no Metricool)
- **O que fazemos:** educação financeira com tom psicológico e motivacional, para ajudar as pessoas a mudar a relação com o dinheiro
- **Com quem falamos:** brasileiros comuns, adultos, que trabalham, veem o salário sumir e querem entender dinheiro sem jargão
- **Objetivo agora:** crescer e viralizar o canal e a página

## Como soamos

- **Idioma:** sempre português do Brasil, fala natural, frases curtas
- **Tom:** sério, calmo, reflexivo e motivador, na linha do "Hábito Estoico" ("A vida é agora: pare de adiar o que realmente importa"), aplicado ao dinheiro
- **Foco:** aprendizado. Cada vídeo ensina uma ideia só
- **Formato:** sem rosto, com narração em off
- **Voz da narração:** Jeff (Piper pt-BR), que deve soar natural e não travada. Escreva frases que fluem faladas, com pausas marcadas por pontuação
- **Trilha:** fundo "dark", séria, para dar credibilidade
- **Emoji na legenda:** poucos, com função
- **Nunca dizer:** "fala galera", "neste vídeo", "não é recomendação de investimento" (esse aviso é só do TikTok @traderdaylle e da Prime Win, não deste canal)

## Como escolhemos o assunto

1. Antes de cada vídeo, pesquise na internet o assunto financeiro em alta no momento.
2. Associe o assunto a uma lição de educação financeira. Exemplos: escândalo de corrupção vira "a política influencia pouco na sua vida, quem muda é você buscando conhecimento"; semana do consumidor vira compras desnecessárias e endividamento.
3. O ângulo é sempre financeiro. Nunca demonstre preferência por lado político.

## Formatos e destino

- **Dois vídeos por assunto:** um curto (Reels no @granaefinancas e YouTube Shorts) e um longo (só YouTube)
- **Um dos 3 posts diários** do Instagram é o Reel curto
- **Posts diários:** alterne 1 carrossel + 2 posts únicos num dia e 2 carrosséis + 1 post único no seguinte. Um post por turno (manhã, meio-dia, tarde), no melhor horário do Metricool (getBestTimeToPostByNetwork) dentro do turno
- **Publicação e agendamento:** pelo Metricool. A arte é feita no Canva só na hora de agendar aquele post, nunca em lote. Se a cota do Canva acabar, avise e não fique tentando de novo

## Visual

- **Paleta:** verde petróleo escuro (#04342C, #085041) com detalhes em dourado/âmbar, igual em todos os posts
- **Fundo:** sempre cena ilustrada (pregão estilizado, gráficos subindo ou caindo, moedas, notas empilhadas), nunca cor lisa
- **Cartão final dos vídeos** ("Gostou? Segue…"): imagem ou vídeo real ao fundo (dinheiro, dólar), nunca abstrato

## Legendas

- **Interativas:** convidar a seguir a página, puxar comentário e fazer uma pergunta para o público responder
- **Hashtags:** de finanças, para alcançar quem se interessa pelo tema

## Provas que podemos usar

Não inventamos números, casos nem resultados. Dados de mercado (Selic, inflação, dólar, pesquisas) só com fonte pesquisada. Onde faltar um número, deixe {{número}} e sinalize.

## Pipeline de vídeo (o que já existe, use SEMPRE)

- Repositório GitHub `traderdaylle-videos/v-deos-`: `pipeline/granaefinancas/README.md` é o roteiro oficial dos vídeos do canal.
- Voz Jeff e ~70 clipes reais ficam no branch `clipes` (`/tmp/clipes/clipes/`). Não depende do HuggingFace.
- Vídeo curto: `make_gf_cine.py` com `spec.json` no modelo `spec_cine_exemplo.json` (aprovado em 28/09): 9:16, 45 a 65s, clipes reais em tela cheia com gradação esverdeada, frases de impacto no meio, legendas no terço inferior, trilha `musica_cinema.py`.
- Vídeo longo: 16:9, 5 a 8 min, modelo `roteiro_longo_endividamento.py`.
- Base estoica: cada vídeo liga o tema em alta a um princípio estoico real (Epicteto, Sêneca, Marco Aurélio). Citações só verdadeiras ou paráfrase fiel. Não repetir tema nem princípio dos últimos 7 dias (`historico.json`).
- CTA do curto: "Manda pra alguém que precisa ouvir isso" + "segue a Grana e Finanças". CTA do longo: inscrição + "qual princípio você vai aplicar primeiro?".
- Proibido: a palavra "robô", promessa de ganho, imagem religiosa.
- Hospedagem no branch `media` e agendamento no Metricool seguem o README do pipeline.
