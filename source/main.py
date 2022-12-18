#!/data/data/com.termux/files/usr/bin/python3
import os
from fail import fail
from utils import parse
from padlock import padlock, Padlock

try:
    desbloqueio: bool = False

    for contador in range(1, 4):
        if contador == 1:
            desbloqueio: bool = padlock(Padlock.BIOMETRIC)
        else:
            desbloqueio: bool = padlock(Padlock.PASSWORD)

        if desbloqueio == True:
            break

    if desbloqueio == True:
        padlock(Padlock.UNLOCKED)

        caminho_bio = parse('$HOME/.bloqueio/bio')

        if os.path.isfile(caminho_bio):
            os.remove(caminho_bio)

        for i in range(1, 4):
            caminho_key = parse(f'$HOME/.bloqueio/key-{i}')

            if os.path.isfile(caminho_key):
                os.remove(caminho_key)

        os.system('cd $HOME ; bash')
    else:
        padlock(Padlock.FULL_LOCK)
        fail()
except KeyboardInterrupt:
    exit(1)