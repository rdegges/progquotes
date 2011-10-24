"""Production settings."""


from os import environ

from common import *


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[%s]' % SITE_NAME
EMAIL_USE_TLS = False
SERVER_EMAIL = environ['EMAIL_HOST_USER']
########## END EMAIL CONFIGURATION


########## SECRET CONFIGURATION
# Our secret key.
SECRET_KEY = environ['SECRET_KEY']
########## END SECRET CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    # Memcached cache. See
    # http://docs.djangoproject.com/en/1.3/topics/cache/#memcached for more
    # information.
    'default': {
       'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
       'LOCATION': environ['MEMCACHE_SERVERS'] + ':11211',
    }
}
########## END CACHE CONFIGURATION
