# Proyecto Django 

## Integrantes
- Ledesma, Matias Manuel
- Gaona, Juan Maria
- Oviedo, Lucas
- Alegre, Nicolas

---

##  Tecnologías utilizadas

- **Python 3.10+**
- **Django 5.0+**
- **SQLite** (base de datos por defecto, fácil de migrar a PostgreSQL u otros)
- **Bootstrap 5** (para estilos básicos del frontend)

---

##  Instalación y configuración del entorno

Seguí estos pasos para levantar el proyecto en tu máquina local:


```bash 

1. Clonar el repositorio

git clone https://github.com/Matiasledesma449/PythonProyecto1.git
cd proyecto-django-grupo

-------------------------------------------------------------------------------------

2. Crear y activar el entorno virtual

bash
python -m venv venv
venv\Scripts\activate
---------------------------------------------------------------------------------------
3. Instalar las dependencias
pip install -r requirements.txt

Si no tenés el archivo requirements.txt, instalá Django directamente
pip install django


Luego genera el archivo con: 
pip freeze > requirements.txt
-----------------------------------------------------------------------------------------
4. Realizar las migraciones de la base de datos
python manage.py makemigrations
python manage.py migrate

-----------------------------------------------------------------------------------------
5. Crear un superusuario (para el panel de administración)

python manage.py createsuperuser
-----------------------------------------------------------------------------------------
6. Ejecutar el servidor de desarrollo

python manage.py runserver

El proyecto estará disponible en:
👉 http://127.0.0.1:8000/