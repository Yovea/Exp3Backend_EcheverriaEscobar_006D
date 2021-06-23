from django.db import models

# Create your models here.
class Formulario(models.Model):
    rutFormulario = models.CharField(primary_key=True, max_length=12, blank=False, verbose_name='Rut Formulario')
    nombreFormulario = models.CharField(max_length=50, blank=False, verbose_name='Nombre Formulario')
    mailFormulario = models.CharField(max_length=60, blank=False, verbose_name='e-Mail de')
    passFormulario = models.CharField(max_length=100, blank=False, verbose_name='Contraseña')
    celnumFormulario = models.IntegerField( blank=False, verbose_name='Numero Telefonico')
    regionFormulario = models.CharField(max_length=50, blank=False, verbose_name='Region')
    ciudadFormulario = models.CharField(max_length=50, blank=False, verbose_name='Ciudad')
    comunaFormulario = models.CharField(max_length=50, blank=False, verbose_name='Comuna')
    dirFormulario = models.CharField(max_length=100, blank=False, verbose_name='Direccion')
    metodFormulario = models.CharField(max_length=100, blank=False, verbose_name='Metodo de pago')

    def __str__(self):
        return self.nombreFormulario