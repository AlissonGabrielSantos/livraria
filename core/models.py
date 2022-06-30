from django.db import models
from django.forms import URLField

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField() 

    def __str__(self):
        return self.nome