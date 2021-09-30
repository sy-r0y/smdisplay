
# Use apps.py module to store configuration settings for the 'boards' app

from django.apps import AppConfig


class BoardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boards'
