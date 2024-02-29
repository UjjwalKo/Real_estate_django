from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from broker_app.models import Broker

# Create your models here.
class Listing(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.DO_NOTHING)         #Broker ko naam lera aauna yo use garya yaha
    title = models.CharField(max_length=180)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)          # Blank=True mean this is optional to fillup
    price = models.IntegerField(validators=[MinValueValidator(0)])
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])  #MinValueValidator(0) ensures that the value of each field is greater than or equal to 0.
    bathrooms = models.IntegerField(validators=[MinValueValidator(0)])
    parking = models.IntegerField(validators=[MinValueValidator(0)])
    sqft = models.IntegerField(validators=[MinValueValidator(0)])
    image_com = models.ImageField(upload_to='images')
    image_1 = models.ImageField(upload_to='images', blank=True)   #Optional
    image_2 = models.ImageField(upload_to='images', blank= True)   #Optional
    is_published = models.BooleanField(default = True)
    post_date = models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.title