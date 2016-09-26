from __future__ import unicode_literals
from django.db import models

class Quantity(models.Model):
    # TODO: verify that if a code unit is present, system is requied
    # TODO: QuantityComparator required for comparator

    COMPARATOR = [
        ('<', 'less than'),
        ('<=', 'less than or equal to'),
        ('>=', 'greater than or equal to'),
        ('>', 'greater than'),
    ]

    value = models.DecimalField(blank=True, null=True, max_digits=20,
        decimal_places=5)
    comparator = models.CharField(choices=COMPARATOR, blank=True, null=True,
        max_length=100)
    unit = models.CharField(blank=True, null=True, max_length=100)
    system = models.URLField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=100)
