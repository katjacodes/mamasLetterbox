from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.penpal_list, name='penpal_list'),
    path('me/', views.my_penpal_profile, name='penpal_me'),
    path('me/edit/', views.my_penpal_profile_edit, name='penpal_me_edit'),
    path('create/', views.penpal_create, name='penpal_create'),
    path('<int:penpal_id>/', views.penpal_detail, name='penpal_detail'),
]
