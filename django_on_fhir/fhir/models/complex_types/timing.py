from __future__ import unicode_literals
from django.db import models

# import additional models
from quantity import Quantity
from range import Range
from period import Period

class Timing(models.Model):
    # TODO: TimingAbbreviation preferred for code
    CODE_CHOICES = [
        ('QD', 'QD'),
        ('QOD', 'QOD'),
        ('Q4D', 'Q4D'),
        ('Q6D', 'Q6D'),
        ('BID', 'BID'),
        ('TID', 'TID'),
        ('QID', 'QID'),
        ('AM', 'AM'),
        ('PM', 'PM'),
    ]

    event = models.DateTimeField(blank=True)
    code = models.CharField(choices=CODE_CHOICES, blank=True, max_length=100)

class RepeatTiming(models.Model):
    # TODO: better way to model which type of bound?
    # TODO: assert tests that only single bounds type is used
    # TODO: assert that if boundsType = NULL that bounds are in fact null
    # TODO: duration has to be positive
    # TODO: period has to be positive

    # TODO: unitsOfTime required for durationUnits
    # TODO: unitsOfTime required for periodUnits
    # TODO: EventTiming required for when

    BOUNDS_TYPE_CHOICES = [
        ('quantity', 'quantity'),
        ('range', 'range'),
        ('period', 'period'),
    ]
    DURATION_UNITS_CHOICES = [
        ('s', 's'),
        ('min', 'min'),
        ('h', 'h'),
        ('d', 'd'),
        ('wk', 'wk'),
        ('mo', 'mo'),
        ('a', 'a'),
    ]
    PERIOD_UNITS_CHOICES = [
        ('s', 's'),
        ('min', 'min'),
        ('h', 'h'),
        ('d', 'd'),
        ('wk', 'wk'),
        ('mo', 'mo'),
        ('a', 'a'),
    ]

    timing = models.ManyToManyField(Timing)
    boundsType = models.CharField(choices=BOUNDS_TYPE_CHOICES, blank=True,
        max_length=100)
    boundQuantity = models.ForeignKey(Quantity, blank=True, on_delete=models.CASCADE)
    boundRange = models.ForeignKey(Range, blank=True, on_delete=models.CASCADE)
    boundPeriod = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(blank=True)
    duration = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    durationMax = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    durationUnits = models.CharField(choices=DURATION_UNITS_CHOICES, blank=True,
        max_length=100)
    frequency = models.IntegerField(blank=True)
    frequencyMax = models.IntegerField(blank=True)
    period = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    periodMax = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    periodUnits = models.CharField(choices=PERIOD_UNITS_CHOICES, blank=True,
        max_length=100)
    when = models.CharField(blank=True, max_length=100)
