#!/data/data/com.termux/files/usr/bin/python3

from os import system
from hashlib import sha256

ciano = '\033[1;36m'
limpeza = '\x1b[H\x1b[2J\x1b'
fim = '\033[m'

system('mkdir $HOME/.bloqueio ; echo "$HOME/Safe-Termux/source/main.py" >> $HOME/.bashrc ; echo "exit" >> $HOME/.bashrc')

print(f'{limpeza}{ciano}Digite a sua senha desejada!\nLembre-se que não é possível alterar sua senha depois.{fim}')
senha = str (input ('Senha: '))

senha = sha256()
senha = senha.hexdigest()

arquivo = open('/data/data/com.termux/files/home/.bloqueio/.kp', 'w')
arquivo.write(senha)

print(f'{limpeza}{ciano}Senha definida com sucesso!{fim}')
