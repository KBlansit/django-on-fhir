from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.codeable_concept import CodeableConcept
from fhir.models.complex_types.quantity import Quantity
from fhir.models.complex_types.period import Period

class GroupCode(CodeableConcept):
    pass

class Group(models.Model):
    type = models.CharField(max_length=100)
    actual = models.BooleanField()
    code = models.ForeignKey(GroupCode, blank=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    quantity = models.PositiveIntegerField(blank=True)

class GroupIdentifier(Identifier):
    group = models.ManyToManyField(Group)

class GroupCharacteristicCode(CodeableConcept):
    pass

class GroupCharacteristicValue(CodeableConcept):
    pass

class GroupCharacteristic(models.Model):
    VALUE_CHOICES = [
        ('codeable_concept', 'codeable_concept'),
        ('boolean', 'boolean'),
        ('quantity', 'quantity'),
        ('range', 'range'),
    ]

    group = models.ManyToManyField(Group)
    code = models.ManyToManyField(GroupCharacteristicCode,
        related_name='group_characteristic_code')
    valueType = models.CharField(choices=VALUE_CHOICES, max_length=100)
    valueBoolean = models.BooleanField(blank=True)
    code = models.ManyToManyField(GroupCharacteristicCode)
    valuesQuantity = models.ForeignKey(Quantity, blank=True,
        on_delete=models.CASCADE)
    exclude = models.BooleanField()
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)

class GroupMember(models.Model):
    group = models.ManyToManyField(Group)
    # entity =
    period = models.ForeignKey(Period, blank=True)
    inactive = models.BooleanField(blank=True)
