# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fbid', models.CharField(max_length=20)),
                ('fbusername', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('discipler', models.CharField(max_length=50)),
                ('chain', models.ForeignKey(blank=True, to='campaigns.Person', null=True)),
            ],
        ),
    ]
