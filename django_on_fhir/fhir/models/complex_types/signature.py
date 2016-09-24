from __future__ import unicode_literals
from django.db import models

class Signature(models.model):
    # TODO: Signature Type Codes preffered for type
    # TODO: refactor whoReference to link to an actual person
    # TODO: refactor blob for file reference

    type = models.CharField()
    when = models.DateTimeField()
    whoUri = models.URLField()
    whoReference = models.CharField()
    contentType = models.URLField()
    blob = models.BinaryField()
