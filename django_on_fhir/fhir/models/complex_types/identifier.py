from __future__ import unicode_literals
from django.db import models

# import additional models
from codeable_concept import CodeableConcept
from period import Period

class Identifier(models.Model):
    # TODO: IdentifierUse required for use
    # TODO: IdentifierUse required for type
    # TODO: refactor assigner to org

    USE_CHOICES = [
        ('usual', 'usual'),
        ('official', 'official'),
        ('temp', 'temp'),
        ('secondary', 'secondary'),
    ]

    use = models.CharField(choices=USE_CHOICES, blank=True, null=True,
        max_length=100)
    type = models.ForeignKey(CodeableConcept, blank=True, null=True,
        on_delete=models.CASCADE)
    system = models.URLField(blank=True, null=True)
    value = models.CharField(blank=True, null=True, max_length=100)
    period = models.ForeignKey(Period, blank=True, null=True,
        on_delete=models.CASCADE)
    assigner = models.CharField(blank=True, null=True, max_length=100)
