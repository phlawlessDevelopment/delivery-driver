import math
import random
from django.db import models
# Create your models here.

class Settings(models.Model):
    mapbox_access_token = models.CharField(max_length=128)

class Address(models.Model):
    postcode = models.CharField( max_length=8)
    name = models.CharField( max_length=16)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def to_dict(self):
        return {
            'name': self.name,
            'postcode':self.postcode,
            'long':self.longitude,
            'lat':self.latitude,
        }
    
    @classmethod
    def get_random_item(cls):
        max_id = list(cls.objects.aggregate(models.Max('id')).values())[0]
        min_id = math.ceil(max_id*random.random())
        return cls.objects.filter(id__gte=min_id)[0]

    def __str__(self) -> str:
        return f'{self.name} - {self.postcode}'
    
