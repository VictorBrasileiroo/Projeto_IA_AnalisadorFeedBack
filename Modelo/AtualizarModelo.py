import subprocess

print("Executando atualização de sentimentos...")
subprocess.run(["python", "PredicaoModelo.py"])

print("Re-treinando o modelo...")
subprocess.run(["python", "TreinamentoModelo.py"])

print("Processo completo!")