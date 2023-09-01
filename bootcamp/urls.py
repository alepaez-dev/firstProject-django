from django.urls import path

from .views import list_koders, get_koder

urlpatterns = [path("koders/", list_koders), path("koders/<int:id>/", get_koder)]
