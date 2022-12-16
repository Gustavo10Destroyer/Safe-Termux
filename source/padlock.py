#!/data/data/com.termux/files/usr/bin/python3

'''Curiosidade, o cadeado visto em arte ASCII em nosso programa, é da marca Pado.'''

def padlock(status):

    try:

        from os import system
        from time import sleep

        from check import check

        verde = '\033[1;32m'
        ciano = '\033[1;36m'
        amarelo = '\033[1;33m'
        vermelho = '\033[1;31m'
        limpeza = '\x1b[H\x1b[2J\x1b'
        fim = '\033[m'

        if status == 0:

            print(f'{limpeza}{verde}Safe-Termux - Termux Desbloqueado!{fim}')
            print('')
            print(f'{verde}          vILLYs2q:{fim}')
            print(f'{verde}        sBq 77::rY1ZB{fim}')
            print(f'{verde}       IQ ..     i .B{fim}')
            print(f'{verde}       B i.       L 7B{fim}')
            print(f'{verde}      rB B        .B B{fim}')
            print(f'{verde}      jg B            {fim}')
            print(f'{verde}      sg B            {fim}')
            print(f'{verde}     .U:i.::iirr7r7rUYd{fim}')
            print(f'{verde}     .J7ii:::r7777v122I{fim}')
            print(f'{verde}     .Irr::.::i:ii7v115{fim}')
            print(f'{verde}     .U7i777r77v7JsIUUI{fim}')
            print(f'{verde}     .27ri.irvrJvirj2US{fim}')
            print(f'{verde}     .dUs7rvvvsj1s2Pgdg{fim}')
            print('')

            sleep(3)
    
        elif status == 1:

            print(f'{limpeza}{ciano}Safe-Termux - Bloqueio Biometrico!{fim}')
            print('')
            print(f'{ciano}          vILLYs2q:{fim}')
            print(f'{ciano}        sBq 77::rY1ZB{fim}')
            print(f'{ciano}       IQ ..     i .B{fim}')
            print(f'{ciano}       B i.       L 7B{fim}')
            print(f'{ciano}      rB B        .B B{fim}')
            print(f'{ciano}      jg B        .B B{fim}')
            print(f'{ciano}      sg B         B B{fim}')
            print(f'{ciano}     .U:i.::iirr7r7rUYd{fim}')
            print(f'{ciano}     .J7ii:::r7777v122I{fim}')
            print(f'{ciano}     .Irr::.::i:ii7v115{fim}')
            print(f'{ciano}     .U7i777r77v7JsIUUI{fim}')
            print(f'{ciano}     .27ri.irvrJvirj2US{fim}')
            print(f'{ciano}     .dUs7rvvvsj1s2Pgdg{fim}')
            print('')

            sleep(3)

            try:

                tentativa_anterior_bio = open('/data/data/com.termux/files/home/.bloqueio/.bio', 'r')
                tentativa_anterior_bio.close()

                resultado = False
                return resultado

            except:

                system('termux-fingerprint -t "Autenticação Biométrica" -d "Por favor, coloque sua digital no sensor:" | grep -n AUTH_RESULT > $HOME/.bloqueio/.bio')

                resultado = check(1, '/data/data/com.termux/files/home/.bloqueio/.bio')

                return resultado

        elif status == 2:

            print(f'{limpeza}{amarelo}Safe-Termux - Bloqueio de Senha!{fim}')
            print('')
            print(f'{amarelo}          vILLYs2q:{fim}')
            print(f'{amarelo}        sBq 77::rY1ZB{fim}')
            print(f'{amarelo}       IQ ..     i .B{fim}')
            print(f'{amarelo}       B i.       L 7B{fim}')
            print(f'{amarelo}      rB B        .B B{fim}')
            print(f'{amarelo}      jg B        .B B{fim}')
            print(f'{amarelo}      sg B         B B{fim}')
            print(f'{amarelo}     .U:i.::iirr7r7rUYd{fim}')
            print(f'{amarelo}     .J7ii:::r7777v122I{fim}')
            print(f'{amarelo}     .Irr::.::i:ii7v115{fim}')
            print(f'{amarelo}     .U7i777r77v7JsIUUI{fim}')
            print(f'{amarelo}     .27ri.irvrJvirj2US{fim}')
            print(f'{amarelo}     .dUs7rvvvsj1s2Pgdg{fim}')
            print('')

            sleep(3)

            tentativas = 3

            try:
                tentativas_anteriores = open('/data/data/com.termux/files/home/.bloqueio/.key-1', 'r')
                tentativas_anteriores.close()
                tentativas -= 1
            except:
                pass

            try:
                tentativas_anteriores = open('/data/data/com.termux/files/home/.bloqueio/.key-2', 'r')
                tentativas_anteriores.close()
                tentativas -= 1
            except:
                pass

            try:
                tentativas_anteriores = open('/data/data/com.termux/files/home/.bloqueio/.key-3', 'r')
                tentativas_anteriores.close()
                tentativas -= 1
            except:
                pass

            for contador in range (tentativas, 0, -1):

                if tentativas == 1:
                    system('termux-dialog -t "Por favor, digite a sua senha de usuário:" -i "Senha" -p > $HOME/.bloqueio/.key-1')
                    resultado = check(2, '/data/data/com.termux/files/home/.bloqueio/.key-1')

                elif tentativas == 2:
                    system('termux-dialog -t "Por favor, digite a sua senha de usuário:" -i "Senha" -p > $HOME/.bloqueio/.key-2')
                    resultado = check(2, '/data/data/com.termux/files/home/.bloqueio/.key-2')

                elif tentativas == 3:
                    system('termux-dialog -t "Por favor, digite a sua senha de usuário:" -i "Senha" -p > $HOME/.bloqueio/.key-3')
                    resultado = check(2, '/data/data/com.termux/files/home/.bloqueio/.key-3')

                tentativas -= 1

                if resultado == True:
                    return resultado

                else:
                    print (f'Tente novamente, você tem {tentativas} tentativas sobrando!')

            resultado = False
            return resultado
    
        elif status == 3:

            print(f'{limpeza}{vermelho}Safe-Termux - Bloqueio Total!{fim}')
            print('')
            print(f'{vermelho}          vILLYs2q:{fim}')
            print(f'{vermelho}        sBq 77::rY1ZB{fim}')
            print(f'{vermelho}       IQ ..     i .B{fim}')
            print(f'{vermelho}       B i.       L 7B{fim}')
            print(f'{vermelho}      rB B        .B B{fim}')
            print(f'{vermelho}      jg B        .B B{fim}')
            print(f'{vermelho}      sg B         B B{fim}')
            print(f'{vermelho}     .U:i.::iirr7r7rUYd{fim}')
            print(f'{vermelho}     .J7ii:::r7777v122I{fim}')
            print(f'{vermelho}     .Irr::.::i:ii7v115{fim}')
            print(f'{vermelho}     .U7i777r77v7JsIUUI{fim}')
            print(f'{vermelho}     .27ri.irvrJvirj2US{fim}')
            print(f'{vermelho}     .dUs7rvvvsj1s2Pgdg{fim}')
            print('')

            sleep(3)

    except (KeyboardInterrupt):

        exit()
