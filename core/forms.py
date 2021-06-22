from django import forms
from django.forms import ModelForm
from .models import Formulario

#hell.

class FormularioForm(ModelForm):

    class Meta:
        model = Formulario 
        fields =['rutFormulario', 'nombreFormulario', 'mailFormulario', 'passFormulario', 'celnumFormulario']
 