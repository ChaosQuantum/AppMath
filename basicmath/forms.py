from django import forms
from .models import SumaPrimos, SecuenciaFibonacci

class SumaPrimosForm(forms.ModelForm):
    class Meta:
        model = SumaPrimos
        fields = ['n']
        labels = {
            'n': 'Ingresa el valor de n'
        }
        widgets = {
            'n': forms.NumberInput(attrs={'min': '1'}),
        }

class SecuenciaFibonacciForm(forms.ModelForm):
    class Meta:
        model=SecuenciaFibonacci
        fields = ['n']
        labels = {
            'n': 'Número de términos'
        }
        widgets={
            'n': forms.NumberInput(attrs={'step': '1', 'min': '1'}),
        }
        
    def clean_n(self):
        n = self.cleaned_data.get('n')
        if n <= 0:
            raise forms.ValidationError('El número de términos debe ser un entero positivo')
        return n