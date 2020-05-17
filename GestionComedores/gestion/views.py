import csv

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Sum, Count
from django.shortcuts import render

# Create your views here.
from gestion.models import Solicitante, Escuela


def grafico_solicitudes(request):
    labels = []
    data = []
    queryset = Solicitante.objects.values('fecha').annotate(Count('fecha'))
    for solicitante in queryset:
        labels.append(solicitante['fecha'])
        data.append(solicitante['fecha__count'])

    return render(request, 'grafico.html', {
        'labels': labels,
        'data': data,
    })


@login_required
def cargar_escuelas(request):
    with open('escuelas.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        my_group = Group.objects.get(name='Escuela')
        for row in spamreader:
             if not Escuela.objects.filter(cue=row[1]).exists() and not row[2] == 'Nombre':
                 esc = Escuela()
                 usr = User()
                 usr.username = row[1]
                 usr.is_staff = True
                 usr.set_password(row[1][0:4]+'2020')
                 usr.save()
                 my_group.user_set.add(usr)
                 esc.usuario = usr
                 esc.cue = row[1]
                 esc.nombre = row[2]
                 esc.ambito = row[4]
                 esc.direccion = row[5]
                 esc.distrito_id = 1
                 esc.ciudad = row[10]
                 esc.telefono = row[8]
                 esc.save()
