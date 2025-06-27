# 🧠 Analisador de Feedbacks
<img src="https://raw.githubusercontent.com/VictorBrasileiroo/AnalisadorFeedBack/main/banner.png" alt="Banner do Projeto Analisador de Feedbacks" style="width: 100%; max-width: 800px; height: auto;" />

![ASP.NET Core](https://img.shields.io/badge/ASP.NET%20Core-Minimal%20API-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-machine--learning-yellowgreen)
![SQL Server](https://img.shields.io/badge/SQL-Server-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-orange)

---

## 💡 Sobre o Projeto

Projeto para análise automática de sentimentos em avaliações de clientes usando Inteligência Artificial.  
Utiliza ASP.NET Core Minimal API para backend, Python para modelagem do classificador e SQL Server para armazenamento dos dados.  

Conta com um sistema inteligente que re-treina o modelo e atualiza os dados periodicamente. Também oferece uma interface simples para testes manuais.

---

## 🚀 Funcionalidades

- Classificação automática de sentimentos usando IA
- API desenvolvida com **ASP.NET Core Minimal API**
- Modelo de machine learning treinado em **Python** com **scikit-learn**
- Armazenamento dos dados com **SQL Server**
- Agendamento inteligente: reentreinamento periódico do modelo e atualização automática no banco
- Interface interativa com **Streamlit** para testes manuais da IA

## 🛠 Tecnologias Utilizadas

- **ASP.NET Core (Minimal API)**
- **Python 3.12**
  - `scikit-learn`
  - `pandas`
  - `joblib`
- **SQL Server**
- **Streamlit**
- **SQLAlchemy + pyodbc**
- **Joblib** (para salvar/carregar modelo)

---

## 🗂 Estrutura do Projeto

```bash
AnalisadorFeedbacks/
│
├── API/ # Projeto ASP.NET Core Minimal API
│ └── Controllers, Program.cs, etc.
│
├── Modelo/ # Scripts de treino e predição do modelo
│ ├── TreinamentoModelo.py
│ ├── PredicaoModelo.py
│ └── modelo_sentimento.joblib (gerado)
│
├── Interface/ # Interface com Streamlit
│ └── app.py
│
├── Dados/ # (Opcional) Dados usados no treinamento
│
├── README.md
```

---

## 📌 Execução do Projeto

```bash
#1. Rodar a API
cd API
dotnet run

#2. Rodar a Interface (Streamlit)
cd Interface
streamlit run app.py

#3. Executar Predição e Re-modelagem
cd Modelo
python PredicaoModelo.py
```

---

## 📅 Agendamento Inteligente
O sistema pode ser configurado para:

- Buscar periodicamente feedbacks com sentimentos nulos
- Predizer e atualizar esses dados no banco
- Re-treinar o modelo para mantê-lo atualizado

---

## ⚖️ Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

## 📧 Contato

Victor André Lopes Brasileiro - valb1@ic.ufal.br
