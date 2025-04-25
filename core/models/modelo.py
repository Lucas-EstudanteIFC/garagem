from pickle import TRUE
from django.db import models

from django.template.defaultfilters import upper

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f"{upper(self.nome)}/{upper(self.marca)} ({self.id})"