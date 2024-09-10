from django.shortcuts import render
from django.http import HttpResponse
from .forms import CaidaLibreForm

def index(request):
    return render(request, 'HttpResponse')

def calcular_caida_libre(request):
    result = None
    if request.method == 'POST':
        form = CaidaLibreForm(request.POST)
        if form.is_valid():
            g = form.cleaned_data['gravedad']
            c = form.cleaned_data['coef_resistencia']
            y = form.cleaned_data['altura_inicial']
            v = 0
            dt = form.cleaned_data['intervalo_tiempo']
            t = 0
            
            while y > 0:
                a = g - c * v
                v += a * dt
                y -= v * dt
                t += dt
                if y < 0:
                    y = 0

            result = {
                'time': t,
                'velocity': v,
                'height': y
            }
    else:
        form = CaidaLibreForm()

    return render(request, 'physics/caida_libre.html', {'form': form, 'result': result})