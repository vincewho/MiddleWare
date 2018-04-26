# /solarProject/solarpv/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registerU/', views.reg, name='registeruser'),
    path('registerC/', views.regC, name='registercompany'),
    path('registerTL/', views.regTL, name='registertest'),
    path('pvmodule/', views.pvModule, name='pvmodulepage'),
    path('pvmodule/testpage/', views.testp, name='testpage'),
    path('registerPro/', views.regPro, name='registerproduct'),
]
