# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0002_auto_20161005_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupuserdetails',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'1', b'yet to happen'), (b'2', b'happened'), (b'3', b'postponed'), (b'4', b'cancelled')]),
        ),
    ]
