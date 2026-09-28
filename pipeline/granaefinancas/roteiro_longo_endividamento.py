import json
# (texto, pausa, clipe_opcional, offset)  — clipe muda quando informado
R = []
def s(t, p=0.4, clip=None, off=None, frac=None, luz=None): R.append(dict(t=t, p=p, clip=clip, off=off, frac=frac, luz=luz))

# ABERTURA
s("Oitenta e dois por cento das famílias brasileiras estão endividadas.", 0.7, "cidade-noite-aerea-42343.mp4", 3)
s("Um recorde.", 0.5, "avenida-noite-41161.mp4", 2)
s("A inflação voltou a subir. A conta de luz ficou mais de sete por cento mais cara em um único mês.", 0.4, "transito-timelapse-4240.mp4", 2)
s("E o salário... parece encolher a cada ano.", 0.8, "ampulheta-28901.mp4", 3, luz=0.07)
s("Então é fácil concluir: a culpa é do país.", 0.5, "transito-chuva-noite-4331.mp4", 1)
s("Do governo. Dos juros. Da crise.", 0.8, "raio-trovao-47948.mp4", 1)
s("Mas deixa eu te fazer uma pergunta desconfortável.", 0.5, "homem-banco-sozinho-25896.mp4", 5)
s("Se amanhã a inflação caísse pela metade... a sua vida financeira mudaria?", 0.6, "chuva-janela-2846.mp4", 2)
s("Ou você encontraria outro motivo para o dinheiro sumir?", 1.0, "homem-contando-dinheiro-ansioso-49438.mp4", 1)
s("Há dois mil anos, um grupo de filósofos já tinha a resposta.", 0.4, "teatro-romano-1759.mp4", 1)
s("Eles viveram guerras, pragas, impérios desabando. Alguns perderam tudo.", 0.4, "tempestade-noite-4422.mp4", 2)
s("E mesmo assim, deixaram um manual para viver com clareza em tempos difíceis.", 0.5, "corredor-colunas-estatuas-32893.mp4", 1)
s("Eles eram chamados de estoicos.", 0.7, "mapa-antigo-vela-21612.mp4", 2)
s("Neste vídeo, você vai aprender cinco princípios estoicos que mudam a forma como você lida com o dinheiro.", 0.4, "vela-acendendo-3461.mp4", 2, luz=0.07)
s("E o último é o que separa quem vive apertado de quem finalmente respira.", 1.1, "homem-sozinho-rio-35426.mp4", 2)
# 1 — DICOTOMIA DO CONTROLE
s("Princípio número um. A dicotomia do controle.", 0.8, "xadrez-pensando-49885.mp4", 1)
s("Epicteto nasceu escravo, no Império Romano.", 0.3, "teatro-romano-1759.mp4", 1)
s("Não tinha liberdade, não tinha dinheiro, não tinha nada.", 0.4, "trilhos-inverno-31942.mp4", 2)
s("E foi ele quem ensinou: algumas coisas dependem de nós. Outras, não.", 0.9, "teatro-romano-1759.mp4", 6)
s("Você não controla a inflação. Não controla os juros. Não controla o preço da gasolina.", 0.4, "transito-timelapse-4240.mp4", 8)
s("Mas controla o que acontece entre o salário cair na conta e o último real ir embora.", 0.6, "dinheiro-transacao-18247.mp4", 1)
s("Controla o que você compra. Quando compra. E por que compra.", 0.7, "cartao-compra-online-14009.mp4", 1)
s("O erro da maioria é gastar toda a energia reclamando do que não pode mudar...", 0.3, "homem-estressado-49225.mp4", 1)
s("e nenhuma energia no que pode.", 0.8)
s("O exercício é simples: pegue uma folha e divida em duas colunas.", 0.3, "homem-escrevendo-46768.mp4", 1)
s("De um lado, o que você não controla. Do outro, o que você controla.", 0.4, "insonia-escrevendo-16139.mp4", 1)
s("E a partir de hoje, toda a sua atenção vai para a segunda coluna.", 1.1, "xadrez-madeira-49721.mp4", 1)
# 2 — O DESEJO
s("Princípio número dois. O desejo que nunca termina.", 0.8, "fumaca-50951.mp4", 2)
s("Sêneca foi um dos homens mais ricos de Roma.", 0.3, "teatro-romano-1759.mp4", 5)
s("E justamente por isso, ele sabia do que estava falando quando escreveu:", 0.4, "fumaca-50951.mp4", 5)
s("não é pobre quem tem pouco. É pobre quem deseja mais.", 1.1, "vela-acendendo-3461.mp4", 8, luz=0.07)
s("Pense no último celular que você comprou.", 0.3, "olho-laptop-46575.mp4", 2, luz=0.12)
s("Lembra da empolgação? Quanto tempo ela durou?", 0.5, "mulheres-shopping-9060.mp4", 1)
s("Uma semana? Um mês?", 0.6)
s("A psicologia chama isso de adaptação hedônica.", 0.3, "numeros-oculos-47792.mp4", 1)
s("Tudo o que você conquista vira normal muito rápido. E o cérebro já começa a querer o próximo.", 0.5, "cidade-noite-aerea-42343.mp4", 12)
s("É uma esteira. Você corre, corre... e continua no mesmo lugar.", 0.4, "avenida-noite-41161.mp4", 8)
s("Só que agora, com uma fatura para pagar.", 1.0, "mulher-calculando-contas-49131.mp4", 2)
s("A saída estoica não é deixar de querer. É questionar o desejo antes de obedecer a ele.", 0.4, "homem-pensando-rio-15777.mp4", 1)
s("Antes de qualquer compra que não seja essencial, espere quarenta e oito horas.", 0.3, "relogio-parede-28886.mp4", 1)
s("Se depois de dois dias a vontade continuar, talvez ela seja real.", 0.3, "ampulheta-28901.mp4", 8, luz=0.07)
s("Mas na maioria das vezes... ela simplesmente desaparece.", 1.1, "fumaca-50951.mp4", 10)
# 3 — PREPARE-SE PARA O PIOR
s("Princípio número três. Imagine o pior.", 0.8, "nuvens-tempestade-9624.mp4", 2)
s("Parece pessimismo. Mas é exatamente o contrário.", 0.4, "ceu-nublado-9680.mp4", 1)
s("Os estoicos praticavam um exercício chamado premeditação dos males.", 0.3, "fonte-roma-11045.mp4", 10)
s("Eles imaginavam, com calma, o que poderia dar errado.", 0.3, "homem-estrada-35809.mp4", 1)
s("Não para sofrer antes da hora. Mas para nunca serem pegos de surpresa.", 0.8, "ondas-tempestade-45239.mp4", 3)
s("Agora faça isso com o seu dinheiro.", 0.3, "homem-banco-sozinho-25896.mp4", 1)
s("Se a sua renda parasse amanhã, quantos meses você aguentaria?", 0.9, "chuva-janela-2846.mp4", 10)
s("Para muita gente, a resposta é: nenhum.", 0.9, "homem-ansiedade-47206.mp4", 1)
s("É assim que um imprevisto vira dívida. E a dívida vira desespero.", 0.6, "casal-contas-problemas-48974.mp4", 2)
s("A reserva de emergência é a versão moderna desse exercício.", 0.3, "contando-dinheiro-23168.mp4", 1)
s("Comece pequeno. Um valor por mês, guardado num lugar que você não mexe.", 0.3, "maquina-contando-dinheiro-49134.mp4", 1)
s("Com o tempo, a meta é juntar o custo de três a seis meses da sua vida.", 0.4, "investidor-tablet-escritorio-45706.mp4", 1)
s("Não é sobre ficar rico. É sobre dormir em paz.", 1.1, "relaxando-por-do-sol-33968.mp4", 1)
# 4 — DESCONFORTO VOLUNTÁRIO
s("Princípio número quatro. Escolha o desconforto, antes que ele escolha você.", 0.8, "mulher-chuva-fria-46707.mp4", 2)
s("Sêneca recomendava separar alguns dias para viver com o mínimo.", 0.3, "ceu-nublado-9680.mp4", 3)
s("Comida simples. Roupa simples. Nada de luxo.", 0.4, "trilhos-inverno-31942.mp4", 9)
s("E durante esses dias, perguntar a si mesmo: era disso que eu tinha medo?", 1.1, "vela-acendendo-3461.mp4", 14, luz=0.07)
s("Faça o teste: escolha um dia por semana sem gastar nada além do essencial.", 0.3, "homem-escrevendo-46768.mp4", 6)
s("Sem delivery. Sem compra por impulso. Sem aquele cafezinho de dez reais.", 0.4, "cartao-compra-online-14009.mp4", 5)
s("Você vai descobrir duas coisas.", 0.5, "xadrez-pensando-49885.mp4", 7)
s("Primeiro: você precisa de muito menos do que imagina.", 0.4, "homem-sozinho-rio-35426.mp4", 6)
s("Segundo: muita compra não é necessidade. É fuga.", 0.5, "transito-chuva-noite-4331.mp4", 7)
s("Fuga do tédio. Da ansiedade. De um dia ruim.", 0.4, "homem-estressado-49225.mp4", 4)
s("Quando você percebe isso, o dinheiro para de mandar em você.", 1.1, "homem-pensando-rio-15777.mp4", 6)
# 5 — O HÁBITO
s("Princípio número cinco. E este é o mais importante.", 0.8, "tempestade-noite-4422.mp4", 9)
s("Você não é o que decide. Você é o que repete.", 0.8, "relogio-parede-28886.mp4", 5)
s("Epicteto ensinava que todo hábito é fortalecido pelas ações que o alimentam.", 0.3, "corredor-colunas-estatuas-32893.mp4", 3)
s("Cada compra por impulso fortalece o impulso.", 0.3, "mulheres-shopping-9060.mp4", 4)
s("Cada real guardado fortalece a disciplina.", 0.8, "contando-dinheiro-23168.mp4", 5)
s("Por isso, não conte com força de vontade. Ela acaba no fim do dia.", 0.4, "cansado-computador-14763.mp4", 1)
s("Pague-se primeiro.", 0.5, "dinheiro-transacao-18247.mp4", 8)
s("Assim que o salário cair, separe uma parte antes de pagar qualquer outra coisa.", 0.3, "investidor-tablet-escritorio-45706.mp4", 6)
s("Mesmo que seja pouco. O valor importa menos que o hábito.", 0.7, "xadrez-madeira-49721.mp4", 3)
s("E faça o que Sêneca fazia toda noite:", 0.3, "insonia-escrevendo-16139.mp4", 5)
s("antes de dormir, ele revisava o próprio dia. O que fez bem. Onde errou.", 0.4, "vela-acendendo-3461.mp4", 20, luz=0.07)
s("Faça isso com os seus gastos. Dois minutos, toda noite.", 0.3, "homem-escrevendo-46768.mp4", 9)
s("Você não vai se julgar. Vai se conhecer.", 1.1, "chuva-janela-2846.mp4", 16)
# CONCLUSÃO
s("O país pode estar difícil. E talvez continue difícil por muito tempo.", 0.5, "cidade-noite-aerea-42343.mp4", 20)
s("Mas os estoicos nos lembram de algo que nenhuma crise tira de você:", 0.4, "teatro-romano-1759.mp4", 3)
s("a capacidade de escolher como responder.", 1.0, "mapa-antigo-vela-21612.mp4", 9)
s("Então, antes da próxima compra, pare por um segundo e pergunte:", 0.4, "homem-sozinho-rio-35426.mp4", 10)
s("eu preciso disso... ou só quero me sentir melhor agora?", 1.2, "vela-acendendo-3461.mp4", 26, luz=0.07)
s("Essa pergunta, sozinha, pode valer mais do que qualquer aumento de salário.", 1.0, "homem-mar-tranquilo-26667.mp4", 2)
s("Se esse vídeo te fez pensar, se inscreva no canal Grana e Finanças.", 0.3, "maquina-contando-dinheiro-49134.mp4", 4)
s("E me conta nos comentários: qual desses cinco princípios você vai aplicar primeiro?", 0.5)
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
  {"seg": 0, "ate": 0, "linhas": [{"t": "82%", "estilo": "Num", "y": 430}, {"t": "das famílias brasileiras estão endividadas", "estilo": "Sub", "y": 650, "t0": 0.3}]},
  {"seg": find("Um recorde"), "ate": find("Um recorde"), "linhas": [{"t": "Recorde", "estilo": "Tit", "y": 520}]},
  {"seg": find("Mas deixa eu"), "ate": find("Mas deixa eu"), "linhas": [{"t": "A pergunta desconfortável", "estilo": "Tit", "y": 520}]},
  {"seg": find("Eles eram chamados"), "ate": find("Eles eram chamados"), "linhas": [{"t": "Os estoicos", "estilo": "Tit", "y": 520}]},
  {"seg": find("Neste vídeo"), "ate": find("Neste vídeo"), "linhas": [{"t": "5 PRINCÍPIOS ESTOICOS", "estilo": "Kick", "y": 520}]},
  cap(1, "A dicotomia do controle", "Princípio número um"),
  cit("E foi ele quem ensinou", "“Algumas coisas dependem de nós.\nOutras, não.”", "EPICTETO"),
  {"seg": find("O exercício é simples"), "ate": find("E a partir de hoje"), "linhas": [
     {"t": "NÃO CONTROLO", "estilo": "Kick", "x": 620, "y": 380}, {"t": "CONTROLO", "estilo": "Kick", "x": 1300, "y": 380, "t0": 0.4},
     {"t": "Inflação\nJuros\nGasolina", "estilo": "Sub", "x": 620, "y": 530, "t0": 2.0},
     {"t": "O que compro\nQuando compro\nPor que compro", "estilo": "Sub", "x": 1300, "y": 530, "t0": 4.0}]},
  cap(2, "O desejo que nunca termina", "Princípio número dois"),
  cit("não é pobre quem tem pouco", "“Não é pobre quem tem pouco.\nÉ pobre quem deseja mais.”", "SÊNECA"),
  {"seg": find("A psicologia chama"), "ate": find("Tudo o que você conquista"), "linhas": [{"t": "Adaptação hedônica", "estilo": "Tit", "y": 520}]},
  {"seg": find("Antes de qualquer compra"), "ate": find("Mas na maioria"), "linhas": [{"t": "REGRA DAS", "estilo": "Kick", "y": 380}, {"t": "48 horas", "estilo": "Tit", "y": 500, "t0": 0.2}]},
  cap(3, "Imagine o pior", "Princípio número três"),
  {"seg": find("Os estoicos praticavam"), "ate": find("Os estoicos praticavam"), "linhas": [{"t": "Premeditação dos males", "estilo": "Tit", "y": 520}]},
  {"seg": find("Se a sua renda parasse"), "ate": find("Para muita gente"), "linhas": [{"t": "Quantos meses\nvocê aguentaria?", "estilo": "Tit", "y": 500}]},
  {"seg": find("Com o tempo, a meta"), "ate": find("Com o tempo, a meta"), "linhas": [{"t": "RESERVA DE EMERGÊNCIA", "estilo": "Kick", "y": 380}, {"t": "3 a 6 meses", "estilo": "Tit", "y": 500, "t0": 0.2}]},
  {"seg": find("Não é sobre ficar rico"), "ate": find("Não é sobre ficar rico"), "linhas": [{"t": "Dormir em paz", "estilo": "Tit", "y": 520}]},
  cap(4, "O desconforto voluntário", "Princípio número quatro"),
  cit("E durante esses dias", "“Era disso que eu tinha medo?”", "SÊNECA"),
  {"seg": find("Faça o teste"), "ate": find("Sem delivery"), "linhas": [{"t": "1 DIA POR SEMANA", "estilo": "Kick", "y": 380}, {"t": "Gasto zero", "estilo": "Tit", "y": 500, "t0": 0.2}]},
  {"seg": find("Segundo: muita compra"), "ate": find("Fuga do tédio"), "linhas": [{"t": "Não é necessidade.\nÉ fuga.", "estilo": "Tit", "y": 500}]},
  cap(5, "O hábito", "Princípio número cinco"),
  {"seg": find("Você não é o que decide"), "ate": find("Você não é o que decide"), "linhas": [{"t": "Você é o que repete", "estilo": "Tit", "y": 520}]},
  {"seg": find("Pague-se primeiro"), "ate": find("Mesmo que seja pouco"), "linhas": [{"t": "Pague-se primeiro", "estilo": "Tit", "y": 520}]},
  {"seg": find("antes de dormir"), "ate": find("Você não vai se julgar"), "linhas": [{"t": "REVISÃO NOTURNA", "estilo": "Kick", "y": 380}, {"t": "2 minutos", "estilo": "Tit", "y": 500, "t0": 0.2}]},
  {"seg": find("a capacidade de escolher"), "ate": find("a capacidade de escolher"), "linhas": [{"t": "Escolher como responder", "estilo": "Tit", "y": 520}]},
  {"seg": find("eu preciso disso"), "ate": find("Essa pergunta"), "linhas": [{"t": "“Eu preciso disso…\nou só quero me sentir melhor agora?”", "estilo": "Sub", "y": 500}]},
  {"seg": find("Se esse vídeo"), "ate": len(R) - 1, "linhas": [{"t": "Inscreva-se", "estilo": "Tit", "y": 420}, {"t": "Grana e Finanças", "estilo": "Handle", "y": 600, "t0": 0.6},
     {"t": "Qual princípio você vai aplicar primeiro?", "estilo": "Sub", "y": 740, "t0": 3.0}]},
]
imp = [0, find("Mas deixa eu"), find("Eles eram chamados"), find("Princípio número um"), find("Princípio número dois"),
       find("Princípio número três"), find("Princípio número quatro"), find("Princípio número cinco"), find("a capacidade de escolher")]
spec = {"formato": "16:9", "segs": [[r["t"], r["p"]] for r in R], "target": [300, 600],
        "voice": {"length_scale": 1.0, "noise_scale": 0.72, "noise_w": 0.9, "pitch_semitons": -1.5},
        "clips": clips, "overlays": overlays, "impactos_seg": imp,
        "keywords_gold": ["82%", "OITENTA E DOIS", "ESTOICOS", "EPICTETO", "SÊNECA", "CONTROLA", "PRINCÍPIO", "DESEJA MAIS",
                          "QUARENTA E OITO HORAS", "RESERVA DE EMERGÊNCIA", "HÁBITO", "PAGUE-SE PRIMEIRO", "REPETE", "FUGA",
                          "DORMIR EM PAZ", "GRANA E FINANÇAS", "PRECISO"],
        "output": "gf-longo-endividamento.mp4"}
json.dump(spec, open("spec.json", "w"), ensure_ascii=False, indent=1)
words = sum(len(r["t"].split()) for r in R)
print("frases", len(R), "palavras", words, "clipes", len(clips))
