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
- **Modelos (atualizado 08/10/2026, pedido do usuário):** tarefas que produzem e agendam posts usam `claude-sonnet-5-5`; a tarefa de Checagem usa `claude-haiku-5-5`. O Opus (`claude-opus-5-5`) fica reservado só para configurar e manter o pipeline, não para postar.
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
- Metricool (plano pago), contas confirmadas pelo usuário em 08/10/2026:
  - brand `7082205`: Instagram @granaefinancas, TikTok @traderdaylle, YouTube "Grana e Finanças" (`UCDeUffa8mTd3TOv8_wBV6Qw`);
  - brand `7160301`: Instagram @pwinautomacoes (Prime Win), TikTok **@rankingcuriosos** (Rankin Curiosos, antigo Mundo Numeral). Use sempre este handle, não "rankincuriosos".
  - A brand `7212955` (ilarrointeriores) não faz parte deste pipeline.
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

### Rotina (atualizado 08/10/2026)
- **2 Reels por dia**, publicados direto, sem esperar aprovação. Postagem pelo **Metricool** (o Zapier do Instagram foi abandonado).
  - Disparo das **08:05** (turno manhã): formato **DESEJO**, para quem ainda não opera na bolsa.
  - Disparo das **20:05** (turno noite): formato **MAGNETO**, anúncio do MagnetoV12 com relatórios diários de contas reais (ocultar dados da conta, titular e nome da automação), resultado e % de acerto, com o link da landing page na legenda: https://claude.ai/artifact/YUK1E8u7oTnN6uBZbCFvgd
- Os formatos **SERVIÇO** (turno tarde) e os turnos de almoço e tarde ficam **fora da rotina atual**; só voltam se o usuário pedir.

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

## 4b. Estado das tarefas agendadas (09/10/2026)

- Todas as tarefas de vídeo estão **ativas** desde 08/10/2026 à noite e renderizam pelo GitHub (seção 6), com os prompts reescritos:
  - **Vídeos Grana e Finanças — fase 1 (PRODUÇÃO)**: 08:54 — gera o curto e o longo pelo motor gf, espera o render e grava o manifesto `pipeline/logs/<data>-gf-pronto.json`.
  - **Vídeos Grana e Finanças — fase 2 (AGENDAMENTO)**: 11:30 — lê o manifesto, confere o branch media e agenda Reels, Short e longo no Metricool (Sonnet).
  - **Agendar posts de imagem @granaefinancas**: 05:52 — 1 post único e 1 carrossel, com Canva (não mudou).
  - **Prime Win (Reels)**: 08:05 (DESEJO) e 20:05 (MAGNETO) — motor video, pasta primewin.
  - **TikTok @traderdaylle**: 10:40 — 2 vídeos, motor video, pasta tiktok.
  - **Rankin / @rankingcuriosos**: 06:06 — 2 rankings, motor ranking, pasta mundonumeral.
  - **Checagem diária**: 13:10 e 21:10 (Haiku), dispara tarefas só para o que faltar.
- Testes de render validados em 08/10/2026 (`teste-gf-curto`, `teste-primewin`, `teste-ranking`). Workflow `render.yml` verde.
- Ainda não testado: a espera pelo render dentro de uma execução agendada. Se falhar, a tarefa corrige sozinha (seção 6).
- O limite do plano renova na **quarta-feira, 14/10/2026, às 12:00**. Não gastar uso à toa.

---

## 5. TikTok @rankingcuriosos (antigo "Mundo Numeral")

- Rankings/comparações animados entre países e empresas (preços, salários etc.). Metricool brand `7160301`, TikTok `rankingcuriosos`.
- Rotina atual (08/10/2026): **2 posts por dia**, num único disparo às **06:06**, que agenda os posts de ~07:30 e ~12:30. A tarefa estava pausada desde 01/10 e foi reativada pelo usuário.
- Estilo aprovado: clipes reais por país, fundo em movimento ligado ao tema (ex.: bandeira tremulando), música alegre e interativa, voz Santa mais grave e mais rápida, narração sem pausas falsas.
- Sempre legendas na tela, hashtags e legenda do post interativa. Paleta próxima à foto de perfil (mapa-múndi com cidades acesas e "1" dourado).

---

## 6. Renderização fora do Claude (08/10/2026, pedido do usuário)

- Vídeos são renderizados no **GitHub Actions** (`.github/workflows/render.yml`), não no Claude.
- Para renderizar, a tarefa escreve um spec JSON em `pipeline/fila/<nome>.json`, com as chaves:
  - `motor`: `gf` (make_gf_cine.py) | `video` (make_video.py) | `ranking` (make_ranking.py);
  - `pasta`: `granaefinancas`, `tiktok`, `primewin`, `mundonumeral` ou `teste`;
  - `output`: nome do mp4 final (ex.: `gf-curto-v3.mp4`);
  - `explainer_args` (só Prime Win): argumentos do explainer_primewin.py.
- Depois: `git add`, `git commit`, `git push` para `main`. O push dispara o render automaticamente.
- Resultado no branch `media`: `<pasta>/<nome>.mp4` (+ `<nome>-capa.jpg` quando houver capa).
- Se falhar: `<pasta>/<nome>.erro.txt` com as últimas linhas do erro. Nesse caso, a tarefa anota a falha no resumo e não agenda o post.
- Polling: a tarefa consulta o branch `media` até o mp4 ou o erro aparecer (checar a cada ~1 min, no máximo ~15 min).
- Link para o Metricool: `https://raw.githubusercontent.com/traderdaylle-videos/V-deos-/media/<pasta>/<nome>.mp4`.
- Limpeza: o workflow apaga os arquivos com data de mais de 3 dias e remove o `.erro.txt` quando o mp4 sai.
- Testes validados em 08/10/2026: `teste-gf-curto` (motor gf), `teste-primewin` (motor video com explainer), `teste-ranking` (motor ranking). Os specs de teste ficam em `pipeline/fila/teste-*.json`; cada push que os altere gera novo render.
- Dependências do runner: ffmpeg, fontes DejaVu, matplotlib, numpy, scipy, pillow, kokoro-onnx, soundfile, piper-tts (instaladas pelo workflow).
- Duração do gf (curto): a faixa é 45–70 s; se o roteiro ficar curto, o render falha com "fora da faixa" e o roteiro precisa ser ampliado.
- **Falhas técnicas (08/10/2026, pedido do usuário):** as tarefas corrigem sozinhas problemas do pipeline (repositório, workflow, spec, branch media) sem pedir permissão, registram a correção no log e refazem. Se não conseguirem resolver, avisam com PushNotification em menos de 200 caracteres.
- **YouTube:** se o Short ou o vídeo longo do YouTube não ficar agendado, a tarefa Grana avisa com PushNotification com a causa exata.
- **Correções de 10/10/2026 (causas reais das falhas da Grana):**
  - As tarefas agendadas precisam chamar **sempre** `add_repo traderdaylle-videos/V-deos-` (push) + `register_repo_root`, mesmo que a pasta exista; sem isso o push dá 403.
  - O GitHub recusa arquivos acima de 100 MB: o `make_gf_cine.py` agora limita o bitrate (mp4 ≤ ~85 MB) e o `render.sh` falha com erro claro se passar de 95 MB.
  - Vídeo longo: roteiro de **900 a 1000 palavras** (745 palavras deram 216 s). Se ainda ficar curto, o motor alonga as pausas em vez de falhar.
  - Ao refazer um spec que deu erro, salvar com novo nome (`-v2`), porque o `.erro.txt` antigo engana a espera.
  - Disparo manual do workflow exige o input `spec` (renderizar a fila toda estoura o tempo).
