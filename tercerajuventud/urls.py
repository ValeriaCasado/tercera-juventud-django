from django.urls import path
from . import views
from django.shortcuts import render 

urlpatterns = [ 
    path('', lambda x: render(x, 'index.html'), name='inicio'),
    path('proyectos', lambda x: render(x, 'proyectos.html'), name='proyectos'),
    path('informacion', lambda x: render(x, 'info.html'), name='informacion'),
    path('privacidad', lambda x: render(x, 'privacidad.html'), name='privacidad'),
    path('contacto', lambda x: render(x, 'contacto.html'), name='contacto')
]
