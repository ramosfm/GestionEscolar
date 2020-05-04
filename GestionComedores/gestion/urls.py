
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from gestion import views

urlpatterns = [
url(r"^grafico_solicitudes/$", views.grafico_solicitudes, name='grafico_solicitudes'),

]
