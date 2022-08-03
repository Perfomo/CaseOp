from cgitb import handler
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Cases),
    path('get', views.GetGun),
    path('login', views.Login),
    path('itsatrap', views.Trap),
    path('Shadow', views.OpenCase),
    path('Cobblestone', views.OpenCase),
]

