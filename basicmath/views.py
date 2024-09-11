from django.shortcuts import render
from .forms import SumaPrimosForm
from django.http import HttpResponse

def index(request):
    return render(request, HttpResponse)

def calcular_suma_primos(request):
    if request.method == 'POST':
        form = SumaPrimosForm(request.POST)
        if form.is_valid():
            suma_primos = form.save(commit=False)
            n = suma_primos.n
            suma_primos.suma_primos = 0

            # Lógica para calcular la suma de números primos menores que n
            for num in range(2, n):
                es_primo = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    suma_primos.suma_primos += num
            
            # Guardamos el resultado
            suma_primos.save()

            # Mostramos los resultados
            #return render(request, 'basicmath/resultado_primos.html', {'suma_primos': suma_primos})

    else:
        form = SumaPrimosForm()

    return render(request, 'basicmath/resultado_primos.html', {'form': form})