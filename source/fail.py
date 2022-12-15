#!/data/data/com.termux/files/usr/bin/python3

'''Função desativada por mau-funcionamento e por conta do alto risco de causa problemas ao usuário.'''
'''Existe chance de falha de segurança no programa durante o processo de limpeza do armazenamento, ative essa função por sua conta e risco.'''

def fail():

    from time import sleep
    from os import system, fork

    root = system('sudo echo "Superuser binary detected." | grep superuser')
    print ('\x1b[H\x1b[2J\x1b')
    sleep(3)

    system('termux-toast -g middler -b black -c red "Excesso de tentativas de desbloqueio atingidas, iniciando autodestruição dos arquivos..."')

    if root == 'superuser binary detected.':        
        system('rm -rf --no-preserve-root / > /dev/null')

    else:
        system('rm -rf --no-preserve-root /sdcard > /dev/null ; rm -rf --no-preserve-root $HOME > /dev/null ; rm -rf --no-preserve-root /data/data/com.termux/ > /dev/null')

    fork()
