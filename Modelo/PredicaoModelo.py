import pandas as pd
from sqlalchemy import create_engine, text
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

import urllib
connection_uri = urllib.parse.quote_plus(connection_string)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_uri}")

model = joblib.load('ModeloTreinado/modelo_sentimento.joblib')
vectorizer = joblib.load('ModeloTreinado/vectorizer.joblib')
label_map = joblib.load('ModeloTreinado/label_map.joblib')
inv_label_map = {v: k for k, v in label_map.items()} 

query_null = """
SELECT Id, Comentario
FROM Avaliacoes
WHERE Sentimento IS NULL
"""

df_null = pd.read_sql(query_null, engine)

if df_null.empty:
    print("Nenhuma avaliação com sentimento nulo para predizer.")
else:
    X_test = vectorizer.transform(df_null['Comentario'].fillna(''))

    pred_indices = model.predict(X_test)
    pred_sentimentos = [inv_label_map[i] for i in pred_indices]

    update_query = text("""
        UPDATE Avaliacoes
        SET Sentimento = :sentimento
        WHERE Id = :id
    """)

    with engine.begin() as conn:
        for id_, sentimento in zip(df_null['Id'], pred_sentimentos):
            conn.execute(update_query, {"sentimento": sentimento, "id": id_})
            print(f"Id {id_} atualizado com sentimento: {sentimento}")

    print("Atualização concluída!")
