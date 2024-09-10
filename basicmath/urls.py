from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='basicmath'),
    path('suma-primos/', views.calcular_suma_primos, name='calcular_suma_primos'),
]