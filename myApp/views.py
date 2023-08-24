from django.shortcuts import render


# Importar HttpResponse
from django.http import HttpResponse


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
    return HttpResponse(f"Hola {nombre}")
