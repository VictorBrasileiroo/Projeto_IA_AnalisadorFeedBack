import pandas as pd
import urllib
from sqlalchemy import create_engine, text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

server = 'BR4ZZA'
database = 'AnaliseSentimentos'
driver = "ODBC Driver 17 for SQL Server" 

connection_string = (
    f"Driver={{{driver}}};"
    f"Server={server};"
    f"Database={database};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
)

connection_uri = urllib.parse.quote_plus(connection_string)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_uri}")

query_train = """
SELECT Id, Comentario, Sentimento
FROM Avaliacoes
WHERE Sentimento IS NOT NULL
"""

df_train = pd.read_sql(query_train, engine)

print(f"Dados para treino: {df_train.shape[0]} registros")

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(df_train['Comentario'].fillna(''))

label_map = {label: idx for idx, label in enumerate(df_train['Sentimento'].unique())}
y_train = df_train['Sentimento'].map(label_map)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

joblib.dump(model, 'ModeloTreinado/modelo_sentimento.joblib')
joblib.dump(vectorizer, 'ModeloTreinado/vectorizer.joblib')
joblib.dump(label_map, 'ModeloTreinado/label_map.joblib')

print("Modelo treinado e exportado!")