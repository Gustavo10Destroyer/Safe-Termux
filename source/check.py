#!/data/data/com.termux/files/usr/bin/python3

def check(algoritmo, arquivo_nome):

    try:

        from json import loads
        from hashlib import sha256

        amarelo = '\033[1;33m'
        vermelho = '\033[1;31m'
        fim = '\033[m'

        if algoritmo == 1:

            arquivo = open('/data/data/com.termux/files/home/.bloqueio/.bio', 'r')
            arquivo_dados = arquivo.read()
            arquivo.close()

            if 'SUCCESS' in arquivo_dados:
                resultado = True

            elif 'FAILURE' in arquivo_dados:
                resultado = False

            elif 'UNKNOWN' in arquivo_dados:
                print(f'{amarelo}Aconteceu algum erro, mas foi detectado pelo sistema!{fim}')
                resultado = False

            else:
                print(f'{vermelho}Aconteceu algum erro desconhecido, que não foi detectado pelo sistema!{fim}')
                resultado = False

            return resultado

        if algoritmo == 2:

            arquivo = open(arquivo_nome)
            arquivo_dados = arquivo.read()
            arquivo_dados = loads(arquivo_dados)
            arquivo.close()

            arquivo = open('/data/data/com.termux/files/home/.bloqueio/.kp')
            arquivo_senha = arquivo.read()
            arquivo.close()

            arquivo_senha_digitada = arquivo_dados['text']
            arquivo_senha_digitada = sha256(arquivo_senha_digitada.encode('utf-8')).hexdigest()

            if arquivo_senha_digitada == arquivo_senha:
                resultado = True

            else:
                resultado = False

            return resultado

    except (KeyboardInterrupt):

        exit()
