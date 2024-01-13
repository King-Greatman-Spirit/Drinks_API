# drinks/serializers.py
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    # Define a serializer for the Drink model with specified fields
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
