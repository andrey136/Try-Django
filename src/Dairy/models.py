from django.db import models

# Create your models here.
class Milk(models.Model):
    title = models.CharField(max_length=100)
    fat_perc = models.DecimalField(max_digits=4, decimal_places=2)