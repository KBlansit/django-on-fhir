from __future__ import unicode_literals
from django.db import models

class Coding(models.Model):
    system = models.URLField(blank=True)
    version = models.CharField(blank=True, max_length=100)
    code = models.CharField(blank=True, max_length=100)
    display = models.CharField(blank=True, max_length=100)
    userSelected = models.BooleanField(blank=True)
