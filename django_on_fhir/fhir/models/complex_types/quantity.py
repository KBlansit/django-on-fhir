from __future__ import unicode_literals
from django.db import models

class Quantity(models.Model):
    # TODO: verify that if a code unit is present, system is requied
    # TODO: QuantityComparator required for comparator

    COMPARATOR = ['<', '<=', '>=', '>']

    value = models.DecimalField(blank=True)
    comparator = models.CharField(choices=COMPARATOR, blank=True)
    unit = models.CharField(blank=True)
    system = models.URLField(blank=True)
    code = models.CharField(blank=True)
