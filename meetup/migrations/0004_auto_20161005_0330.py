# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0003_auto_20161005_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupuserdetails',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupuserdetails',
            name='user',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupUserDetails',
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
    ]
