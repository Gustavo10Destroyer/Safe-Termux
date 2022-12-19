#!/data/data/com.termux/files/usr/bin/python3
import os
import shutil

def uninstall() -> None:
    shutil.rmtree(os.path.expanduser('~/.bloqueio'), ignore_errors=True)

    if os.path.isfile(os.path.expanduser('~/.hushlogin')):
        os.remove(os.path.expanduser('~/.hushlogin'))

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "r")
    data = file.read().split("\n")
    file.close()

    for i in range(len(data), 0, -1):
        line = data[i - 1]

        if line.endswith('# Safe-Termux'):
            del data[i - 1]

    file = open("/data/data/com.termux/files/usr/etc/termux-login.sh", "w")
    file.write('\n'.join(data))
    file.close()

    os.system('chsh -s bash')

if __name__ == '__main__':
    print("[*] Desinstalando Safe-Termux...")
    uninstall()
    print("[*] Safe-Termux desinstalado com sucesso!")