# CLAUDE.md — Preferências do usuário (páginas, vídeos e tarefas agendadas)

> Leia este arquivo antes de qualquer tarefa. Ele vale para todas as execuções, inclusive as tarefas agendadas.
> O usuário **não fala inglês**: responda e escreva tudo em **português (pt-BR)**.
> Quando duas regras parecerem conflitar, vale a mais recente (datas entre parênteses).

---

## 1. Regras gerais

### Economia do plano (prioridade)
- Economizar o limite do plano Claude **sem** reduzir as tarefas agendadas e **sem** perder qualidade nem as preferências dos vídeos já aprovados.
- Renderizar os vídeos **fora do Claude** (ex.: GitHub Actions), mantendo a mesma voz, os mesmos clipes e o `make_gf_cine.py`.
- **Checar o limite do Metricool antes de produzir**, para não gastar em posts que vão travar.
- Conferir só **4 a 6 quadros por vídeo**, sem reler o que já foi conferido.
- Prompts das tarefas enxutos.
- **Nunca trocar o modelo das tarefas por um mais barato.**
- Usar primeiro tudo o que está disponível de graça no Claude; só depois considerar conectores ou assinaturas pagas.

### Mudanças em tarefas agendadas
- **Antes de mudar qualquer tarefa agendada (inclusive para economizar), mostrar ao usuário o que muda.**
- Quando existir uma opção melhor ou mais automática que exija conectar outro app/conta, pode sugerir a conexão diretamente.

### Falhas e limites
- Se acabar a cota de geração de imagens do Canva, ou créditos de outra ferramenta, **avisar claramente e parar**, sem ficar tentando de novo. Manter o que já deu certo e anotar a limitação no resumo.

### Infraestrutura
- GitHub: conta `traderdaylle-videos`, repositório público `V-deos-`.
  - Pipeline gratuito na pasta `pipeline/` (seguir `pipeline/README.md`).
  - Clipes e voz no branch `clipes`; vídeos prontos hospedados no branch `media` e enviados ao Metricool pela URL `raw.githubusercontent`.
- Metricool: brand `7082205` (@granaefinancas e TikTok @traderdaylle); brand `7160301` (rankincuriosos). Plano pago.
- Fuso horário: America/Sao_Paulo.

---

## 2. Instagram @granaefinancas + YouTube "Grana e Finanças"

### Rotina diária (desde 02/10/2026)
- **3 posts por dia no Instagram**: 1 post único, 1 carrossel e 1 Reels. (O teste com 4/dia fez os vídeos pararem de sair; voltou ao formato que funcionava.)
- Mais o **YouTube**: 1 Short + 1 vídeo longo.
- Um post por turno (manhã, meio-dia, tarde), cada um no **melhor horário do Metricool** (`getBestTimeToPostByNetwork`) para aquele dia da semana — nunca horário fixo.
- Feed alternado: post, carrossel e vídeo — **nunca dois Reels seguidos**.
- **Todo Reels precisa ter capa.**

### Notícias e posts
- Ângulo **estritamente financeiro/de mercado**, mesmo quando o assunto envolve política. **Nunca** mostrar preferência por lado político.
- Paleta: verde-petróleo escuro (`#04342C`, `#085041`) com detalhes em dourado/âmbar, igual em todos os posts.
- Imagens sempre com **fundo de cena ilustrada** (pregão estilizado, gráficos subindo/caindo, moedas, notas) — **nunca fundo liso**.
- Imagens feitas no Canva, **só no momento de agendar aquele post** — nunca gerar todas do dia antecipadamente.
- Legendas interativas: convidar a seguir, comentar e responder uma pergunta, mais hashtags de finanças.

### Vídeos (curto e longo)
- **Sempre produzidos pelo pipeline do GitHub** (`pipeline/granaefinancas`, `make_gf_cine.py`), **nunca refeitos do zero**.
- Sempre 2 vídeos por assunto: um **curto** (~60 s, Instagram + YouTube Shorts) e um **longo** (~4,5 min, só YouTube). O longo é feito a partir do curto aprovado.
- Antes de cada vídeo, pesquisar os assuntos financeiros em alta.
- **Conteúdo = educação financeira** (29/09): pegar a notícia do dia e ensinar sobre ela — o que aconteceu, por que acontece, o que afeta (ex.: "dólar subiu 5%" → importados, inflação, mercado americano). O estoicismo fica só como ideia de fundo (responsabilidade sobre o próprio dinheiro), sem dominar o roteiro.
- Padrão aprovado ("sensacional", 28/09): clipes reais em tela cheia, frases de impacto com número grande, legendas no terço inferior, um princípio real com paráfrase fiel, ferramenta prática + pergunta-espelho.
- CTA final: "Manda pra alguém que precisa ouvir isso. E segue a Grana e Finanças".
- Cartão final ("Gostou? Segue…") com **imagem/vídeo real ao fundo** (dinheiro, dólar etc.), nunca fundo abstrato.
- Tom cinematográfico/documentário, palavras caprichadas e chamativas.
- Roteiros passam pelas skills `/ig-*` adaptadas: gancho com número concreto de fonte pesquisada, pontuação em pt-BR, legenda revisada.
- **Voz: Piper "Faber"** (desde 30/09; substituiu a Jeff) — dinâmica e realista, com dicção limpa e sem pausas desnecessárias (ajuste aprovado em 01/10).
- **Trilha: mais atraente e um pouco mais alegre** (aprovada em 30/09), junto com a capa automática.
- **NÃO usar** o aviso "não é recomendação de investimento" nesses vídeos (esse aviso é só do TikTok @traderdaylle e da Prime Win).

