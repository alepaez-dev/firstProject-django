from django.shortcuts import render


# Importar HttpResponse
from django.http import HttpResponse
from django.template import loader

# Las vistas son funciones


# Cliente -> Pide -> Request
# Servidor -> Responde -> Response
def bienvenida(request):
    # Responder
    return HttpResponse("Bienvenido koders!!")


def despedida(request):
    return HttpResponse("Despedida")


def saludo(request):
    return HttpResponse("Saludando a koders")


def saludar_con_nombre(request, nombre):
    context = {
        # "nombre": nombre,
        "apellido": "Hernandez",
    }  # Va a servir para pasarle info al template
    template = loader.get_template("templates/base.html")
    return HttpResponse(template.render(context, request))
