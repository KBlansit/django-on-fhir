from __future__ import unicode_literals
from django.db import models

class Annotation(models.model):
    author = models.ManyToMany(AnnotationAuthors, blank=True, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)
    text = models.CharField(blank=True)

class AnnotationAuthors(models.model):
    # TODO: refactor to reference actual person

    authorReference = models.CharField(blank=True)
    authorString = models.CharField(blank=True)
