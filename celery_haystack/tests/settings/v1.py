from os import path, environ, pardir

TEST_ROOT = path.abspath(path.join(path.dirname(__file__), pardir))

INSTALLED_APPS = [
    'django_nose',
    'haystack',
    'djcelery',
    'celery_haystack',
    'celery_haystack.tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

HAYSTACK_SITECONF = 'celery_haystack.tests.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = path.join(TEST_ROOT, 'whoosh_index')

BROKER_TRANSPORT = "memory"
CELERY_ALWAYS_EAGER = True
CELERY_IGNORE_RESULT = True
CELERYD_LOG_LEVEL = "DEBUG"
CELERY_DEFAULT_QUEUE = "celery-haystack"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'