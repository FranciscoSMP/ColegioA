from django import forms
from .models import *

#login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length = 140, required = True)
    last_name = forms.CharField(max_length = 140, required = False)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',
        ) 