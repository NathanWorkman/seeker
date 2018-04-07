import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'seeker.seeker.settings'
# from seeker.seeker.settings import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = 'super-secret-key'
