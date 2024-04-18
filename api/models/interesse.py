from django.db import models

class Interesse(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    animal_id = models.CharField(max_length=100)

    def __str__(self):
        return self.interessado