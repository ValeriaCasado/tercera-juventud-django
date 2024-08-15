from django.shortcuts import render
from django.http import HttpResponse

import os


def inicio(request):
    debug_mode = os.environ.get('DJANGO_DEBUG')
    if debug_mode:
        return HttpResponse('All good in the hood')
    return HttpResponse("No environ variable detected ")


def proyectos(request):
    return HttpResponse("Proyectos")


def info(request):
    return HttpResponse("Info")