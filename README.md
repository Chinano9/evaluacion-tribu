# Prueba tecnica TribuCo
El proyecto es un sistema de chat en línea que permite a los usuarios registrados comunicarse a través de salas de chat. Proporciona una interfaz intuitiva y amigable para que los usuarios puedan unirse a salas existentes, crear nuevas salas y participar en conversaciones grupales.
## Características principales

El proyecto incluye las siguientes características principales:

    Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión en el sistema. Esto garantiza que solo los usuarios autenticados tengan acceso a las funcionalidades del chat.

    Gestión de salas: Los usuarios pueden explorar la lista de salas disponibles, unirse a salas existentes y crear nuevas salas. Cada sala tiene un nombre que los usuarios pueden especificar al crearla.

    Panel de administración: Existe un panel de administración donde los superusuarios pueden gestionar las salas y los usuarios registrados. Esto incluye la capacidad de eliminar salas, editarlas y cerrarlas si es necesario.

## Tecnologías utilizadas

El proyecto se ha desarrollado utilizando las siguientes tecnologías:

    Django: Un framework web de alto nivel basado en Python, utilizado para el desarrollo del backend del proyecto. Proporciona una estructura sólida y herramientas eficientes para la creación de aplicaciones web.
    
    HTML, CSS y JavaScript: Estas tecnologías se utilizan para la creación de la interfaz de usuario del proyecto. HTML se encarga de la estructura del sitio web, CSS se utiliza para dar estilo y apariencia visual, y JavaScript permite la interactividad y la comunicación en tiempo real con el servidor.

## Instalación del proyecto

Sigue los pasos a continuación para instalar y configurar el proyecto en tu entorno de desarrollo:

1. **Clonar el repositorio**: Comienza clonando el repositorio del proyecto desde GitHub. Abre una terminal y ejecuta el siguiente comando:

   ```
   git clone <url_del_repositorio>
   ```

2. **Crear un entorno virtual**: Se recomienda utilizar un entorno virtual para mantener las dependencias del proyecto aisladas. Navega hasta la carpeta del proyecto clonado y crea un nuevo entorno virtual ejecutando el siguiente comando:

   ```
   python3 -m venv env
   ```

   Esto creará un nuevo entorno virtual en una carpeta llamada "env".

3. **Activar el entorno virtual**: Activa el entorno virtual recién creado ejecutando el siguiente comando:

   - En macOS y Linux:

     ```
     source env/bin/activate
     ```

   - En Windows:

     ```
     env\Scripts\activate
     ```

4. **Instalar dependencias**: Una vez que el entorno virtual esté activado, instala las dependencias del proyecto ejecutando el siguiente comando:

   ```
   pip install -r requirements.txt
   ```

   Esto instalará todas las dependencias necesarias para ejecutar el proyecto.

5. **Configurar la base de datos**: Configura la base de datos de tu elección en el archivo de configuración del proyecto. Abre el archivo `settings.py` en la carpeta del proyecto y encuentra la sección de configuración de la base de datos. Asegúrate de proporcionar la información correcta para tu base de datos.

6. **Aplicar migraciones**: Ejecuta el siguiente comando para aplicar las migraciones y configurar la base de datos:

   ```
   python manage.py migrate
   ```

7. **Crear un superusuario**: Opcionalmente, puedes crear un superusuario que te permitirá acceder al panel de administración del proyecto. Ejecuta el siguiente comando y sigue las instrucciones:

   ```
   python manage.py createsuperuser
   ```

8. **Ejecutar el servidor de desarrollo**: Finalmente, inicia el servidor de desarrollo ejecutando el siguiente comando:

   ```
   python manage.py runserver
   ```

   El servidor se ejecutará en `http://localhost:8000/` por defecto.


