from django.db.models import Sum, Count
from django.shortcuts import render

# Create your views here.
from gestion.models import Solicitante


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
