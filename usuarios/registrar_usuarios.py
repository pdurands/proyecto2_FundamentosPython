from datetime import datetime

from persistencia.manejo_del_csv import validar_csv_creado, save_user_db, get_user_info
from usuarios.validaciones_de_inputs import is_valid_email, is_valid_password


def registrar_usuarios() -> str | None:
    """
    Registra un nuevo usuario en la base de datos CSV.
    """
    email = is_valid_email()
    validar_csv_creado()
    if not get_user_info(email):
        password = is_valid_password()
        registered_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(save_user_db(email, password, registered_at))
        return email
    else:
        return None
