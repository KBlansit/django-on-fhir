from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.primitive_types.string import FhirString
from period import Period

class HumanName(models.Model):
    # TODO: NameUse required for use

    USE_CHOICES = [
        ('usual', 'usual'),
        ('official', 'offical'),
        ('temp', 'temp'),
        ('nickname', 'nickname'),
        ('anonymous', 'anonymous'),
        ('old', 'old'),
        ('maiden', 'maiden'),
    ]

    use = models.CharField(choices=USE_CHOICES, blank=True, null=True,
        max_length=1000)
    text = models.CharField(blank=True, null=True, max_length=1000)
    period = models.ForeignKey(Period, blank=True, null=True,
        on_delete=models.CASCADE)

class HumanNameFamily(FhirString):
    humanName = models.ManyToManyField(HumanName)

class HumanNameGiven(FhirString):
    humanName = models.ManyToManyField(HumanName)

class HumanNamePrefix(FhirString):
    humanName = models.ManyToManyField(HumanName)

class HumanNameSuffix(FhirString):
    humanName = models.ManyToManyField(HumanName)
