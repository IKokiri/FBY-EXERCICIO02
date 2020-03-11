from django.db import models

class Fisica(models.Model):
        cnpj = models.CharField(max_length=14)