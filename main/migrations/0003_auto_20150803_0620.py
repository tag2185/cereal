# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150730_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True)),
                ('protein', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('sodium', models.FloatField(null=True)),
                ('fiber', models.FloatField(null=True)),
                ('carbs', models.FloatField(null=True)),
                ('sugars', models.IntegerField(null=True)),
                ('display_shelf', models.IntegerField(null=True)),
                ('potassium', models.IntegerField(null=True)),
                ('vitamins_and_minerals', models.IntegerField(null=True)),
                ('cereal', models.OneToOneField(to='main.Cereal')),
            ],
        ),
        migrations.RemoveField(
            model_name='nutritional_facts',
            name='cereal',
        ),
        migrations.DeleteModel(
            name='Nutritional_facts',
        ),
    ]
