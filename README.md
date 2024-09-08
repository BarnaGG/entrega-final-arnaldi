# Entrega Final - Proyecto Django

## Video visita al sitio

https://youtu.be/yV-xRA91cAI

## Descripción

Este es el proyecto final para la cursada de Python de CoderHouse, desarrollado por Bruno Nicolás Arnaldi. El proyecto consiste en una aplicación web para la gestión de perfiles de streamers, casters, hosts, jugadores e influencers. Permite agregar, editar y visualizar información relevante de cada perfil, así como gestionar la representación y management de talentos en el ámbito de esports y gaming.

## Usuario con permisos:
user: superprofesor
pass: coderhouse

## Requisitos

- Python 3.8 o superior
- Django 4.1 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/BarnaGG/entrega-final-arnaldi
    ```

2. **Navegar al directorio del proyecto:**

    ```bash
    cd entrega-final-arnaldi
    ```

3. **Crear un entorno virtual e instalar las dependencias:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos:**

    ```bash
    python manage.py migrate
    ```

5. **Crear un superusuario para el panel de administración (opcional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Iniciar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

## Uso

1. **Acceder a la aplicación:**

    Abre tu navegador web y dirígete a [(http://127.0.0.1:8000/apptalentos/inicio)).

2. **Navegar por la aplicación:**

    - **Página de inicio:** Visualiza la primera view del sitio.
    - **Formulario de registro:** Permite añadir nuevos perfiles.
    - **Panel de administración:** Accede al panel para gestionar perfiles y configuraciones (accesible en [(http://127.0.0.1:8000/admin/)).
    - **Páginas Streamers, Host/Casters, Players, Influencers:** Visualiza los detalles de cada uno de las categorias.

## Contribución

1. **Hacer un fork del repositorio.**
2. **Crear una nueva rama para tus cambios:**

    ```bash
    git checkout -b nombre-de-la-rama
    ```

3. **Realizar tus cambios y hacer commits:**

    ```bash
    git add .
    git commit -m "Descripción de los cambios"
    ```

4. **Pushear los cambios a tu fork:**

    ```bash
    git push origin nombre-de-la-rama
    ```

5. **Crear una pull request desde tu fork en GitHub.**

