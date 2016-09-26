from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.human_name import HumanName
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address
from fhir.models.complex_types.attachment import Attachment
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.period import Period

from organization import Organization
from location import Location
from healthcare_service import HealthcareService

class Practitioner(models.Model):
    # TODO: AdministrativeGender required for gender

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('unknown', 'unknown'),
    ]

    active = models.NullBooleanField(blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    birthDate = models.DateTimeField(blank=True)

class PractitionerIdentifier(Identifier):
    practitioner = models.ManyToManyField(Practitioner)

class PractitionerTelecom(ContactPoint):
    practitioner = models.ManyToManyField(Practitioner)

class PractitionerAddress(Address):
    practitioner = models.ManyToManyField(Practitioner)

class PractitionerPhoto(Attachment):
    practitioner = models.ManyToManyField(Practitioner)

class PractitionerRoleType(CodeableConcept):
    pass

class PractionRoleSpecialty(CodeableConcept):
    pass

class PractitionerRole(models.Model):
    practitioner = models.ManyToManyField(Practitioner)
    managingOrganization = models.ForeignKey(Organization, blank=True)
    role = models.ManyToManyField(PractitionerRoleType, blank=True)
    specialty = models.ManyToManyField(PractionRoleSpecialty, blank=True)
    period = models.ForeignKey(Period, blank=True)

class PractitionerRoleLocation(models.Model):
    practitionerRole = models.ManyToManyField(PractitionerRole)
    location = models.ForeignKey(Location)

class PractitionerRoleHealthcareService(models.Model):
    practitionerRole = models.ManyToManyField(PractitionerRole)
    location = models.ForeignKey(HealthcareService)

class PractitionerQualificationCode(CodeableConcept):
    pass

class PractitionerQualification(models.Model):
    practitioner = models.ManyToManyField(Practitioner)
    identifier = models.ManyToManyField(Identifier, blank=True)
    code = models.ManyToManyField(PractitionerQualificationCode, blank=True)
    period = models.ForeignKey(Period, blank=True)
    issuer = models.ForeignKey(Organization)

class PractitionerQualificationIdentifier(Identifier):
    PractitionerQualification = models.ManyToManyField(PractitionerQualification)

class PractitionerCommunication(CodeableConcept):
    # TODO: add in language suppoert

    practitioner = models.ManyToManyField(Practitioner)
