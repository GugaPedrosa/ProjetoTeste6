from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    sinopse = models.TextField()

    GENERO_CHOICES = [
        ('acao', 'Ação'),
        ('comedia', 'Comédia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ficcao', 'Ficção Científica'),
    ]

    genero = models.CharField(
    max_length=20,
    choices=GENERO_CHOICES,
    default='drama'  # ou outro gênero que você quiser como padrão
    )

    def __str__(self):
        return self.titulo

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo