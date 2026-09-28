import json
# (texto, pausa, clipe_opcional, offset)  — clipe muda quando informado
R = []
def s(t, p=0.4, clip=None, off=None, frac=None, luz=None): R.append(dict(t=t, p=p, clip=clip, off=off, frac=frac, luz=luz))

# ABERTURA
s("Seus mil reais parados viram novecentos e cinquenta e dois em um ano.", 0.7, "contando-dinheiro-23168.mp4", 1)
s("Ninguém tirou nada da sua conta.", 0.4, "cidade-noite-aerea-42343.mp4", 3)
s("O número continua lá. Mil reais.", 0.4, "dinheiro-transacao-18247.mp4", 1)
s("Mas ele compra menos. Todo mês, um pouco menos.", 0.8, "ampulheta-28901.mp4", 3, luz=0.07)
s("Nesta semana, o mercado revisou a previsão de inflação para dois mil e vinte e seis: quatro vírgula noventa e nove por cento.", 0.5, "grafico-tempo-real-47018.mp4", 1)
s("E a maioria das pessoas nem percebeu.", 0.8, "avenida-noite-41161.mp4", 2)
s("Porque a inflação não faz barulho. Ela não chega com uma fatura.", 0.4, "transito-chuva-noite-4331.mp4", 1)
s("Ela trabalha em silêncio. Enquanto você dorme tranquilo, achando que está seguro.", 0.9, "relaxando-por-do-sol-33968.mp4", 2)
s("Então deixa eu te fazer uma pergunta desconfortável.", 0.5, "homem-banco-sozinho-25896.mp4", 5)
s("O seu dinheiro está parado... ou está sendo esquecido?", 1.0, "homem-pensando-rio-15777.mp4", 6)
s("Há dois mil anos, um grupo de filósofos já pensava sobre isso. Não sobre inflação. Sobre algo maior.", 0.4, "teatro-romano-1759.mp4", 1)
s("Sobre o tempo. E sobre o que ele faz com tudo o que a gente deixa parado.", 0.5, "corredor-colunas-estatuas-32893.mp4", 1)
s("Eles eram chamados de estoicos.", 0.7, "mapa-antigo-vela-21612.mp4", 2)
s("Neste vídeo, você vai aprender três princípios estoicos para parar de perder dinheiro sem perceber.", 0.4, "vela-acendendo-3461.mp4", 2, luz=0.07)
s("E o último é o que mais dói. Porque ele fala de você.", 1.1, "homem-sozinho-rio-35426.mp4", 2)
# 1 — O TEMPO
s("Princípio número um. O único bem que é seu.", 0.8, "relogio-parede-28886.mp4", 1)
s("Sêneca escreveu a um amigo que quase nada é realmente nosso. Só o tempo.", 0.5, "insonia-escrevendo-16139.mp4", 1)
s("E que a maioria de nós deixa esse tempo escapar sem perceber.", 0.9, "fumaca-50951.mp4", 2)
s("Com o dinheiro acontece o mesmo.", 0.4, "maquina-contando-dinheiro-49134.mp4", 1)
s("Todo real que você tem está mergulhado no tempo. E o tempo nunca fica parado.", 0.5, "relogio-parede-28886.mp4", 6)
s("Com quatro vírgula noventa e nove por cento de inflação, mil reais esquecidos perdem uns quarenta e oito reais de poder de compra em um ano.", 0.5, "mulher-calculando-contas-49131.mp4", 2)
s("Em cinco anos, a conta fica bem pior.", 0.9, "numeros-oculos-47792.mp4", 1)
s("O problema não é o dinheiro. É o dinheiro sem destino.", 0.9, "homem-contando-dinheiro-ansioso-49438.mp4", 1)
s("O exercício é simples: abra o seu extrato hoje.", 0.3, "homem-escrevendo-46768.mp4", 1)
s("Olhe para cada valor parado e pergunte: esse dinheiro tem um destino?", 1.1, "olho-laptop-46575.mp4", 2, luz=0.12)
# 2 — TUDO MUDA
s("Princípio número dois. Nada fica como está.", 0.8, "nuvens-tempestade-9624.mp4", 2)
s("Marco Aurélio governava o maior império do mundo.", 0.3, "templo-luxor-47380.mp4", 1)
s("E mesmo assim, escrevia para si mesmo que o universo é transformação.", 0.4, "estatua-rochas-4063.mp4", 1)
s("Tudo muda. Os preços, os salários, as crises.", 0.9, "transito-timelapse-4240.mp4", 2)
s("Mas a nossa cabeça gosta de fingir que o dinheiro guardado é uma coisa fixa.", 0.4, "homem-banco-sozinho-25896.mp4", 8)
s("Que mil reais hoje são mil reais amanhã.", 0.8, "contando-dinheiro-23168.mp4", 5)
s("Não são.", 1.0, "vela-acendendo-3461.mp4", 8, luz=0.07)
s("A pergunta estoica é: se tudo muda, você está mudando junto?", 0.5, "homem-estrada-35809.mp4", 1)
s("Aprender como o dinheiro funciona é a sua forma de acompanhar a mudança, em vez de ser atropelado por ela.", 0.4, "homem-laptop-trabalhando-9756.mp4", 2)
s("Guardar é o primeiro passo. Proteger o que você guardou, pelo menos da inflação, é o segundo.", 0.5, "investidor-tablet-escritorio-45706.mp4", 1)
s("E é exatamente no segundo passo que a maioria para.", 1.1, "xadrez-pensando-49885.mp4", 1)
# 3 — PARE DE ADIAR
s("Princípio número três. Pare de adiar.", 0.8, "ondas-tempestade-45239.mp4", 3)
s("Sêneca dizia que, enquanto a gente adia, a vida passa.", 0.9, "chuva-janela-2846.mp4", 2)
s("Quantas vezes você disse: mês que vem eu organizo.", 0.5, "cansado-computador-14763.mp4", 1)
s("Quando o salário aumentar, eu começo.", 0.5, "homem-estressado-49225.mp4", 1)
s("Quando sobrar, eu cuido disso.", 0.9, "casal-contas-problemas-48974.mp4", 2)
s("Adiar também custa. E custa em silêncio, como a inflação.", 0.9, "fumaca-50951.mp4", 5)
s("Então comece pequeno. Hoje.", 0.4, "homem-escrevendo-46768.mp4", 6)
s("Separe o dinheiro que tem um destino do dinheiro que só está esquecido.", 0.4, "dinheiro-transacao-18247.mp4", 5)
s("E dê um trabalho a cada real.", 1.0, "xadrez-rei-49736.mp4", 1)
# CONCLUSÃO
s("Você não controla a inflação. Nem o que o mercado vai prever na semana que vem.", 0.5, "cidade-noite-aerea-42343.mp4", 20)
s("Mas os estoicos nos lembram de algo que nenhuma crise tira de você:", 0.4, "teatro-romano-1759.mp4", 3)
s("a escolha de não deixar o tempo trabalhar contra você.", 1.0, "mapa-antigo-vela-21612.mp4", 9)
s("Então hoje, antes de dormir, abra o extrato e faça a pergunta:", 0.4, "homem-sozinho-rio-35426.mp4", 10)
s("o que o meu dinheiro está fazendo por mim?", 1.2, "vela-acendendo-3461.mp4", 26, luz=0.07)
s("Se esse vídeo te fez pensar, se inscreva no canal Grana e Finanças.", 0.3, "maquina-contando-dinheiro-49134.mp4", 4)
s("E me conta nos comentários: qual desses três princípios você vai aplicar primeiro?", 0.5)
s("Nos vemos no próximo vídeo.", 0.3)

idx = {}
clips = []
for i, r in enumerate(R):
    if r["clip"]:
        c = {"seg": i, "src": r["clip"], "offset": r["off"] or 1}
        if r["luz"]: c["luz"] = r["luz"]
        clips.append(c)
# cortes extras no meio de frases longas (ritmo): troca para um 2º plano do mesmo clipe na metade
extra = []
for c_i, c in enumerate(clips):
    i = c["seg"]; nxt = clips[c_i + 1]["seg"] if c_i + 1 < len(clips) else len(R)
    if nxt - i >= 2:   # clipe cobre 2+ frases: corta na frase seguinte para outro trecho do mesmo clipe
        extra.append({"seg": i + 1, "src": c["src"], "offset": c["offset"] + 4, **({"luz": c["luz"]} if "luz" in c else {})})
clips = sorted(clips + extra, key=lambda c: (c["seg"], c.get("frac", 0)))

def find(prefix): return next(i for i, r in enumerate(R) if r["t"].startswith(prefix))
cap = lambda n, nome, pre: {"seg": find(pre), "ate": find(pre), "linhas": [
    {"t": f"PRINCÍPIO {n}", "estilo": "Kick", "y": 400}, {"t": nome, "estilo": "Tit", "y": 520, "t0": 0.25}]}
cit = lambda pre, txt, autor, ate=None: {"seg": find(pre), "ate": find(ate) if ate else find(pre), "linhas": [
    {"t": txt, "estilo": "Sub", "y": 470}, {"t": autor, "estilo": "Kick", "y": 600, "t0": 0.6}]}
