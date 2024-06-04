# <samp>Saberes previos sobre Django</samp>
Django sigue el Model View Template (MVT)

<img src="latex/img/model_view_template.png" alt="Model View Template">

# <samp> :wrench: Configuraciones previas</samp>
Para probar la funcionalidad de los programas, debe de realizar los siguientes pasos que están como recordatorio.

> Instalamos django en nuestra maquina o en nuestro entorno de python
```sh
pip install django
```

> Verificamos la version instalada
```sh
pip list
pip show Django

# También podemos usar
django-admin --version
```

> Clonar el repositorio
```sh
# For example: Using the HTTPS protocol
git clone https://github.com/jorghee/django-projects.git
```

# <samp>Sistema de notas :spiral_notepad:</samp>
Ya hemos creado un proyecto en Django que lo nombramos `University`. Dentro de este proyecto hemos creado una app que la nombramos `grades`. Solo se necesita realizar las migraciones para probar el programa.

> Realizar las migraciones en la base de datos
```sh
python manage.py makemigrations grades
python manage.py migrate
```

> Lanzamo el servidor para probar el proyecto
```sh
python manage.py runserver
```
Si no ha obtenido ningún error, puede ingresar la url que le sugiere en la descripcion del inicio del servidor desde su navegador de preferencia.

# <samp>Destinos turisticos :airplane:</samp>
Se ha creado otro proyecto en este repositorio, el cual se ha nombrado como `turismo_Peru`, dentro de este proyecto se ha creado una aplicación denominada `destinos_turisticos`, entonces como se mencionó anteriormente se necesita tambien necesitamos modificar la estructura de la base datos.

> Realizar las migraciones en la base de datos
```sh
python manage.py makemigrations destinos_turisticos
python manage.py migrate
```
Luego nuevamente iniciamos el servidor pero para este proyecto y espero que no haya tenido ningún error.

## <samp> :eyes: Lógicas importantes</samp>
