from __future__ import unicode_literals
from django.db import models

# import additional models
from period import Period

class ContactPoint(models.model)
    # TODO: ContactPointSystem required for system
    # TODO: ContactPointUse required for use
    # TODO: verify value is present if system is present

    SYSTEM_CHOICES = ['phone', 'fax', 'email', 'pager', 'other']
    USE_CHOICES = ['home', 'work', 'temp', 'old', 'mobile']

    system = models.CharField(choices=SYSTEM_CHOICES, blank=True)
    value = models.CharField(blank=True)
    use = models.CharField(blank=True)
    rank = models.PositiveIntegerField(blank=True)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
