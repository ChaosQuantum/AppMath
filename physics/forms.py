from django import forms
from .models import CaidaLibre

class CaidaLibreForm(forms.ModelForm):
    class Meta:
        model = CaidaLibre
        fields = ['gravedad', 'coef_resistencia', 'altura_inicial', 'intervalo_tiempo']
        labels = {
            'gravedad': 'Gravedad (m/s^2)',
            'coef_resistencia': 'Coeficiente de Resistencia del Aire',
            'altura_inicial': 'Altura Inicial (m)',
            'intervalo_tiempo': 'Intervalo de Tiempo (s)'
        }
        widgets = {
            'gravedad': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '9.81'}),
            'coef_resistencia': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '0.47'}),
            'altura_inicial': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '100'}),
            'intervalo_tiempo': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '0.1'}),
        }

    def clean_gravedad(self):
        gravedad = self.cleaned_data.get('gravedad')
        if gravedad <= 0:
            raise forms.ValidationError('La gravedad debe ser un valor positivo.')
        return gravedad

    def clean_altura_inicial(self):
        altura_inicial = self.cleaned_data.get('altura_inicial')
        if altura_inicial < 0:
            raise forms.ValidationError('La altura inicial no puede ser negativa.')
        return altura_inicial

    def clean_intervalo_tiempo(self):
        intervalo_tiempo = self.cleaned_data.get('intervalo_tiempo')
        if intervalo_tiempo <= 0:
            raise forms.ValidationError('El intervalo de tiempo debe ser un valor positivo.')
        return intervalo_tiempo