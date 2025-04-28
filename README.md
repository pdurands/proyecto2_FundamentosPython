# 🔐 Proyecto Final: Sistema de Autenticación con CSV Seguro
## 📘 Contexto/Introducción
Construir un sistema de registro e inicio de sesión es fundamental para cualquier sistema que requiera autenticación. Este proyecto simula un sistema realista de login que almacena los datos de los usuarios en un archivo .csv, pero va más allá: incluye validación, modularización y buenas prácticas de seguridad como el uso de hash para las contraseñas, sin frameworks ni bases de datos externas.

Este es un mini-backend funcional que podría utilizarse para aplicaciones locales, prototipos o herramientas internas.

## ✅ Requerimientos Funcionales
### 📁 Base de datos de usuarios (users.csv)
Debe almacenar los siguientes campos:

email, password_hash, registered_at

Si el archivo no existe, debe crearse automáticamente al iniciar el programa.

## 👤 Registro de usuario
Solicita email, contraseña, y confirmación de contraseña.

Validar:

Que el email tenga un formato válido (regex simple).

Que el email no esté ya registrado.

Que las contraseñas coincidan.

Almacenar contraseña como hash (usa hashlib.sha256()).

Guardar la fecha de registro usando datetime.datetime.now().

## 🔑 Inicio de sesión
Solicita email y contraseña.

Validar si el email existe y la contraseña coincide (comparando hash).

Si es correcto, marcar al usuario como "logueado" en memoria (no guardar estado en el CSV).

En sesión activa, permitir cerrar sesión o salir.

## 🔁 Loop de ejecución
El sistema corre hasta que el usuario decida salir.

Si el usuario está logueado, debe poder:

Ver su información (email y fecha de registro).

Cerrar sesión.

Si no está logueado, debe poder:

Registrarse
Iniciar sesión
Salir

Ejemplo de menú:

```
📌 Menú principal
1. Registrarse
2. Iniciar sesión
3. Salir
```
Cuando está logueado:

```
👋 Bienvenido, usuario@mail.com
1. Ver mi información
2. Cerrar sesión
3. Salir
```

## 🎯 Desafío Opcional (Nivel 2% Más)
Agrega la funcionalidad de bloqueo de cuenta tras 3 intentos fallidos de login consecutivos:

- Lleva un registro en memoria (no en el archivo).

- Muestra un mensaje de “Usuario bloqueado, reinicia la aplicación para intentar de nuevo.”

También puedes agregar una función de cambio de contraseña desde el menú logueado:

- Solicitar la contraseña actual.
- Validar que sea correcta.
- Solicitar nueva contraseña y confirmación.
- Actualizar la línea correspondiente en el CSV.


## 🧠 Buenas prácticas y sugerencias técnicas
Usa typing para todas tus funciones.

Usa csv.DictReader y csv.DictWriter para trabajar con el archivo.

Usa hashlib.sha256() para encriptar contraseñas (sin sal para mantenerlo dentro del alcance).

Usa re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) para validar emails.

Crea funciones puras y separadas:

- register_user(), login_user(), load_users(), save_user(), hash_password(), is_valid_email(), etc.

Usa try/except para capturar errores de entrada y de archivos.

Modulariza tu menú y tu lógica en una función principal main().

## 🧾 Ejemplo de Entrada/Salida

```
Bienvenido al sistema 🛡️

1. Registrarse
2. Iniciar sesión
3. Salir
> 2

Email: mario@mail.com
Contraseña: ********
❌ Usuario o contraseña incorrecta.

> 2
Email: mario@mail.com
Contraseña: ********
✔ Bienvenido, mario@mail.com

👤 Opciones
1. Ver mi información
2. Cerrar sesión
3. Salir
> 1

Email: mario@mail.com
Registrado el: 2025-04-15 00:33:52
```
