from __future__ import unicode_literals
from django.db import models

class Annotation(models.Model):
    author = models.ManyToManyField(AnnotationAuthors, blank=True,
        on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)
    text = models.CharField(blank=True)

class AnnotationAuthors(models.Model):
    # TODO: refactor to reference actual person

    authorReference = models.CharField(blank=True)
    authorString = models.CharField(blank=True)
