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
    
    def clean_cnpj(cnpj):
        cnpj = only_digits(cnpj)
        
        if len(cnpj) != 14:
            return False
        
        if cnpj == '00000000000000' or cnpj == '11111111111111' or cnpj == '22222222222222' or cnpj == '33333333333333' or cnpj == '44444444444444' or cnpj == '55555555555555' or cnpj == '66666666666666' or cnpj == '77777777777777' or cnpj == '88888888888888' or cnpj == '99999999999999':
            return False
        
        tamanho = len(cnpj) - 2
        numeros = cnpj[:tamanho]
        digitos = cnpj[tamanho:]
        soma = 0
        pos = tamanho - 7
        
        for i in range(tamanho):
            soma += int(numeros[i]) * pos
            pos -= 1
            if pos < 2:
                pos = tamanho - 1
        
        resultado = (soma * 10) % 11
        digito = 0 if resultado == 10 else resultado
        
        if digito != int(digitos[0]):
            return False
        
        tamanho += 1
        numeros = cnpj[:tamanho]
        soma = 0
        pos = tamanho - 7
        
        for i in range(tamanho):
            soma += int(numeros[i]) * pos
            pos -= 1
            if pos < 2:
                pos = tamanho - 1
        
        resultado = (soma * 10) % 11
        digito = 0 if resultado == 10 else resultado
        
        if digito != int(digitos[1]):
            return False
        
        return True

