from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.attachment import Attachment
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.period import Period

from fhir.models.primitive_types.string import FhirString

from organization import Organization
from location import Location

class HealthcareService(models.Model):
    providedBy = models.ForeignKey(Organization, blank=True)
    serviceCategory = models.ForeignKey(CodeableConcept, blank=True)
    location = models.ForeignKey(Location)
    serviceName = models.CharField(blank=True)
    comment = models.CharField(blank=True)
    extraDetails = models.CharField(blank=True)
    eligibility = models.ForeignKey(CodeableConcept, blank=True)
    eligibilityNote = models.CharField(blank=True)
    publicKey = models.CharField(blank=True)
    appointmentRequired = models.BooleanField(blank=True)

class HealthcareServiceIdentifier(Identifier):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceServiceType(models.Model):
    healthcareService = models.ManyToManyField(HealthcareService)
    type = models.ForeignKey(CodeableConcept)

class ServiceTypeSpecialty(CodeableConcept):
    healthcareServiceServiceType = models.ManyToManyField(HealthcareServiceServiceType)

class HealthcareServicePhoto(Attachment):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceTelecom(ContactPoint):
    healthcareService = models.ManyToManyField(HealthcareService)

class healthcareServiceCoverageArea(models.Model):
    healthcareService = models.ManyToManyField(HealthcareService)
    location = models.ForeignKey(Location)

class HealthcareServiceServiceProvisionCode(CodeableConcept):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceProgramName(FhirString):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceCharacteristic(CodeableConcept):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceReferralMethod(CodeableConcept):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceAvailableTime(models.Model):
    healthcareService = models.ManyToManyField(HealthcareService)
    allDay = models.BooleanField(blank=True)
    availableStartTime = models.TimeField(blank=True)
    availableEndTime = models.TimeField(blank=True)

class AvailableTimeDaysOfWeek(models.Model):
    # TODO: daysOfWeek requires DaysOfWeek

    DAY_CHOICES = ['mon', 'tues', 'wed', 'thu', 'fri', 'sat', 'sun']

    availableTime = models.ManyToManyField(HealthcareServiceAvailableTime)
    dayOfWeek = models.CharField(choices = DAY_CHOICES)

class HealthcareServiceNotAvailable(models.Model):
    description = models.CharField()
    during = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
