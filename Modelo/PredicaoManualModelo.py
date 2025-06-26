import joblib

model = joblib.load('modelo/modelo_sentimento.joblib')
vectorizer = joblib.load('modelo/vectorizer.joblib')
label_map = joblib.load('modelo/label_map.joblib')

def prever_sentimento(texto):
    X = vectorizer.transform([texto])
    pred_idx = model.predict(X)[0]
    sentimento_previsto = [k for k, v in label_map.items() if v == pred_idx][0]
    return sentimento_previsto

testes = [
    "Comprei um Gift Card e depois de horas ainda nada. O site promete entregar o Gift Card em no máximo 1 horas. Já se passaram umas 10h e nada. Não atendem o telefone e não me deixam cancelar a compra.",
    "Péssimo atendimento, não recomendo a loja.",
    "O produto é ok, nada demais.",
    "Demorou muito para entregar, fiquei frustrado.",
    "Ótima experiência de compra, super satisfeito!",
    "Não gostei, veio com defeito e ninguém resolveu.",
    "Tive uma experiência horrível com meu pedido online,fiz o pedido e optei por retirar na loja e mesmo assim me cobrou o frete sff",
    "loja super confiável, fiz uma compra de um TV Philco, o mesmo após um tempo apresentou um defeito na garantia extendida, levei em uma empresa credenciada que a condenou, fui na loja e prontamente resolveram o problema, super indico, obrigado",
    "Loja super apertada, me deixou caustrofobico, porém seus produtos são de qualidade, nada a reclamar."
]

for texto in testes:
    sentimento = prever_sentimento(texto)
    print(f"Comentário: {texto}\nSentimento previsto: {sentimento}\n")