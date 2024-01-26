"""Development settings."""

from .base_setting import *  # NOQA
from .base_setting import env

# Base
DEBUG = True

# Security
# SECRET_KEY = env('DJANGO_SECRET_KEY', default='6+bzj=y4+jhih@6=gkk20#n(6zto15#n7og#b6ysmrgl1knz*y')
ALLOWED_HOSTS = [
    # "localhost",
    # "0.0.0.0",
    # "127.0.0.1",
    "*"
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_USE_TLS = True
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'host@gmail.com'
EMAIL_HOST_PASSWORD = 'hypfphfvqmtwmvuua'
EMAIL_PORT = 587
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window

# django-extensions
# INSTALLED_APPS += ['django_extensions']  # noqa F405
