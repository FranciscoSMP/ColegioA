from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import * 
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class CrearEstudianteAView(CreateView):
    template_name='crearEstudianteA.html'
    form_class=EstudianteAForm
    success_url=reverse_lazy('home:listadoapp')

class CrearEstudiantePView(CreateView):
    template_name = 'CrearEstudianteP.html'
    form_class = EstudiantePForm
    success_url = reverse_lazy('home:listadoapp')

class CrearArticuloView(CreateView):
    template_name = 'CrearArticulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:listadoapp')

class CrearPublicacionView(CreateView):
    template_name = 'CrearPublicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('home:listadoapp')

class CrearComentarioView(CreateView):
    template_name = 'CrearComentario.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:listadoapp')

class ListarEstudiantesPView(ListView):
    template_name = 'listado.html'
    model = EstudiantesPublicaciones
    context_object_name = 'estudiantespublicaciones_list'

    def get_query(self):
        return EstudiantesPublicaciones.objects.all()

class ListarEstudiantesAView(ListView):
    template_name = 'listadoA.html'
    model = EstudiantesAutorizaciones
    context_object_name = 'estudiantesautorizaciones_list'

    def get_query(self):
        return EstudiantesAutorizaciones.objects.all() 

class ListarComentarios(ListView):
    template_name = 'listadoC.html'
    model = Comentarios
    context_object_name = 'comentarios_list'

    def get_query(self):
        return Comentarios.objects.all()

class ListarArticulos(ListView):
    template_name = 'listadoArti.html'
    model = Articulos
    context_object_name = 'articulos_list'

    def get_query(self):
        return Articulos.objects.all() 

class ListarPublicaciones(ListView):
    template_name = 'listadoP.html'
    model = Publicaciones
    context_object_name = 'publicaciones_list'

    def get_query(self):
        return Publicaciones.objects.all() 