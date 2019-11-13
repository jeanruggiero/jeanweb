"""Staging app settings"""
import os
from .settings import *
import dj_database_url

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'),
                 'localhost',
                 'jeanweb-prod.herokuapp.com',
                 'jeanweb-staging.herokuapp.com',]
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

SECRET_KEY = os.environ.get('SECRET_KEY')


