import json
R = []
def s(t, p=0.4, clip=None, off=None, frac=None, luz=None): R.append(dict(t=t, p=p, clip=clip, off=off, frac=frac, luz=luz))

# ABERTURA
s("O dólar caiu hoje para cinco reais e dezessete centavos.", 0.6, "contando-dinheiro-23168.mp4", 1)
s("A Bolsa subiu um vírgula trinta e sete por cento e fechou setembro com alta de cinco por cento.", 0.5, "grafico-tempo-real-47018.mp4", 1)
s("Foi o melhor mês desde janeiro.", 0.6, "lucro-bolsa-47012.mp4", 1)
s("E o motivo não está aqui. Está a milhares de quilômetros daqui.", 0.8, "mn-bandeira-eua-tremulando-46901.mp4", 1)
s("Nos Estados Unidos, a inflação veio abaixo do que o mercado esperava.", 0.5, "mn-cidade-noite-aerea-42342.mp4", 2)
s("E um número divulgado lá mexe no preço do pão, da gasolina e do celular aqui.", 0.8, "mulheres-shopping-9060.mp4", 1)
s("Parece distante. Mas não é.", 0.9, "homem-pensando-rio-15777.mp4", 6)
s("Neste vídeo, você vai entender por que isso acontece, o que muda no seu bolso e o que fazer agora.", 0.5, "homem-laptop-trabalhando-9756.mp4", 2)
s("E no final, a parte mais importante: o que depende de você.", 1.0, "vela-acendendo-3461.mp4", 2, luz=0.07)
# 1 — O FATO
s("Primeiro, o fato.", 0.6, "relogio-parede-28886.mp4", 1)
s("O dólar comercial fechou em queda de zero vírgula oitenta e um por cento, a cinco reais e dezessete centavos.", 0.5, "dinheiro-transacao-18247.mp4", 1)
s("O Ibovespa terminou o dia em cento e oitenta e seis mil pontos.", 0.4, "tendencia-tela-9607.mp4", 1)
s("O gatilho foi o índice de inflação que o banco central americano mais acompanha.", 0.5, "grafico-closeup-47016.mp4", 1)
s("E ele veio mais fraco do que o previsto.", 0.8, "numeros-oculos-47792.mp4", 1)
# 2 — POR QUE ACONTECE
s("Agora, a parte que quase ninguém explica. Por que a inflação de lá muda o dólar daqui?", 0.8, "xadrez-pensando-49885.mp4", 1)
s("Pense no dinheiro do mundo como água. Ele corre para onde rende mais, com segurança.", 0.5, "ondas-tempestade-45239.mp4", 3)
s("Quando a inflação americana está alta, os juros de lá ficam altos.", 0.4, "mn-bandeira-eua-closeup-8764.mp4", 1)
s("E o investidor prefere deixar o dinheiro nos Estados Unidos, ganhando juros na moeda mais forte do planeta.", 0.6, "investidor-tablet-escritorio-45706.mp4", 1)
s("Quando essa inflação perde força, a pressão sobre os juros americanos diminui.", 0.4, "grafico-homem-analisando-47214.mp4", 1)
s("Aí parte desse dinheiro sai procurando retorno em outros lugares, como o Brasil, onde os juros são altos.", 0.5, "avenida-noite-41161.mp4", 2)
s("Esse dinheiro chega em dólar e é trocado por reais.", 0.4, "maquina-contando-dinheiro-49134.mp4", 1)
s("Mais gente vendendo dólar aqui dentro. E o preço do dólar cai.", 0.4, "dinheiro-transacao-18247.mp4", 6)
s("Parte desse dinheiro vai para a Bolsa. Por isso as ações sobem juntas.", 0.9, "lucro-bolsa-47012.mp4", 6)
# 3 — O QUE MUDA NO SEU BOLSO
s("Agora, o que isso muda na sua vida.", 0.6, "homem-cafe-88009.mp4", 1)
s("O Brasil compra muita coisa cotada em dólar.", 0.4, "transito-timelapse-4240.mp4", 2)
s("O trigo do pão e do macarrão. Peças de carro. Eletrônicos. E o petróleo, que vira gasolina e diesel.", 0.5, "mulher-calculando-contas-49131.mp4", 2)
s("Com o dólar mais barato, tudo isso custa menos para entrar no país.", 0.4, "cartao-compra-online-14009.mp4", 1)
s("Menos pressão nos preços significa menos pressão na inflação.", 0.4, "mulheres-shopping-9060.mp4", 6)
s("E inflação mais comportada dá ao Banco Central mais espaço para, no futuro, baixar os juros.", 0.4, "grafico-tempo-real-47018.mp4", 7)
s("Juros menores deixam o crédito mais barato: o financiamento, o empréstimo, a compra parcelada.", 0.6, "casal-contas-problemas-48974.mp4", 2)
s("É uma corrente. Começa num número nos Estados Unidos e termina no seu carrinho de supermercado.", 0.9, "cidade-noite-aerea-42343.mp4", 3)
s("Mas atenção. Um dia não é tendência.", 0.6, "nuvens-tempestade-9624.mp4", 2)
s("No mês inteiro de setembro, o dólar caiu só zero vírgula quinze por cento.", 0.4, "numeros-oculos-47792.mp4", 5)
s("O petróleo continua caro, acima de cem dólares o barril.", 0.4, "transito-chuva-noite-4331.mp4", 1)
s("E as eleições de domingo deixam o mercado mais nervoso do que o normal.", 0.9, "tempestade-noite-4422.mp4", 1)
# 4 — QUEM GANHA E QUEM PERDE
s("Então, quem ganha com o dólar mais barato?", 0.5, "xadrez-madeira-49721.mp4", 1)
s("Quem vai viajar para fora. Quem compra produto importado. E as empresas que dependem de peças de fora.", 0.5, "relaxando-por-do-sol-33968.mp4", 2)
s("E quem perde?", 0.5, "homem-pensativo-duvida-47495.mp4", 1)
s("Quem exporta, porque recebe em dólar e passa a ganhar menos reais em cada venda.", 0.4, "homem-analisando-graficos-17415.mp4", 1)
s("E quem guardou dinheiro em dólar vê esse valor encolher quando olha em reais.", 0.9, "contando-dinheiro-23168.mp4", 6)
# 5 — O QUE FAZER
s("E você? O que faz com o seu dinheiro agora?", 0.8, "homem-banco-sozinho-25896.mp4", 5)
s("Primeiro: não tente adivinhar o dólar. Nem os profissionais acertam o dia de amanhã.", 0.5, "jovem-trabalhando-computador-44072.mp4", 1)
s("Segundo: a sua reserva de emergência fica em reais, num lugar seguro e fácil de sacar. Reserva não é aposta.", 0.5, "investidor-tablet-45708.mp4", 1)
s("Terceiro: se você tem um gasto em dólar pela frente, como uma viagem, não espere o preço perfeito. Compre aos poucos, mês a mês.", 0.5, "homem-escrevendo-46768.mp4", 1)
s("Quarto: dívida cara vem antes de tudo. O juro do cartão pesa muito mais do que qualquer oscilação do dólar.", 0.5, "homem-estressado-49225.mp4", 1)
s("E quinto: não antecipe compras só porque o dólar caiu num dia.", 0.9, "homem-jogando-dinheiro-49133.mp4", 1)
# FECHAMENTO
s("Há quase dois mil anos, Epicteto ensinava que algumas coisas dependem de nós, e outras não.", 0.5, "corredor-colunas-estatuas-32893.mp4", 1)
s("O dólar não depende de você. A inflação americana também não.", 0.5, "mn-bandeira-eua-tremulando-46901.mp4", 6)
s("Mas o seu orçamento depende. A sua reserva depende. A sua dívida depende.", 0.6, "mulher-graficos-ipad-45662.mp4", 1)
s("Quem entende a corrente para de ser surpreendido por ela.", 0.9, "homem-estrada-35809.mp4", 1)
s("Então hoje, faça um teste simples: olhe as contas do mês e marque tudo o que sobe quando o dólar sobe.", 0.5, "olho-laptop-46575.mp4", 2, luz=0.12)
s("Esse é o pedaço do seu bolso que vive nos Estados Unidos.", 1.0, "homem-sozinho-rio-35426.mp4", 2)
s("Se esse vídeo te ajudou, se inscreva no canal Grana e Finanças.", 0.3, "maquina-contando-dinheiro-49134.mp4", 4)
s("E me conta nos comentários: onde o dólar pesa mais no seu bolso? No mercado, no combustível ou na viagem?", 0.5)
s("Nos vemos no próximo vídeo.", 0.3)

