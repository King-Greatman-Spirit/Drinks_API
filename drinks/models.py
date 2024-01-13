# drinks/models.py
from django.db import models

class Drink(models.Model):
    # Define a model for drinks with name and description fields
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        # Define a human-readable representation of the Drink model
        return self.name + ' ' + self.description
