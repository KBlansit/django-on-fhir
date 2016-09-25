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

class HealthcareService(models.model):
    identifier = models.ManyToMany(HealthcareServiceIdentifier, blank=True,
        on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, blank=True)
    serviceCategory = models.ForeignKey(CodeableConcept, blank=True)
    serviceType = models.ManyToMany(HealthcareService, blank=True,
        on_delete=models.CASCADE)
    # location
    serviceName = models.CharField(blank=True)
    comment = models.CharField(blank=True)
    extraDetails = models.CharField(blank=True)
    photo = models.ForeignKey(HealthcareServicePhoto, blank=True,
        on_delete=models.CASCADE)
    telecom = models.ManyToMany(ContactPoint, blank=True)
    # coverageArea =
    serviceProvisionCode = models.ManyToMany(HealthcareServiceServiceProvisionCode,
        blank=True, on_delete=models.CASCADE)
    eligibility = models.ForeignKey(CodeableConcept, blank=True)
    eligibilityNote = moddels.CharField(blank=True)
    programName = models.ManyToMany(HealthcareServiceProgramName, blank=True,
        on_delete=models.CASCADE)
    characterstic = models.ManyToMany(HealthcareServiceCharacteristic,
        blank=True, on_delete=model.CASCADE)
    referralMethod = models.ManyToMany(HealthcareServiceReferralMethod,
        blank=True, on_delete=models.CASCADE)
    publicKey = models.CharField(blank=True)
    appointmentRequired = models.BooleanField(blank=True)
    availableTime = models.ManyToMany(HealthcareServiceAvailableTime,
        blank=True, on_delete=models.CASCADE)
    notAvailableTime = models.ManyToMany(HealthcareServiceNotAvailable,
    blank=True, on_delete=models.CASCADE)

class HealthcareServiceIdentifier(Identifier):
    pass

class HealthcareServiceServiceType(model.model):
    type = models.ForeignKey(CodeableConcept)
    specialty = models.ManyToMany(ServiceTypeSpecialty,
        blank=True, on_delete=moels.CASCADE)

class ServiceTypeSpecialty(CodeableConcept):
    pass

class HealthcareServicePhoto(Attachment):
    pass

class HealthcareServiceTelecom(ContactPoint):
    pass

class HealthServiceCoverageArea(models.model):
    # location =

class HealthcareServiceServiceProvisionCode(CodeableConcept):
    pass

class HealthcareServiceProgramName(FhirString):
    pass

class HealthcareServiceCharacteristic(CodeableConcept):
    pass

class HealthcareServiceReferralMethod(CodeableConcept):
    pass

class HealthcareServiceAvailableTime(models.model):
    daysOfWeek = models.ManyToMany(AvailableTimeDaysOfWeek, blank=True)
    allDay = models.BooleanField(blank=True)
    availableStartTime = models.TimeField(blank=True)
    availableEndTime = models.TimeField(blank=True)

class AvailableTimeDaysOfWeek(model.model):
    # TODO: daysOfWeek requires DaysOfWeek

    DAY_CHOICES = ['mon', 'tues', 'wed', 'thu', 'fri', 'sat', 'sun']

    dayOfWeek = models.CharField(choices = DAY_CHOICES)

class HealthcareServiceNotAvailable(models.model):
    description = models.CharField()
    during = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
