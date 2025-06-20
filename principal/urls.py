from django.urls import path
from . import views
from django.http import HttpResponse
import random
urlpatterns	=	[
                path("hola/",views.hola),
                path('',	views.saludo),
                path("saludar_usuario/<str:nombre>/",views.saludar_usuario),
                path("numero/", views.numero),
                path("inicio",views.inicio, name="inicio"),
                path("curriculum",views.curriculum),]


