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
from django.contrib.auth.decorators import login_required

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('listado/', login_required(ListarEstudiantesPView.as_view()), name='listadoapp'),
    path('listadoA/', login_required(ListarEstudiantesAView.as_view()), name='listadoAapp'),
    path('listadoC/', login_required(ListarComentarios.as_view()), name='listadoCapp'),
    path('listadoArti/', login_required(ListarArticulos.as_view()), name='listadoArtiapp'),
    path('listadoP/', login_required(ListarPublicaciones.as_view()), name='listadoPapp'),
    path('editarEP/<int:pk>', EditarEstudiantePView.as_view(), name = 'editarEApp'),
    path('editarEA/<int:pk>', EditarEstudianteAView.as_view(), name = 'editarEAApp'),
    path('editarArt/<int:pk>', EditarArticuloView.as_view(), name = 'editarArtiApp'),
    path('editarPub/<int:pk>', EditarPublicacionView.as_view(), name = 'editarPubApp'),
    path('editarCome/<int:pk>', EditarComentarioView.as_view(), name = 'editarComeApp'),
    path('crearEstA/', login_required(CrearEstudianteAView.as_view()), name='crearEstAapp'),
    path('crearEstP/', login_required(CrearEstudiantePView.as_view()), name='crearEstP'),
    path('crearArt/', login_required(CrearArticuloView.as_view()), name='crearArtapp'),
    path('crearPub/', login_required(CrearPublicacionView.as_view()), name='crearPubapp'),
    path('crearCome/', login_required(CrearComentarioView.as_view()), name='crearComeapp'),
    path('registro/', login_required(RegistroView.as_view()), name='registroApp'),
    path('login/', Login, name = 'loginapp'),
    path('logout/', Logout, name = 'logoutapp')
]
    