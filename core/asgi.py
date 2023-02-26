import os

from django.core.asgi import get_asgi_application
from core.settings import base

enviroment = 'core.settings.local' if base.DEBUG else 'core.settings.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', enviroment)

application = get_asgi_application()
