
from __future__ import unicode_literals
from django.db import models

# import additional models
from simple_quantity import SimpleQuantity

class Range(models.Model):
    # TODO: verify that high has in fact a higher value

    low = ForeignKey(SimpleQuantity, blank=True)
    high = ForeignKey(SimpleQuantity, blank=True)
