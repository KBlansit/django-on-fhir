from __future__ import unicode_literals
from django.db import models

# import additional models
from ../primitive_types/date_time import FhirDateTime
from quantity import Quantity
from fhir_range import Range
from period import Period

class Timing(models.Model):
    # TODO: TimingAbbreviation preferred for code
    CODE_CHOICES = ['QD', 'QOD', 'Q4D', 'Q6D', 'BID', 'TID', 'QID', 'AM', 'PM']

    event = models.ManyToManyField(FhirDateTime, blank=True, on_delete=models.CASCADE)
    repeat = models.ForeignKey(RepeatTiming, blank=True, on_delete=models.CASCADE)
    code = models.CharField(choices=CODE_CHOICES, blank=True)

class RepeatTiming(models.Model):
    # TODO: better way to model which type of bound?
    # TODO: assert tests that only single bounds type is used
    # TODO: assert that if boundsType = NULL that bounds are in fact null
    # TODO: duration has to be positive
    # TODO: period has to be positive

    # TODO: unitsOfTime required for durationUnits
    # TODO: unitsOfTime required for periodUnits
    # TODO: EventTiming required for when

    BOUNDS_TYPE_CHOICES = ['quantity', 'range', 'period']
    DURATION_UNITS_CHOICES = ['s', 'min', 'h', 'd', 'wk', 'mo', 'a']
    PERIOD_UNITS_CHOICES = ['s', 'min', 'h', 'd', 'wk', 'mo', 'a']

    boundsType = models.CharField(choices=BOUNDS_TYPE_CHOICES, blank=True)
    boundQuantity = models.ForeignKey(Quantity, blank=True, on_delete=models.CASCADE)
    boundRange = models.ForeignKey(Range, blank=True, on_delete=models.CASCADE)
    boundPeriod = models.ForeignKey(Period, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(blank=True)
    duration = models.DecimalField(blank=True)
    durationMax = models.DecimalField(blank=True)
    durationUnits = models.CharField(choices=DURATION_UNITS_CHOICES, blank=True)
    frequency = models.IntegerField(blank=True)
    frequencyMax = models.IntegerField(blank=True)
    period = models.DecimalField(blank=True)
    periodMax = models.DecimalField(blank=True)
    periodUnits = models.CharField(choices=PERIOD_UNITS_CHOICES, blank=True)
    when = CharField(blank=True)
