from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('searchpenpals/', views.searchpenpals, name='searchpenpals'),
    path('profile/', views.profile, name='profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('edit_profile/<id>/', views.edit_profile, name='edit_profile')
]
