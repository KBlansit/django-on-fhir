from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address
from fhir.models.complex_types.human_name import HumanName
from fhir.models.complex_types.contact_point import ContactPoint

class Organization(models.Model):
    active = models.BooleanField(blank=True)
    type = models.ForeignKey(CodeableConcept, blank=True)
    name = models.CharField(blank=True)
    partOf = models.ForeignKey('self', blank=True)

class OrganizationIdentifier(Identifier):
    organization = models.ManyToManyField(Organization)

class OrganizationAddress(Address):
    organization = models.ManyToManyField(Organization)

class OrganizationContact(models.Model):
    organization = models.ManyToManyField(Organization)
    provider = models.ManyToManyField(Organization)
    purpose = models.ForeignKey(CodeableConcept, blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    address = models.ForeignKey(Address, blank=True)

class OrganizationContactTelecom(ContactPoint):
    organizationContact = models.ManyToManyField(OrganizationContact)
