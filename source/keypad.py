import os
import json
import subprocess
from enum import Enum
from utils import parse
from typing import Union

class Authenticator(Enum):
    """Enumeration of authentication methods."""
    PASSWORD = 0
    BIOMETRIC = 1

class BiometricResult(Enum):
    """Enumeration of biometric authentication results."""
    SUCCESS = 0
    FAILURE = 1
    UNKNOWN = 2
    TIMEOUT = 3

class PasswordResult(Enum):
    """Enumeration of password authentication results."""
    SUCCESS = 0
    CANCELLED = 1
    NOT_DEFINED = 2
    password: str = "" # type: str

def authenticate(authenticator: Authenticator = Authenticator.BIOMETRIC) -> Union[PasswordResult, BiometricResult]:
    """Authenticate the user with the given authentication method"""
    if authenticator == Authenticator.PASSWORD:
        if not os.path.isfile(parse('$HOME/.bloqueio/kp')):
            return PasswordResult.NOT_DEFINED

        _command = ["termux-dialog", "text", "-t", "Digite a senha", "-i", "Safe-Termux v1.0.13", "-p"]
        _password = subprocess.check_output(_command).decode('utf-8')

        try:
            _password = json.loads(_password)
        except json.decoder.JSONDecodeError:
            exit(1) # Isso vai fazer o Termux do usuário fechar
            # Quando ele abrir novamente, vai rodar tudo normal
            # (um erro de JSON incompleto acontece no termux-dialog, quando, assim que a janela aparece
            # você troca de app, ai a janela é fechada)

        if _password.get("code", 0) == -2:
            return PasswordResult.CANCELLED

        _result = PasswordResult.SUCCESS
        _result.password = _password.get("text", "")
        return _result
    elif authenticator == Authenticator.BIOMETRIC:
        _command = ["termux-fingerprint", "-t", "Safe-Termux", "-s", "v1.0.13", "-d", "Use a impressão digital para desbloquear o Safe-Termux", "-c", "Usar senha"]
        _result = subprocess.check_output(_command).decode("utf-8")

        try:
            _result = json.loads(_result)
        except json.decoder.JSONDecodeError:
            exit(1) # Eu não sei se a mesma coisa acontece na biometria (provavelmente não
            # pelo menos no meu Galaxy A31, a janela de biometria remove a barra de ação
            # impossibilitando a pessoa de pressionar qualquer um dos botões) e se o usuário
            # trocar de janela, a biometria provavelmente é dada por cancelada

        if ("ERROR_TIMEOUT" in _result.get("errors", [])):
            return BiometricResult.TIMEOUT

        if _result.get("auth_result") == "AUTH_RESULT_SUCCESS":
            return BiometricResult.SUCCESS
        elif _result.get("auth_result") == "AUTH_RESULT_FAILURE":
            return BiometricResult.FAILURE
        else:
            return BiometricResult.UNKNOWN
