import smtplib


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
    # criado conexão com gmail
    conexao = smtplib.SMTP('smtp.gmail.com', 587)
    # res = conexao.ehlo()  # teste da conexao
    conexao.starttls()  # Criptohgrafa os dados
    res = conexao.login(user=EMAIL, password=PASSWORD)
    assert res[0] in range(200, 299)
