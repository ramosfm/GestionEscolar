"""
Django settings for GestionComedores project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0_-k3l#up3fyq6(br92kw#0v6lloq1h0i$yvd9h69@xf3w8uw!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'gestion',
    #'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GestionComedores.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GestionComedores.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'es'


USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'America/Argentina/Buenos_Aires'

DATE_FORMAT = "d/m/Y"

DATETIME_FORMAT = 'd/m/Y H:i'

DATE_INPUT_FORMATS = ['%d/%m/%Y']

DATETIME_INPUT_FORMATS = [
    '%m/%d/%Y %H:%M:%S',  # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',  # '10/25/2006 14:30'
    '%m/%d/%Y',  # '10/25/2006'
    '%c',  # '2008-01-02T10:30:00.000123+02:00'
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static
JET_DEFAULT_THEME = 'green'
STATIC_URL = '/static/'

STATIC_ROOT = '/home/facu/stormTech/comedores/GestionComedores/gestion/static'


JET_SIDE_MENU_ITEMS = [
    {
        'label': 'Usuarios', 'permissions': ['Admin'],
        'items': [
            {'name': 'auth.user', },
            {'name': 'auth.group', },
        ]
    },

    {
        'label': 'Gestion',
        'items': [
            {'name': 'gestion.escuela', 'label': 'Escuela', 'permissions': ['Admin']},
            {'name': 'gestion.solicitante', 'label': 'Solicitante'},
            {'name': 'gestion.distrito', 'label': 'Distrito', 'permissions': ['Admin']},
            {'name': 'gestion.necesidad', 'label': 'Opcion Necesidad', 'permissions': ['Admin']},
            {'name': 'gestion.necesidadsolicitante', 'label': 'Necesidades',},
        ]
    },
]

X_FRAME_OPTIONS = 'ALLOWALL'
