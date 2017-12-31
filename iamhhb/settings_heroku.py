# flake8: noqa
import os
import dj_database_url
from iamhhb.settings import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES['default'].update(dj_database_url.config(conn_max_age=50))
SECURE_SSL_REDIRECT = False

# Use pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Use postgresql storage
DEFAULT_FILE_STORAGE = 'postorage.storage.PostgreStorage'
INSTALLED_APPS = ['postorage.apps.PostorageConfig'] + INSTALLED_APPS
