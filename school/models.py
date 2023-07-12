from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    pincode = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    def __str__(self):
        return str(self.name)
