import streamlit as st
import joblib

# Carregar modelo e vetor
model = joblib.load("ModeloTreinado/modelo_sentimento.joblib")
vectorizer = joblib.load("ModeloTreinado/vectorizer.joblib")
label_map = joblib.load("ModeloTreinado/label_map.joblib")
inv_label_map = {v: k for k, v in label_map.items()}

# Título com emoji centralizado e espaçamento
st.markdown("""
    <div style='text-align: center; margin-top: 40px; margin-bottom: 10px;'>
        <h1 style='font-size: 2.8rem;'>🧠 Analisador de FeedBacks</h1>
        <p style='font-size: 1.2rem; color: #fff;'>Simule o envio de uma avaliação para prever o sentimento.</p>
    </div>
""", unsafe_allow_html=True)

with st.form("formulario_avaliacao"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    comentario = st.text_area("Comentário", height=120)
    enviado = st.form_submit_button("Enviar avaliação")

st.markdown("</div>", unsafe_allow_html=True)

if enviado:
    if comentario.strip() == "":
        st.warning("⚠️ Por favor, preencha o campo de comentário.")
    else:
        vetor = vectorizer.transform([comentario])
        pred = model.predict(vetor)[0]
        sentimento = inv_label_map[pred]

        # Cores e emojis por sentimento
        emojis = {"positivo": "😊", "negativo": "😠", "neutro": "😐"}
        cores = {"positivo": "#27ae60", "negativo": "#e74c3c", "neutro": "#7f8c8d"}
        explicacoes = {
            "positivo": "Esse comentário expressa uma opinião favorável, demonstrando satisfação ou aprovação com o serviço ou produto.",
            "negativo": "Esse comentário demonstra insatisfação ou crítica em relação à experiência com o serviço ou produto.",
            "neutro": "Esse comentário não expressa claramente uma opinião positiva ou negativa, mantendo um tom mais objetivo ou indiferente."
        }

        st.markdown(f"""
        <div style='
            padding: 1.5rem;
            border-radius: 10px;
            background: linear-gradient(90deg, {cores[sentimento]} 80%, #fff 100%);
            color: white;
            text-align: center;
            font-size: 1.7rem;
            font-weight: bold;
            margin-top: 30px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.4);
        '>
            {emojis[sentimento]} Sentimento previsto: <span style='letter-spacing:2px;'>{sentimento.upper()}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='
            margin-top: 15px;
            background-color: #f4f4f4;
            padding: 1rem;
            border-left: 6px solid {cores[sentimento]};
            border-radius: 5px;
            font-size: 1rem;
            color: #333;
        '>
            <strong>Interpretação:</strong> {explicacoes[sentimento]}
        </div>
        """, unsafe_allow_html=True)
