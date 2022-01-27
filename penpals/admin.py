from django.contrib import admin
from .models import PenpalProfile

class PenpalProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user']


# Register your models here.
admin.site.register(PenpalProfile, PenpalProfileAdmin)
