from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.primiative_types.string import FhirString
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

    use = models.CharField(choices=USE_CHOICES, blank=True, max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, blank=True, max_length=100)
    text = models.TextField(blank=True)
    city = models.CharField(blank=True, max_length=100)
    district = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    postalCode = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    period = models.ForeignKey(Period, blank=True)

class AddressFhirString(FhirString):
    address = models.ManyToManyField(Address)
