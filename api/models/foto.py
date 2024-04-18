from django.db import models

class Foto(models.Model):
    arquivo = models.ImageField(upload_to='fotos/')
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    animal_id = models.CharField(max_length=100)

    def __str__(self):
        return self.foto