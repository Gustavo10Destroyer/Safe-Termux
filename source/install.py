#!/data/data/com.termux/files/usr/bin/python3
from os import system
from time import sleep
from hashlib import sha256
from getpass import getpass

ciano = '\x1b[1;36m'
limpeza = '\x1b[H\x1b[2J\x1b[3J'
fim = '\x1b[0m'

system('apt update -y ; apt full-upgrade -y ; apt install termux-api -y ; python -m pip install --upgrade pip ; touch $HOME/.hushlogin ; mkdir $HOME/.bloqueio ; echo -n "python $HOME/Safe-Termux/source/main.py # Safe-Termux\nexit # Safe-Termux\n" >> $PREFIX/etc/termux-login.sh ; echo "exit" > null.sh ; chmod +x null.sh ; mv null.sh $PREFIX/bin ; chsh -s $PREFIX/bin/null.sh')

print(f'{limpeza}{ciano}Digite a sua senha desejada!\nLembre-se que não é possível alterar sua senha depois.{fim}')
senha: str
tentativas: int = 0

while True:
    try:
        senha: str = getpass(f'{ciano}Senha: {fim}')
    except (EOFError, KeyboardInterrupt):
        print(f'{limpeza}{ciano}Você precisa definir uma senha!{fim}')
        continue

    if len(senha) < 8:
        print(f'{limpeza}{ciano}Sua senha deve conter no mínimo 8 caracteres!{fim}')
        continue

    break

while True:
    try:
        confirma_senha: str = getpass(f'{ciano}Confirme sua senha: {fim}')
    except (EOFError, KeyboardInterrupt):
        print(f'{limpeza}{ciano}Você precisa definir uma senha!{fim}')
        continue

    if senha == confirma_senha:
        break

    tentativas += 1
    print(f'{limpeza}{ciano}As senhas não coincidem!{fim}')

    if tentativas == 3:
        print(f'{limpeza}{ciano}Você atingiu o limite de tentativas!{fim}')
        senha: str = getpass(f'{ciano}Digite uma nova senha: {fim}')
        tentativas = 0

senha_hash = sha256(senha.encode("utf-8")).hexdigest()

arquivo = open('/data/data/com.termux/files/home/.bloqueio/kp', 'w')
arquivo.write(senha_hash)
arquivo.close()

print(f'{limpeza}{ciano}Senha definida com sucesso!{fim}')