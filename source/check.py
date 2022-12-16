#!/data/data/com.termux/files/usr/bin/python3

def check(algoritmo, arquivo_nome):

    try:

        from time import sleep
        from json import loads
        from hashlib import sha256

        amarelo = '\033[1;33m'
        vermelho = '\033[1;31m'
        fim = '\033[m'

        if algoritmo == 1:

            arquivo = open(arquivo_nome, 'r')
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

            arquivo_digitado = open(arquivo_nome, 'r')
            arquivo_senha_digitada = arquivo_digitado.read()
            arquivo_senha_digitada = loads(arquivo_senha_digitada)
            arquivo_senha_digitada = arquivo_senha_digitada['text']
            arquivo_senha_digitada = ((arquivo_senha_digitada).encode('utf-8'))
            hash = sha256(arquivo_senha_digitada).hexdigest()
            arquivo_digitado.close()

            print (hash)
            print (arquivo_senha_digitada)
            sleep (8)

            arquivo = open('/data/data/com.termux/files/home/.bloqueio/.kp', 'r')

            print (arquivo.read())
            sleep (8)

            if arquivo_senha_digitada == arquivo.read():
                resultado = True
                arquivo.close()

            else:
                resultado = False
                arquivo.close()

            return resultado

    except (KeyboardInterrupt):

        exit()
