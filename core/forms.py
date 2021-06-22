from django import forms
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import widgets
from . models import Formulario

#hell.

class FormularioForm(ModelForm):

    class Meta:
        model = Formulario 
        fields =['rutFormulario', 'nombreFormulario', 'mailFormulario', 'passFormulario', 'celnumFormulario']
        labels ={
            'rutFormulario': 'Rut',
            'nombreFormulario': 'Nombre',
            'mailFormulario': 'Mail',
            'passFormulario': 'Password',
            'celnumFormulario': 'Celular',
        }
        widgets={
            'rutFormulario': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingresar rut',
                'id': 'rut'
                }
            ),
            'nombreFormulario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Nombre',
                    'id': 'Nombre'
                }
            ),
            'mailFormulario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Mail',
                    'id': 'Mail'
                }
            ),
            'passFormulario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Contraseña',
                    'id': 'Pass'
                }
            ),
            'celnumFormulario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar numero telefonico',
                    'id': 'Cel'
                }
            )
        }