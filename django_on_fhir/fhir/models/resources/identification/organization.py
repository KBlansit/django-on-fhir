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
    identifier = models.ManyToMany(OrganizationIdentifier, blank=True,
        on_delete=models.CASCADE)
    active = models.BooleanField(blank=True)
    type = models.ForeignKey(CodeableConcept, blank=True)
    name = models.CharField(blank=True)
    telecom = models.ManyToMany(OrganizationTelecom, blank=True,
        on_delete=models.CASCADE)
    address = models.ManyToMany(OrganizationAddress, blank=True,
        on_delete=models.CASCADE)
    partOf = models.ForeignKey('self', blank=True)

class OrganizationContact(models.model):
    purpose = models.ForeignKey(CodeableConcept, blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    telecom = models.ManyToMany(OrganizationTelecom, blank=True,
        on_delete=models.CASCADE)
    address = models.ForeignKey(Address, blank=True)

class OrganizationIdentifier(Identifier):
    pass

class OrganizationAddress(Address):
    pass

class OrganizationTelecom(ContactPoint)
    pass
