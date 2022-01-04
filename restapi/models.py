from django.db import models

# Create your models here.
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    date = models.DateField(max_length=10)
    urlImg = models.CharField(max_length=1000)

    def __str__(self):
        return self.title