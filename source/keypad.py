import json
import subprocess
from enum import Enum
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
    password: str = "" # type: str

def authenticate(authenticator: Authenticator = Authenticator.BIOMETRIC) -> Union[PasswordResult, BiometricResult]:
    """Authenticate the user with the given authentication method"""
    if authenticator == Authenticator.PASSWORD:
        _command = "termux-dialog"
        _command += " text"
        _command += " -t 'Digite a senha'"
        _command += " -i 'Safe-Termux v1.0.2'"
        _command += " -p"

        _password = subprocess.check_output(_command, shell=True).decode('utf-8')

        try:
            _password = json.loads(_password)
        except json.decoder.JSONDecodeError:
            raise RuntimeError('Invalid JSON returned from termux-dialog')

        if _password.get("code", 0) == -2:
            return PasswordResult.CANCELLED

        _result = PasswordResult.SUCCESS
        _result.password = _password.get("text", "")
        return _result
    elif authenticator == Authenticator.BIOMETRIC:
        _command = "termux-fingerprint"
        _command += " -t 'Safe-Termux'"
        _command += " -i 'v1.0.2'"
        _command += " -s 'Use a impressão digital para desbloquear o Safe-Termux'"
        _command += " -c 'Cancelar'"

        _result = subprocess.check_output(_command, shell=True).decode('utf-8')

        try:
            _result = json.loads(_result)
        except json.decoder.JSONDecodeError:
            raise RuntimeError('Invalid JSON returned from termux-biometric')

        if ("ERROR_TIMEOUT" in _result.get("errors", [])):
            return BiometricResult.TIMEOUT

        if _result.get("auth_result") == "AUTH_RESULT_SUCCESS":
            return BiometricResult.SUCCESS
        elif _result.get("auth_result") == "AUTH_RESULT_FAILURE":
            return BiometricResult.FAILURE
        else:
            return BiometricResult.UNKNOWN