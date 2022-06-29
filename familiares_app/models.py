from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=250);
    edad = models.IntegerField()