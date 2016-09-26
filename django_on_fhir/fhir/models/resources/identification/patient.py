from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.human_name import HumanName
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address
from fhir.models.complex_types.attachment import Attachment
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address
from fhir.models.complex_types.period import Period

from organization import Organization

class Patient(models.Model):
    # TODO: AdministrativeGender required for gender
    # TODO: Martial Ststus Codes required for martialStatus
    # TODO: AdministrativeGender required for contact: geneder
    # TODO: refactor careProvider to refer to actual organization | provider (generic relation)
    # TODO: refactor manaagingOrganization to refer to actual organization
    # TODO: ensure that deceasedType types are semantically correct
    # TODO: custom signal to clean up database or add in CASCADE delete

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('unknown', 'unknown'),
    ]
    DECEASED_TYPE = [
        ('boolean', 'boolean'),
        ('date_time', 'date_time'),
    ]
    Multiple_Birth_Type = [
        ('boolean', 'boolean'),
        ('integer', 'integer'),
    ]

    active = models.BooleanField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=False)
    birthDate = models.DateTimeField(blank=True)
    deceasedType = models.CharField(choices=DECEASED_TYPE, blank=True)
    deceasedBoolean = models.BooleanField(blank=True)
    deceasedDateTime = models.DateTimeField(blank=True)
    martialStatus = models.CharField(blank=True)
    multipleBirth = models.BooleanField()
    multipleBirthType = models.CharField(blank=True)
    multipleBirthBoolean = models.BooleanField(blank=True)
    multipleBirthInteger = models.IntegerField(blank=True)
    # careProvider = models.CharField(blank=True)
    managingOrganization = models.ForeignKey(Organization, blank=True)

class PatientIdentifier(Identifier):
    patient = models.ManyToManyField(Patient)

class PatientName(HumanName):
    patient = models.ManyToManyField(Patient)

class PatientTelecom(ContactPoint):
    patient = models.ManyToManyField(Patient)

class PatientAddress(Address):
    patient = models.ManyToManyField(Patient)

class PatientPhoto(Attachment):
    patient = models.ManyToManyField(Patient)

class PatientContact(models.Model):
    # TODO: AdministrativeGender required for gender

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('unknown', 'unknown'),
    ]

    patient = models.ManyToManyField(Patient)
    name = models.ForeignKey(HumanName, blank=True)
    telecom = models.ForeignKey(ContactPoint, blank=True)
    address = models.ForeignKey(Address, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES, blank=True)
    organization = models.ForeignKey(Organization, blank=True)
    period = models.ForeignKey(Period, blank=True)

class ContactRelationship(CodeableConcept):
    patient = models.ManyToManyField(PatientContact)

class ContactTelecom(ContactPoint):
    patient = models.ManyToManyField(PatientContact)

class PatientAnimal(models.Model):
    patient = models.ForeignKey(Patient)
    species = models.ForeignKey(CodeableConcept)
    breed = models.ForeignKey(CodeableConcept, blank=True)
    genderStatus = models.ForeignKey(CodeableConcept, blank=True)

class PatientCommunication(models.Model):
    patient = models.ManyToManyField(Patient)
    language = models.ForeignKey(CodeableConcept)
    preferred = models.BooleanField(blank=True)

class PatientLink(models.Model):
    # TODO: LinkType required for PatientLink: type

    TYPE_CHOICES = ['replace', 'refer', 'seealso']

    patient = models.ManyToManyField(Patient)
    other = models.ForeignKey(Patient)
    type = models.CharField(choices=TYPE_CHOICES)
