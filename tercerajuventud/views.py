from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

import os


def inicio(request):

    return render(request, 'index.html')


def proyectos(request):
    return HttpResponse("Proyectos")


def info(request):
    return HttpResponse("Info")