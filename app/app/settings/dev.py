from .base import *


DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = 'django-insecure-@!*n-io-u_6!wy$#q9m=sh42i$%%(m%j_5rg_zu==*!_83wix#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SLACK_BOT_ACCESS_TOKEN = os.getenv('SLACK_BOT_ACCESS_TOKEN')






