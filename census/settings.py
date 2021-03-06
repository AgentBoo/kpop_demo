"""
Django settings for census project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, 'staticfiles')

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


'''
Import local settings from local_settings (local_settings is never committed to version control)
A specific local_settings is created for each dev and production environments.
'''

DEBUG = bool(os.getenv('DJANGO_DEBUG', False))

if DEBUG:
    try:
        from .local_settings import *

        SECRET_KEY = DJANGO_SECRET_KEY
        ALLOWED_HOSTS = LOCAL_HOSTS
        CORS_ORIGIN_WHITELIST = LOCAL_WHITELIST
        CSRF_TRUSTED_ORIGINS = LOCAL_TRUSTED_ORIGINS
        DATABASES = LOCAL_DATABASE
        DEBUG_PROPAGATE_EXCEPTIONS = True

    except ImportError:
        raise Exception('A local_settings.py file is required to run this project') 

else:
    import dj_database_url
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    # SECURITY WARNING: keep the secret key used in production secret!
    
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
   
    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)  
    }

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_BROWSER_XSS_FILTER = True  

    SECURE_CONTENT_TYPE_NOSNIFF = True  

    SECURE_SSL_REDIRECT = False  

    CSRF_COOKIE_SECURE = True  

    SESSION_COOKIE_SECURE = True 

    X_FRAME_OPTIONS = 'DENY'

    DEBUG_PROPAGATE_EXCEPTIONS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'widget_tweaks',
    'census.landing',
    'census.survey'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'census.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATES_DIR ],
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

WSGI_APPLICATION = 'census.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# WhiteNoise requires specifying the staticfiles dir
STATIC_ROOT = STATIC_DIR

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = []


# Installed apps 

