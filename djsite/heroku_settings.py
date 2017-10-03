import os

NAME_DB = os.getenv('NAME_DB', 'Ringo')  #take name from heroku dash
USERNAME_DB = os.getenv('USERNAME_DB', 'George')  #take name from heroku dash
PASSWD_DB = os.getenv('PASSWD_DB', 'Paul')  #take name from heroku dash
HOST_DB = os.getenv('HOST_DB', 'John')  #take name from heroku dash
SALT_KEY = os.getenv('SALT_KEY', 'your_salt_key')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME_DB,
        'USER': USERNAME_DB,
        'PASSWORD': PASSWD_DB,
        'HOST': HOST_DB,
        'PORT': '5432',
    }
}