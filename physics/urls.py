from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='physics'),
    path('caida-libre/', views.calcular_caida_libre, name='calcular_caida_libre'),
]