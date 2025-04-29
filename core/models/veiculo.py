
from django.db import models
from django.db.models.fields.related import ForeignKey


from core.models import Acessorio, Cor, Modelo

class Veiculo(models.Model):
    modelo = ForeignKey(Modelo, on_delete=models.PROTECT, related_name="carros")
    cor = ForeignKey(Cor, on_delete=models.PROTECT, related_name="carros")
    acessorios = models.ManyToManyField(Acessorio, related_name="carros", blank=True)
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True )


    def __str__ (self):
        return f"{self.modelo.nome} {self.cor.nome} {self.ano} ({self.id})"