clips = []
for i, r in enumerate(R):
    if r["clip"]:
        c = {"seg": i, "src": r["clip"], "offset": r["off"] or 1}
        if r["luz"]: c["luz"] = r["luz"]
        clips.append(c)
extra = []
for c_i, c in enumerate(clips):
    i = c["seg"]; nxt = clips[c_i + 1]["seg"] if c_i + 1 < len(clips) else len(R)
    if nxt - i >= 2:
        extra.append({"seg": i + 1, "src": c["src"], "offset": c["offset"] + 4, **({"luz": c["luz"]} if "luz" in c else {})})
clips = sorted(clips + extra, key=lambda c: (c["seg"], c.get("frac", 0)))

def find(prefix): return next(i for i, r in enumerate(R) if r["t"].startswith(prefix))
cap = lambda kick, nome, pre: {"seg": find(pre), "ate": find(pre), "linhas": [
    {"t": kick, "estilo": "Kick", "y": 400}, {"t": nome, "estilo": "Tit", "y": 520, "t0": 0.25}]}
overlays = [
  {"seg": 0, "ate": 0, "linhas": [{"t": "R$ 5,17", "estilo": "Num", "y": 430}, {"t": "dólar comercial no fechamento de 30/09", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": 1, "ate": 2, "linhas": [{"t": "+5%", "estilo": "Num", "y": 430}, {"t": "Ibovespa em setembro, o melhor mês desde janeiro", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("Parece distante"), "ate": find("Parece distante"), "linhas": [{"t": "Parece distante.\nMas não é.", "estilo": "Tit", "y": 500}]},
  cap("CAPÍTULO 1", "O fato", "Primeiro, o fato"),
  {"seg": find("O dólar comercial"), "ate": find("O dólar comercial"), "linhas": [{"t": "-0,81%", "estilo": "Num", "y": 430}, {"t": "dólar a R$ 5,174 (InfoMoney)", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("O Ibovespa terminou"), "ate": find("O Ibovespa terminou"), "linhas": [{"t": "186.340", "estilo": "Num", "y": 430}, {"t": "pontos no Ibovespa (+1,37%)", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("O gatilho foi"), "ate": find("E ele veio mais fraco"), "linhas": [{"t": "PCE", "estilo": "Num", "y": 430}, {"t": "a inflação que o Fed mais acompanha\nveio abaixo do esperado", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  cap("CAPÍTULO 2", "Por que acontece", "Agora, a parte que quase"),
  {"seg": find("Pense no dinheiro"), "ate": find("Pense no dinheiro"), "linhas": [{"t": "O dinheiro corre\npara onde rende mais", "estilo": "Tit", "y": 500}]},
  {"seg": find("Mais gente vendendo"), "ate": find("Mais gente vendendo"), "linhas": [{"t": "Mais dólar à venda\n= dólar mais barato", "estilo": "Tit", "y": 500}]},
  cap("CAPÍTULO 3", "O que muda no seu bolso", "Agora, o que isso muda"),
  {"seg": find("O trigo do pão"), "ate": find("O trigo do pão"), "linhas": [{"t": "Trigo · peças · eletrônicos · petróleo", "estilo": "Sub", "y": 520}]},
  {"seg": find("É uma corrente"), "ate": find("É uma corrente"), "linhas": [{"t": "Dólar → preços → inflação\n→ juros → crédito → seu bolso", "estilo": "Sub", "y": 500}]},
  {"seg": find("Mas atenção"), "ate": find("Mas atenção"), "linhas": [{"t": "Um dia\nnão é tendência", "estilo": "Tit", "y": 500}]},
  {"seg": find("No mês inteiro"), "ate": find("No mês inteiro"), "linhas": [{"t": "-0,15%", "estilo": "Num", "y": 430}, {"t": "dólar no mês de setembro", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("O petróleo continua"), "ate": find("O petróleo continua"), "linhas": [{"t": "US$ 103", "estilo": "Num", "y": 430}, {"t": "o barril do petróleo Brent", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  cap("CAPÍTULO 4", "Quem ganha e quem perde", "Então, quem ganha"),
  cap("CAPÍTULO 5", "O que fazer agora", "E você? O que faz"),
  {"seg": find("Primeiro: não tente"), "ate": find("Primeiro: não tente"), "linhas": [{"t": "1. Não tente adivinhar o dólar", "estilo": "Sub", "y": 520}]},
  {"seg": find("Segundo: a sua reserva"), "ate": find("Segundo: a sua reserva"), "linhas": [{"t": "2. Reserva não é aposta", "estilo": "Sub", "y": 520}]},
  {"seg": find("Terceiro: se você"), "ate": find("Terceiro: se você"), "linhas": [{"t": "3. Gasto em dólar? Compre aos poucos", "estilo": "Sub", "y": 520}]},
  {"seg": find("Quarto: dívida cara"), "ate": find("Quarto: dívida cara"), "linhas": [{"t": "4. Dívida cara primeiro", "estilo": "Sub", "y": 520}]},
  {"seg": find("E quinto"), "ate": find("E quinto"), "linhas": [{"t": "5. Não antecipe compras", "estilo": "Sub", "y": 520}]},
  {"seg": find("Há quase dois mil"), "ate": find("Há quase dois mil"), "linhas": [{"t": "Algumas coisas dependem de nós.\nOutras não.", "estilo": "Sub", "y": 470}, {"t": "EPICTETO", "estilo": "Kick", "y": 600, "t0": 0.6}]},
  {"seg": find("Mas o seu orçamento"), "ate": find("Mas o seu orçamento"), "linhas": [{"t": "O que depende de você", "estilo": "Tit", "y": 520}]},
  {"seg": find("Esse é o pedaço"), "ate": find("Esse é o pedaço"), "linhas": [{"t": "“O que no meu bolso\nsobe com o dólar?”", "estilo": "Sub", "y": 500}]},
  {"seg": find("Se esse vídeo"), "ate": len(R) - 1, "linhas": [{"t": "Inscreva-se", "estilo": "Tit", "y": 420}, {"t": "Grana e Finanças", "estilo": "Handle", "y": 600, "t0": 0.6},
     {"t": "Onde o dólar pesa mais no seu bolso?", "estilo": "Sub", "y": 740, "t0": 3.0}]},
]
imp = [0, find("Parece distante"), find("Primeiro, o fato"), find("Agora, a parte que quase"), find("Agora, o que isso muda"),
       find("Mas atenção"), find("Então, quem ganha"), find("E você? O que faz"), find("Há quase dois mil")]
spec = {"formato": "16:9", "segs": [[r["t"], r["p"]] for r in R], "target": [240, 330],
        "voice": {"length_scale": 1.0, "noise_scale": 0.72, "noise_w": 0.9, "pitch_semitons": -1.5},
        "clips": clips, "overlays": overlays, "impactos_seg": imp, "music_seed": 7,
        "keywords_gold": ["CINCO REAIS E DEZESSETE", "CINCO POR CENTO", "ESTADOS UNIDOS", "INFLAÇÃO", "JUROS", "DÓLAR",
                          "CORRENTE", "TENDÊNCIA", "RESERVA", "EPICTETO", "DEPENDE", "GRANA E FINANÇAS"],
        "output": "gf-longo-dolar.mp4"}
json.dump(spec, open("spec.json", "w"), ensure_ascii=False, indent=1)
words = sum(len(r["t"].split()) for r in R)
print("frases", len(R), "palavras", words, "clipes", len(clips))
