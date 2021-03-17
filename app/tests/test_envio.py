import smtplib


def test_ehlo():
    '''
    Testa se a conexão foi ok
    '''
    conexao = smtplib.SMTP('smtp.gmail.com', 587)
    res = conexao.ehlo()
    assert res[0] in range(200, 299)
