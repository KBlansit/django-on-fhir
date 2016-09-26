from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.primitive_types.string import FhirString
from period import Period

class Address(models.Model):
    # TODO: AddressUse required for use
    # TODO: AddressType required for type

    USE_CHOICES = [
        ('home', 'home'),
        ('work', 'work'),
        ('temp', 'temp'),
        ('old', 'old'),
    ]
    TYPE_CHOICES = [
        ('postal', 'period'),
        ('physical', 'physical'),
        ('both', 'both'),
    ]

    use = models.CharField(choices=USE_CHOICES, blank=True, null=True,
        max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, blank=True, null=True,
        max_length=100)
    text = models.TextField(blank=True, null=True)
    city = models.CharField(blank=True, null=True, max_length=100)
    district = models.CharField(blank=True, null=True, max_length=100)
    state = models.CharField(blank=True, null=True, max_length=100)
    postalCode = models.CharField(blank=True, null=True, max_length=100)
    country = models.CharField(blank=True, null=True, max_length=100)
    period = models.ForeignKey(Period, blank=True, null=True)

    # __unicode__ on Python 2
    def __str__(self):
        return self.text

class AddressFhirString(FhirString):
    address = models.ManyToManyField(Address)

    # __unicode__ on Python 2
    def __str__(self):
        return self.string
