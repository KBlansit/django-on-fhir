from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.quantity import Quantity
from fhir.models.complex_types.period import Period

class Group(models.Model):
    type = models.CharField()
    actual = models.BooleanField()
    code = models.ForeignKey(CodeableConcept, blank=True)
    name = models.CharField(blank=True)
    quantity = models.PositiveIntegerField(blank=True)

class GroupIdentifier(Identifier):
    group = models.ManyToManyField(Group)

class GroupCharacteristic(models.Model):
    VALUE_CHOICES = ['codeable_concept', 'boolean', 'quantity', 'range']

    group = models.ManyToManyField(Group)
    code = models.ForeignKey(CodeableConcept)
    valueType = models.CharField(choices=VALUE_CHOICES)
    valueCodeableConcept = models.ForeignKey(CodeableConcept, blank=True,
        on_delete=models.CASCADE)
    valueBoolean = models.BooleanField(blank=True)
    valuesQuantity = models.ForeignKey(Quantity, blank=True,
        on_delete=models.CASCADE)
    exclude = models.BooleanField()
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)

class GroupMember(models.Model):
    group = models.ManyToManyField(Group)
    # entity =
    period = models.ForeignKey(Period, blank=True)
    inactive = models.BooleanField(blank=True)
