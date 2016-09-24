from __future__ import unicode_literals
from django.db import models

# import additional models
from ../primitive_types/code import FhirCode

class CodeableConcept(models.model):
    coding = models.ManyToMany(FhirCode, blank=TRUE, on_delete=models.CASCADE)
    text = models.CharField(blank=True)
