from django.db import models

class Endereco(models.Model):
        cep = models.CharField(max_length=8)
        numero = models.CharField(max_length=10)
