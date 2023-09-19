# Easy Trade: Stock and Investments

### Una aplicación web destinada a realizar trading e inversiones de forma segura, integral y fácil de usar, accesible para cualquier usuario, independientemente de su nivel de experiencia, ya que está dirigida a todas aquellas personas interesadas en el mundo del trading e inversiones, tanto expertas como principiantes

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Instalación
Para instalar el backend es necesario:
- Python3.9
- PostgreSQL

Luego de clonar el repositorio, se debe activar un entorno de desarrollo para python:
```
        $ virtualenv venv
```
Despues de crear el entorno se debe activar
```
        $ source venv/bin/activate
```

Una vez activado el entorno se descargan las dependencias
```
        $ pip install -r requirements/local.txt
```

Procedemos a migrar los modelos a la base de datos
```
        $ python manage.py migrate
```

Por ultimo iniciamos el servidor
```
        $ python manage.py runserver
```
