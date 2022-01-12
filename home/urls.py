from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('penpals/', views.penpals, name='penpals'),
    path('profile/', views.profile, name='profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
]