overlays = [
  {"seg": 0, "ate": 0, "linhas": [{"t": "R$ 952", "estilo": "Num", "y": 430}, {"t": "é o que valem R$ 1.000 parados em um ano", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("Nesta semana"), "ate": find("Nesta semana"), "linhas": [{"t": "4,99%", "estilo": "Num", "y": 430}, {"t": "inflação prevista para 2026 (Boletim Focus)", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("Então deixa eu"), "ate": find("Então deixa eu"), "linhas": [{"t": "A pergunta desconfortável", "estilo": "Tit", "y": 520}]},
  {"seg": find("Eles eram chamados"), "ate": find("Eles eram chamados"), "linhas": [{"t": "Os estoicos", "estilo": "Tit", "y": 520}]},
  {"seg": find("Neste vídeo"), "ate": find("Neste vídeo"), "linhas": [{"t": "3 PRINCÍPIOS ESTOICOS", "estilo": "Kick", "y": 520}]},
  cap(1, "O único bem que é seu", "Princípio número um"),
  cit("Sêneca escreveu a um amigo", "Quase nada é nosso.\nSó o tempo.", "SÊNECA"),
  {"seg": find("Com quatro vírgula"), "ate": find("Em cinco anos"), "linhas": [{"t": "- R$ 48", "estilo": "Num", "y": 430}, {"t": "de poder de compra em 1 ano", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("O exercício é simples"), "ate": find("Olhe para cada"), "linhas": [{"t": "Esse dinheiro\ntem um destino?", "estilo": "Tit", "y": 500}]},
  cap(2, "Nada fica como está", "Princípio número dois"),
  cit("E mesmo assim, escrevia", "O universo é transformação.", "MARCO AURÉLIO"),
  {"seg": find("Não são."), "ate": find("Não são."), "linhas": [{"t": "Não são.", "estilo": "Tit", "y": 520}]},
  {"seg": find("Guardar é o primeiro"), "ate": find("E é exatamente"), "linhas": [{"t": "GUARDAR NÃO É PROTEGER", "estilo": "Kick", "y": 380}, {"t": "O segundo passo", "estilo": "Tit", "y": 500, "t0": 0.2}]},
  cap(3, "Pare de adiar", "Princípio número três"),
  cit("Sêneca dizia que", "Enquanto adiamos,\na vida passa.", "SÊNECA"),
  {"seg": find("Adiar também custa"), "ate": find("Adiar também custa"), "linhas": [{"t": "Adiar também custa", "estilo": "Tit", "y": 520}]},
  {"seg": find("E dê um trabalho"), "ate": find("E dê um trabalho"), "linhas": [{"t": "Dê um trabalho\na cada real", "estilo": "Tit", "y": 500}]},
  {"seg": find("a escolha de não deixar"), "ate": find("a escolha de não deixar"), "linhas": [{"t": "O tempo a seu favor", "estilo": "Tit", "y": 520}]},
  {"seg": find("o que o meu dinheiro"), "ate": find("o que o meu dinheiro"), "linhas": [{"t": "“O que o meu dinheiro\nestá fazendo por mim?”", "estilo": "Sub", "y": 500}]},
  {"seg": find("Se esse vídeo"), "ate": len(R) - 1, "linhas": [{"t": "Inscreva-se", "estilo": "Tit", "y": 420}, {"t": "Grana e Finanças", "estilo": "Handle", "y": 600, "t0": 0.6},
     {"t": "Qual princípio você vai aplicar primeiro?", "estilo": "Sub", "y": 740, "t0": 3.0}]},
]
imp = [0, find("Então deixa eu"), find("Eles eram chamados"), find("Princípio número um"), find("Princípio número dois"),
       find("Princípio número três"), find("a escolha de não deixar")]
spec = {"formato": "16:9", "segs": [[r["t"], r["p"]] for r in R], "target": [240, 330],
        "voice": {"length_scale": 1.0, "noise_scale": 0.72, "noise_w": 0.9, "pitch_semitons": -1.5},
        "clips": clips, "overlays": overlays, "impactos_seg": imp,
        "keywords_gold": ["MIL REAIS", "NOVECENTOS E CINQUENTA E DOIS", "QUATRO VÍRGULA NOVENTA E NOVE", "ESTOICOS", "SÊNECA", "MARCO AURÉLIO",
                          "TEMPO", "PRINCÍPIO", "DESTINO", "TRANSFORMAÇÃO", "ADIAR", "GRANA E FINANÇAS"],
        "output": "gf-longo-inflacao.mp4"}
json.dump(spec, open("spec.json", "w"), ensure_ascii=False, indent=1)
words = sum(len(r["t"].split()) for r in R)
print("frases", len(R), "palavras", words, "clipes", len(clips))
