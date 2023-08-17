#Standard libraries imports
from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    class Meta:
        verbose_name_plural='Locais'
    
    endereco=models.TextField(max_length=256, verbose_name='Endereço do local')
    link=models.URLField(max_length=60, blank=True, null=True, verbose_name='Link do Google Maps para o local')

    def __str__(self):
        return self.endereco

class Evento(models.Model):
    titulo=models.CharField(max_length=50, verbose_name='Título do evento')
    banner=models.ImageField(upload_to='',verbose_name='Banner para divulgação do evento')
    data=models.DateField(auto_now=False, auto_now_add=False)
    descricao=models.TextField(max_length=150, verbose_name='Descrição do evento')

    def __str__(self):
        return self.titulo

class Parceiro(models.Model):
    nome=models.CharField(max_length=30, verbose_name='Nome do parceiro')
    logo=models.ImageField(upload_to='sponsors_logos', verbose_name='Logo do parceiro')
    site=models.URLField(max_length=60, null=True, verbose_name='URL do site do parceiro')

    def __str__(self):
        return self.nome

class Testemunho(models.Model):
    autor=models.CharField(max_length=50, verbose_name='Nome da pessoa')
    comentario=models.TextField(max_length=150, verbose_name='Comentário do testemunho')

    def __str__(self):
        return self.comentario

class Galeria(models.Model):
    imagem=models.ImageField(upload_to='galeria_imagens', verbose_name='Imagem da galeria')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.imagem

class Programacao(models.Model):
    class Meta:
        verbose_name='Programação'
        verbose_name_plural='Programações'

    evento=models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name='Evento')
    hora=models.TimeField(verbose_name='Horário do evento')
    local=models.ForeignKey(Local, on_delete=models.CASCADE, verbose_name='Local do evento')

    def __str__(self):
        return self.evento