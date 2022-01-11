from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class News(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    date = models.DateField(max_length=10)
    source = models.CharField(max_length=60)
    rhn =  models.IntegerField(default=1,validators=[MaxValueValidator(10), MinValueValidator(1)])
    urlImg = models.CharField(max_length=1000)

    def __str__(self):
        return self.title