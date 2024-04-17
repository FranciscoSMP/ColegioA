"""
URL configuration for ColegioA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('listado/', ListadoView.as_view(), name='listadoapp'),
    path('crearEstA/,', CrearEstudianteAView.as_view(), name='crearEstAapp'),
    path('crearEstP/,', CrearEstudiantePView.as_view(), name='crearEstP'),
    path('crearArt/,', CrearArticuloView.as_view(), name='crearArtapp'),
    path('crearPub/,', CrearPublicacionView.as_view(), name='crearPubapp'),
    path('crearCome/,', CrearComentarioView.as_view(), name='crearComeapp'),
]
