import os

from django.core.wsgi import get_wsgi_application
from core.settings import base

enviroment = 'core.settings.local' if base.DEBUG else 'core.settings.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', enviroment)

application = get_wsgi_application()
