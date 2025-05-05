
# Proyecto Django Blog

Este es un proyecto Django de un blog básico donde los usuarios pueden ver, crear, editar y eliminar publicaciones. También permite a los administradores gestionar categorías.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) (gestor de paquetes de Python)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (para clonar el repositorio)

## Pasos para instalar el proyecto

### 1. Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
2. Crear un entorno virtual
Es recomendable utilizar un entorno virtual para aislar las dependencias de tu proyecto. Si no tienes virtualenv instalado, instálalo primero:

bash
Copiar
Editar
pip install virtualenv
Ahora crea un entorno virtual en el directorio del proyecto:

bash
Copiar
Editar
cd tu_repositorio
virtualenv venv
3. Activar el entorno virtual
Windows:

bash
Copiar
Editar
venv\Scripts\activate
Mac/Linux:

bash
Copiar
Editar
source venv/bin/activate
4. Instalar las dependencias
Una vez activado el entorno virtual, instala todas las dependencias del proyecto con el siguiente comando:

bash
Copiar
Editar
pip install -r requirements.txt
5. Configuración de la base de datos
El proyecto utiliza SQLite por defecto, por lo que no necesitas configurar una base de datos externa. Si deseas usar una base de datos diferente (como PostgreSQL o MySQL), necesitarás modificar las configuraciones en settings.py.

Ejecuta las migraciones para configurar la base de datos:

bash
Copiar
Editar
python manage.py migrate
6. Crear un superusuario (opcional)
Para acceder al panel de administración de Django y gestionar las publicaciones y categorías, necesitas crear un superusuario:

bash
Copiar
Editar
python manage.py createsuperuser
Se te pedirá un nombre de usuario, correo electrónico y contraseña.

7. Ejecutar el servidor
Una vez que todo esté configurado, ejecuta el servidor de desarrollo de Django con el siguiente comando:

bash
Copiar
Editar
python manage.py runserver
El servidor debería estar corriendo en http://127.0.0.1:8000.

8. Acceder al panel de administración
Para acceder al panel de administración de Django, ve a la siguiente URL:

arduino
Copiar
Editar
http://127.0.0.1:8000/admin/
Inicia sesión con el nombre de usuario y la contraseña que proporcionaste al crear el superusuario.

9. Subir archivos estáticos
Si necesitas servir archivos estáticos en un entorno de producción, ejecuta el siguiente comando:

bash
Copiar
Editar
python manage.py collectstatic
Esto recopilará todos los archivos estáticos en la carpeta /static/.

Contribuir
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del proyecto.

Crea una rama para tu cambio (git checkout -b feature/nueva-caracteristica).

Haz commit de tus cambios (git commit -m 'Agregado nueva característica').

Haz push a tu rama (git push origin feature/nueva-caracteristica).

Crea un pull request.
