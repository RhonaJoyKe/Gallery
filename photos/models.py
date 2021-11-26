from django.db import models
import datetime as dt

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/' ,blank=True)
    name = models.CharField(max_length =30)
    description = models.CharField()
    location = models.CharField(max_length = 10,blank =True)
    category=models.CharField()
class Catego