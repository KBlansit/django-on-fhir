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

class HealthcareServiceServiceCategory(ContactPoint):
    pass

class HealthcareServiceEligibility(CodeableConcept):
    pass

class HealthcareService(models.Model):
    providedBy = models.ForeignKey(Organization, blank=True)
    serviceCategory = models.ManyToManyField(HealthcareServiceServiceCategory,
        blank=True)
    location = models.ForeignKey(Location)
    serviceName = models.CharField(blank=True, null=True, max_length=100)
    comment = models.CharField(blank=True, null=True, max_length=100)
    extraDetails = models.CharField(blank=True, null=True, max_length=100)
    eligibility = models.ManyToManyField(HealthcareServiceEligibility, blank=True)
    eligibilityNote = models.CharField(blank=True, null=True, max_length=100)
    publicKey = models.CharField(blank=True, null=True, max_length=100)
    appointmentRequired = models.NullBooleanField(blank=True)

class HealthcareServiceIdentifier(Identifier):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceType(CodeableConcept):
    pass

class HealthcareServiceServiceType(models.Model):
    healthcareService = models.ManyToManyField(HealthcareService)
    type = models.ForeignKey(HealthcareServiceType)

class ServiceTypeSpecialty(CodeableConcept):
    healthcareServiceServiceType = models.ManyToManyField(HealthcareServiceServiceType)

class HealthcareServicePhoto(Attachment):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceTelecom(ContactPoint):
    healthcareService = models.ManyToManyField(HealthcareService)

class HealthcareServiceCoverageArea(models.Model):
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

    DAY_CHOICES = [
        ('mon', 'mon'),
        ('tue', 'tue'),
        ('wed', 'wed'),
        ('thu', 'thu'),
        ('fri', 'fri'),
        ('sat', 'sat'),
        ('sun', 'sun'),
    ]

    availableTime = models.ManyToManyField(HealthcareServiceAvailableTime)
    dayOfWeek = models.CharField(choices = DAY_CHOICES, max_length=100)

class HealthcareServiceNotAvailable(models.Model):
    description = models.CharField(max_length=1000)
    during = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
