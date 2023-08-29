from django.contrib import admin
from django.urls import path


# Me van a hacer un vista saludo, que diga 'Saludando a Koders'
# Su ruta http://127.0.0.1:8000/saludo/Benjamin

# Views
from .views import bienvenida, despedida, saludo, saludar_con_nombre

urlpatterns = [
    # Custom URLs
    path("despedida/", despedida),
    path("", bienvenida),
    path("saludo/", saludo),
    path("saludo/<str:nombre>", saludar_con_nombre),
]
