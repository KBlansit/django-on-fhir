from __future__ import unicode_literals
from django.db import models

class Period(models.model):
    # TODO: verify end date is larger than start date

    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
