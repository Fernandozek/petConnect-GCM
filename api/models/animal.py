from django.db import models


class Animal(models.Model):
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    descricao = models.TextField()
    personalidade = models.TextField()
    adotado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.especie




