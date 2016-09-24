from __future__ import unicode_literals
from django.db import models

class Period(models.model):
    start = models.DateTimeField()
    end = models.DateTimeField()
