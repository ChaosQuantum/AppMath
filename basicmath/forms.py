from django import forms
from .models import SumaPrimos

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