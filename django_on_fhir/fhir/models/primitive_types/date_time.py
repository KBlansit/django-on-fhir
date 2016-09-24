from __future__ import unicode_literals
from django.db import models

class FhirDateTime(models.model):
    """
    used to store multiple FHIR date times    
    """
    date = models.DateTimeField()
