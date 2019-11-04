import os
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost',
                 'jeanweb.herokuapp.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'jeanweb/static')]