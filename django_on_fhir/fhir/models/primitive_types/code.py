from __future__ import unicode_literals
from django.db import models

class FhirCode(models.model):
    """
    used to store multiple FHIR codes
    """
    string = models.CharField()
