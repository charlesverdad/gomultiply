# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20151031_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='difficulty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='field',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='goals',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='max_people',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='needs',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='requirements',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
