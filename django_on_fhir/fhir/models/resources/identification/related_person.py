from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/human_name import HumanName
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/address import Address
from ../../complex_types/attachment import Attachment
from ../../complex_types/period import Period

from patient import Patient

class RelatedPerson(models.Model):
    # TODO: need to create table of relationships for relationship
    # TODO: need to create table of AdministrativeGender for gender

    GENDER_CHOICES = ['male', 'female', 'other', 'unknown']

    patient = models.ForeignKey(Patient)
    relationship = models.ForeignKey(CodeableConcept)
    name = models.ForeignKey(HumanName, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True)
    birthDate = models.DateTimeField(blank=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

class RelatedPersonIdentifier(Identifier):
    realtedPerson = models.ManyToManyField(RealtedPerson)

class RelatedPersonTelecom(ContactPoint):
    realtedPerson = models.ManyToManyField(RealtedPerson)

class RelatedPersonAddress(Address):
    realtedPerson = models.ManyToManyField(RealtedPerson)

class RelatedPersonPhoto(Attachment):
    realtedPerson = models.ManyToManyField(RealtedPerson)
