CREACION DE APLICACION EN DJANGO

1. Instalación de entorno virtual para proyecto

En terminal: 
Sobre la carpeta de trabajo 
>pip install virtualenv

>python -m virtualenv env

2. Activar el archivo 'activate' de la carpeta 'Scripts'

Sobre la carpeta de trabajo
>.\venv\Scripts\activate

3. Instalar Django 4.2.1 + DjangoRest framework

> py -m pip install django==4.2.1 
> pip install djangorestframework

4. Iniciar proyecto

> django-admin starproject Producto .	//Para crear en directorio actual

5. Run server para verificación de versiones

> python manage.py runserver		//Abrir dirección arrojada por la terminal para corroborar la versión de Django

6. Crear proyectos y enlazar con 'settings.py'

En terminal:
> pyton manage.py startapp projects

En la carpeta 'Producto' abrir el archivo 'settings.py' y agregar:

'projects',
'rest_framework',   

a la lista que guarda 'INSTALLED_APPS' 	

7. Creación del modelo de projecto (migraciones)

En projectos en el archivo 'models.py' se establecerá la clase Project
en donde se definirán los atributos de cada uno de los productos.
Posterior a eso ejecutar el comando:

> pyton mange.py makemigrations

Para la creación de las tablas de proyecto ejecutar

> python manage.py migrate

Desarrollo de la API

En la carpeta projectos hay un archivo de nombre 'serializers' donde del modelo '.project' se importa el modelo de nuestraapp
Los campos consultados son :
'id' - generado automáticamente
'nombre' - requerido
'descripcion' - opcional
'precio' - requerido
'disponible' -  en valor predefinido

Se crea la clase PrejectSerializer y en esta la clase Meta
donde en modelo se importará 'Project' y se establecerán  los campos:

>fields = ('id','nombre','descripcion','precio','disponible')

En la misma carpeta se encuentra el archivo 'api.py' donde se consultarán todos los objetos de la tabla. En esta misma se consultan estos datos y se define desde donde se usará el serializer.

El archivo 'urls.py' en la misma carpeta, importa los routers desde el rest_framework y se exporta un objeto es donde se generarán las urls.

 
En la carpeta 'Producto' se ingresa a 'urls.py' donde se conectará con la otra aplicación importando desde 'projectos' el archvio 'urls.py' que pertenece al mismo 

> path ('', include('projectos.urls'))


