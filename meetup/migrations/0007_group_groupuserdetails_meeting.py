# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('meetup', '0006_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupUserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('joined', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='meetup.Group')),
                ('user', models.ForeignKey(to='profiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('agenda', models.TextField(null=True, blank=True)),
                ('fees', models.CharField(max_length=5)),
                ('scheduled', models.DateTimeField(null=True, blank=True)),
                ('venue', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, max_length=50, null=True, choices=[(b'1', b'yet to happen'), (b'2', b'happened'), (b'3', b'postponed'), (b'4', b'cancelled')])),
                ('group', models.ForeignKey(to='meetup.Group')),
            ],
        ),
    ]
