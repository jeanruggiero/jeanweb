import os
from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'),
                 'localhost',
                 'jeanweb-prod.herokuapp.com',
                 'jeanmruggiero.com',
                 'www.jeanmruggiero.com']
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

SECRET_KEY = os.environ.get('SECRET_KEY')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'jean_site/static')]
