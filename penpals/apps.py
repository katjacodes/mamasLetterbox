""" Default Configuration """

from django.apps import AppConfig


class PenpalsConfig(AppConfig):
    """ 64-bit integer """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'penpals'
