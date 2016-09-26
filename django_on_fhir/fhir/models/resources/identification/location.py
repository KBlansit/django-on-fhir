from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address

from organization import Organization

class Location(models.Model):
    # TODO: LocationStatus required for status
    # TODO: LocationMode required for mode

    STATUS_CHOICES = ['active', 'suspended', 'inactive']
    MODE_CHOICES = ['instance', 'kind']

    status = models.CharField(choices=STATUS_CHOICES, blank=True)
    name = models.CharField(blank=True)
    description = models.CharField(choices=STATUS_CHOICES, blank=True)
    mode = models.CharField(choices=MODE_CHOICES, blank=True)
    type = models.ForeignKey(CodeableConcept)
    managingOrganization = models.ForeignKey(Organization, blank=True)
    partOf = models.ForeignKey('self', blank=True)

class LocationIdentifier(Identifier):
    location = models.ManyToManyField(Location)

class LocationTelecom(ContactPoint):
    location = models.ManyToManyField(Location)

class LocationPosition(models.Model):
    location = models.ManyToManyField(Location)
    longitude = models.DecimalField()
    latitude = models.DecimalField()
    altitude = models.DecimalField(blank=True)
