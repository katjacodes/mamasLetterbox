from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stationery, name='stationery'),
    path('<stationery_item_id>', views.stationery_detail, name='stationery_detail'),
]
