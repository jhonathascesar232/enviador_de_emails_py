import smtplib
import json
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent  # DIR app


def ler_arquivo(arquivo: str):
    # ler arquivo settings.json
    with open(os.path.join(BASE_DIR, arquivo), 'rb') as file:
        data = json.load(file)
    return data


# ler arquivo settings.json
data = ler_arquivo('settings.json')

# criado conexão com gmail
conexao = smtplib.SMTP('smtp.gmail.com', 587)
conexao.starttls()  # Criptohgrafa os dados
res = conexao.login(
    user=data['EMAIL'],
    password=data['PASSWORD']
)
print(res)
