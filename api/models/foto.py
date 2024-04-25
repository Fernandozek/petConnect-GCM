from django.db import models

class Foto(models.Model):
    arquivo = models.ImageField(upload_to='fotos/')
    animal = models.ForeignKey('api.Animal', on_delete=models.CASCADE)
   
