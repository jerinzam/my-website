# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0005_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
