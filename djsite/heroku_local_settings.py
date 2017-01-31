import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'take_it_from_heroku',
        'USER': 'take_it_from_heroku',
        'PASSWORD': 'take_it_from_heroku',
        'HOST': 'take_it_from_heroku',
        'PORT': 'take_it_from_heroku',
    }
}

DEBUG = True