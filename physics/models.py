from django.db import models

class CaidaLibre(models.Model):
    gravedad = models.FloatField(help_text="Gravedad (m/s^2)")
    coef_resistencia = models.FloatField(help_text="Coeficiente de resistencia del aire")
    altura_inicial = models.FloatField(help_text="Altura inicial (m)")
    intervalo_tiempo = models.FloatField(help_text="Intervalo de tiempo (s)")
    tiempo_total = models.FloatField(null=True, blank=True)
    velocidad_final = models.FloatField(null=True, blank=True)
    altura_final = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Caída desde {self.altura_inicial} m con g={self.gravedad} m/s^2"