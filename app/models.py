from django.db import models

# Create your models here.

class Product(models.Model):
    date = models.DateField()
    popularity = models.IntegerField()
    rating = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img_name = models.CharField(max_length=100)
