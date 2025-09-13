# TechConnect 2025

Aplicación web para la gestión de asistentes al evento TechConnect 2025.

## Requisitos

- Python 3.10+
- pip
- (Opcional) Docker

## Instalación

1. Clona el repositorio o copia los archivos en tu máquina.
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

3. Realiza las migraciones de la base de datos:
   ```sh
   python manage.py migrate
   ```

4. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

5. Accede a la aplicación en [http://localhost:8000](http://localhost:8000).

## Uso con Docker (opcional)

1. Construye la imagen:
   ```sh
   docker build -t techconnect2025 .
   ```

2. Ejecuta el contenedor:
   ```sh
   docker run -p 8000:8000 techconnect2025
   ```

## Estructura principal

- `asistentes/`: App principal para gestión de asistentes.
- `config/`: Configuración del proyecto Django.
- `templates/`: Archivos HTML.
- `db.sqlite3`: Base de datos SQLite.

## Migraciones y administración

- Para crear un superusuario:
  ```sh
  python manage.py createsuperuser
  ```
- Accede al panel de administración en `/admin`.

---

Para dudas o soporte, contacta al equipo de TechConnect.