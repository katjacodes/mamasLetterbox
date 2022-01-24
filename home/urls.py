from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('searchprofiles/', views.searchprofiles, name='searchprofiles'),
    path('profile/', views.profile, name='profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]
