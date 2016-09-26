from __future__ import unicode_literals
from django.db import models

# import additional models
from simple_quantity import SimpleQuantity

class SampledData(models.Model):
    # TODO: restrict data field to either strings or DATA_CHOICES
    DATA_CHOICES = [
        ('E', 'E'),
        ('U', 'U'),
        ('L', 'L'),
    ]

    origin = models.ForeignKey(SimpleQuantity, on_delete=models.CASCADE)
    period = models.DecimalField(max_digits=20, decimal_places=5)
    factor = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    lowerLimit = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    upperLimit = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    dimensions = models.PositiveIntegerField()
    data = models.CharField(max_length=100)
