from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

# Models
from bootcamp.models import Koder


def list_koders(request):
    context = {
        "koders": [
            {
                "name": "Ale",
                "is_active": True,
                "generation": "1g",
                "bootcamp": "Python",
            }
        ]
    }
    template = loader.get_template("templates/list_koders.html")
    return HttpResponse(template.render(context, request))


def get_koder(request, id):
    # Traerse a un koder por su id

    return HttpResponse(f"FOunder koder ---> {founded_koder}")
