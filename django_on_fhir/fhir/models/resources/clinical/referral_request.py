from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept

from ../identification/patient import Patient

class ReferralRequest(models.Model):
    STATUS_CHOICES = ['draft', 'requested', 'active', 'cancelled', 'accepted',
        'rejected', 'completed']

    status = models.CharField(choices=STATUS_CHOICES)
    date = models.DateTimeField(blank=True)
    type = models.ForeignKey(CodeableConcept)
    specialty = models.ForeignKey(CodeableConcept)
    priority = models.ForeignKey(CodeableConcept)
    patient = models.ForeignKey(Patient)
    requester = GenericForeignKey('content_type', 'object_id')

class ReferralRequestIdentifier(models.Model):
    referralRequest = models.ManyToManyField(ReferralRequest)

class ReferralRequestRequester(models.Model)
