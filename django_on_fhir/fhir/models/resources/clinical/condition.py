
from __future__ import unicode_literals
from django.db import models

# import additional models
from ../../complex_types/identifier import Identifier

from ../identification/patient import Patient

class Condition(models.Model):
    patient = model.ForeignKey(Patient)

class ConditionIdentifier(Identifier):
    condition = models.ManyToManyField(Condition)
