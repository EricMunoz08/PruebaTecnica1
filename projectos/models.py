from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)