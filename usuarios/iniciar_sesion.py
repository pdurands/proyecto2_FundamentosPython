import maskpass

from excepciones.excepts import SalirdelPrograma
from persistencia.manejo_del_csv import validar_csv_creado, is_login_correct
from usuarios.validaciones_de_inputs import is_valid_email
from utils.seguridad import hash_pwd


def iniciar_sesion(intentos: int = 3) -> str:
    """
       Permite al usuario iniciar sesión con un máximo de 3 intentos.
       Valida la existencia del CSV, solicita email y contraseña,
       y verifica credenciales. Si falla, bloquea al usuario.
    """

    validar_csv_creado()
    while intentos:
        email = is_valid_email()
        password = hash_pwd(maskpass.askpass("Ingrese su contraseña: ", mask="*"))
        if is_login_correct(email, password):
            return email
        else:
            print("\n❌ Email o contraseña incorrectos\n")

        intentos -= 1

    # Usuario bloqueado
    while True:
        print("\nUsuario bloqueado, reinicia la aplicación para intentar de nuevo.")
        print("1. Salir")
        op = input("Seleccione una opción: ").strip()
        if op == "1":
            raise SalirdelPrograma
