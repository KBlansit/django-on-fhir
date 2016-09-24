from __future__ import unicode_literals
from django.db import models

class Patient(models.model):
    identifier = models.AutoField(primary_key=True)
    active = models.BooleanField(default=False) # optional but default to false
