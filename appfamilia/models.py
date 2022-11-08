from django.db import models


# Create your models here.

class listadefamiliares(models.Model):

    Nombre = models.CharField( max_length = 50 )
    edad   = models.IntegerField()
    fecha = models.DateField()
    