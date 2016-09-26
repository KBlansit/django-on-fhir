from __future__ import unicode_literals
from django.db import models

# import additional models
from quantity import Quantity

class Ratio(models.Model):
    # TODO: verify existance state of both numerator and denominator is the same
    # TODO: if both nonexistant, there should be some extension present

    pass

class RatioNumerator(Quantity):
    ratio = models.ForeignKey(Ratio, on_delete=models.CASCADE)
    
class Ratiodenominator(Quantity):
    ratio = models.ForeignKey(Ratio, on_delete=models.CASCADE)
