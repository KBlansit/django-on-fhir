from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.human_name import HumanName
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.address import Address
from fhir.models.complex_types.attachment import Attachment
from fhir.models.complex_types.period import Period

from patient import Patient

class RelatedPersonRelationship(CodeableConcept):
    pass

class RelatedPerson(models.Model):
    # TODO: need to create table of relationships for relationship
    # TODO: need to create table of AdministrativeGender for gender

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('unknown', 'unknown'),
    ]

    patient = models.ForeignKey(Patient)
    relationship = models.ManyToManyField(RelatedPersonRelationship)
    name = models.ForeignKey(HumanName, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True,
        max_length=100)
    birthDate = models.DateTimeField(blank=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

class RelatedPersonIdentifier(Identifier):
    realtedPerson = models.ManyToManyField(RelatedPerson)

class RelatedPersonTelecom(ContactPoint):
    realtedPerson = models.ManyToManyField(RelatedPerson)

class RelatedPersonAddress(Address):
    realtedPerson = models.ManyToManyField(RelatedPerson)

class RelatedPersonPhoto(Attachment):
    realtedPerson = models.ManyToManyField(RelatedPerson)
