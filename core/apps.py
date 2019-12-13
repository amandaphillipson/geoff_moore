from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

‘core.apps.CoreConfig’

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog', 
]