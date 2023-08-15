from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True) 

class ReservaDeBanho(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    dia_reserva = models.DateField()
    observacoes = models.TextField()