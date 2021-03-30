from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4z7oz!5fth(bvf@t1+g9!^yol!xpa!*kjpnngy(8dc_23ax25%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    # ...
    'debug_toolbar',
]

STATIC_URL = '/static/'

MIDDLEWARE = MIDDLEWARE + [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

try:
    from .local import *
except ImportError:
    pass
