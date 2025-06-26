import random
import requests

API_URL = "https://localhost:7214/avaliacoes"

positivas = [
    "Atendimento excepcional, super recomendo!",
    "Entrega foi rápida e eficiente.",
    "Experiência maravilhosa, voltarei a comprar.",
    "Tudo saiu melhor do que eu esperava.",
    "Produto excelente, super satisfeito.",
    "Recebi antes do prazo, muito bom.",
    "Qualidade surpreendente, parabéns à equipe.",
    "Produto igual ao anunciado, perfeito.",
    "Equipe muito atenciosa e prestativa.",
    "Compra fácil e sem complicações.",
    "Fui muito bem atendido, nota máxima.",
    "Superou todas as minhas expectativas.",
    "Produto chegou em perfeito estado.",
    "Recomendo para todos, serviço impecável.",
    "Muito feliz com a compra realizada.",
    "A loja foi muito transparente em tudo.",
    "Recebi brindes junto com o pedido, adorei.",
    "A embalagem veio super protegida.",
    "Tudo funcionou perfeitamente do início ao fim.",
    "Voltarei a comprar com certeza.",
    "O suporte foi rápido e resolveu tudo.",
    "Me surpreendi positivamente com a qualidade.",
    "A entrega foi feita antes do combinado.",
    "Produto veio lacrado e novo.",
    "A experiência de compra foi excelente.",
    "Fácil de comprar e pagar.",
    "O site é muito intuitivo.",
    "Recebi todas as informações por e-mail.",
    "O produto é melhor do que imaginei.",
    "A loja está de parabéns pelo atendimento."
]

negativas = [
    "Péssimo atendimento, não recomendo.",
    "Demorou muito para chegar.",
    "Recebi o produto errado.",
    "Veio com defeito, fiquei insatisfeito.",
    "Não resolveram meu problema.",
    "Produto de qualidade ruim.",
    "Atendimento deixou a desejar.",
    "Muito caro para o que oferece.",
    "Produto veio usado e danificado.",
    "Não gostei da experiência.",
    "Faltou peça no meu pedido.",
    "O suporte não respondeu minhas dúvidas.",
    "A embalagem chegou rasgada.",
    "Tive dor de cabeça com a compra.",
    "Não cumpriram o prazo de entrega.",
    "O produto não corresponde à descrição.",
    "Me senti enganado pela loja.",
    "Não recomendo para ninguém.",
    "A devolução foi complicada.",
    "Não consegui contato com o suporte.",
    "O site é confuso e difícil de usar.",
    "Tive problemas para finalizar a compra.",
    "O produto veio com cheiro estranho.",
    "A loja não foi transparente.",
    "Não recebi nota fiscal.",
    "O rastreio não funcionou.",
    "O produto parou de funcionar rápido.",
    "A caixa veio aberta.",
    "Não tive retorno sobre minha reclamação.",
    "Me arrependi da compra."
]

neutras = [
    "Compra ocorreu normalmente.",
    "Recebi o produto como esperado.",
    "Nada de diferente, tudo certo.",
    "Serviço dentro do padrão.",
    "Produto chegou no prazo.",
    "Sem problemas durante a compra.",
    "Tudo conforme anunciado.",
    "Atendeu ao que foi prometido.",
    "Nada a destacar, experiência comum.",
    "Recebi o que comprei.",
    "Processo de compra foi simples.",
    "Produto funciona como deveria.",
    "Não tive surpresas.",
    "Entrega foi feita normalmente.",
    "Tudo dentro do esperado.",
    "Nada de especial a comentar.",
    "Compra sem complicações.",
    "Recebi o produto sem danos.",
    "O atendimento foi adequado.",
    "A loja cumpriu o combinado.",
    "O produto é o que imaginei.",
    "Não tive dificuldades.",
    "A experiência foi neutra.",
    "Nada me chamou atenção.",
    "Recebi o pedido corretamente.",
    "O site funcionou bem.",
    "A embalagem estava ok.",
    "O pagamento foi processado normalmente.",
    "Não houve atrasos.",
    "Tudo ocorreu como planejado."
]

todas = positivas + negativas + neutras

avaliacoes = []

for i in range(100):
    comentario = random.choice(todas)
    avaliacao = {
        "comentario": comentario,
        "sentimento": None
    }
    avaliacoes.append(avaliacao)

random.shuffle(avaliacoes)

for i, avaliacao in enumerate(avaliacoes):
    try:
        response = requests.post(API_URL, json=avaliacao, verify=False)
        print(f"[{i+1}/100] {avaliacao['comentario']} => Status {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar avaliação {i+1}: {e}")
