from django import forms
from .models import CaidaLibre, EnfriamientoNewton

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
    
class EnfriamientoNewtonForm(forms.ModelForm):
    class Meta:
        model=EnfriamientoNewton
        fields={'temperatura_inicial', 'temperatura_ambiente', 'k_enfriamiento', 'inter_tiempo'}
        labels={
            'temperatura_inicial':'Temperatura inicial del objeto (°C)', 
            'temperatura_ambiente':'Temperatura ambiente (°C)', 
            'k_enfriamiento':'Constante de enfriamiento k', 
            'inter_tiempo':'Intervalo de tiempo dt (s)'
        }
        widgets={
            'temperatura_inicial': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ejemplo: 100'}),
            'temperatura_ambiente': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ejemplo: 25'}),
            'k_enfriamiento': forms.NumberInput(attrs={'step': '0.001', 'placeholder': 'Ejemplo: 0.02'}),
            'inter_tiempo': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ejemplo: 1'}),
        }

    def clean_temperatura_inicial(self):
        temperatura_inicial=self.cleaned_data.get('temperatura_inicial')
        if temperatura_inicial <=0:
            raise forms.ValidationError('La temperatura inicial debe ser un valor positivo')
        return temperatura_inicial
    
    def clean_temperatur_ambiente(self):
        temperatura_ambiente=self.cleaned_data.get('temperatura_ambiente')
        if temperatura_ambiente <= 0:
            raise forms.ValidationError('La temperatura ambiente debe ser un valor positivo')
        return temperatura_ambiente
    
    def clean_k_enfriamiento(self):
        k_enfriamiento=self.cleaned_data.get('k_enfriamiento')
        if k_enfriamiento <= 0:
            raise forms.ValidationError('La constante de enfriamiento debe ser un valor positivo')
        return k_enfriamiento
    
    def clean_inter_tiempo(self):
        inter_tiempo=self.cleaned_data.get('inter_tiempo')
        if inter_tiempo <= 0:
            raise forms.ValidationError('El intervalo de tiempo debe de ser un valor positivo')
        return inter_tiempo