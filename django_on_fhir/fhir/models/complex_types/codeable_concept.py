from __future__ import unicode_literals
from django.db import models

# import additional models
from fhir.models.primitive_types.code import FhirCode

class CodeableConcept(models.Model):
    text = models.TextField(blank=True, null=True, max_length=100)

class CodeableConceptCoding(FhirCode):
    codeableConcept = models.ManyToManyField(CodeableConcept)
