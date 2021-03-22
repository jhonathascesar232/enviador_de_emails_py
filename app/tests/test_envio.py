import smtplib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # DIR app


def test_ehlo():
    '''
    Testa se a conexão foi ok
    '''
    # criado conexão com gmail
    conexao = smtplib.SMTP('smtp.gmail.com', 587)
    res = conexao.ehlo()
    assert res[0] in range(200, 299)


def test_protocolo_tls():
    '''
    Utilizado para seguranca de senhas
    '''
    from app.app.main import ler_arquivo

    data = ler_arquivo('settings.json')
    # criado conexão com gmail
    conexao = smtplib.SMTP('smtp.gmail.com', 587)
    # res = conexao.ehlo()  # teste da conexao
    conexao.starttls()  # Criptohgrafa os dados
    res = conexao.login(
        user=data['EMAIL'],
        password=data['PASSWORD']
    )
    print('RES-->', res)
    assert res[0] in range(200, 299)