---

## 3. TikTok @traderdaylle (vídeos de trading)

- **2 vídeos por dia**, via tarefa agendada e Metricool (brand `7082205`).
- Vídeos originais narrados, sem aparecer na câmera: Fibonacci, reversões, padrões de candle, tendências, forex, índice.
- **Não** precisa seguir a paleta do @granaefinancas. **Não** postar esses vídeos no @granaefinancas.
- Duração: **"1 min e pouco"** (61–72 s, roteiro de ~150–175 palavras), fala acelerada. Sempre acima de 60 s (monetização do TikTok).
- **Voz: Kokoro "Santa"** (`pm_santa`).
- Estrutura:
  1. Abrir com clipe explicativo claro (diagrama animado com título e rótulos, nada vago);
  2. Meio com clipes reais em movimento (pessoas analisando gráficos, mãos digitando, dinheiro, celular), trocando a cada ~7–10 s — **nunca uma imagem parada o vídeo todo**;
  3. Logo antes do final, repetir o clipe explicativo;
  4. Fechamento: imagem clara e literal do padrão explicado (pode ser gerada de graça com matplotlib/mplfinance).
- Pode mostrar zonas genéricas de "onde os técnicos costumam observar compra/venda", como ilustração educativa, nunca como recomendação.
- **Legendas obrigatórias**, perguntas ao espectador e legenda do post com interação e hashtags.
- Trilha instrumental mais animada ("contagiante"), um pouco mais alta que a ambiente antiga, sem tirar o foco da voz.
- Ordem do final: **anúncio da 5PI** (link na descrição: https://www.5pi.com.br/parceiros/prime-win — factual, sem prometer lucro nem aprovação) → **"segue aqui pra mais dicas"** → **aviso "não é recomendação de investimento"**.
- Imagens realistas: Canva (Pro). Explicações: gráficos animados abstratos.

---

## 4. Prime Win (Instagram + MagnetoV12)

### Rotina
- **4 Reels por dia**, publicados direto, sem esperar aprovação. Postagem pelo **Metricool** (o Zapier do Instagram foi abandonado).
- 2 dos 4 Reels são **anúncios do MagnetoV12** com relatórios diários de contas reais (ocultar dados da conta, titular e nome da automação), resultado e % de acerto, com o link da landing page na legenda: https://claude.ai/artifact/YUK1E8u7oTnN6uBZbCFvgd
- 1 vídeo por dia abre com imagens que despertam desejo de ter uma automação (para quem ainda nem opera na bolsa).
- 1 vídeo por dia oferece o serviço de **automatizar a estratégia** de quem já tem uma.

### Estilo dos vídeos
- Objetivo: **persuasão, não educação** — convencer que operar com automação é mais viável ("já pensou em nunca mais clicar em comprar ou vender?"), usando dores reais (prejuízos, quebra de conta, psicológico, decisões emocionais).
- Dizer que a Prime Win automatiza estratégias e que as automações são sempre testadas em conta real. Manter o anúncio da mesa proprietária 5PI.
- Em vez de "link na bio": pedir para comentar **"PRIME"** e receber as informações por direct (exceto nos anúncios do MagnetoV12, que usam o link da landing page).
- **NUNCA usar a palavra "robô".** Falar de automações em geral; nunca sugerir que o vídeo mostra uma automação ou operação específica (o gráfico é só ilustração).
- Gráfico abstrato: deixar mais tempo na tela; variar (um movimento longo, várias entradas curtas na mesma tendência, entrada em retração de Fibonacci, candles em vez de linhas).
- Depois do gráfico, **clipes reais em movimento** (vídeos prontos do Canva), não fotos paradas.
- Paleta: azul-marinho/roxo escuro, ciano e dourado neon. "PRIME" branco/ciano, "WIN" dourado.
- Voz **Santa**, levemente acelerada; pronúncia **"PRAIME win"**. Trilha alto-astral. Pouco mais de 1 minuto.
- Cartão final: texto "AUTOMAÇÕES DE MERCADO FINANCEIRO" sob o logo, com foto/vídeo real ao fundo e fonte marcante (nada de fundo liso).
- Legendas dos posts caprichadas.

### MagnetoV12 (para textos de divulgação)
- Automação para o Profit Pro; opera sozinha na compra e na venda, média de acerto ~70% ao dia, faz leitura de fluxo e entra no sentido da força do mercado.
- **Enfatizar: NÃO faz preço médio contra a posição.**
- Venda via link do Mercado Pago; também no marketplace da 5PI (5PI Store).
- O sistema de e-mail de compra (Google Apps Script) é só para compradores e **não deve ser alterado**; o teste grátis de 3 dias dos leads do WhatsApp tem sistema e e-mail próprios.

---

## 5. TikTok rankincuriosos (antigo "Mundo Numeral")

- Rankings/comparações animados entre países e empresas (preços, salários etc.). Metricool brand `7160301`.
- Rotina de 4 posts/dia — **tarefa pausada** desde 01/10; só retomar se o usuário pedir.
- Estilo aprovado: clipes reais por país, fundo em movimento ligado ao tema (ex.: bandeira tremulando), música alegre e interativa, voz Santa mais grave e mais rápida, narração sem pausas falsas.
- Sempre legendas na tela, hashtags e legenda do post interativa. Paleta próxima à foto de perfil (mapa-múndi com cidades acesas e "1" dourado).
