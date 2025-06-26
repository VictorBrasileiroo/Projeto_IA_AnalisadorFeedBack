import random
import requests

API_URL = "https://localhost:7214/avaliacoes"

positivas = [
    "Excelente atendimento, recomendo!",
    "Muito bom! Chegou rápido.",
    "Amei a experiência, nota 10!",
    "Tudo perfeito, melhor compra que já fiz!",
    "Ótimo serviço, continuem assim.",
    "Produto de ótima qualidade, estou satisfeito.",
    "Atendimento rápido e eficiente!",
    "Gostei muito da loja.",
    "Funcionários educados e prestativos.",
    "Entrega no prazo e produto impecável.",
    "Superou minhas expectativas, parabéns!",
    "Compra fácil e entrega rápida.",
    "Produto veio bem embalado.",
    "Recomendo para todos, excelente!",
    "Voltarei a comprar com certeza.",
    "Atendimento personalizado e atencioso.",
    "Tudo ocorreu perfeitamente.",
    "Fui muito bem atendido.",
    "Produto exatamente como anunciado.",
    "Serviço de qualidade, fiquei satisfeito.",
    "Entrega antes do prazo, adorei!",
    "Equipe muito competente.",
    "Fácil de comprar, site intuitivo.",
    "Recebi brindes, adorei o cuidado.",
    "Compra segura e tranquila.",
    "Produto novo e funcionando perfeitamente.",
    "Atendimento nota 10!",
    "Muito satisfeito com a experiência.",
    "Recomendo sem dúvidas.",
    "Tudo certo do início ao fim.",
    "Excelente custo-benefício.",
    "Produto chegou em perfeito estado.",
    "Empresa confiável, recomendo.",
    "Fui surpreendido positivamente.",
    "Ótima experiência de compra.",
    "Tudo saiu conforme o combinado.",
    "Atendimento diferenciado.",
    "Muito feliz com a compra.",
    "Produto de alta qualidade.",
    "Entrega super rápida.",
    "Loja organizada e limpa.",
    "Equipe prestativa e simpática.",
    "Compra rápida e eficiente.",
    "Produto melhor do que esperava.",
    "Serviço impecável.",
    "Atendimento cordial e eficiente.",
    "Recebi tudo certinho.",
    "Gostei do acompanhamento do pedido.",
    "Empresa séria e comprometida.",
    "Voltarei a comprar em breve."
]

negativas = [
    "Horrível, nunca mais compro aqui.",
    "Produto veio errado e demorou.",
    "Muito ruim, atendimento péssimo.",
    "Demorou demais, perdi a paciência.",
    "Veio quebrado, fiquei decepcionado.",
    "Não recomendo, péssima experiência.",
    "Comprei e não recebi até agora.",
    "Fui mal atendido, me ignoraram.",
    "Erro na entrega e ninguém resolve.",
    "Serviço lento e despreparado.",
    "Produto de baixa qualidade, não gostei.",
    "Atendimento deixou a desejar.",
    "Entrega atrasada, não cumpriram o prazo.",
    "Recebi o produto errado.",
    "Não solucionaram meu problema.",
    "Faltou item no pedido.",
    "Produto veio com defeito.",
    "Não consegui contato com o suporte.",
    "Muito caro pelo que oferece.",
    "Não recomendo para ninguém.",
    "Experiência frustrante.",
    "Me arrependi da compra.",
    "Site confuso, difícil de comprar.",
    "Não gostei do atendimento.",
    "Demoraram para responder.",
    "Produto não corresponde à descrição.",
    "Veio faltando peças.",
    "Não devolveram meu dinheiro.",
    "Tive que reclamar várias vezes.",
    "Não cumpriram o combinado.",
    "Péssima logística.",
    "Fui mal tratado pelo atendente.",
    "Não recomendo, perdi dinheiro.",
    "Produto veio usado.",
    "Não gostei da embalagem.",
    "Demorou para aprovar o pagamento.",
    "Não entregaram no endereço correto.",
    "Tive problemas com a garantia.",
    "Não resolveram meu caso.",
    "Atendimento robotizado, sem solução.",
    "Produto veio aberto.",
    "Não consegui cancelar a compra.",
    "Não gostei da experiência.",
    "Não recomendo, serviço ruim.",
    "Faltou atenção ao cliente.",
    "Não cumpriram o prazo de entrega.",
    "Produto chegou danificado.",
    "Não consegui trocar o produto.",
    "Atendimento demorado e ineficiente.",
    "Não gostei do serviço prestado."
]

neutras = [
    "Foi ok, nada de especial.",
    "Atendeu às expectativas, apenas isso.",
    "Sem problemas, mas também sem destaques.",
    "Compra normal, nada a reclamar.",
    "Tudo certo com o pedido.",
    "Razoável, como o esperado.",
    "Loja comum, serviço comum.",
    "Não tenho do que reclamar.",
    "Correu tudo normalmente.",
    "Achei normal, dentro do esperado.",
    "Nada surpreendente, mas funcionou.",
    "Recebi o produto, tudo certo.",
    "Entrega dentro do prazo, sem problemas.",
    "Serviço padrão, nada a destacar.",
    "Foi uma experiência comum.",
    "Produto como anunciado.",
    "Nada além do esperado.",
    "Tudo ocorreu como deveria.",
    "Sem atrasos, sem surpresas.",
    "Recebi o que comprei.",
    "Atendimento regular.",
    "Nada a acrescentar, tudo normal.",
    "Compra tranquila.",
    "Serviço aceitável.",
    "Produto chegou, tudo certo.",
    "Não tive problemas.",
    "Tudo conforme o combinado.",
    "Nada de ruim, nada de ótimo.",
    "Foi uma compra comum.",
    "Nada fora do padrão.",
    "Recebi normalmente.",
    "Sem destaques positivos ou negativos.",
    "Tudo dentro da normalidade.",
    "Nada a reclamar, nada a elogiar.",
    "Serviço dentro do esperado.",
    "Produto entregue normalmente.",
    "Compra sem intercorrências.",
    "Tudo ocorreu como planejado.",
    "Nada que chame atenção.",
    "Serviço neutro.",
    "Recebi o pedido normalmente.",
    "Atendimento dentro do padrão.",
    "Nada de especial a comentar.",
    "Tudo certo, como deveria ser.",
    "Compra sem emoções.",
    "Produto chegou como esperado.",
    "Serviço sem surpresas.",
    "Nada de diferente.",
    "Foi tudo como imaginei.",
    "Nenhum problema, nenhum destaque."
]

origens = ["Site", "App", "Loja Física"]

avaliacoes = []

for i in range(500):
    if i < 165:
        sentimento = "positivo"
        texto = random.choice(positivas)
    elif i < 330:
        sentimento = "negativo"
        texto = random.choice(negativas)
    else:
        sentimento = "neutro"
        texto = random.choice(neutras)

    avaliacao = {
    "comentario": texto,
    "sentimento": sentimento,
    }

    avaliacoes.append(avaliacao)

for i, avaliacao in enumerate(avaliacoes):
    try:
        response = requests.post(API_URL, json=avaliacao, verify=False)
        print(f"[{i+1}/500] {avaliacao['comentario']} => Status {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar avaliação {i+1}: {e}")