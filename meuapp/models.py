from django.db import models

class Pessoa(models.Model):
        nome = models.CharField(max_length=30)
        sobrenome = models.CharField(max_length=30)
        idade = models.IntegerField(default=18) 

class Endereco(models.Model):
        cep = models.CharField(max_length=8)
        numero = models.CharField(max_length=10)

class profissao(models.Model):
        nome = models.CharField(max_length=30)
# Create your models here.
