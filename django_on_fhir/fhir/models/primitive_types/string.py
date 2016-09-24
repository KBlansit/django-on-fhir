from __future__ import unicode_literals
from django.db import models

class FhirString(models.model):
    """
    used to store multiple FHIR strings
    """
    string = models.CharField()
