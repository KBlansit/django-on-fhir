from __future__ import unicode_literals
from django.db import models

class FhirCode(models.Model):
    code = models.CharField(max_length=100)
