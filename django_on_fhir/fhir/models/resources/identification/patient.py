from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/human_name import HumanName
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address
from ../../complex_types/attachment import Attachment
from ../../complex_types/codeable_cconcept import CodeableConcept
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address
from ../../complex_types/period import Period

class Patient(models.model):
    # TODO: AdministrativeGender required for gender
    # TODO: Martial Ststus Codes required for martialStatus
    # TODO: AdministrativeGender required for contact: geneder
    # TODO: refactor careProvider to refer to actual organization | provider (generic relation)
    # TODO: refactor manaagingOrganization to refer to actual organization
    # TODO: ensure that deceasedType types are semantically correct
    # TODO: custom signal to clean up database or add in CASCADE delete

    GENDER_CHOICES = ['male', 'female', 'other', 'unknown']
    DECEASED_TYPE = ['boolean', 'date_time']
    Multiple_Birth_Type = ['boolean', 'integer']

    identifier = models.ManyToMany(Identifier, blank=False)
    active = models.BooleanField(blank=True)
    name = models.ManyToMany(HumanName, blank=False, on_delete=models.CASCADE)
    telecom = models.ManyToMany(ContactPoint, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, blank=False)
    birthDate = models.DateTimeField(blank=True)

    # deceased
    multipleBirth = models.BooleanField()
    deceasedType = models.CharField(choices=DECEASED_TYPE, blank=True)
    deceasedBoolean = models.BooleanField(blank=True)
    deceasedDateTime = models.DateTimeField(blank=True)

    address = models.ManyToMany(Address, blank=True)
    martialStatus = models.CharField(blank=True)

    # multipleBirth
    multipleBirth = models.BooleanField()
    multipleBirthType = models.CharField(blank=True)
    multipleBirthBoolean = models.BooleanField(blank=True)
    multipleBirthInteger = models.IntegerField(blank=True)

    photo = models.ManyToMany(Attachment, blank=True)
    contact = models.ManyToMany(PatientContact, blank=True)
    animal = models.ForeignKey(PatientAnimal, blank=True)
    communication = models.ForeignKey(PatientCommunication, blank=True)
    careProvider = models.CharField(blank=True)
    managingOrganization = CharField(blank=True)
    link = models.ForeignKey(PatientLink, blank=True)

class PatientContact(models.model):
    # TODO: refactor PatientContact: organization to refer to actual organization

    relationship = models.ManyToMany(CodeableConcept, blank=True)
    name = models.ForeignKey(HumanName, blank=True)
    telecom = models.ManyToMany(ContactPoint, blank=True)
    address = models.ForeignKey(Address, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES, blank=True)
    organization = models.CharField(blank=True)
    period = models.ForeignKey(Period, blank=True)

class PatientAnimal(models.model):
    species = models.ForeignKey(CodeableConcept)
    breed = models.ForeignKey(CodeableConcept, blank=True)
    genderStatus = models.ForeignKey(CodeableConcept, blank=True)

class PatientCommunication(models.model):
    language = models.ForeignKey(CodeableConcept)
    preferred = models.BooleanField(blank=True)

class PatientLink(models.model):
    # TODO: LinkType required for PatientLink: type

    TYPE_CHOICES = ['replace', 'refer', 'seealso']

    other = models.ForeignKey(Patient)
    type = models.CharField(choices=TYPE_CHOICES)
