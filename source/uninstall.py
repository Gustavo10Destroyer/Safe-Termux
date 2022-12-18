import os
import shutil

def uninstall() -> None:
    shutil.rmtree(os.path.expanduser('~/.bloqueio'))
    os.remove(os.path.expanduser('~/.hushlogin'))

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "r")
    data = file.read().splitlines()
    file.close()

    for i, line in enumerate(data):
        if line == "python $HOME/Safe-Termux/source/main.py":
            data.pop(i)

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "w")
    file.write('\r\n'.join(data))
    file.close()

    os.system('chsh -s bash')

if __name__ == '__main__':
    print("[*] Desinstalando Safe-Termux...")
    uninstall()
    print("[*] Safe-Termux desinstalado com sucesso!")