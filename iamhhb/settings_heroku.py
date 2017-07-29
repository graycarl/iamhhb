# flake8: noqa
import os
import dj_database_url
from iamhhb.settings import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES['default'].update(dj_database_url.config(conn_max_age=50))
