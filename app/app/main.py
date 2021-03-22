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
    PASSWORD = DATA['PASSWORD']  # 'freefire1'
    # extrutura da msg
    msg = email.message.Message()  # DICT com a extrutura da msg
    msg['Subject'] = 'Assunto da Mensagem'
    body = """
<h1>Ola, email.message.Message()</h1>
<p>
    Corpo da Mensagens
    </br>
    <link style:"border: 1px solid black; color: white; text-decoration: None; text-tranform: None">
        Click
    </link>
</p>
    """
    msg['From'] = DATA['EMAIL']
    msg['To'] = DATA['TO']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)  # code de da msg

    context = ssl.create_default_context()
    # criado conexão com gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.ehlo()
        conexao.starttls(
            context=context
        )  # Criptohgrafa os dados
        conexao.login(msg['From'], PASSWORD)
        conexao.sendmail(
            msg['From'],
            msg['To'],
            msg.as_string().encode('utf-8')
        )
