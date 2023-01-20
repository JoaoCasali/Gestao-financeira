from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=20)
    dt_cadastro = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_movimentacao = models.DateField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    descricao = models.CharField(max_length=250)