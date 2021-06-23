from django.shortcuts import render
from .models import Formulario

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def whyarehere(request):
    return render(request, 'core/whyarehere.html')

def cutestpets(request):
    return render(request, 'core/cutestpets.html')

def exitscam(request):
    return render(request, 'core/exitscam.html')

def dummylogin(request):
    return render(request, 'core/dummylogin.html') ##

def viewer(request):

    formularios = Formulario.objects.all()
    datos = {
        'formularios': formularios
    }
    return render(request, 'core/viewer.html', datos) ##


def dummydata(request):
    return render(request, 'core/dummydata.html')

def succes(request):
    return render(request, 'core/succes.html')

