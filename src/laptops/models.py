from django.db import models

class MacBook(models.Model):
    title = models.CharField(max_length=100)
    vendor = models.CharField(max_length=180)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
