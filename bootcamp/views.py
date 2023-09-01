from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def list_koders(request):
    context = {
        "bootcamp": {"name": "Python", "module": "Django"},
        "koders": [
            {
                "name": "Benjamin",
                "generation": "1g",
                "bootcamp": "Python",
                "is_active": True,
            },
            {
                "name": "Luis",
                "generation": "1g",
                "bootcamp": "Python",
                "is_active": True,
            },
            {
                "name": "Irving",
                "generation": "1g",
                "bootcamp": "Python",
                "is_active": False,
            },
        ],
    }

    # Creamos template
    template = loader.get_template("bootcamp/templates/list_koders.html")

    return HttpResponse(template.render(context, request))


def get_koder(request, id):
    koders = [
        {"id": 0, "name": "Benjamin", "generation": "1g", "bootcamp": "Python"},
        {"id": 1, "name": "Luis", "generation": "1g", "bootcamp": "Python"},
        {"id": 2, "name": "Irving", "generation": "1g", "bootcamp": "Python"},
    ]

    founded_koder = [koder for koder in koders if koder["id"] == id]
    print("founded koderr -->>>>", founded_koder[0])
    return HttpResponse(f"FOunder koder ---> {founded_koder}")
