from django.urls import path
from . import views

app_name = 'basicmath'

urlpatterns = [
    path('', views.basicmath_index, name='index'),
    path('suma-primos/', views.calcular_suma_primos, name='calcular_suma_primos'),
]