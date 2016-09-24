from __future__ import unicode_literals
from django.db import models

# import additional models
from period import Period

class ContactPoint(models.model)
    system = models.CharField()
    value = models.CharField()
    use = models.CharField()
    rank = models.PositiveField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
