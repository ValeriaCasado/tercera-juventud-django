from django.urls import path
from . import views
from django.shortcuts import render 

urlpatterns = [ 
    path('', lambda x: render(x, 'index.html'), name='inicio'),
    path('actividades', lambda x: render(x, 'actividades.html'), name='actividades'),
    path('informacion', lambda x: render(x, 'info.html'), name='informacion'),
    path('equipo', lambda x: render(x, 'equipo.html'), name='equipo'),
    path('contacto', lambda x: render(x, 'contacto.html'), name='contacto')
]
