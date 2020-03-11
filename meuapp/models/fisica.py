from django.db import models

class Fisica(models.Model):
        cpf = models.CharField(max_length=11)