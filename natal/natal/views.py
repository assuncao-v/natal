# Standard libraries imports
from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
# Local apps imports
from .models import *

def index(request):
    context={
        'parceiros':Parceiro.objects.all(),
        'eventos':Evento.objects.all(),
        'testemunhos':Testemunho.objects.all(),   
    }
    return render(request, 'natal_app/index.html', context)

def galeria(request):
    context = {
        'fotos':Galeria.objects.all(),
    }
    return render(request, 'natal_app/galeria.html', context)

def programacao(request):
    context = {
        'programacoes':Programacao.objects.all(),
    }
    return render(request, 'natal_app/programacao.html', context)

def sobreNovaFriburgo(request):
    return render(request, 'natal_app/sobreNovaFriburgo.html')
