#Stardard libraries imports
from django.contrib import admin
from .models import *

admin.site.register([Local,Evento,Parceiro,Testemunho,Galeria,Programacao])
