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
SERVER_EMAIL = 'root@localhost'
########## END EMAIL CONFIGURATION


########## SECRET CONFIGURATION
# Our secret key.
SECRET_KEY = environ['SECRET_KEY']
########## END SECRET CONFIGURATION
