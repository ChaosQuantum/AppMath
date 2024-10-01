from django.shortcuts import render
import numpy as np
from .forms import SumaPrimosForm, SecuenciaFibonacciForm
from .models import SecuenciaFibonacci
from django.http import HttpResponse

def basicmath_index(request):
    return render(request, 'basicmath/basicmath_index.html') 

def calcular_suma_primos(request):
    result = None 
    if request.method == 'POST':
        form = SumaPrimosForm(request.POST)
        if form.is_valid():
            suma_primos = form.save(commit=False)
            n = suma_primos.n
            suma_primos.suma_primos = 0

            for num in range(2, n):
                es_primo = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    suma_primos.suma_primos += num

            suma_primos.save()

            result = {
                'n': n,
                'suma_primos': suma_primos.suma_primos,
            }
    else:
        form = SumaPrimosForm()

    return render(request, 'basicmath/resultado_primos.html', {'form': form, 'result': result})

def calcular_secuencia_fibonacci(request):
    if request.method == 'POST':
        form = SecuenciaFibonacciForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            a, b = 0, 1
            secuencia = []
            for _ in range(n):
                secuencia.append(a)
                a, b = b, a + b
            
            resultado = SecuenciaFibonacci(n=n, secuencia=secuencia)
            resultado.save()
            
            return render(request, 'basicmath/fibonacci_resultado.html', {'form': form, 'result': resultado})
    else:
        form = SecuenciaFibonacciForm()
    
    return render(request, 'basicmath/fibonacci_resultado.html', {'form': form})