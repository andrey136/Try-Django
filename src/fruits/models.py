from django.db import models

# Create your models here.

class Fruit(models.Model):
    title       = models.CharField(max_length=80),
    price       = models.DecimalField(2, 2),
    description = models.TextField(),
