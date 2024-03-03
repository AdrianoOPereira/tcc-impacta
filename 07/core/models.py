from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    #sobre_nome = models.CharField(max_length=255)
    #cpf = models.CharField(max_length=14, unique=True, default='12345678901')  # Adicione um valor padrão aqui
    
    def __str__(self):
        return self.nome