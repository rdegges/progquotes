"""Test settings and globals. These are optimized for running our test suites
ONLY.
"""


from common import *


########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TEST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

# Our custom test runner. This only tests our locally developed apps, as well as
# runs local-only coverage reports.
TEST_RUNNER = 'runner.LocalRunner'

# See: https://bitbucket.org/kmike/django-coverage/src/15fd7d2b7909/django_coverage/settings.py
COVERAGE_MODULE_EXCLUDES = ['tests$', 'settings$', 'urls$', 'locale$',
    'common.views.test', '__init__', 'django', 'migrations', 'fixtures',
    'templates',
]
COVERAGE_MODULE_EXCLUDES += DJANGO_APPS

# See: https://bitbucket.org/kmike/django-coverage/src/15fd7d2b7909/django_coverage/settings.py
COVERAGE_USE_STDOUT = True
########## END TEST CONFIGURATION
