from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/human_name import HumanName
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address
from ../../complex_types/attachment import Attachment
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/period import Period

class Provider(models.model):
    # TODO: AdministrativeGender required for gender
    # TODO: custom signal to clean up database or add in CASCADE delete

    GENDER_CHOICES = ['male', 'female', 'other', 'unknown']

    identifier = models.ManyToMany(ProviderIdentifier, blank=True,
        on_delete=models.CASCADE)
    active = models.BooleanField(blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    telecom = models.ManyToMany(ProviderTelecom, blank=True,
        on_delete=models.CASCADE)
    address = models.ManyToMany(ProviderAddress, blank=True,
        on_delete=models.CASCADE)
    gender = models.ForeignKey(choices=GENDER_CHOICES, blank=True,
        on_delete=models.CASCADE)
    birthDate = models.DateTimeField(blank=True)
    photo = models.ManyToMany(ProviderPhoto, blank=True, on_delete=models.CASCADE)
    practitionerRole = models.ManyToMany(ProviderPractitionerRole, blank=True,
        on_delete=models.CASCADE)
    qualification = models.ManyToMany(ProviderQualification, blank=True,
        on_delete=models.CASCADE)
    communication = models.ManyToMany(ProviderCommunication, blank=True,
        on_delete=models.CASCADE)

class ProviderIdentifier(Identifier):
    pass

class ProviderTelecom(ContactPoint):
    pass

class ProviderAddress(Address):
    pass

class ProviderPhoto(Attachment):
    pass

class ProviderPractitionerRole(models.model):
    # TODO: refactor manaagingOrganization to refer to actual organization
    # TODO: refactor location to refer to actual location
    # TODO: refactor healthcareService to refer to actual healthcareService

    managingOrganization = models.CharField(blank=True)
    role = models.ForeignKey(CodeableConcept, blank=True)
    specialty = models.ManyToMany(CodeableConcept, blank=True)
    period = models.ForeignKey(Period, blank=True)
    # location
    # healthcareService

class ProviderQualification(models.model):
    # TODO: refactor issuer to refer to actual issuer

    identifier = models.ManyToMany(Identifier, blank=True)
    code = models.ForeignKey(CodeableConcept, blank=True)
    period = models.ForeignKey(Period, blank=True)
    # issuer = models.

class ProviderCommunication(CodeableConcept):
    # TODO: add in language suppoert
    pass
