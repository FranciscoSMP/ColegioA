from django import forms
from .models import *

class EstudianteAForm(forms.ModelForm):
    class Meta:
        model = EstudiantesAutorizaciones
        fields = '__all__'

class EstudiantePForm(forms.ModelForm):
    class Meta:
        model = EstudiantesPublicaciones
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'