from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo