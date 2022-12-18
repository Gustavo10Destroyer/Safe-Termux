#!/data/data/com.termux/files/usr/bin/python3
from hashlib import sha256
from keypad import PasswordResult

amarelo = '\x1b[1;33m'
vermelho = '\x1b[1;31m'
fim = '\x1b[0m'

def check(resultado: PasswordResult) -> bool:
    senha_digitada = resultado.password # type: str
    senha_digitada = senha_digitada.encode('utf-8')
    hash_digitada = sha256(senha_digitada).hexdigest()

    arquivo = open('/data/data/com.termux/files/home/.bloqueio/kp', 'r')
    hash_arquivo = arquivo.read()
    arquivo.close()

    return hash_digitada == hash_arquivo