# Configuración de Heroku, AWS y Django
Como integrar Heroku y AWS a tu aplicación de Django. 
Lo primero que debemos hacer para no tener conflictos es subir nuestra aplicación a Heroku para ello seguimos los siguientes pasos.
# Configuración de Heroku 
1. Crear una cuenta en heroku desde su página oficial https://www.heroku.com/ 
2. Instalamos los pip necesarios en nuestra virtualenv de nuestro proyecto:
- `pip install gunicorn`
- `pip install psycopg2==2.7.4`
- `pip install dj-database-url`
- `pip install whitenoise`
- `pip install django-heroku`
3. creamos nuestro archivo requirements.txt con el siguiente comando: 
  `   pip freeze > requirements.txt`
**# Nota. Siempre que instalemos un nuevo pip debemos actualizar el requirements.txt con el comando anterior. Y en el caso de que ya tengamos el requirements.txt y queramos instalar, utilizamos el siguiente comando **
`pip install -r requirements.txt`
4. Es hora de ir a nuestro setings.py e importar: 
`import django_heroku`
y modificar nuestra constante DEBUG, colocamos su valor como False.
`DEBUG = False`
Asignamos los hosts válidos. En este caso coloco asterisco , indicando que acepte todos los hosts.
`ALLOWED_HOSTS = ['*']`
Agregamos las siguientes líneas de código al final de nuestro archivo settings.py.
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
Procedemos a agregar el middleware WhiteNoiseMiddleware
```python
MIDDLEWARE = [
         ...
     'whitenoise.middleware.WhiteNoiseMiddleware',
]
```
Es hora de ir al archivo urls.py (el principal) agregamos las siguientes líneas de código, esto con la finalidad de poder utilizar los archivos estáticos.
`urlpatterns = [
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`
3. Se crea un archivo en la raíz del proyecto, es decir, a nivel del manage.py con el nombre Procfile en el cual se copia lo siguiente:
`web: gunicorn noombredetuproyecto.wsgi  `
4. Creamos otro archivo en la raíz del proyecto, es decir, a nivel del manage.py con el nombre runtime.txt y ponemos la versión de python que estemos utilizando para el proyecto
5. en el archivo wsgi.py agregamos lo siguiente:


    import os
    
    from django.core.wsgi import get_wsgi_application
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Configuracion.settings')
    
    application = get_wsgi_application()

