from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/attachment import Attachment
from ../../complex_types/contact_point import ContactPoint
from ../../complex_types/period import Period

from ../../primitive_types/string import FhirString

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
    eligibilityNote = moddels.CharField(blank=True)
    publicKey = models.CharField(blank=True)
    appointmentRequired = models.BooleanField(blank=True)

class HealthcareServiceIdentifier(Identifier):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceServiceType(model.Model):
    healthcareService = models.ManyToManyField(HealthcareService)
    type = models.ForeignKey(CodeableConcept)
    specialty = models.ManyToManyField(ServiceTypeSpecialty,
        blank=True, on_delete=moels.CASCADE)

class ServiceTypeSpecialty(CodeableConcept):
    healthcareService = models.ManyToManyField(HealthcareService)

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

class AvailableTimeDaysOfWeek(model.Model):
    # TODO: daysOfWeek requires DaysOfWeek

    DAY_CHOICES = ['mon', 'tues', 'wed', 'thu', 'fri', 'sat', 'sun']

    availableTime = models.ManyToManyField(HealthcareServiceAvailableTime)
    dayOfWeek = models.CharField(choices = DAY_CHOICES)

class HealthcareServiceNotAvailable(models.Model):
    description = models.CharField()
    during = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
