import os
import shutil
from utils import parse

def uninstall() -> None:
    shutil.rmtree(os.path.expanduser('~/.bloqueio'), ignore_errors=True)

    if os.path.isfile(os.path.expanduser('~/.hushlogin')):
        os.remove(os.path.expanduser('~/.hushlogin'))

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "r")
    data = file.read().split("\n")
    file.close()

    for i, line in enumerate(data):
        if line.endswith('# Safe-Termux'):
            data.pop(i)

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "w")
    file.write('\n'.join(data))
    file.close()

    os.system('chsh -s bash')

if __name__ == '__main__':
    print("[*] Desinstalando Safe-Termux...")
    uninstall()
    print("[*] Safe-Termux desinstalado com sucesso!")