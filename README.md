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

## 💬 Como os modelos utilizados funcionam?
1. Pré-processamento dos Comentários: Utiliza o TfidfVectorizer para transformar os textos dos comentários em vetores numéricos, baseando-se na frequência e relevância das palavras no conjunto de dados.  
2. Treinamento Supervisionado: Um classificador Logistic Regression é treinado com dados previamente rotulados. Cada comentário possui um sentimento associado, permitindo que o modelo aprenda os padrões linguísticos de cada classe.
3. Mapeamento e Predição: Ao receber um novo comentário, ele passa pela mesma vetorização. O modelo então prevê a classe mais provável, retornando o sentimento correspondente ao texto inserido.
4. Atualização Automática: Comentários sem rótulo são identificados, classificados automaticamente pelo modelo, e têm seu sentimento atualizado diretamente no banco de dados. Além disso, o modelo pode ser re-treinado periodicamente com os novos dados, mantendo a IA sempre atualizada.

---

## 🗂 Estrutura do Projeto

```bash
AnalisadorFeedbacks/
│
├── API/
│ └── Program.cs, etc.
│
├── Modelo/
│ ├── TreinamentoModelo.py
│ ├── PredicaoModelo.py
│ └── modelo_sentimento.joblib
|  └── app.py 
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

## 📧 Contato

Victor André Lopes Brasileiro - valb1@ic.ufal.br
