from __future__ import unicode_literals
from django.db import models

class Annotation(models.Model):
    # TODO: refactor to reference actual person

    authorReference = models.CharField(blank=True, max_length=100)
    authorString = models.CharField(blank=True, max_length=100)
    time = models.DateTimeField(blank=True)
    text = models.TextField(max_length=10000)
