# /solarProject/solarpv/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registerU/', views.regU, name='registeruser'),
    path('registerM/', views.regM, name='registermodule'),
]
