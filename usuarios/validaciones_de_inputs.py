# Validaciones de los datos de entrada
import re

import maskpass

from utils.seguridad import hash_pwd


def is_valid_email() -> str:
    """
    Valida el formato de un correo electrónico.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Ingrese su correo: ").strip()
        if re.fullmatch(email_regex, email):
            return email.lower()
        else:
            print("El correo electrónico no es válido. Intente nuevamente.")


def is_valid_password() -> str:
    """
    Valida el formato de una contraseña valida.
    Confirma la contraseña.
    Hashea la contraseña.
    """
    msn = "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula, un número y un carácter especial."
    pwd_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    while True:
        password = maskpass.askpass(f"{msn}\nContraseña: ", mask="*")
        password2 = maskpass.askpass("Confirme su contraseña: ", mask="*")
        if not password or not re.fullmatch(pwd_regex, password):
            print("La contraseña no es válida. Intente nuevamente\n.")
        elif password != password2:
            print("Las contraseñas no coinciden. Intente nuevamente\n.")
        else:
            return hash_pwd(password)
