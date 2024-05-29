from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .forms import * 
from django.urls import reverse_lazy

#Login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class CrearEstudianteAView(CreateView):
    template_name='CrearEstudianteA.html'
    form_class=EstudianteAForm
    success_url=reverse_lazy('home:listadoAapp')

class CrearEstudiantePView(CreateView):
    template_name = 'CrearEstudianteP.html'
    form_class = EstudiantePForm
    success_url = reverse_lazy('home:listadoapp')

class EditarEstudiantePView(UpdateView):
    template_name = 'editarEstudianteP.html'
    model = EstudiantesPublicaciones
    form_class = EstudiantePForm
    success_url = reverse_lazy('home:listadoapp')

class EditarEstudianteAView(UpdateView):
    template_name = 'editarEstudianteA.html'
    model = EstudiantesAutorizaciones
    form_class = EstudianteAForm
    success_url = reverse_lazy('home:listadoAapp')

class EditarArticuloView(UpdateView):
    template_name = 'editarArticulo.html'
    model = Articulos
    form_class = ArticuloForm
    success_url = reverse_lazy('home:listadoArtiapp')

class EditarPublicacionView(UpdateView):
    template_name = 'editarPublicacion.html'
    model = Publicaciones
    form_class = PublicacionForm
    success_url = reverse_lazy('home:listadoPapp')

class EditarComentarioView(UpdateView):
    template_name = 'editarComentario.html'
    model = Comentarios
    form_class = ComentarioForm
    success_url = reverse_lazy('home:listadoCapp')

class CrearArticuloView(CreateView):
    template_name = 'CrearArticulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:listadoArtiapp')

class CrearPublicacionView(CreateView):
    template_name = 'CrearPublicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('home:listadoPapp')

class CrearComentarioView(CreateView):
    template_name = 'CrearComentario.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:listadoCapp')

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')

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

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            NombreUsuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            usuario = authenticate(username=NombreUsuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return redirect("home:homeapp")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def Logout(request):
    logout(request)
    return redirect("home:loginapp")