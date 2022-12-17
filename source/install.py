#!/data/data/com.termux/files/usr/bin/python3

try:

    from os import system
    from time import sleep
    from hashlib import sha256

    ciano = '\033[1;36m'
    limpeza = '\x1b[H\x1b[2J\x1b'
    fim = '\033[m'

    system('apt update -y ; apt full-upgrade -y ; apt install fish termux-api -y ; python -m pip install --upgrade pip ; touch $HOME/.hushlogin ; mkdir $HOME/.bloqueio ; echo "$HOME/Safe-Termux/source/main.py" >> $HOME/.bashrc ; echo "exit" >> $HOME/.bashrc ; ln -s $HOME/.config/fish/config.fish $HOME/.fishrc')
    system('echo "python $HOME/Safe-Termux/source/main.py" >> $PREFIX/etc/termux-login.sh')

    print(f'{limpeza}{ciano}Copie suas configurações de ".bashrc" em ".fishrc" assim que possível.')
    sleep(5)

    print(f'{limpeza}{ciano}Digite a sua senha desejada!\nLembre-se que não é possível alterar sua senha depois.{fim}')
    senha = str (input ('Senha: '))

    senha = ((senha).encode('utf-8'))
    hash = sha256(senha).hexdigest()

    arquivo = open('/data/data/com.termux/files/home/.bloqueio/.kp', 'w')
    arquivo.write(hash)

    print(f'{limpeza}{ciano}Senha definida com sucesso!{fim}')

except (KeyboardInterrupt):

    exit()
