from django.contrib import admin

from main.models import Cereal, Manufacturer, NutritionFacts
# Register your models here.

admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(NutritionFacts)