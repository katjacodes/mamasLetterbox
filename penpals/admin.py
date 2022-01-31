""" Models to appear in the Admin Console """

from django.contrib import admin
from .models import PenpalProfile


class PenpalProfileAdmin(admin.ModelAdmin):
    """ Model to hold penpal profile data """
    readonly_fields = ['user']


admin.site.register(PenpalProfile, PenpalProfileAdmin)