6. Es hora de crear nuestra aplicación en heroku para ello lo vamos hacer de la manera mas rapida, es decir, desde nuestra cuenta, donde podemos configurar para que se sincronice con github cada vez que hagamos un push.
7. Una vez que tengamos nuestra aplicación creada vamos a instalar heroku en nuestra consola de comandos (shell).
8. Luego ponemos el siguiente comando para autenticarnos con heroku
`heroku login`
9. En la consola introducimos lo siguiente 
`heroku config:set DISABLE_COLLECTSTATIC=1`
10. Con esto subimos los cambios a github y deployamos desde nuestra cuenta de heroku.
Una vez que tengamos nuestra aplicación en heroku seguimos con la configuración de Amazon Web Services (S3).
# Pasos de Configuración de AWS
1. Lo primero que se debe hacer es crear su cuenta en Amazon Web Service desde su pagina oficial https://aws.amazon.com/es/, llenar todos los campos obligatorios, estos campos deben ser verdaderos, al momento de crear su cuenta le pedirá ingresar una tarjeta de débito o crédito de la cual se debitará $1 pero no se preocupe que será reembolsado, con la finalidad de poder confirmar que sus datos o su tarjeta esté funcionando correctamente. Esta plataforma brinda 12 meses gratis, que incluye uso de Amazon S3, Amazon EC2, Amazon DynamoDB. En este caso utilizaremos y configuraremos el servicio de Amazon S3 (Amazon Simple Storage Service).
2. Una vez que estamos en el menú de AWS nos dirigimos a **servicios/Seguridad, Identidad y Conformidad y  seleccionamos IAM**, en el menú que se encuentra a lado izquierdo y selecione Usuario; se le presentara sus usuarios creados si los tuviera en el caso que no vamos a crear uno, en la parte superior hacemos click en añadir usuario, escribimos el nombre de usuario y seleccionamos la casilla de  **Acceso mediante programación y Acceso a la Consola de administración de AWS**, seleccionamos contraseña personalizada y la introducimos; una vez echo esto hacemos click en  **siguiente:Permisos**.
[![Crear Usuario](https://elysiumists.s3.us-east-2.amazonaws.com/1crearUser.png "Crear Usuario")](https://elysiumists.s3.us-east-2.amazonaws.com/1crearUser.png "Crear Usuario")

3. En la siguiente interfaz seleccionamos **Añadir un usuario al grupo** y en el menú que le aparece seleccione **Crear un grupo**, si ya tiene uno puede escogerlo.
![NuevoGrupo](https://elysiumists.s3.us-east-2.amazonaws.com/2.png "CrearGrupo")
4. Vamos a poner el nombre del grupo y seleccionar la política **AmazonS3FullAccess** y hacemos click en **Crear un grupo**
![CrearGrupo](https://elysiumists.s3.us-east-2.amazonaws.com/3crearGrupo.png "CrearGrupo")
5. Nos aparece la interfaz anterior del usuario ya selecionado el grupo al que va a pertenecer y damos click en  **Siguiente:Etiquetas**, aquí nos pide que ingresemos una etiqueta con la cual nos sirven para organizar, hacer un seguimiento o controlar el acceso para este usuario.
![Agrgar Etiqueta](https://elysiumists.s3.us-east-2.amazonaws.com/3+copia.png "Agrgar Etiqueta")
5. Nos presenta todos nuestros datos que ingresamos anteriormente para poder revisar y poder continuar con la creación del usuario, si todo esta bien podemos seguir haciendo click en **Crear un usuario** caso contrario podemos volver hacia a tras y corregir.
![Revision ](https://elysiumists.s3.us-east-2.amazonaws.com/4revision+de+datos.png "Revision ")
6. Aparece un mensaje de confirmación que se a creado correctamente nuestro usuario y **sus credenciales de seguridad las cuales las deberá descargar o copiar por que solo esta vez se muestran y estan disponibles para descargar; estas claves las vamos a necesitar para configurar nuestra aplicación y también para registarlas en Heroku.**
![Mensaje Confirmación](https://elysiumists.s3.us-east-2.amazonaws.com/5.png "Mensaje Confirmación")
Pasamos a crear nuestro bucket(cubo donde se guardaran nuestros datos).
7. Nos dirigimos nuevamente a * **Servicios** y seleccionamos * **Almacenamiento/S3** en esta parte vamos a crear nuestro bucket haciendo click en **Crear Bucket** 
![Nuevo Bucket](https://elysiumists.s3.us-east-2.amazonaws.com/6bucket.png "Nuevo Bucket")
8. Colocamos el nombre de nuestro nuevo bucket, en la parte de Región debemos escoger la que mayor nos convenga y hacemos click en  **Siguiente**, luego seleccionamos los permisos y configuraciones de nuestro bucket dependiendo de lo que necesitemos, es recomendable dejar las opciones por defecto, lo siguiente es revisar nuestra información y configuración para así poder continuar.
9. Abrimos nuestro bucket y nos dirigimos a **permisos** y luego a políticas del **bucket** aparece un cuadro de edición y vamos a pegar lo siguiente:


    {
      "Version":"2012-10-17",
      "Statement":[{
        "Sid":"PublicReadGetObject",
            "Effect":"Allow",
          "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::nombredesubucket/*"
          ]
        }
      ]
    }
En la parte superior vamos a ver algo similar a esto:
Editor de políticas de cubo ARN: arn: aws: s3 ::: nombreejemplobucket
vamos a copiar la parte que comienza con "arn:" y guárdela en algún lugar.Este es el nombre completo oficial de nuestro grupo S3 que podemos usar para referirnos a nuestro grupo en cualquier lugar de AWS. Luego en el cuadro de edición vamos acopiar nuestro arn: en la linea  **Resource**.
![](https://elysiumists.s3.us-east-2.amazonaws.com/10.png)
10. Es hora de subir manualmente un archivo desde nuestro bucket, una vez que se haya subido lo podemos abrir y podremos ver toda la información  y al último tendremos la url de nuestro archivo. 
![Información ](https://elysiumists.s3.us-east-2.amazonaws.com/12.png "Información ")
11. Vamos agregar las credenciales de AWS en nuestra cuenta en Heroku 
![Agregando variables ](https://elysiumists.s3.us-east-2.amazonaws.com/clavesherouku.jpg "Agregando variables ")
12. Es momento de ir a nuestro settings.py en la aplicacion de Django y hacer las siguientes configuraciones
   

    DEFAULT_FILE_STORAGE = 'nombreproyecto.storage_backends.MediaStorage'
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')#para poner estas claves utilizo python decouple
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'nombre bucket'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'
    AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
    MEDIA_ROOT = ''
    DEFAULT_S3_PATH = 'media/'
    MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
13. Instalar los pip necesarios:
- `pip install boto3 `
- `pip install django-storages`
14. Debemos crear un archivo a nivel del setting.py con el nombre de storage_bakends.py en el cual sirve para subir nuestros archivos media con lo siguiente:


    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    
    
    class MediaStorage(S3Boto3Storage):
        location = 'media'
        file_overwrite = False
Con esto tendremos Heroku, Aws y Django integrados.
