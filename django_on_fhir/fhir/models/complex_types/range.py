
from __future__ import unicode_literals
from django.db import models

# import additional models
from simple_quantity import SimpleQuantity

class Range(models.Model):
    # TODO: verify that high has in fact a higher value

    pass

class RangeSimpleHigh(SimpleQuantity):
    range = models.ForeignKey(Range, on_delete=models.CASCADE)

class RangeSimpleLow(SimpleQuantity):
    range = models.ForeignKey(Range, on_delete=models.CASCADE)
