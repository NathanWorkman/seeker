import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'seeker.settings'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = 'super-secret-key'