# /solarProject/solarpv/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registerU/', views.reg, name='registeruser'),
    path('registerM/', views.regM, name='registermodule'),
    path('registerTL/', views.regTL, name='registertest'),
    path('testpage/', views.testp, name='testpage'),
    path('ratingpage/', views.rating, name='ratingpage'),
    path('registerPro/', views.regPro, name='registerproduct'),
]
