from django.urls import path
from . import views
#added include

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/', views.contactus, name='contactus'),
]
