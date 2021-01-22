import os

from django.core.wsgi import get_wsgi_application

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "awesomepower.settings")

application = get_wsgi_application()
