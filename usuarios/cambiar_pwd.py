import maskpass

from persistencia.manejo_del_csv import change_password, is_login_correct
from usuarios.validaciones_de_inputs import is_valid_password
from utils.seguridad import hash_pwd


def cambiar_pwd(email: str) -> None:
    """
    Cambia la contraseña del usuario.
    """
    print("\n👤 Cambiar contraseña")
    password = hash_pwd(maskpass.askpass(f"Ingrese su contraseña actual: ", mask="*"))
    if is_login_correct(email, password):
        print("\nIngrese su nueva contraseña")
        password = is_valid_password()
        change_password(email, password)
        print("\nContraseña cambiada con éxito")
    else:
        print("\n❌ Contraseña incorrecta\n")
