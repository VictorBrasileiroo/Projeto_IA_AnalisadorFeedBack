import streamlit as st
import joblib

model = joblib.load("modelo/modelo_sentimento.joblib")
vectorizer = joblib.load("modelo/vectorizer.joblib")
label_map = joblib.load("modelo/label_map.joblib")
inv_label_map = {v: k for k, v in label_map.items()}

st.title("Analisador de Sentimentos de Avaliações")

comentario = st.text_area("Digite uma avaliação:")

if st.button("Analisar Sentimento"):
    if comentario.strip() == "":
        st.warning("Por favor, digite uma avaliação.")
    else:
        vetor = vectorizer.transform([comentario])
        pred = model.predict(vetor)[0]
        sentimento = inv_label_map[pred]
        st.success(f"Sentimento previsto: **{sentimento.upper()}**")
