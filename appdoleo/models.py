from django.db import models

# Create your models here.

class Tenistas(models.Model):
  title = models.CharField(max_length=50)
  nome = models.CharField(max_length=50)
  genero = models.CharField(max_length=50)
  patrocinio = models.CharField(max_length=50)
  

class Torneios(models.Model):
  title = models.CharField(max_length=50)
  nomeTorneio = models.CharField(max_length=50)
  nomeJogador = models.CharField(max_length=50)
  vitorias = models.IntegerField()


class Tabela(models.Model):
  nome = models.CharField(max_length=50)
  participa = models.IntegerField()
  vitorias = models.IntegerField()

