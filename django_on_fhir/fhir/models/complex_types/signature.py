from __future__ import unicode_literals
from django.db import models

# import additional models
from coding import Coding

class Signature(models.Model):
    # TODO: Signature Type Codes preffered for type
    # TODO: refactor whoReference to link to an actual person
    # TODO: refactor blob for file reference

    when = models.DateTimeField()
    whoUri = models.URLField()
    whoReference = models.CharField(max_length=100)
    contentType = models.URLField()
    blob = models.BinaryField()

class SignatureType(Coding):
    signature = models.ManyToManyField(Signature)
