from django.urls import path
from .views import home, whyarehere, cutestpets, exitscam, dummylogin ,dummydata, succes

urlpatterns = [
    path('', home,name="home"),
    path('Quienes-somos', whyarehere, name='Quienessomos'),
    path('Galeria', cutestpets, name='Galeria'),
    path('Compra', exitscam, name='Compra'),
    path('Ingreso', dummylogin, name='Form1'),
    path('Registro', dummydata, name='Form2'),
    path('Fin', succes, name='End'),
]