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

from organization import Organization

class Practitioner(models.Model):
    # TODO: AdministrativeGender required for gender

    GENDER_CHOICES = ['male', 'female', 'other', 'unknown']

    active = models.BooleanField(blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    birthDate = models.DateTimeField(blank=True)

class PractitionerIdentifier(Identifier):
    practitioner = ManyToManyField(Practitioner)

class PractitionerTelecom(ContactPoint):
    practitioner = ManyToManyField(Practitioner)

class PractitionerAddress(Address):
    practitioner = ManyToManyField(Practitioner)

class PractitionerPhoto(Attachment):
    practitioner = ManyToManyField(Practitioner)

class PractitionerRole(models.Model):
    practitioner = models.ManyToManyField(Practitioner)
    managingOrganization = models.ForeignKey(Organization, blank=True)
    role = models.ForeignKey(CodeableConcept, blank=True)
    specialty = models.ManyToManyField(CodeableConcept, blank=True)
    period = models.ForeignKey(Period, blank=True)

class PractitionerRoleLocation(models.Model):
    practitionerRole = models.ManyToManyField(PractitionerRole)
    location = models.ForeignKey(Location)

class PractitionerRoleHealthcareService(models.Model):
    practitionerRole = models.ManyToManyField(PractitionerRole)
    location = models.ForeignKey(HealthcareService)

class PractitionerQualification(models.Model):
    provider = models.ManyToManyField(Provider)
    identifier = models.ManyToManyField(Identifier, blank=True)
    code = models.ForeignKey(CodeableConcept, blank=True)
    period = models.ForeignKey(Period, blank=True)
    issuer = models.ForeignKey(Organization)

class PractitionerQualificationIdentifier(Identifier):
    PractitionerQualification = models.ManyToManyField(PractitionerQualification)

class PractitionerCommunication(CodeableConcept):
    # TODO: add in language suppoert

    provider = ManyToManyField(Provider)
