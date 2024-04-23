from django.db import models

class Interesse(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)   
    animal = models.ForeignKey('api.Animal', on_delete=models.CASCADE)
    
 
    def __str__(self):
        return str(self.id)