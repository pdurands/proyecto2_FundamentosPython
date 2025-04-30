import csv
import os

ruta_db = os.path.join(os.path.dirname(__file__), '../users.csv')


# Crear un archivo CSV y escribir en él
def validar_csv_creado():
    try:
        with open(ruta_db, 'x', newline='', encoding="utf-8"):
            pass
    except FileExistsError:
        pass


def save_user_db(email: str, password: str, registered_at: str) -> str:
    dato = {'email': email, 'password_hash': password, 'registered_at': registered_at}
    with open(ruta_db, 'a', newline='', encoding="utf-8") as base_de_datos:
        writer = csv.DictWriter(base_de_datos, fieldnames=dato.keys())
        if base_de_datos.tell() == 0:
            writer.writeheader()
        writer.writerow(dato)

    return "Registro exitoso\n"


def is_login_correct(email: str, password_hash: str) -> bool:
    with open(ruta_db, 'r', newline='', encoding="utf-8") as base_de_datos:
        reader = csv.DictReader(base_de_datos)
        for row in reader:
            if row['email'] == email and row['password_hash'] == password_hash:
                return True
    return False


def change_password(email: str, new_password: str) -> str:
    rows = []
    with open(ruta_db, 'r', newline='', encoding="utf-8") as base_de_datos:
        reader = csv.DictReader(base_de_datos)
        for row in reader:
            if row['email'] == email:
                row['password_hash'] = new_password
            rows.append(row)

    with open(ruta_db, 'w', newline='', encoding="utf-8") as base_de_datos:
        writer = csv.DictWriter(base_de_datos, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    return "Contraseña cambiada exitosamente\n"


def get_user_info(email: str) -> dict:
    with open(ruta_db, 'r', newline='', encoding="utf-8") as base_de_datos:
        reader = csv.DictReader(base_de_datos)
        for row in reader:
            if row['email'] == email:
                return row
    return None
