from django.shortcuts import render
import numpy as np
from django.http import HttpResponse
from .forms import CaidaLibreForm, EnfriamientoNewtonForm, CircuitoRCForm

def physics_index(request):
    return render(request, 'physics/physics_index.html')

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

def calcular_enfriamiento_newton(request):
    result=None
    if request.method=='POST':
        form=EnfriamientoNewtonForm(request.POST)
        if form.is_valid():
            T=form.cleaned_data['temperatura_inicial']
            T_amb=form.cleaned_data['temperatura_ambiente']
            k=form.cleaned_data['k_enfriamiento']
            dt=form.cleaned_data['inter_tiempo']
            tiempo=0

            while T > T_amb + 0.1:
                dT = -k * (T - T_amb) * dt
                T += dT
                tiempo += dt

            result = {
                'tiempo_total': tiempo,
                'temperatura_final': T,
            }

    else:
        form = EnfriamientoNewtonForm()

    return render(request, 'physics/enfriamiento_newton.html', {'form': form, 'result': result})

def calcular_circuito_rc(request):
    tiempos = []
    voltajes = []
    result = None
    
    if request.method == 'POST':
        form = CircuitoRCForm(request.POST)
        if form.is_valid():
            R = form.cleaned_data['R']
            C = form.cleaned_data['C']
            V_0 = form.cleaned_data['V_0']
            t_final = form.cleaned_data['t_final']
            dt = form.cleaned_data['dt']

            # Cálculo de voltajes en el condensador
            t = 0
            while t < t_final:
                Vc = V_0 * (1 - np.exp(-t / (R * C)))
                tiempos.append(t)
                voltajes.append(Vc)
                t += dt

            result = {
                'tiempos': tiempos,
                'voltajes': voltajes,
            }

    else:
        form = CircuitoRCForm()

    return render(request, 'circuito_rc.html', {'form': form, 'result': result,
    })