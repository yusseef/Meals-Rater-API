from dj_static import Cling
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mealsrater.settings')

application = Cling(get_wsgi_application())
