from __future__ import unicode_literals
from django.db import models

class Coding(models.model):
    system = model.URLField(blank=True)
    version = models.CharField(blank=True)
    code = models.CharField(blank=True)
    display = models.CharField(blank=True)
    userSelected = models.BooleanField(blank=True)
