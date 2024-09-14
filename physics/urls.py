from django.urls import path
from . import views

app_name = 'physics'

urlpatterns = [ 
    path('', views.physics_index, name='index'),
    path('caida-libre/', views.calcular_caida_libre, name='calcular_caida_libre'),
    path('enfriamiento-newton/', views.calcular_enfriamiento_newton, name='calcular_enfriamiento_newton'),
]