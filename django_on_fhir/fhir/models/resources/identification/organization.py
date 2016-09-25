from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address
from ../../complex_types/human_name import HumanName
from ../../complex_types/telecom import Telecom

class Organization(models.model):
    active = models.BooleanField(blank=True)
    type = models.ForeignKey(CodeableConcept, blank=True)
    name = models.CharField(blank=True)
    partOf = models.ForeignKey('self', blank=True)

class OrganizationIdentifier(Identifier):
    organization = ManyToMany(Organization)

class OrganizationAddress(Address):
    organization = ManyToMany(Organization)

class OrganizationContact(models.model):
    organization = ManyToMany(Organization)
    provider = ManyToMany(Organization)
    purpose = models.ForeignKey(CodeableConcept, blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    address = models.ForeignKey(Address, blank=True)

class OrganizationContactTelecom(ContactPoint)
    organizationContact = ManyToMany(OrganizationContact)
