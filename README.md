# Taller ORM

Aplicación web desarrollada con Django para administrar cuentas bancarias. Permite consultar, registrar, actualizar y eliminar cuentas.

## Requisitos

- Python 3.10 o superior
- MySQL

## Instalación y ejecución

1. Clona el repositorio y entra en la carpeta del proyecto.
2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   En Windows, actívalo con:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la conexión a MySQL en `proyecto/settings.py` y asegúrate de que la base de datos exista.
5. Ejecuta las migraciones y levanta el servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. Abre <http://127.0.0.1:8000/cuentas/>.

## Funcionalidades

- Listar cuentas.
- Registrar una cuenta con tipo, descripción y saldo.
- Actualizar los datos de una cuenta.
- Eliminar una cuenta.

## Rutas principales

- `/cuentas/`: listado y registro de cuentas.
- `/actualizar/<id>/`: actualización de una cuenta.
- `/eliminar/<id>/`: eliminación de una cuenta.
- `/admin/`: administración de Django.
