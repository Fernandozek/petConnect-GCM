from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOISE_TIPO_USUARIO = (
        ('1', 'ONG'),
        ('2', 'VOLUNTARIO'),
    )
    tipo_usuario = models.CharField(max_length=30, blank=True, null=True, choices=CHOISE_TIPO_USUARIO)
    nome = models.CharField(max_length=30, blank=True, null=True)
    endereco = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=30, blank=True, null=True)
    contato = models.CharField(max_length=30, blank=True, null=True)
    historico = models.TextField(max_length=500, blank=True, null=True)
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.nome

