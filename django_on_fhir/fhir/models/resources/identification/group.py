from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier
from ../../complex_types/codeable_concept import CodeableConcept
from ../../complex_types/quantity import Quantity
from ../../complex_types/period import Period

class Group(models.model):
    type = models.CharField()
    actual = models.BooleanField()
    code = models.ForeignKey(CodeableConcept, blank=True)
    name = models.CharField(blank=True)
    quantity = models.PositiveInteger(blank=True)

class GroupIdentifier(Identifier):
    group = models.ManyToMany(Group)

class GroupCharacteristic(models.model):
    VALUE_CHOICES = ['codeable_concept', 'boolean', 'quantity', 'range']

    group = models.ManyToMany(Group)
    code = models.ForeignKey(CodeableConcept)
    valueType = models.Char(choices=VALUE_CHOICES)
    valueCodeableConcept = models.ForeignKey(CodeableConcept, blank=True,
        on_delete=models.CASCADE)
    valueBoolean = models.BooleanField(blank=True)
    valuesQuantity = models.ForeignKey(Quantity, blank=True,
        on_delete=models.CASCADE)
    exclude = models.BooleanField()
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)

class GroupMember(models.model):
    group = models.ManyToMany(Group)
    # entity =
    period = models.ForeignKey(Period, blank=True)
    inactive = models.BooleanField(blank=True)
