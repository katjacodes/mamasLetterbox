from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.penpal, name='penpal'),
    path('searchpenpals/', views.searchpenpals, name='searchpenpals'),
    path('add_penpal/', views.add_penpal, name='add_penpal'),
    path('edit_penpal/<id>/', views.edit_penpal, name='edit_penpal')
]
