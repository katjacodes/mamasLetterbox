from dotenv import load_dotenv
load_dotenv()

from .base import *  # CAUTION: must come after load_dotenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tiph1-knz9m&1@s&y*&85dm34jdke^^x+uj!e78i5(*i(9orak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'katjacodes@gmail.com'