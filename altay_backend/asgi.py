import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "altay_backend.settings")

django_application = get_asgi_application()
