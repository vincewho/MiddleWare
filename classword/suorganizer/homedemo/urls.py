# homedemo/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homedemo, name='homedemomain'),
    path('sport/', views.sport, name='sport'),
]
