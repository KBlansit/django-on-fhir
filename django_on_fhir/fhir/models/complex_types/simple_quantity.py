from __future__ import unicode_literals
from django.db import models

# import additional models
from quantity import Quantity

class SimpleQuantity(Quantity):
    # TODO: make test assertion that SimpleQuantity doesn't have comparator
    
    @property
    def comparator(self):
        raise AttributeError
