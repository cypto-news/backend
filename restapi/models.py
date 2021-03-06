from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import TextField


class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField(max_length=10)
    source = models.CharField(max_length=60)
    rhn =  models.IntegerField(default=1,validators=[MaxValueValidator(10), MinValueValidator(1)])
    urlImg = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class Market(models.Model):
    coin = models.TextField()
    date = models.DateField(max_length=10)
    price =  models.FloatField()
    logo_coin = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class Predict(models.Model):
    coin = models.TextField()
    date = models.DateField(max_length=10)
    prediction =  models.IntegerField(default=1,validators=[MaxValueValidator(100000000), MinValueValidator(1)])
    logo_coin = models.CharField(max_length=1000)

    def __str__(self):
        return self.title