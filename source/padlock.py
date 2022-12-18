#!/data/data/com.termux/files/usr/bin/python3

"""Curiosidade, o cadeado visto em arte ASCII em nosso programa, é da marca Pado."""

from os import path
from enum import Enum
from time import sleep
from check import check
from typing import Union
from utils import print_centered
from keypad import authenticate, Authenticator, BiometricResult, PasswordResult

verde = '\x1b[1;32m'
ciano = '\x1b[1;36m'
amarelo = '\x1b[1;33m'
vermelho = '\x1b[1;31m'
limpeza = '\x1b[H\x1b[2J\x1b[3J'
fim = '\x1b[0m'

class Padlock(Enum):
    '''Classe que define o tipo de bloqueio.'''
    UNLOCKED = 0
    BIOMETRIC = 1
    PASSWORD = 2
    FULL_LOCK = 3

def padlock(lock: Padlock) -> Union[None, bool]:
    try:
        if lock == Padlock.UNLOCKED:
            print(limpeza, end='')

            mensagem = f"""{verde}Safe-Termux - Termux Desbloqueado!{fim}\n
{verde}          vILLYs2q:{fim}    
{verde}        sBq 77::rY1ZB{fim}  
{verde}       IQ ..     i .B{fim}  
{verde}       B i.       L 7B{fim} 
{verde}      rB B        .B B{fim} 
{verde}      jg B            {fim} 
{verde}      sg B            {fim} 
{verde}     .U:i.::iirr7r7rUYd{fim}
{verde}     .J7ii:::r7777v122I{fim}
{verde}     .Irr::.::i:ii7v115{fim}
{verde}     .U7i777r77v7JsIUUI{fim}
{verde}     .27ri.irvrJvirj2US{fim}
{verde}     .dUs7rvvvsj1s2Pgdg{fim}"""

            print_centered(mensagem)
            sleep(3)

            return None
        elif lock == Padlock.BIOMETRIC:
            mensagem = f"""{ciano}Safe-Termux - Bloqueio Biometrico!{fim}\n
{ciano}          vILLYs2q:{fim}    
{ciano}        sBq 77::rY1ZB{fim}  
{ciano}       IQ ..     i .B{fim}  
{ciano}       B i.       L 7B{fim} 
{ciano}      rB B        .B B{fim} 
{ciano}      jg B        .B B{fim} 
{ciano}      sg B         B B{fim} 
{ciano}     .U:i.::iirr7r7rUYd{fim}
{ciano}     .J7ii:::r7777v122I{fim}
{ciano}     .Irr::.::i:ii7v115{fim}
{ciano}     .U7i777r77v7JsIUUI{fim}
{ciano}     .27ri.irvrJvirj2US{fim}
{ciano}     .dUs7rvvvsj1s2Pgdg{fim}"""

            print_centered(mensagem)
            sleep(3)

            result = authenticate(Authenticator.BIOMETRIC) # type: BiometricResult

            if result == BiometricResult.SUCCESS:
                return True # Autenticação bem sucedida
            elif result == BiometricResult.FAILURE:
                return False # Autenticação falhou
            elif result == BiometricResult.UNKNOWN:
                return False # Erro desconhecido
            elif result == BiometricResult.TIMEOUT:
                # Nessa parte aqui, eu recomendo continuar tentando até cair em um dos outros resultados
                return False # Tempo limite excedido
        elif lock == Padlock.PASSWORD:
            mensagem = f"""{amarelo}Safe-Termux - Bloqueio de Senha!{fim}\n
            {amarelo}          vILLYs2q:{fim}
            {amarelo}        sBq 77::rY1ZB{fim}
            {amarelo}       IQ ..     i .B{fim}
            {amarelo}       B i.       L 7B{fim}
            {amarelo}      rB B        .B B{fim}
            {amarelo}      jg B        .B B{fim}
            {amarelo}      sg B         B B{fim}
            {amarelo}     .U:i.::iirr7r7rUYd{fim}
            {amarelo}     .J7ii:::r7777v122I{fim}
            {amarelo}     .Irr::.::i:ii7v115{fim}
            {amarelo}     .U7i777r77v7JsIUUI{fim}
            {amarelo}     .27ri.irvrJvirj2US{fim}
            {amarelo}     .dUs7rvvvsj1s2Pgdg{fim}"""

            print_centered(mensagem)
            tentativas = 3

            for i in range(1, 4):
                if path.isfile(f'/data/data/com.termux/files/home/.bloqueio/key-{i}'):
                    tentativas -= 1

            print(f'Você tem direito a {tentativas} tentativas!')

            resultado: bool = False # O resultado padrão
            # Se a senha estiver correta, o valor será alterado para True

            for _ in range (tentativas, 0, -1):
                sleep(3)

                resultado: PasswordResult

                while True:
                    resultado = authenticate(Authenticator.PASSWORD)

                    if resultado == PasswordResult.SUCCESS:
                        break

                resultado = check(resultado)

                f = open(f'/data/data/com.termux/files/home/.bloqueio/key-{tentativas}', 'w')
                f.write('')
                f.close()

                tentativas -= 1

                if resultado == True:
                    break
                else:
                    print(f'Tente novamente, você tem {tentativas} tentativas sobrando!')

            resultado = False
            return resultado

        elif lock == Padlock.FULL_LOCK:
            print(f'{limpeza}{vermelho}Safe-Termux - Bloqueio Total!{fim}\n')
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
            print(f'{vermelho}     .dUs7rvvvsj1s2Pgdg{fim}\n')

            sleep(3)
    except KeyboardInterrupt:
        return False