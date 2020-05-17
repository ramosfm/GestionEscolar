

from .settings import *

DEBUG = True
TEMPLATE = {
    'DEBUG': DEBUG,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aa',
        'USER': 'aa',
        'PASSWORD': 'aa',
        'HOST': 'aa',
        'PORT': 'aa',

    }
}
STATIC_ROOT = "/home/"

DATE_INPUT_FORMATS = ['%d/%m/%Y']
