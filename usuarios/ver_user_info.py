def ver_user_info(email: str) -> None:
    """
    Muestra la información del usuario.
    """
    from persistencia.manejo_del_csv import get_user_info
    user_info = get_user_info(email)

    if user_info:
        print("\n👤 Información del usuario:")
        print(f"- Email: {user_info['email']}")
        print(f"- Fecha de registro: {user_info['registered_at']}")
    else:
        print("👤 Usuario no encontrado.")
