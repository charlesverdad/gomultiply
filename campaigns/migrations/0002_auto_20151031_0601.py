# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.FloatField(null=True, blank=True)),
                ('location', models.CharField(max_length=300)),
                ('duration', models.FloatField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('difficulty', models.IntegerField()),
                ('field', models.CharField(max_length=30)),
                ('requirements', models.CharField(max_length=200)),
                ('max_people', models.IntegerField()),
                ('needs', models.CharField(max_length=200)),
                ('goals', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='chain',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
