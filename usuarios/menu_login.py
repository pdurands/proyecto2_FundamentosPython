from excepciones.excepts import SalirdelPrograma
from usuarios.cambiar_pwd import cambiar_pwd
from usuarios.ver_user_info import ver_user_info


def menu_login(email: str) -> None:
    while True:
        print("\n👤Menú de Usuario👤\n1. Ver mi información\n2. Cerrar sesión\n3.Cambiar contraseña\n4. Salir")
        op = input("Seleccione una opción: ").strip()
        if op == "1":
            ver_user_info(email)

        elif op == "2":
            print("👤 Cerrando sesión...\n")
            return

        elif op == "3":
            cambiar_pwd(email)

        elif op == "4":
            raise SalirdelPrograma

        else:
            print("Opción no válida. Intente nuevamente.")
