from django.db import models

class SumaPrimos(models.Model):
    n = models.IntegerField(help_text="Ingresa el valor de n")
    suma_primos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Suma de primos menores que {self.n}"
    
class SecuenciaFibonacci(models.Model):
    n = models.IntegerField(help_text="Número de términos de la secuencia de Fibonacci")
    secuencia = models.JSONField(null=True, blank=True, help_text="Secuencia de Fibonacci generada")

    def __str__(self):
        return f"Secuencia de Fibonacci con {self.n} términos"