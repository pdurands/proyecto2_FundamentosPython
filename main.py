from excepciones.excepts import SalirdelPrograma
from usuarios.iniciar_sesion import iniciar_sesion
from usuarios.menu_login import menu_login
from usuarios.registrar_usuarios import registrar_usuarios


def main_menu():
    try:
        while True:
            print("️\n🛡️ Sistema de Autenticación 🛡️\n")
            print("👤 Menú Principal 👤")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Salir\n")
            op = input("📌 Seleccione una opción: ").strip()
            if op == "1":
                print("\n📌 Registro")
                email = registrar_usuarios()
                if email:
                    print(f"\n✔ Bienvenido, {email}")
                    menu_login(email)
                else:
                    print(f"\n❌ Usuario ya existe, intente con otro email\n")

            elif op == "2":
                print("\n📌 Iniciar sesión")
                email = iniciar_sesion()
                print(f"\n✔ Bienvenido, {email}")
                menu_login(email)

            elif op == "3":
                print("\n\n📌 Saliendo del programa...\n\n")
                break

            else:
                print("\nOpción no válida. Intente nuevamente\n")


    except KeyboardInterrupt:
        print("\n\n📌 Saliendo del programa...\n\n")

    except SalirdelPrograma:
        print("\n\n📌 Saliendo del programa...\n\n")


if __name__ == "__main__":
    main_menu()
