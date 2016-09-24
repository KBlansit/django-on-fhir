from __future__ import unicode_literals
from django.db import models

# import additional models
from period import Period

class Address(models.model):
    use = models.CharField()
    type = models.CharField()
    text = models.CharField()
    line = models.CharField()
    city = models.CharField()
    district = models.CharField()
    state = models.CharField()
    postalCode = models.CharField()
    country = models.CharField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
