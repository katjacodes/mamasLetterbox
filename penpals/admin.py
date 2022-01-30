from django.contrib import admin
from .models import PenpalProfile


class PenpalProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user']


admin.site.register(PenpalProfile, PenpalProfileAdmin)
