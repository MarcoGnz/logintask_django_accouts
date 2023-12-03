# logintask_django_accouts
Si has realizado una migración en el pasado, la migración fallará debido a la aplicación admin que Django tiene por defecto.
Para solucionar este problema, debes eliminar temporalmente la aplicación admin de tu proyecto.
Comenta una línea en settings.py y urls.py respectivamente como sigue

[loginApp/settings.py].
INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
]
-------------------------------------------------------------------------------------
[loginApp/urls.py].
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]

Una vez más, realice la migración.

$ python manage.py migrate
Con esto, User se registra de acuerdo con el contenido del usuario personalizado.
Después de migrar con éxito, devuelva a la normalidad las líneas de cada archivo que comentó anteriormente.

