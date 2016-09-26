from __future__ import unicode_literals
from django.db import models

class Signature(models.Model):
    # TODO: Signature Type Codes preffered for type
    # TODO: refactor whoReference to link to an actual person
    # TODO: refactor blob for file reference

    type = models.CharField(max_length=100)
    when = models.DateTimeField()
    whoUri = models.URLField()
    whoReference = models.CharField(max_length=100)
    contentType = models.URLField()
    blob = models.BinaryField()
