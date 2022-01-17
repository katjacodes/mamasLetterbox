from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('writer/', views.writer, name='writer'),
    path('add_writer/', views.add_writer, name='add_writer'),
    path('edit_writer/<id>/', views.edit_writer, name='edit_writer')
]
