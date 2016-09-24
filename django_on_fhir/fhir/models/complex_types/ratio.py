from __future__ import unicode_literals
from django.db import models

# import additional models
from quantity import Quantity

class Ratio(models.model):
    # TODO: verify existance state of both numerator and denominator is the same
    # TODO: if both nonexistant, there should be some extension present

    numerator = models.ForeignKey(Quantity, blank=True, on_delete=models.CASCADE)
    denominator = models.ForeignKey(Quantity, blank=True, on_delete=models.CASCADE)
