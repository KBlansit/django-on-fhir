from __future__ import unicode_literals
from django.db import models

# import additional models
from period import Period

class ContactPoint(models.Model):
    # TODO: ContactPointSystem required for system
    # TODO: ContactPointUse required for use
    # TODO: verify value is present if system is present

    SYSTEM_CHOICES = [
    ('phone', 'phone'),
    ('fax', 'fax'),
    ('email', 'email'),
    ('pager', 'pager'),
    ('other', 'other'),
    ]
    USE_CHOICES = [
    ('home', 'home'),
    ('work', 'work'),
    ('temp' 'temp'),
    ('old', 'old'),
    ]

    system = models.CharField(choices=SYSTEM_CHOICES, blank=True, max_length=100)
    value = models.CharField(blank=True, max_length=100)
    use = models.CharField(blank=True, max_length=100)
    rank = models.PositiveIntegerField(blank=True)
    period = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
