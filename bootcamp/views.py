from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

# Models
from bootcamp.models import Koder


def list_koders(request):
    koders = Koder.objects.all()

    return HttpResponse(koders)


def get_koder(request, id):
    # Traerse a un koder por su id

    return HttpResponse(f"FOunder koder ---> {founded_koder}")
