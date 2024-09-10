from django.db import models

class SumaPrimos(models.Model):
    n = models.IntegerField(help_text="Ingresa el valor de n")
    suma_primos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Suma de primos menores que {self.n}"