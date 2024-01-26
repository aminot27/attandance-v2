"""Base settings to build other settings files upon."""
import json
import os
from datetime import timedelta
from pathlib import Path
import environ
from master_serv.environments import Environments

env = environ.Env()

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / 'apps'

# SECURITY WARNING: keep the secret key used in prod secret!
# SECRET_KEY = 'django-insecure-$7kr7yhn&r52m+mf(4xuou&xhchm!fn_r0r5t*rj3-c)k7h4vo'
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-$7kr7yhn&r52m+mf(4xuou&xhchm!fn_r0r5t*rj3-c)k7h4vo')
# Base
with open(str(ROOT_DIR / 'env.json')) as data_file:
    DEBUG = env.bool('DJANGO_DEBUG', json.load(data_file)['DEBUG'])
# DEBUG = env.bool('DJANGO_DEBUG', True)
print("IMPORTANT NOTE!!!!: ENVIRONMENT FLAG FOR DEBUG IS: " + str(DEBUG))
ALLOWED_HOSTS = ["*"]
# Language and timezone
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES
apps_names = ['default']
DATABASES = Environments().load_environment(apps_names=apps_names, is_lite_db=False)
print(DATABASES)
DATABASES['default']['ATOMIC_REQUESTS'] = True
# URLs
ROOT_URLCONF = 'master_serv.urls'

# WSGI
WSGI_APPLICATION = 'master_serv.wsgi.application'

# Users & Authentication
# AUTH_USER_MODEL = 'users.User'

# Apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'django_filters'
]
LOCAL_APPS = [
    'apps.master.apps.MasterConfig',
    'apps.warehouse.apps.WarehouseConfig',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Middlewares
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
CORS_ORIGIN_ALLOW_ALL = True
# Static files
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATIC_URL = '/static/'
# STATICFILES_DIRS = [str(APPS_DIR / 'static')]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media
# MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'
TEMPLATE_PATH = os.path.join(ROOT_DIR)
# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'loaders': (
                # 'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            # 'debug': DEBUG,
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
# Email
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# Admin
ADMIN_URL = 'admin/'
ADMINS = [
    ("""jcarlos""", 'josecarloshq@gmail.com'),
]
MANAGERS = ADMINS

# Celery
# INSTALLED_APPS += ['cride.taskapp.celery.CeleryAppConfig']
# if USE_TZ:
#     CELERY_TIMEZONE = TIME_ZONE
# CELERY_BROKER_URL = env('CELERY_BROKER_URL')
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERYD_TASK_TIME_LIMIT = 5 * 60
# CELERYD_TASK_SOFT_TIME_LIMIT = 60

# Django REST Framework
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'master_serv.utils.exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ]
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(hours=24),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
