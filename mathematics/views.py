from django.shortcuts import render
import numpy as np

def index(request):
    return render(request, 'index.html', {})