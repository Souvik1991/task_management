# -*- coding: utf-8 -*-
from .base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'task_management',
		'USER': 'souvik', #Replace it before you start
		'PASSWORD': 'almond123', #Replace it before you start
		'HOST': '127.0.0.1',
		'PORT': ''
	}
}
