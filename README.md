
# Sistema de Autenticación 🛡️

Este proyecto es un sistema de autenticación básico desarrollado en Python que utiliza un archivo CSV como base de datos para almacenar la información de los usuarios. Implementa el uso de **hashes** para proteger las contraseñas y garantizar la seguridad de los datos. Permite registrar usuarios, iniciar sesión, cambiar contraseñas y ver información del usuario.

## Características

- **Registro de usuarios**: Permite registrar nuevos usuarios con un correo electrónico, contraseña y fecha de registro.
- **Inicio de sesión**: Verifica las credenciales del usuario utilizando contraseñas en formato hash.
- **Cambio de contraseña**: Los usuarios pueden actualizar su contraseña, que se almacena de forma segura.
- **Visualización de información**: Los usuarios pueden consultar su información almacenada en la base de datos.
- **Base de datos en CSV**: La información de los usuarios se almacena en un archivo `users.csv`.
- **Seguridad**: Las contraseñas se almacenan como hashes, lo que evita que sean visibles en texto plano.
- **Validación de entradas**: Se asegura que los correos electrónicos y contraseñas cumplan con los requisitos mínimos de seguridad.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias. Puedes instalarlas utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Dependencias

- `evdev==1.9.1`
- `maskpass==0.3.7`
- `pynput==1.8.1`
- `python-xlib==0.33`
- `six==1.17.0`

## Uso

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

4. **Opciones del menú principal**:
   - `1. Registrarse`: Registra un nuevo usuario.
   - `2. Iniciar sesión`: Inicia sesión con un usuario existente.
   - `3. Salir`: Cierra el programa.

5. **Opciones del menú de usuario**:
   - `1. Ver mi información`: Muestra la información del usuario.
   - `2. Cerrar sesión`: Regresa al menú principal.
   - `3. Cambiar contraseña`: Permite actualizar la contraseña del usuario.
   - `4. Salir`: Finaliza el programa.

## Base de Datos

El archivo `users.csv` se utiliza como base de datos para almacenar la información de los usuarios. Este archivo contiene las siguientes columnas:

- `email`: Correo electrónico del usuario.
- `password_hash`: Contraseña en formato hash.
- `registered_at`: Fecha y hora de registro.

## Seguridad

- **Hashing de contraseñas**: Las contraseñas se almacenan como hashes utilizando algoritmos seguros, lo que protege los datos en caso de acceso no autorizado al archivo CSV.
- **Validación de entradas**: Se implementan validaciones estrictas para garantizar que los datos ingresados sean seguros y válidos.

## Notas

- Asegúrate de que el archivo `users.csv` tenga los permisos necesarios para lectura y escritura.
- El programa maneja errores comunes como usuarios duplicados o credenciales incorrectas.
- Las contraseñas no se almacenan en texto plano, lo que mejora la seguridad del sistema.

## Autor

Desarrollado por Paul B. Durand Sarango.