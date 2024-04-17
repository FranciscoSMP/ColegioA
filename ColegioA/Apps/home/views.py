from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import EstudiantePForm, EstudianteAForm, ComentarioForm, PublicacionForm, ArticuloForm 
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class ListadoView(TemplateView):
    template_name='listado.html'

class CrearEstudianteAView(CreateView):
    template_name='crearEstudianteA.html'
    form_class=EstudianteAForm
    success_url=reverse_lazy('home:listadoapp')

class CrearEstudiantePView(CreateView):
    template_name='crearEstudianteP.html'
    form_class=EstudiantePForm
    success_url=reverse_lazy('home:listadoapp')

class CrearArticuloView(CreateView):
    template_name='CrearArticulo.html'
    form_class=ArticuloForm
    success_url=reverse_lazy('home:listadoapp')

class CrearPublicacionView(CreateView):
    template_name='CrearPublicacion.html'
    form_class=PublicacionForm
    success_url=reverse_lazy('home:listadoapp')

class CrearComentarioView(CreateView):
    template_name='CrearComentario.html'
    form_class=ComentarioForm
    success_url=reverse_lazy('home:listadoapp')