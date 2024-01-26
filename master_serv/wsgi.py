"""
WSGI config for master_serv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "master_serv"))
print('***USING WSGI CONFIG WITH DEV SETTING***')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'master_serv.settings.dev_setting')

# Use this config if you want run with django dev server
application = get_wsgi_application()
# Use this config if you want run in a docker container
# application = get_asgi_application()
