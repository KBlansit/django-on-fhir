from __future__ import unicode_literals
from django.db import models

# import additional models
from ../primitive_type/string import FhirString
from period import Period

class HumanName(models.Model):
    # TODO: NameUse required for use

    USE_CHOICES = ['usual', 'official', 'temp', 'nickname', 'anonymous',
        'old', 'maiden']

    use = models.CharField(blank=True)
    text = models.CharField(blank=True)
    family = models.ManyToManyField(FhirString, blank=True, on_delete=models.CASCADE)
    given = models.ManyToManyField(FhirString, blank=True, on_delete=models.CASCADE)
    prefix = models.ManyToManyField(FhirString, blank=True, on_delete=models.CASCADE)
    suffix = models.ManyToManyField(FhirString, blank=True, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
