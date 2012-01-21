"""Production settings and globals."""


from os import environ
from sys import exc_info
from urlparse import urlparse

from S3 import CallingFormat

from common import *


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
try:
    url = urlparse(environ['DATABASE_URL'])
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
except:
    print 'Unexpected error:', exc_info()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'localhost:11211',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'ketama': True,
        }
    }
}
########## END CACHE CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME', '')

STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
########## END STORAGE CONFIGURATION


########## WEBSERVER CONFIGURATION
# See: http://gunicorn.org/
INSTALLED_APPS += (
    'gunicorn',
)
########## END WEBSERVER CONFIGURATION


########## SECRET KEY CONFIGURATION
SECRET_KEY = environ.get('SECRET_KEY', '')
########## END SECRET KEY CONFIGURATION
