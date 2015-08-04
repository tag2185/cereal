#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Manufacturer, Cereal, NutritionFacts

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cereal.csv')

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:

	manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

	manu_obj.save()

	cereal_obj, created = Cereal.objects.get_or_create(name=row['Cereal Name'].replace('_', ' '))
	cereal_obj.type = row['Type']
	cereal_obj.manufacturer = manu_obj

	cereal_obj.save()

	nutri_obj, created = NutritionFacts.objects.get_or_create(cereal=cereal_obj)
	nutri_obj.calories = row['Calories']
	nutri_obj.protein = row['Protein (g)']
	nutri_obj.fat = row['Fat']
	nutri_obj.sodium = row['Sodium']
	nutri_obj.fiber = row['Dietary Fiber']
	nutri_obj.carbs = row['Carbs']
	nutri_obj.sugars = row['Sugars']
	nutri_obj.potassium = row['Potassium']
	nutri_obj.vitamins_and_minerals = row['Vitamins and Minerals']

	nutri_obj.save()