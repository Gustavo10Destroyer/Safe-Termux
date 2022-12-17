#!/data/data/com.termux/files/usr/bin/python3

try:

    from os import system

    from fail import fail
    from padlock import padlock

    desbloqueio = False
    bypass = False

    for contador in range(1,4):

        if bypass == True:
            break

        desbloqueio = padlock(contador)

        if desbloqueio == True:
            bypass = True

    if desbloqueio == True:

        padlock(0)
        system('rm -f $HOME/.bloqueio/bio $HOME/.bloqueio/key-1 $HOME/.bloqueio/key-2 $HOME/.bloqueio/key-3 > /dev/null ; cd $HOME ; bash')

    else:

        fail()

except (KeyboardInterrupt):

    exit()
