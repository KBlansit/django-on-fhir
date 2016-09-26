from __future__ import unicode_literals
from django.db import models

# import additional models
from ../primitive_type/string import FhirString
from period import Period

class Address(models.Model):
    # TODO: AddressUse required for use
    # TODO: AddressType required for type

    USE_CHOICES = ['home', 'work', 'temp', 'old']
    TYPE_CHOICES = ['postal', 'physical', 'both']

    use = models.CharField(choices=USE_CHOICES, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, blank=True)
    text = models.CharField(blank=True)
    line = models.ManyToManyField(FhirString, blank=True, on_delete=models.CASCADE)
    city = models.CharField(blank=True)
    district = models.CharField(blank=True)
    state = models.CharField(blank=True)
    postalCode = models.CharField(blank=True)
    country = models.CharField(blank=True)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
