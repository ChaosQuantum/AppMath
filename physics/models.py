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
    
class EnfriamientoNewton(models.Model):
    temperatura_inicial=models.FloatField(help_text="Temperatura inicial del objeto (°C)")
    temperatura_ambiente=models.FloatField(help_text="Temperatura ambiente (°C)")
    k_enfriamiento=models.FloatField(help_text="Constante de enfriamiento k")
    inter_tiempo=models.FloatField(help_text="Intervalo de tiempo dt (s)")

    def __str__(self):
        return f"Enfriamiento desde {self.temperatura_inicial}°C"
    
class CircuitoRC(models.Model):
    R = models.FloatField(help_text="Resistencia (ohmios)")
    C = models.FloatField(help_text="Capacitancia (faradios)")
    V_0 = models.FloatField(help_text="Voltaje de la fuente (voltios)")
    t_final = models.FloatField(help_text="Tiempo final (segundos)")
    dt = models.FloatField(help_text="Intervalo de tiempo (segundos)")

    def __str__(self):
        return f"Circuito RC: R={self.R}, C={self.C}, V0={self.V_0}"