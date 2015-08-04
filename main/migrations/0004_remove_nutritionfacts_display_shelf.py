# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150803_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritionfacts',
            name='display_shelf',
        ),
    ]
