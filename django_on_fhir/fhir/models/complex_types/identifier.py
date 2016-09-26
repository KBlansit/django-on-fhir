from __future__ import unicode_literals
from django.db import models

# import additional models
from codeable_concept import CodeableConcept
from period import Period

class Identifier(models.Model):
    # TODO: IdentifierUse required for use
    # TODO: IdentifierUse required for type
    # TODO: refactor assigner to org

    USE_CHOICES = ['usual', 'official', 'temp', 'secondary']

    use = models.CharField(blank=True, max_length=100)
    type = models.ForeignKey(CodeableConcept, blank=True, on_delete=models.CASCADE)
    system = models.URLField(blank=True)
    value = models.CharField(max_length=100)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
    assigner = models.CharField(max_length=100)
