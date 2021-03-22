import smtplib
import ssl
import json
import os
import email.message
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent  # DIR app


def ler_arquivo(arquivo: str):
    # ler arquivo settings.json
    with open(os.path.join(BASE_DIR, arquivo), 'rb') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    # ler arquivo settings.json
    DATA = ler_arquivo('settings.json')
    DE = DATA['EMAIL']  # 'enviadordeemail99@gmail.com'
    PASSWORD = DATA['PASSWORD']  # 'freefire1'
    PARA = DATA['TO']  # "jhonathascesar232@gmail.com"

    msg = email.message.Message()

    MSG = f"""
    Helo Jhonathas 222222
    """
    context = ssl.create_default_context()
    # criado conexão com gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.ehlo()
        conexao.starttls(
            context=context
        )  # Criptohgrafa os dados
        conexao.login(DE, PASSWORD)
        conexao.sendmail(DE, PARA, MSG)
