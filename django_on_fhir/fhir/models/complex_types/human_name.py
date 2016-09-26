from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.primiative_types.string import FhirString
from period import Period

class HumanName(models.Model):
    # TODO: NameUse required for use

    USE_CHOICES = ['usual', 'official', 'temp', 'nickname', 'anonymous',
        'old', 'maiden']

    use = models.CharField(blank=True, max_length=1000)
    text = models.CharField(blank=True, max_length=1000)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)

class HumanNameFamily(FhirString):
    HumanName = models.ManyToManyField(HumanName)

class HumanNameGiven(FhirString):
    HumanName = models.ManyToManyField(HumanName)

class HumanNamePrefix(FhirString):
    HumanName = models.ManyToManyField(HumanName)

class HumanNameSuffix(FhirString):
    HumanName = models.ManyToManyField(HumanName)
