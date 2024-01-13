# drinks/admin.py
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)

# add data of drinks (name, description in the django admin)