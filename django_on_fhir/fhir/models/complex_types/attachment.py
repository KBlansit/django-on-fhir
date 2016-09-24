from __future__ import unicode_literals
from django.db import models

class Attachment(models.model):
    # TODO: refactor data to store in a file server
    # TODO: MineType codes required for contentType
    # TODO: make methods that can caluclate: size and hash automatically

    contentType = models.CharField(blank=True)
    langauge = models.CharField(blank=True)
    data = models.BinaryField(blank=True)
    url = models.URLField(blank=True)
    size = models.PositiveIntegerField(blank=True))
    hash = models.BinaryField(blank=True)
    title = models.CharField(blank=True)
    creation = models.DateTimeField(blank=True)
