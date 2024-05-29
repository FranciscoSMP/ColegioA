from django.contrib import admin
from .models import EstudiantesAutorizaciones, EstudiantesPublicaciones, Articulos, Publicaciones, Comentarios, Usuario
# Register your models here.

admin.site.register(EstudiantesAutorizaciones)
admin.site.register(EstudiantesPublicaciones)
admin.site.register(Articulos)
admin.site.register(Publicaciones)
admin.site.register(Comentarios)
admin.site.register(Usuario)