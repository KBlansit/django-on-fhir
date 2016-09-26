from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address

from organization import Organization

class LocationType(CodeableConcept):
    pass

class Location(models.Model):
    # TODO: LocationStatus required for status
    # TODO: LocationMode required for mode

    STATUS_CHOICES = [
        ('active', 'active'),
        ('suspended', 'suspended'),
        ('inactive', 'inactive'),
    ]
    MODE_CHOICES = [
        ('instance', 'instance'),
        ('kind', 'kind'),
    ]

    status = models.CharField(choices=STATUS_CHOICES, blank=True, null=True,
        max_length=100)
    name = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(choices=STATUS_CHOICES, blank=True, null=True,
        max_length=1000)
    mode = models.CharField(choices=MODE_CHOICES, blank=True, null=True,
        max_length=100)
    type = models.ManyToManyField(LocationType)
    managingOrganization = models.ForeignKey(Organization, blank=True)
    partOf = models.ForeignKey('self', blank=True)

class LocationIdentifier(Identifier):
    location = models.ManyToManyField(Location)

class LocationTelecom(ContactPoint):
    location = models.ManyToManyField(Location)

class LocationPosition(models.Model):
    location = models.ManyToManyField(Location)
    longitude = models.DecimalField(max_digits=20, decimal_places=5)
    latitude = models.DecimalField(max_digits=20, decimal_places=5)
    altitude = models.DecimalField(max_digits=20, decimal_places=5,
        blank=True, null=True)
