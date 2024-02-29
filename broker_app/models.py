from django.db import models

# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images')
    phone = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name