from __future__ import unicode_literals
from django.db import models

# import additional models
from simple_quantity import SimpleQuantity

class SampledData(models.model):
    # TODO: restrict data field to either strings or DATA_CHOICES
    DATA_CHOICES = ['E', 'U', 'L']

    origin = models.ForeignKey(SimpleQuantity, on_delete=models.CASCADE)
    period = models.DecimalField()
    factor = models.DecimalField(blank=True)
    lowerLimit = models.DecimalField(blank=True)
    upperLimit = models.DecimalField(blank=True)
    dimensions = models.PositiveField()
    data = models.CharField()
