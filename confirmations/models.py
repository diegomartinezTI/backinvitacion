from django.db import models

class Confirmations(models.Model):
    familia = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.familia
